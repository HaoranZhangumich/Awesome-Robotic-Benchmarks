#!/usr/bin/env python3
"""Check the benchmark files: schema first, then every link.

    pip install pyyaml
    python scripts/validate.py                  # all of benchmarks/
    python scripts/validate.py benchmarks/libero.yaml benchmarks/calvin.yaml
    python scripts/validate.py --no-net         # schema only, no network

What it checks
  schema  required keys, domain / area against taxonomy.yaml, date format, clean URLs
  arXiv   each arxiv.org link is looked up; the real title and submission date are
          printed next to the entry name, and a title that does not mention the
          benchmark is reported as a failure (this catches wrong paper ids)
  GitHub  each repo is looked up: exists, renamed, archived, stars
  other   every other URL is fetched and its HTTP status reported

A full run with the network on also refreshes scripts/github_stars.json, which
build_readme.py uses for the star counts.

GitHub allows 60 lookups an hour without a token. Set GITHUB_TOKEN, or log in
with the GitHub CLI (`gh auth login`), to lift that limit.
Exit code 1 if any entry fails.
"""
import html
import json
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
BENCH = ROOT / "benchmarks"
TAXONOMY = ROOT / "taxonomy.yaml"
STARS = ROOT / "scripts" / "github_stars.json"

SETTINGS = {"sim", "real"}
COLLECTION = {"human_demonstration", "human_annotation", "motion_planner", "synthetic",
              "rl_policy", "mixed", "none", "unknown"}
URL_RE = re.compile(r"^https?://[^\s()]+$")
DATE_RE = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")
ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})", re.I)
GITHUB_RE = re.compile(r"^https?://github\.com/([^/\s]+)/([^/\s#?]+)", re.I)
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
BLOCKED = {"403", "405", "406", "418", "429", "999"}


def norm(text):
    return re.sub(r"[^a-z0-9]+", "", str(text).lower())


def tokens(text):
    return [t for t in re.split(r"[^a-z0-9]+", str(text).lower()) if len(t) >= 3]


def curl(url, timeout=30, headers=()):
    cmd = ["curl", "-sL", "--max-time", str(timeout), "-A", UA, "-w", "\n%{http_code}"]
    for h in headers:
        cmd += ["-H", h]
    try:
        p = subprocess.run(cmd + [url], capture_output=True, text=True, timeout=timeout + 10)
        body, _, code = p.stdout.rpartition("\n")
        return code.strip() or "000", body
    except Exception:
        return "000", ""


def hub_api(url):
    """Hugging Face pages are rate-limited hard; the Hub API answers the same question (does it exist?)."""
    m = re.match(r"https://huggingface\.co/(datasets|spaces)/([^/?#]+/[^/?#]+)", url)
    if m:
        return f"https://huggingface.co/api/{m.group(1)}/{m.group(2)}"
    m = re.match(r"https://huggingface\.co/(?!datasets/|spaces/|collections/|papers/|docs/|blog/)([^/?#]+/[^/?#]+)/?$", url)
    if m:
        return f"https://huggingface.co/api/models/{m.group(1)}"
    return url


def check_url(url):
    """HTTP status of a link, retrying the answers that usually mean 'busy', not 'gone'."""
    target = hub_api(url)
    code = "000"
    for attempt in range(3):
        code = curl(target)[0]
        if code not in ("000", "429", "502", "503"):
            break
        time.sleep(10 * (attempt + 1))
    return code


def github_token():
    for var in ("GITHUB_TOKEN", "GH_TOKEN"):
        if os.environ.get(var):
            return os.environ[var]
    try:
        p = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=10)
        return p.stdout.strip() if p.returncode == 0 else ""
    except Exception:
        return ""


def arxiv_lookup(aid):
    """DataCite (arXiv's DOI registrar) first, the arXiv abstract page as fallback."""
    code, body = curl(f"https://api.datacite.org/dois/10.48550/arXiv.{aid}")
    if code == "200":
        try:
            a = json.loads(body)["data"]["attributes"]
            title = " ".join((a["titles"][0]["title"] or "").split())
            submitted = sorted(d["date"] for d in a.get("dates", []) if d.get("dateType") == "Submitted")
            summary = " ".join(" ".join(d.get("description", "") for d in a.get("descriptions", [])).split())
            author = (a.get("creators") or [{}])[0].get("name", "")
            if title:
                return {"title": title, "published": (submitted[0] if submitted else a.get("created", ""))[:10],
                        "summary": summary, "first_author": author}
        except Exception:
            pass
    for attempt in range(3):
        code, body = curl(f"https://arxiv.org/abs/{aid}")
        if code == "200" and "citation_title" in body:
            def meta(name):
                m = re.search(r'<meta name="%s" content="([^"]*)"' % name, body)
                return html.unescape(m.group(1)) if m else ""
            return {"title": meta("citation_title"), "published": meta("citation_date").replace("/", "-"),
                    "summary": meta("citation_abstract"), "first_author": meta("citation_author")}
        if code == "404":
            return {"error": "no such arXiv id"}
        time.sleep(5 + 5 * attempt)
    return {"error": f"could not look it up (HTTP {code}); try again later"}


