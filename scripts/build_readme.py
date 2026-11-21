#!/usr/bin/env python3
"""Build README.md from benchmarks/*.yaml and taxonomy.yaml.

    pip install pyyaml
    python scripts/build_readme.py

The README is generated: edit the YAML files, never the README itself.
GitHub star counts come from scripts/github_stars.json, which
scripts/validate.py refreshes. The build itself needs no network.
"""
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
BENCH = ROOT / "benchmarks"
README = ROOT / "README.md"
TAXONOMY = ROOT / "taxonomy.yaml"
STARS = ROOT / "scripts" / "github_stars.json"
ASSETS = ROOT / "assets"

NEW_WINDOW_MONTHS = 12
SETTING_LABEL = {("sim",): "Sim", ("real",): "Real", ("real", "sim"): "Sim + Real"}
SOURCE_LABEL = {
    "human_demonstration": "Human demos",
    "human_annotation": "Human labels",
    "motion_planner": "Planner",
    "synthetic": "Synthetic",
    "rl_policy": "RL policy",
    "mixed": "Mixed",
    "both": "Mixed",
    "none": "-",
    "n/a": "-",
    "unknown": "Not stated",
}
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


# ---------------------------------------------------------------- helpers

def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", str(text).lower()).strip("-")


def clean(value):
    """Collapse whitespace; None becomes an empty string."""
    if value is None:
        return ""
    return " ".join(str(value).split())


def parse_date(value):
    """Return (date, precision) where precision is 'day', 'month' or 'year'."""
    if value in (None, ""):
        return None, None
    if isinstance(value, datetime):
        return value.date(), "day"
    if isinstance(value, date):
        return value, "day"
    text = str(value).strip()
    for fmt, precision in (("%Y-%m-%d", "day"), ("%Y-%m", "month"), ("%Y", "year")):
        try:
            return datetime.strptime(text, fmt).date(), precision
        except ValueError:
            continue
    return None, None


def cell(value):
    """Make a value safe inside a Markdown table cell."""
    text = clean(value)
    return text.replace("|", "\\|") if text else "-"


def compact(text, limit):
    """Shorten a table cell: when it is longer than `limit`, drop the bracketed detail, then any second clause.

    The full text stays in the YAML file; the table is for comparing at a glance.
    """
    if len(text) <= limit:
        return text
    cut = re.sub(r"\s*\([^()]*\)\s*$", "", text)
    if len(cut) > limit:
        cut = re.split(r";\s", cut)[0]
    if len(cut) > limit:
        cut = re.sub(r"\s*\([^()]*\)", "", cut)
    return cut.strip() or text


def short_tags(text, limit=40):
    """Subtype cell: keep the leading tags that fit in `limit` characters (always at least one)."""
    tags = [t.strip() for t in text.split(",") if t.strip()]
    kept = []
    for tag in tags:
        if kept and len(", ".join(kept + [tag])) > limit:
            break
        kept.append(tag)
    return ", ".join(kept)


def count_cell(entry, count_key, list_key):
    """A count field, falling back to the length of a list field."""
    value = entry.get(count_key)
    if value in (None, ""):
        items = entry.get(list_key) or []
        if not items:
            return ""
        return f"{len(items)} ({', '.join(str(i).replace('_', ' ') for i in items)})"
    return clean(value)


def fmt_stars(n):
    if n >= 1000:
        return f"{n / 1000:.1f}".rstrip("0").rstrip(".") + "k"
    return str(n)


def repo_key(url):
    m = re.match(r"https?://github\.com/([^/\s]+)/([^/\s#?]+)", url or "")
    return f"{m.group(1)}/{re.sub(r'[.]git$', '', m.group(2))}".lower() if m else None