def github_lookup(owner, repo, token):
    headers = ["Accept: application/vnd.github+json"]
    if token:
        headers.append(f"Authorization: Bearer {token}")
    code, body = curl(f"https://api.github.com/repos/{owner}/{repo}", headers=headers)
    if code != "200":
        hint = " (rate limit? set GITHUB_TOKEN)" if code in ("403", "429") else ""
        return {"error": f"HTTP {code}{hint}"}
    d = json.loads(body)
    return {"full_name": d.get("full_name"), "stars": d.get("stargazers_count"), "archived": d.get("archived"),
            "pushed_at": (d.get("pushed_at") or "")[:10], "description": d.get("description") or ""}


def check_schema(e, taxonomy):
    msgs = []
    dom = e.get("domain")
    for key in ("name", "domain", "description", "resources"):
        if not e.get(key):
            msgs.append(("FAIL", f"missing required key: {key}"))
    if dom and dom not in taxonomy:
        msgs.append(("FAIL", f"unknown domain '{dom}' (see taxonomy.yaml)"))
    area = e.get("area")
    if not area:
        msgs.append(("FAIL", "missing 'area'"))
    elif dom in taxonomy and area not in taxonomy[dom]:
        msgs.append(("FAIL", f"area '{area}' is not listed under {dom} in taxonomy.yaml ({', '.join(taxonomy[dom])})"))
    d = e.get("first_release_date")
    if d in (None, ""):
        msgs.append(("WARN", "first_release_date is empty"))
    elif not DATE_RE.match(str(d)):
        msgs.append(("FAIL", f"first_release_date '{d}' is not YYYY, YYYY-MM or YYYY-MM-DD"))
    words = len(str(e.get("description") or "").split())
    if words > 60:
        msgs.append(("WARN", f"description is {words} words (aim for under 45)"))
    if dom == "Simulation":
        for key in ("physics_engine", "renderer", "os", "license"):
            if not e.get(key):
                msgs.append(("WARN", f"simulator entry is missing '{key}'"))
        if not isinstance(e.get("gpu_support"), bool):
            msgs.append(("WARN", "simulator entry: gpu_support should be true or false"))
    else:
        setting = e.get("setting") or []
        if not setting or any(s not in SETTINGS for s in setting):
            msgs.append(("FAIL", f"setting must be [sim], [real] or [sim, real]; got {setting}"))
        if not e.get("modality"):
            msgs.append(("WARN", "modality list is empty"))
        for key in ("task_count", "robot_config_count"):
            if e.get(key) in (None, ""):
                msgs.append(("WARN", f"{key} is empty (a number, a short string, or 'N/A')"))
        if e.get("metric_count") in (None, "") and not e.get("metrics"):
            msgs.append(("WARN", "metric_count is empty"))
        method = (e.get("data_source") or {}).get("collection_method")
        if method not in COLLECTION:
            msgs.append(("FAIL", f"data_source.collection_method '{method}' is not one of {sorted(COLLECTION)}"))
        if "sim" in setting and not e.get("sim_backend"):
            msgs.append(("WARN", "setting includes sim but sim_backend is empty"))
        for key in ("task_count", "metric_count", "robot_config_count", "sim_backend"):
            if len(str(e.get(key) or "")) > 90:
                msgs.append(("WARN", f"{key} is {len(str(e.get(key)))} characters; it is a table cell, keep it short"))
        if len(str((e.get("data_source") or {}).get("size") or "")) > 110:
            msgs.append(("WARN", "data_source.size is long; it is a table cell, keep it short"))
    res = e.get("resources") or {}
    if not any(res.get(k) for k in ("paper", "homepage", "code")):
        msgs.append(("FAIL", "resources needs at least one of paper / homepage / code"))
    for key, value in res.items():
        if value not in (None, "") and not URL_RE.match(str(value)):
            msgs.append(("FAIL", f"resources.{key} is not a bare URL: '{value}'"))
    return msgs