def months_back(day, months):
    index = day.year * 12 + (day.month - 1) - months
    return date(index // 12, index % 12 + 1, 1)


# ---------------------------------------------------------------- loading

def load_taxonomy():
    data = yaml.safe_load(TAXONOMY.read_text(encoding="utf-8"))
    domains = []
    for d in data["domains"]:
        domains.append({
            "key": d["key"],
            "title": d.get("title", d["key"]),
            "blurb": clean(d.get("blurb")),
            "start_here_note": clean(d.get("start_here_note")),
            "areas": [{"key": a["key"], "title": a.get("title", a["key"])} for a in d.get("areas", [])],
        })
    return domains


def load_entries(today):
    stars = {}
    stars_as_of = ""
    if STARS.exists():
        blob = json.loads(STARS.read_text(encoding="utf-8"))
        stars = {k.lower(): v for k, v in blob.get("stars", {}).items()}
        stars_as_of = blob.get("as_of", "")
    new_since = months_back(today, NEW_WINDOW_MONTHS)

    entries = []
    for path in sorted(BENCH.glob("*.yaml")):
        raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        day, precision = parse_date(raw.get("first_release_date"))
        res = {k: clean(v) for k, v in (raw.get("resources") or {}).items()}
        source = raw.get("data_source") or {}
        setting = tuple(sorted(clean(s).lower() for s in (raw.get("setting") or [])))
        os_field = raw.get("os") or []
        entries.append({
            "file": path.name,
            "name": clean(raw.get("name")),
            "domain": clean(raw.get("domain")) or "Other",
            "area": clean(raw.get("area")),
            "subtype": clean(raw.get("subtype")),
            "date": day,
            "precision": precision,
            "venue": clean(raw.get("venue")),
            "widely_used": bool(raw.get("widely_used")),
            "is_new": bool(day and day >= new_since),
            "description": clean(raw.get("description")),
            "task_count": count_cell(raw, "task_count", "tasks"),
            "metric_count": count_cell(raw, "metric_count", "metrics"),
            "robot_config_count": count_cell(raw, "robot_config_count", "robot_config"),
            "modality": ", ".join(clean(m) for m in (raw.get("modality") or [])),
            "setting": SETTING_LABEL.get(setting, ""),
            "sim_backend": clean(raw.get("sim_backend")),
            "source": SOURCE_LABEL.get(clean(source.get("collection_method")).lower(), clean(source.get("collection_method"))),
            "data_size": clean(source.get("size")),
            "res": res,
            "stars": stars.get(repo_key(res.get("code")) or "", None),
            "physics_engine": clean(raw.get("physics_engine")),
            "renderer": clean(raw.get("renderer")),
            "gpu_support": raw.get("gpu_support"),
            "os": ", ".join(os_field) if isinstance(os_field, list) else clean(os_field),
            "license": clean(raw.get("license")),
        })

    # Short names for index lists and table cells: drop a trailing "(...)" unless that makes two names equal.
    shorts = {}
    for e in entries:
        e["short"] = re.sub(r"\s*\([^)]*\)$", "", e["name"]) or e["name"]
        shorts.setdefault(e["short"].lower(), []).append(e)
    for group_ in shorts.values():
        if len(group_) > 1:
            for e in group_:
                e["short"] = e["name"]

    seen = {}
    for e in entries:
        if not e["name"]:
            sys.exit(f"{e['file']}: missing name")
        e["anchor"] = slug(e["name"])
        if e["anchor"] in seen:
            sys.exit(f"{e['file']} and {seen[e['anchor']]} produce the same anchor '{e['anchor']}': rename one")
        seen[e["anchor"]] = e["file"]
    return entries, stars_as_of, new_since


def sort_key(e):
    return (e["date"] or date.max, e["name"].lower())


def group(entries, domains):
    """Return [(domain, [(area, [entries])])] in taxonomy order, skipping empty groups."""
    known = {d["key"] for d in domains}
    extra = sorted({e["domain"] for e in entries} - known)
    layout = []
    for d in domains + [{"key": k, "title": k, "blurb": "", "start_here_note": "", "areas": []} for k in extra]:
        mine = [e for e in entries if e["domain"] == d["key"]]
        if not mine:
            continue
        area_keys = [a["key"] for a in d["areas"]]
        areas = []
        for a in d["areas"]:
            rows = sorted((e for e in mine if e["area"] == a["key"]), key=sort_key)
            if rows:
                areas.append((a, rows))
        rest = sorted((e for e in mine if e["area"] not in area_keys), key=sort_key)
        if rest:
            areas.append(({"key": "general", "title": "General"}, rest))
        layout.append((d, areas))
    return layout


# ---------------------------------------------------------------- rendering

def entry_block(e, stars_shown):
    year = f" ({e['date'].year})" if e["date"] else ""
    tags = []
    if e["setting"]:
        tags.append(f"`{e['setting']}`")
    if e["widely_used"]:
        tags.append("`widely used`")
    if e["is_new"]:
        tags.append("`new`")
    head = f"- <a id=\"{e['anchor']}\"></a>**{e['name']}**{year}"
    if tags:
        head += " " + " ".join(tags)
    res = e["res"]
    links = []
    if res.get("paper"):
        venue = e["venue"]
        show_venue = venue and not venue.lower().startswith("arxiv")
        links.append(f"[Paper]({res['paper']})" + (f" ({venue})" if show_venue else ""))
    if res.get("homepage"):
        links.append(f"[Website]({res['homepage']})")
    if res.get("code"):
        star = f" ★{fmt_stars(e['stars'])}" if stars_shown and e["stars"] is not None else ""
        links.append(f"[Code]({res['code']}){star}")
    if res.get("docs"):
        links.append(f"[Docs]({res['docs']})")
    if res.get("data"):
        links.append(f"[Data]({res['data']})")
    if res.get("leaderboard"):
        links.append(f"[Leaderboard]({res['leaderboard']})")
    block = f"{head}: {e['description']}"
    if links:
        block += "<br>\n  *Resources*: " + " | ".join(links)
    return block


def name_cell(e):
    link = f"[{e['short']}](#{e['anchor']})"
    return f"**{link}**" if e["widely_used"] else link


def sim_cell(e):
    """The SIM column: the simulator backend, and whether the benchmark also (or only) runs in the real world."""
    backend = cell(e["sim_backend"])
    if e["setting"] == "Real":
        return "Real world"
    if e["setting"] == "Sim + Real":
        return "Real world" if backend == "-" else f"{backend} + real"
    return backend


def summary_table(rows, simulators):
    if simulators:
        lines = ["| Simulator | Physics Engine | Renderer | GPU Support | OS | License |",
                 "|---|---|---|:---:|---|---|"]
        for e in rows:
            gpu = "✓" if e["gpu_support"] is True else "✗" if e["gpu_support"] is False else "-"
            cells = [name_cell(e), cell(e["physics_engine"]), cell(e["renderer"]), gpu, cell(e["os"]), cell(e["license"])]
            lines.append("| " + " | ".join(cells) + " |")
    else:
        lines = ["| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |",
                 "|---|---|---|---|---|---|---|---|---|"]
        for e in rows:
            cells = [name_cell(e), cell(short_tags(e["subtype"])), cell(compact(e["task_count"], 32)),
                     cell(compact(e["metric_count"], 24)), cell(compact(e["robot_config_count"], 40)),
                     cell(e["modality"]), sim_cell(e), cell(e["source"]), cell(e["data_size"])]
            lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


# ---------------------------------------------------------------- chart

CHART_INK = {
    #          column     labels     axis text  gridline   baseline
    "light": ("#2a78d6", "#52514e", "#6e6d68", "#e1e0d9", "#c3c2b7"),
    "dark":  ("#3987e5", "#c3c2b7", "#9a9993", "#2c2c2a", "#484844"),
}
CHART_FIRST_YEAR = 2017     # earlier years are folded into one "up to" column


def year_counts(entries):
    """[(label, count)] per year of first release; years up to CHART_FIRST_YEAR share one column."""
    years = [e["date"].year for e in entries if e["date"]]
    if not years:
        return []
    bins = [(f"≤{CHART_FIRST_YEAR}", sum(y <= CHART_FIRST_YEAR for y in years))]
    for y in range(CHART_FIRST_YEAR + 1, max(years) + 1):
        bins.append((str(y), years.count(y)))
    return bins


def chart_svg(bins, mode):
    """A single-series column chart as a standalone SVG string."""
    bar, ink, axis_ink, grid, base = CHART_INK[mode]
    width, height = 760, 250
    left, right, top, bottom = 46, 14, 26, 34
    plot_w, plot_h = width - left - right, height - top - bottom
    peak = max(c for _, c in bins)
    step = next(s for s in (1, 2, 5, 10, 20, 25, 50, 100, 200, 500) if peak / s <= 5)
    y_max = step * -(-peak // step)
    band = plot_w / len(bins)
    bar_w = min(24, band * 0.6)
    y0 = top + plot_h
    font = "font-family=\"system-ui, -apple-system, 'Segoe UI', sans-serif\""
    summary = ", ".join(f"{label}: {count}" for label, count in bins)
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" '
         f'role="img" aria-labelledby="t d">',
         "<title id=\"t\">Entries in this list by year of first release</title>",
         f"<desc id=\"d\">{summary}</desc>"]
    for tick in range(0, y_max + 1, step):
        y = y0 - plot_h * tick / y_max
        if tick:
            p.append(f'<line x1="{left}" x2="{width - right}" y1="{y:.1f}" y2="{y:.1f}" stroke="{grid}" stroke-width="1"/>')
        p.append(f'<text x="{left - 8}" y="{y + 4:.1f}" text-anchor="end" font-size="11" fill="{axis_ink}" {font}>{tick}</text>')
    labelled = {max(range(len(bins)), key=lambda i: bins[i][1]), len(bins) - 1}
    for i, (label, count) in enumerate(bins):
        cx = left + band * (i + 0.5)
        h = plot_h * count / y_max
        x, y, r = cx - bar_w / 2, y0 - h, min(4, h)
        if count:
            p.append(f'<path d="M{x:.1f},{y0} V{y + r:.1f} Q{x:.1f},{y:.1f} {x + r:.1f},{y:.1f} H{x + bar_w - r:.1f} '
                     f'Q{x + bar_w:.1f},{y:.1f} {x + bar_w:.1f},{y + r:.1f} V{y0} Z" fill="{bar}"/>')
        if i in labelled:
            p.append(f'<text x="{cx:.1f}" y="{y - 7:.1f}" text-anchor="middle" font-size="12" font-weight="600" fill="{ink}" {font}>{count}</text>')
        p.append(f'<text x="{cx:.1f}" y="{y0 + 20}" text-anchor="middle" font-size="12" fill="{axis_ink}" {font}>{label}</text>')
    p.append(f'<line x1="{left}" x2="{width - right}" y1="{y0}" y2="{y0}" stroke="{base}" stroke-width="1"/>')
    p.append("</svg>")
    return "\n".join(p) + "\n"


def write_charts(entries, today):
    """Write the light and dark chart files; return the Markdown that shows them, or '' if there is no data."""
    bins = year_counts(entries)
    if not bins:
        return ""
    ASSETS.mkdir(exist_ok=True)
    for mode in ("light", "dark"):
        (ASSETS / f"entries-by-year-{mode}.svg").write_text(chart_svg(bins, mode), encoding="utf-8")
    partial = f" {today.year} is the year so far." if bins[-1][0] == str(today.year) else ""
    alt = "Column chart of the entries in this list by year of first release. " + \
          ", ".join(f"{label}: {count}" for label, count in bins) + "."
    return ('<p align="center">\n<picture>\n'
            '  <source media="(prefers-color-scheme: dark)" srcset="assets/entries-by-year-dark.svg">\n'
            f'  <img src="assets/entries-by-year-light.svg" alt="{alt}" width="760">\n'
            '</picture>\n<br>\n'
            f'<em>Entries in this list by year of first release.{partial}</em>\n</p>\n')


def when(e):
    if not e["date"]:
        return ""
    if e["precision"] == "year":
        return str(e["date"].year)
    return f"{MONTHS[e['date'].month - 1]} {e['date'].year}"


def build(today):
    domains = load_taxonomy()
    entries, stars_as_of, new_since = load_entries(today)
    layout = group(entries, domains)
    total = len(entries)
    n_sim = sum(e["domain"] == "Simulation" for e in entries)
    stars_shown = bool(stars_as_of)

    def d_anchor(d):
        return slug(d["key"])

    def a_anchor(d, a):
        return f"{slug(d['key'])}-{slug(a['key'])}"

    used = {e["anchor"] for e in entries}
    for d, areas in layout:
        for anchor in [d_anchor(d)] + [a_anchor(d, a) for a, _ in areas]:
            if anchor in used:
                sys.exit(f"anchor '{anchor}' is used twice (a benchmark name collides with a section name)")
            used.add(anchor)

    out = []
    w = out.append

    # ---- header
    stamp = today.isoformat()
    w('<div align="center">\n')
    w("# Awesome Robotics Benchmarks\n")
    w("**A curated, domain-organized map of robotics benchmarks, summarized in concise, comparable tables.**\n")
    w("Manipulation · Dexterous hands · VLA evaluation · World models · Embodied reasoning · Navigation · "
      "Humanoids · Datasets · Simulators · HRI · Safety\n")
    w("[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) "
      f"![{total} entries](https://img.shields.io/badge/entries-{total}-1f6feb) "
      f"![{len(layout)} domains](https://img.shields.io/badge/domains-{len(layout)}-1f6feb) "
      f"![Last updated {stamp}](https://img.shields.io/badge/updated-{stamp.replace('-', '--')}-2da44e) "
      "[![Pull requests welcome](https://img.shields.io/badge/PRs-welcome-2da44e)](#contributing)\n")
    w("</div>\n")

    w(f"This list covers **{total - n_sim} benchmarks and datasets and {n_sim} simulators in {len(layout)} domains**, "
      "from the standard suites that most papers report on to small niche areas, in simulation and on real robots. "
      "Every entry has a short description, its links (paper, website, code, data, leaderboard) and a row in a "
      "comparison table: tasks, metrics, robots, sensing modalities, simulator and data.\n")
    w("Domains run from the most widely used areas to the smaller ones. Inside each sub-area, entries are in order "
      "of first release.\n")
    w("**New to the field?** Go to [Start here](#start-here). "
      "**Keeping up?** Go to [What's new](#whats-new).\n")

    # ---- contents
    w('## <a id="contents"></a>Contents\n')
    w("| Domain | Sub-areas | Entries |")
    w("|---|---|---:|")
    for d, areas in layout:
        subs = " · ".join(f"[{a['title']}](#{a_anchor(d, a)})" for a, _ in areas)
        w(f"| **[{d['title']}](#{d_anchor(d)})** | {subs} | {sum(len(r) for _, r in areas)} |")
    w("")
    w("Also on this page: [Start here](#start-here) · [What's new](#whats-new) · "
      "[How to read this list](#how-to-read-this-list) · [Contributing](#contributing)\n")

    # ---- start here
    w('## <a id="start-here"></a>Start here\n')
    w("The benchmarks that a large share of papers in each area report on. If you are choosing where to evaluate, "
      "these are the ones reviewers will expect.\n")
    w("| Domain | Most widely used |")
    w("|---|---|")
    for d, areas in layout:
        lines = []
        for a, rows in areas:
            picks = [e for e in rows if e["widely_used"]]
            if picks:
                label = f"**{a['title']}:** " if len(areas) > 1 else ""
                lines.append(label + " · ".join(f"[{e['short']}](#{e['anchor']})" for e in picks))
        if d["start_here_note"]:
            lines.append(f"*{d['start_here_note']}*")
        if lines:
            w(f"| [{d['title']}](#{d_anchor(d)}) | " + "<br>".join(lines) + " |")
    w("")

    # ---- what's new
    w('## <a id="whats-new"></a>What\'s new\n')
    w(f"First released since {MONTHS[new_since.month - 1]} {new_since.year} (the last {NEW_WINDOW_MONTHS} months), newest first.\n")
    chart = write_charts(entries, today)
    if chart:
        w(chart)
    any_new = False
    for d, areas in layout:
        fresh = sorted((e for _, rows in areas for e in rows if e["is_new"]), key=sort_key, reverse=True)
        if fresh:
            any_new = True
            w(f"- **{d['title']}:** " + " · ".join(f"[{e['short']}](#{e['anchor']}) ({when(e)})" for e in fresh))
    if not any_new:
        w("Nothing in this window yet.")
    w("")

    # ---- legend
    w('## <a id="how-to-read-this-list"></a>How to read this list\n')
    w("Every entry has the same shape:\n")
    w("> **Name** (year of first release) `Sim` `widely used` `new`: what it evaluates and what sets it apart.<br>\n"
      "> *Resources*: Paper (venue) | Website | Code ★stars | Data | Leaderboard\n")
    w("- `Sim`, `Real`, `Sim + Real`: where the evaluation runs.")
    w("- `widely used`: a de-facto standard of its sub-area. Its name is bold in the tables.")
    w(f"- `new`: first released in the last {NEW_WINDOW_MONTHS} months.")
    if stars_shown:
        w(f"- ★: GitHub stars of the code repository, as of {stars_as_of}.")
    w("")
    w("Each sub-area ends with a **summary comparison** table, one row per entry. "
      "Click a name in a table to jump to its description.\n")
    w("<details>\n<summary><b>What the table columns mean</b></summary>\n")
    w("- **Subtype**: short tags for what sets the benchmark apart.")
    w("- **Task Count, Metric Count, Robot Configs**: recorded as numbers, with the names in brackets when they are short. "
      "Longer details are in the description and in the entry's YAML file.")
    w("- **Modality**: what the benchmark provides as observations (RGB, depth, point cloud, proprioception, language, tactile, ...).")
    w("- **SIM**: the simulator backend (for example MuJoCo, SAPIEN, Isaac Sim). \"Real world\" means the benchmark runs "
      "on real hardware or real recordings only; \"+ real\" means it has both a simulated and a real-world part.")
    w("- **Data Source**: how the trajectories or labels that ship with the benchmark were collected.")
    w("  - *Human demos* (human demonstration): recorded from a person controlling the robot or simulator (teleoperation, VR, kinesthetic teaching) or from human motion capture.")
    w("  - *Human labels* (human annotation): people wrote the questions or labels over existing sensor data.")
    w("  - *Planner* (motion planner): generated by a planner, inverse kinematics, a trajectory optimizer or a scripted expert.")
    w("  - *Synthetic*: generated programmatically or by generative models, with no physics-aware planner and no human.")
    w("  - *RL policy*: rollouts of trained reinforcement-learning policies.")
    w("  - *Mixed*: more than one of the above. A dash means the benchmark ships no data.")
    w("- **Data Size**: what ships with the benchmark.")
    w("- In the **Simulators** section the table compares capabilities instead: physics engine, renderer, GPU support "
      "(✓ only when the physics itself runs on the GPU for parallel environments), operating systems and license.")
    w("\n</details>\n")
    w("**Abbreviations**: VLA, vision-language-action model. VLN, vision-language navigation. WAM, world-action model "
      "(a policy that predicts future observations together with actions). EQA, embodied question answering. "
      "HRI, human-robot interaction.\n")

    # ---- domains
    for d, areas in layout:
        simulators = d["key"] == "Simulation"
        n = sum(len(rows) for _, rows in areas)
        noun = "simulators" if simulators else "entries"
        w("---\n")
        w(f"## <a id=\"{d_anchor(d)}\"></a>{d['title']}\n")
        w(f"{d['blurb']} **{n} {noun}.**\n" if d["blurb"] else f"**{n} {noun}.**\n")
        if len(areas) > 1:
            w("**Sub-areas:** " + " · ".join(f"[{a['title']}](#{a_anchor(d, a)}) ({len(rows)})" for a, rows in areas) + "\n")
        for a, rows in areas:
            w(f"### <a id=\"{a_anchor(d, a)}\"></a>{a['title']}\n")
            for e in rows:
                w(entry_block(e, stars_shown))
                w("")
            w("**Summary comparison**\n")
            w(summary_table(rows, simulators))
            w("")
        w('<p align="right"><a href="#contents">Back to contents ↑</a></p>\n')

    # ---- contributing
    w("---\n")
    w('## <a id="contributing"></a>Contributing\n')
    w("Additions and corrections are both welcome.\n")
    w("This README is generated. Each entry is one YAML file in [`benchmarks/`](benchmarks/), the sections come from "
      "[`taxonomy.yaml`](taxonomy.yaml), and [`scripts/build_readme.py`](scripts/build_readme.py) writes the page. "
      "To add or fix an entry, edit the YAML file and rebuild; do not edit the README by hand. "
      "[CONTRIBUTING.md](CONTRIBUTING.md) has the template and the steps.\n")
    w("Found a wrong number or a dead link? Open an issue or a pull request with the source.\n")

    README.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    print(f"Built README.md: {total} entries in {len(layout)} domains "
          f"({sum(e['is_new'] for e in entries)} new, {sum(e['widely_used'] for e in entries)} widely used).")


def main():
    today = date.today()
    if "--today" in sys.argv:
        today = datetime.strptime(sys.argv[sys.argv.index("--today") + 1], "%Y-%m-%d").date()
    build(today)


if __name__ == "__main__":
    main()