def main():
    net = "--no-net" not in sys.argv
    paths = [Path(a) for a in sys.argv[1:] if not a.startswith("--")]
    full_run = not paths
    files = sorted(BENCH.glob("*.yaml")) if full_run else paths
    tax = yaml.safe_load(TAXONOMY.read_text(encoding="utf-8"))
    taxonomy = {d["key"]: [a["key"] for a in d.get("areas", [])] for d in tax["domains"]}

    entries, report = {}, {}
    for f in files:
        try:
            entries[f] = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
        except Exception as ex:
            report[f] = [("FAIL", f"YAML does not parse: {str(ex)[:200]}")]
            continue
        report[f] = check_schema(entries[f], taxonomy)

    seen = {}
    for f, e in entries.items():
        key = norm(e.get("name"))
        if key in seen:
            report[f].append(("FAIL", f"same name as {seen[key].name}"))
        seen[key] = f

    stars = {}
    if net:
        arxiv_ids, repos, others = set(), set(), set()
        for e in entries.values():
            for value in (e.get("resources") or {}).values():
                value = str(value or "")
                if not URL_RE.match(value):
                    continue
                a, g = ARXIV_RE.search(value), GITHUB_RE.match(value)
                if a:
                    arxiv_ids.add(a.group(1))
                elif g and g.group(1).lower() not in ("orgs", "topics"):
                    repos.add((g.group(1), re.sub(r"\.git$", "", g.group(2))))
                else:
                    others.add(value)
        token = github_token()
        with ThreadPoolExecutor(4) as pool:
            ids = sorted(arxiv_ids)
            arxiv_info = dict(zip(ids, pool.map(arxiv_lookup, ids)))
        with ThreadPoolExecutor(8) as pool:
            repo_list = sorted(repos)
            repo_info = dict(zip(repo_list, pool.map(lambda r: github_lookup(r[0], r[1], token), repo_list)))
            other_list = sorted(others)
            other_info = dict(zip(other_list, pool.map(check_url, other_list)))

        for f, e in entries.items():
            msgs = report[f]
            name = str(e.get("name") or "")
            for key, value in (e.get("resources") or {}).items():
                value = str(value or "")
                if not URL_RE.match(value):
                    continue
                a, g = ARXIV_RE.search(value), GITHUB_RE.match(value)
                if a:
                    info = arxiv_info[a.group(1)]
                    if "error" in info:
                        msgs.append(("FAIL", f"{key}: arXiv {a.group(1)}: {info['error']}"))
                        continue
                    haystack = norm(info["title"] + " " + info["summary"])
                    hit = norm(name) in haystack or any(norm(t) in haystack for t in tokens(name))
                    note = "" if hit else "  <-- the entry name does not appear in the title or abstract: wrong paper?"
                    msgs.append(("INFO" if hit else "FAIL",
                                 f"{key}: arXiv {a.group(1)} = \"{info['title']}\" "
                                 f"({info['first_author']} et al., submitted {info['published']}){note}"))
                elif g and g.group(1).lower() not in ("orgs", "topics"):
                    owner, repo = g.group(1), re.sub(r"\.git$", "", g.group(2))
                    info = repo_info[(owner, repo)]
                    if "error" in info:
                        msgs.append(("FAIL", f"{key}: GitHub {owner}/{repo}: {info['error']}"))
                        continue
                    flags = []
                    if (info["full_name"] or "").lower() != f"{owner}/{repo}".lower():
                        flags.append(f"renamed to {info['full_name']}: update the URL")
                    if info["archived"]:
                        flags.append("archived")
                    msgs.append(("WARN" if flags else "INFO",
                                 f"{key}: GitHub {info['full_name']} ★{info['stars']}, last push {info['pushed_at']}"
                                 + (" | " + "; ".join(flags) if flags else "")))
                    if key == "code" and info["stars"] is not None:
                        stars[f"{owner}/{repo}".lower()] = info["stars"]
                else:
                    code = other_info[value]
                    if code[:1] in ("2", "3"):
                        msgs.append(("INFO", f"{key}: HTTP {code} {value}"))
                    elif code in BLOCKED:
                        msgs.append(("WARN", f"{key}: HTTP {code} {value} (the site refuses scripts; open it in a browser to confirm)"))
                    else:
                        msgs.append(("FAIL", f"{key}: HTTP {code} {value} (dead or mistyped link)"))

    quiet = "--quiet" in sys.argv
    n_fail = n_warn = 0
    for f in files:
        msgs = report.get(f, [])
        worst = "FAIL" if any(m[0] == "FAIL" for m in msgs) else "WARN" if any(m[0] == "WARN" for m in msgs) else "OK"
        n_fail += worst == "FAIL"
        n_warn += worst == "WARN"
        if quiet and worst == "OK":
            continue
        print(f"\n[{worst}] {f.name}  --  {entries.get(f, {}).get('name', '?')}")
        for level, text in msgs:
            if quiet and level == "INFO":
                continue
            print(f"    {level:4s} {text}")
    print(f"\n==== {len(files)} files: {n_fail} FAIL, {n_warn} WARN, {len(files) - n_fail - n_warn} OK ====")

    if net and full_run and stars:
        STARS.write_text(json.dumps({"as_of": date.today().isoformat(), "stars": dict(sorted(stars.items()))}, indent=1) + "\n",
                         encoding="utf-8")
        print(f"Refreshed {STARS.relative_to(ROOT)} ({len(stars)} repositories).")
    sys.exit(1 if n_fail else 0)


if __name__ == "__main__":
    main()
