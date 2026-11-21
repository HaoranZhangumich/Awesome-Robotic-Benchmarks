<div align="center">

# Awesome Robotics Benchmarks

**A curated, domain-organized map of robotics benchmarks, summarized in concise, comparable tables.**

Manipulation · Dexterous hands · VLA evaluation · World models · Embodied reasoning · Navigation · Humanoids · Datasets · Simulators · HRI · Safety

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![361 entries](https://img.shields.io/badge/entries-361-1f6feb) ![13 domains](https://img.shields.io/badge/domains-13-1f6feb) ![Last updated 2026-11-21](https://img.shields.io/badge/updated-2026--11--21-2da44e) [![Pull requests welcome](https://img.shields.io/badge/PRs-welcome-2da44e)](#contributing)

</div>

This list covers **331 benchmarks and datasets and 30 simulators in 13 domains**, from the standard suites that most papers report on to small niche areas, in simulation and on real robots. Every entry has a short description, its links (paper, website, code, data, leaderboard) and a row in a comparison table: tasks, metrics, robots, sensing modalities, simulator and data.

Domains run from the most widely used areas to the smaller ones. Inside each sub-area, entries are in order of first release.

**New to the field?** Go to [Start here](#start-here). **Keeping up?** Go to [What's new](#whats-new).

## <a id="contents"></a>Contents

| Domain | Sub-areas | Entries |
|---|---|---:|
| **[Manipulation](#manipulation)** | [Tabletop & Language-Conditioned](#manipulation-tabletop) · [Bimanual](#manipulation-bimanual) · [Mobile & Household](#manipulation-mobile) · [Assembly & Contact-Rich](#manipulation-contact-rich) · [Articulated Objects](#manipulation-articulated) · [Deformable Objects & Garments](#manipulation-deformable) · [Tactile](#manipulation-tactile) · [Grasping](#manipulation-grasping) | 64 |
| **[Dexterous Manipulation](#dexterous-manipulation)** | [In-Hand & Dexterous Skills](#dexterous-manipulation-dex-manipulation) · [Bimanual Dexterity](#dexterous-manipulation-dex-bimanual) · [Dexterous Grasping](#dexterous-manipulation-dex-grasping) · [Human Hand-Object Data](#dexterous-manipulation-hand-object-data) | 41 |
| **[Generalist Policies & VLA Evaluation](#generalist)** | [Multi-Domain Suites](#generalist-multi-domain) · [Real-World Evaluation](#generalist-real-eval) · [Real-to-Sim Evaluation](#generalist-real2sim) · [Generalization, Robustness & Memory Probes](#generalist-probes) | 27 |
| **[World Models & World-Action Models](#world-models)** | [Embodied World Models](#world-models-wm-embodied) · [Policy Evaluation with World Models & WAM Benchmarks](#world-models-wm-policy-eval) · [Physical Plausibility of Generated Video](#world-models-wm-physics) | 26 |
| **[Embodied Reasoning](#embodied-reasoning)** | [Spatial & Physical Reasoning](#embodied-reasoning-spatial) · [Task Planning & Agents](#embodied-reasoning-planning) · [Embodied Question Answering](#embodied-reasoning-eqa) | 24 |
| **[Navigation](#navigation)** | [Point, Object & Image-Goal Navigation](#navigation-goal-nav) · [Vision-Language Navigation (VLN)](#navigation-vln) · [Interactive Instruction Following](#navigation-interactive) · [Social Navigation](#navigation-social) · [Outdoor, Urban & Aerial](#navigation-outdoor) | 35 |
| **[Locomotion & Humanoids](#locomotion)** | [Classic Continuous Control](#locomotion-continuous-control) · [Legged Locomotion](#locomotion-legged) · [Humanoid & Whole-Body Control](#locomotion-humanoid) · [Motion Data for Humanoids](#locomotion-motion-data) | 28 |
| **[Robot Learning Datasets](#datasets)** | [Robot Datasets](#datasets-robot-data) · [Egocentric & Human Data](#datasets-human-data) | 32 |
| **[Simulators](#simulation)** | [Physics Engines & General Simulators](#simulation-physics) · [Robot-Learning Frameworks](#simulation-learning-framework) · [Embodied-AI Platforms](#simulation-embodied-platform) · [Specialized Simulators](#simulation-specialized) | 30 |
| **[Human-Robot Interaction](#hri)** | [Assistive & Physical HRI](#hri-assistive) · [Handover](#hri-handover) · [Human-Robot Collaboration](#hri-collaboration) | 11 |
| **[Safety](#safety)** | [Safe RL & Control](#safety-safe-rl) · [Safety of LLM / VLA Agents](#safety-embodied-safety) | 16 |
| **[Autonomous Driving](#autonomous-driving)** | [Datasets & Open-Loop Benchmarks](#autonomous-driving-driving-data) · [Closed-Loop Simulation](#autonomous-driving-driving-closed-loop) | 11 |
| **[Other Areas](#other)** | [Offline RL & Data-Driven Control](#other-offline-rl) · [Aerial Robotics](#other-aerial) · [Multi-Robot](#other-multi-robot) · [Competitions](#other-competition) | 16 |

Also on this page: [Start here](#start-here) · [What's new](#whats-new) · [How to read this list](#how-to-read-this-list) · [Contributing](#contributing)

## <a id="start-here"></a>Start here

The benchmarks that a large share of papers in each area report on. If you are choosing where to evaluate, these are the ones reviewers will expect.

| Domain | Most widely used |
|---|---|
| [Manipulation](#manipulation) | **Tabletop & Language-Conditioned:** [RLBench](#rlbench) · [Meta-World](#meta-world) · [Franka Kitchen](#franka-kitchen) · [robomimic](#robomimic) · [CALVIN](#calvin) · [LIBERO](#libero)<br>**Bimanual:** [RoboTwin 2.0](#robotwin-2-0)<br>**Mobile & Household:** [RoboCasa](#robocasa)<br>**Assembly & Contact-Rich:** [NIST Assembly Task Boards](#nist-assembly-task-boards)<br>**Articulated Objects:** [PartNet-Mobility](#partnet-mobility-sapien)<br>**Deformable Objects & Garments:** [SoftGym](#softgym)<br>**Grasping:** [YCB Object and Model Set](#ycb-object-and-model-set) · [GraspNet-1Billion](#graspnet-1billion) |
| [Dexterous Manipulation](#dexterous-manipulation) | **In-Hand & Dexterous Skills:** [Adroit Hand](#adroit-hand-dapg) · [Shadow Dexterous Hand](#shadow-dexterous-hand-gymnasium-robotics)<br>**Bimanual Dexterity:** [Bi-DexHands](#bi-dexhands)<br>**Dexterous Grasping:** [DexGraspNet](#dexgraspnet)<br>**Human Hand-Object Data:** [HO-3D](#ho-3d) · [GRAB](#grab) · [DexYCB](#dexycb) · [ARCTIC](#arctic) |
| [Generalist Policies & VLA Evaluation](#generalist) | **Multi-Domain Suites:** [ManiSkill](#maniskill)<br>**Real-to-Sim Evaluation:** [SimplerEnv](#simplerenv-simpler) |
| [World Models & World-Action Models](#world-models) | **Physical Plausibility of Generated Video:** [PhyGenBench](#phygenbench) · [Physics-IQ](#physics-iq) · [VideoPhy-2](#videophy-2)<br>*No embodied world-model benchmark is a settled standard yet; these are the common physical-plausibility tests for video generators.* |
| [Embodied Reasoning](#embodied-reasoning) | **Spatial & Physical Reasoning:** [VSI-Bench](#vsi-bench) · [ERQA](#erqa-gemini-robotics)<br>**Task Planning & Agents:** [ALFWorld](#alfworld)<br>**Embodied Question Answering:** [OpenEQA](#openeqa) |
| [Navigation](#navigation) | **Point, Object & Image-Goal Navigation:** [AI2-THOR](#ai2-thor) · [Habitat Navigation Challenge](#habitat-navigation-challenge-pointnav-objectnav-imagenav)<br>**Vision-Language Navigation (VLN):** [R2R](#r2r-room-to-room) · [VLN-CE](#vln-ce-vision-and-language-navigation-in-continuous-environments) · [RxR](#rxr-room-across-room)<br>**Interactive Instruction Following:** [ALFRED](#alfred) |
| [Locomotion & Humanoids](#locomotion) | **Classic Continuous Control:** [Gymnasium MuJoCo](#gymnasium-mujoco-openai-gym) · [DeepMind Control Suite](#deepmind-control-suite)<br>**Legged Locomotion:** [legged_gym](#legged-gym)<br>**Motion Data for Humanoids:** [AMASS](#amass) · [LAFAN1](#lafan1) |
| [Robot Learning Datasets](#datasets) | **Robot Datasets:** [RT-1 Robot Action](#rt-1-robot-action-fractal) · [BridgeData V2](#bridgedata-v2) · [Open X-Embodiment](#open-x-embodiment) · [DROID](#droid) · [AgiBot World](#agibot-world)<br>**Egocentric & Human Data:** [EPIC-KITCHENS-100](#epic-kitchens-100) · [Ego4D](#ego4d) |
| [Simulators](#simulation) | **Physics Engines & General Simulators:** [Gazebo](#gazebo) · [MuJoCo](#mujoco) · [PyBullet](#pybullet) · [Isaac Sim](#isaac-sim) · [Isaac Gym](#isaac-gym)<br>**Robot-Learning Frameworks:** [Isaac Lab](#isaac-lab)<br>**Embodied-AI Platforms:** [Habitat-Sim](#habitat-sim) |
| [Human-Robot Interaction](#hri) | **Assistive & Physical HRI:** [Assistive Gym](#assistive-gym)<br>**Human-Robot Collaboration:** [Overcooked-AI](#overcooked-ai) |
| [Safety](#safety) | **Safe RL & Control:** [Safety Gym](#safety-gym) · [Safety-Gymnasium](#safety-gymnasium) |
| [Autonomous Driving](#autonomous-driving) | **Datasets & Open-Loop Benchmarks:** [KITTI](#kitti) · [nuScenes](#nuscenes) · [Waymo Open Dataset](#waymo-open-dataset)<br>**Closed-Loop Simulation:** [CARLA](#carla) |
| [Other Areas](#other) | **Offline RL & Data-Driven Control:** [D4RL](#d4rl) |

## <a id="whats-new"></a>What's new

First released since Nov 2025 (the last 12 months), newest first.

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/entries-by-year-dark.svg">
  <img src="assets/entries-by-year-light.svg" alt="Column chart of the entries in this list by year of first release. ≤2017: 18, 2018: 5, 2019: 15, 2020: 18, 2021: 21, 2022: 22, 2023: 33, 2024: 61, 2025: 98, 2026: 70." width="760">
</picture>
<br>
<em>Entries in this list by year of first release. 2026 is the year so far.</em>
</p>

- **Manipulation:** [ContactBench 1.0](#contactbench-1-0) (Oct 2026) · [SoftVTBench](#softvtbench) (Jul 2026) · [EBench](#ebench) (Jun 2026) · [DuoBench](#duobench) (Jun 2026) · [Tabero](#tabero) (May 2026) · [LeHome](#lehome) (Apr 2026) · [BiCoord](#bicoord) (Apr 2026) · [RoboCasa365](#robocasa365) (Mar 2026) · [MolmoSpaces](#molmospaces) (Feb 2026) · [UniVTAC](#univtac) (Feb 2026) · [RoboBenchMart](#robobenchmart) (Nov 2025) · [RoCo Challenge](#roco-challenge) (Nov 2025)
- **Dexterous Manipulation:** [HandsOn](#handson) (Oct 2026) · [BiDex-100](#bidex-100) (Oct 2026) · [V2D Challenge](#v2d-challenge-video-to-data) (Sep 2026) · [Bench2Dex](#bench2dex) (Sep 2026) · [DexVerse](#dexverse) (Jul 2026) · [DexJoCo](#dexjoco) (May 2026) · [HRDexDB](#hrdexdb) (Apr 2026) · [POMDAR](#pomdar) (Apr 2026)
- **Generalist Policies & VLA Evaluation:** [X2Real](#x2real) (Sep 2026) · [RoboDojo](#robodojo) (Jul 2026) · [Colosseum V2](#colosseum-v2) (May 2026) · [RoboLab](#robolab) (Apr 2026) · [ManipArena](#maniparena) (Mar 2026) · [LIBERO-Para](#libero-para) (Mar 2026) · [vla-eval](#vla-eval) (Mar 2026) · [RoboMME](#robomme) (Mar 2026) · [ManipulationNet](#manipulationnet) (Mar 2026) · [VLA-Arena](#vla-arena) (Dec 2025) · [REALM](#realm) (Dec 2025) · [PolaRiS](#polaris) (Dec 2025)
- **World Models & World-Action Models:** [WorldFailBench](#worldfailbench) (Oct 2026) · [WorldOracle](#worldoracle) (Oct 2026) · [RoboTwin-Phys](#robotwin-phys) (Sep 2026) · [WMBench](#wmbench) (Jul 2026) · [RoboWM-Bench](#robowm-bench) (Apr 2026) · [WR-Arena](#wr-arena) (Mar 2026) · [RoboTwin 2.0-Plus](#robotwin-2-0-plus) (Mar 2026) · [WorldArena](#worldarena) (Feb 2026) · [RBench](#rbench) (Jan 2026) · [WoW-World-Eval](#wow-world-eval) (Jan 2026) · [PAI-Bench](#pai-bench) (Dec 2025)
- **Embodied Reasoning:** [Embodied First Exam](#embodied-first-exam) (Nov 2026) · [BEHAVIOR-Spatial](#behavior-spatial) (Oct 2026) · [ESI-Bench](#esi-bench) (May 2026) · [CaP-X](#cap-x) (Mar 2026) · [RoboReward](#roboreward) (Jan 2026)
- **Navigation:** [SidewalkBench](#sidewalkbench) (Jun 2026) · [OmniNavBench](#omninavbench) (May 2026) · [LangMap](#langmap) (Feb 2026) · [VLNVerse](#vlnverse) (Dec 2025)
- **Locomotion & Humanoids:** [LocoManiLab](#locomanilab) (Oct 2026) · [HiPHI](#hiphi) (Aug 2026) · [HumanTracker](#humantracker) (Aug 2026) · [HumanoidArena](#humanoidarena) (Jun 2026) · [SIMPLE](#simple) (Jun 2026) · [BONES-SEED](#bones-seed) (Mar 2026) · [RoboGauge](#robogauge) (Jan 2026)
- **Robot Learning Datasets:** [FineART](#fineart) (Sep 2026) · [TacVerse](#tacverse) (Sep 2026) · [HiFi-UMI-2K](#hifi-umi-2k) (Jul 2026) · [ABC-130K](#abc-130k) (Jun 2026) · [HIW-500](#hiw-500) (Jun 2026) · [HumanNet](#humannet) (May 2026) · [Open-H-Embodiment](#open-h-embodiment) (Apr 2026) · [EgoVerse](#egoverse) (Apr 2026) · [AgiBot World 2026](#agibot-world-2026) (Apr 2026) · [10Kh RealOmni](#10kh-realomni) (Dec 2025) · [RoboCOIN](#robocoin) (Nov 2025) · [Egocentric-10K](#egocentric-10k) (Nov 2025)
- **Simulators:** [GS-Playground](#gs-playground) (Apr 2026) · [CARLA-Air](#carla-air) (Mar 2026) · [Isaac Lab-Arena](#isaac-lab-arena) (Dec 2025)
- **Human-Robot Interaction:** [HABIT](#habit) (Jun 2026) · [OpenRoboCare](#openrobocare) (Nov 2025)
- **Safety:** [ManiGuard](#maniguard) (Aug 2026) · [LIBERO-Safety](#libero-safety) (Jun 2026) · [CRAX](#crax) (Jun 2026) · [TouchSafeBench](#touchsafebench) (May 2026) · [RoboJailBench](#robojailbench) (May 2026)
- **Autonomous Driving:** [nuReasoning](#nureasoning) (May 2026)

## <a id="how-to-read-this-list"></a>How to read this list

Every entry has the same shape:

> **Name** (year of first release) `Sim` `widely used` `new`: what it evaluates and what sets it apart.<br>
> *Resources*: Paper (venue) | Website | Code ★stars | Data | Leaderboard

- `Sim`, `Real`, `Sim + Real`: where the evaluation runs.
- `widely used`: a de-facto standard of its sub-area. Its name is bold in the tables.
- `new`: first released in the last 12 months.
- ★: GitHub stars of the code repository, as of 2026-11-21.

Each sub-area ends with a **summary comparison** table, one row per entry. Click a name in a table to jump to its description.

<details>
<summary><b>What the table columns mean</b></summary>

- **Subtype**: short tags for what sets the benchmark apart.
- **Task Count, Metric Count, Robot Configs**: recorded as numbers, with the names in brackets when they are short. Longer details are in the description and in the entry's YAML file.
- **Modality**: what the benchmark provides as observations (RGB, depth, point cloud, proprioception, language, tactile, ...).
- **SIM**: the simulator backend (for example MuJoCo, SAPIEN, Isaac Sim). "Real world" means the benchmark runs on real hardware or real recordings only; "+ real" means it has both a simulated and a real-world part.
- **Data Source**: how the trajectories or labels that ship with the benchmark were collected.
  - *Human demos* (human demonstration): recorded from a person controlling the robot or simulator (teleoperation, VR, kinesthetic teaching) or from human motion capture.
  - *Human labels* (human annotation): people wrote the questions or labels over existing sensor data.
  - *Planner* (motion planner): generated by a planner, inverse kinematics, a trajectory optimizer or a scripted expert.
  - *Synthetic*: generated programmatically or by generative models, with no physics-aware planner and no human.
  - *RL policy*: rollouts of trained reinforcement-learning policies.
  - *Mixed*: more than one of the above. A dash means the benchmark ships no data.
- **Data Size**: what ships with the benchmark.
- In the **Simulators** section the table compares capabilities instead: physics engine, renderer, GPU support (✓ only when the physics itself runs on the GPU for parallel environments), operating systems and license.

</details>

**Abbreviations**: VLA, vision-language-action model. VLN, vision-language navigation. WAM, world-action model (a policy that predicts future observations together with actions). EQA, embodied question answering. HRI, human-robot interaction.

---

## <a id="manipulation"></a>Manipulation

Task suites for robot arms and grippers, in simulation and on real hardware. **64 entries.**

**Sub-areas:** [Tabletop & Language-Conditioned](#manipulation-tabletop) (18) · [Bimanual](#manipulation-bimanual) (9) · [Mobile & Household](#manipulation-mobile) (10) · [Assembly & Contact-Rich](#manipulation-contact-rich) (8) · [Articulated Objects](#manipulation-articulated) (3) · [Deformable Objects & Garments](#manipulation-deformable) (6) · [Tactile](#manipulation-tactile) (5) · [Grasping](#manipulation-grasping) (5)

### <a id="manipulation-tabletop"></a>Tabletop & Language-Conditioned

- <a id="rlbench"></a>**RLBench** (2019) `Sim` `widely used`: 100 hand-designed tabletop tasks for a Franka Panda, from reaching to multi-stage tasks such as putting a tray in an oven. Multi-view RGB-D, segmentation and proprioception, with unlimited motion-planned demonstrations; an 18-task subset is a common testbed for 3D manipulation policies.<br>
  *Resources*: [Paper](https://arxiv.org/abs/1909.12271) (RA-L 2020) | [Website](https://sites.google.com/view/rlbench) | [Code](https://github.com/stepjam/RLBench) ★1.8k

- <a id="meta-world"></a>**Meta-World** (2019) `Sim` `widely used`: 50 tabletop manipulation tasks for a simulated Sawyer arm, grouped into multi-task (MT1, MT10, MT50) and meta-learning (ML1, ML10, ML45) benchmarks. The standard testbed for multi-task and meta-reinforcement learning. Meta-World+ (2025), maintained by the Farama Foundation, standardised the environment versions and added MT25 and ML25.<br>
  *Resources*: [Paper](https://arxiv.org/abs/1910.10897) (CoRL 2019) | [Website](https://meta-world.github.io/) | [Code](https://github.com/Farama-Foundation/Metaworld) ★1.9k

- <a id="franka-kitchen"></a>**Franka Kitchen** (2019) `Sim` `widely used`: Kitchen scene from Relay Policy Learning: a 9-DoF Franka arm must complete sequences of sub-tasks (microwave, kettle, burners, light switch, cabinets) learned from unstructured VR demonstrations. A staple of offline-RL (D4RL) and behaviour-cloning papers; maintained in Gymnasium-Robotics.<br>
  *Resources*: [Paper](https://arxiv.org/abs/1910.11956) (CoRL 2019) | [Website](https://relay-policy-learning.github.io/) | [Code](https://github.com/Farama-Foundation/Gymnasium-Robotics) ★1.9k | [Data](https://minari.farama.org/datasets/D4RL/kitchen/)

- <a id="robosuite"></a>**robosuite** (2020) `Sim`: Modular MuJoCo framework with a suite of standardized manipulation tasks: lifting, stacking, pick-and-place, nut assembly, door opening, wiping and three two-arm tasks. It is the base of robomimic, LIBERO, MimicGen and RoboCasa; v1.5 (2024) adds humanoids and whole-body controllers.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2009.12293) | [Website](https://robosuite.ai/) | [Code](https://github.com/ARISE-Initiative/robosuite) ★2.7k

- <a id="ravens-transporter-networks"></a>**Ravens (Transporter Networks)** (2020) `Sim`: PyBullet suite of 10 tabletop rearrangement tasks released with Transporter Networks (block insertion, towers of Hanoi, kit assembly, rope manipulation, pile sweeping), each with a scripted oracle and partial-credit rewards. The base of CLIPort, VIMA-Bench, LoHoRavens and GenSim.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2010.14406) (CoRL 2020) | [Website](https://transporternets.github.io/) | [Code](https://github.com/google-research/ravens) ★628

- <a id="robomimic"></a>**robomimic** (2021) `Sim + Real` `widely used`: Study and framework for learning from offline human demonstrations. Its robosuite tasks (Lift, Can, Square, Transport, Tool Hang) with proficient-human, multi-human and machine-generated datasets are a standard small-data benchmark for imitation learning; three tasks also have real-robot data.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2108.03298) (CoRL 2021) | [Website](https://robomimic.github.io/) | [Code](https://github.com/ARISE-Initiative/robomimic) ★1.6k | [Data](https://huggingface.co/datasets/amandlek/robomimic)

- <a id="cliport"></a>**CLIPort** (2021) `Sim + Real`: Language-conditioned extension of the Ravens suite released with CLIPort: 10 simulated task families (packing, stacking, kit assembly, towers of Hanoi, pile separation) with seen and unseen colour and object splits, plus 9 real-robot tasks. A common testbed for language-grounded pick-and-place.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2109.12098) (CoRL 2021) | [Website](https://cliport.github.io/) | [Code](https://github.com/cliport/cliport) ★549

- <a id="calvin"></a>**CALVIN** (2021) `Sim` `widely used`: Long-horizon language-conditioned manipulation with a Franka Panda in four tabletop environments (A-D). Policies trained on teleoperated play data must complete chains of five instructions; the ABC-to-D split tests zero-shot transfer to an unseen environment.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2112.03227) (RA-L 2022) | [Website](http://calvin.cs.uni-freiburg.de/) | [Code](https://github.com/mees/calvin) ★1k | [Data](https://github.com/mees/calvin/tree/main/dataset) | [Leaderboard](http://calvin.cs.uni-freiburg.de/)

- <a id="vima-bench"></a>**VIMA-Bench** (2022) `Sim`: Ravens-based suite of 17 tabletop task templates specified by multimodal prompts that interleave text and images (goal images, one-shot video, novel concepts). A four-level protocol tests placement, combinatorial, novel-object and novel-task generalization; ships 650K scripted trajectories.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2210.03094) (ICML 2023) | [Website](https://vimalabs.github.io/) | [Code](https://github.com/vimalabs/VIMABench) ★330 | [Data](https://huggingface.co/datasets/VIMA/VIMA-Data)

- <a id="push-t-diffusion-policy"></a>**Push-T (Diffusion Policy)** (2023) `Sim`: Planar task popularised by Diffusion Policy (adapted from Implicit Behavioral Cloning): push a T-shaped block onto a fixed target with a circular end-effector, from state or image observations. A common first test for imitation-learning methods; packaged as gym-pusht in LeRobot.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2303.04137) (RSS 2023) | [Website](https://diffusion-policy.cs.columbia.edu/) | [Code](https://github.com/real-stanford/diffusion_policy) ★4.7k | [Data](https://huggingface.co/datasets/lerobot/pusht)

- <a id="arnold"></a>**ARNOLD** (2023) `Sim`: Language-grounded manipulation with continuous goal states (for example, how far a drawer is opened or how much water is poured) in photo-realistic Isaac Sim scenes: 8 tasks, 40 objects, 20 scenes and 10k demonstrations, with splits for novel objects, scenes and goal states.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2304.04321) (ICCV 2023) | [Website](https://arnold-benchmark.github.io/) | [Code](https://github.com/arnold-benchmark/arnold) ★187 | [Leaderboard](https://sites.google.com/view/arnoldchallenge/)

- <a id="libero"></a>**LIBERO** (2023) `Sim` `widely used`: Lifelong-learning benchmark of 130 language-conditioned tabletop tasks in four suites (Spatial, Object, Goal, LIBERO-100), with 50 human demonstrations per task. Its 10-task suites are now the most common simulation testbed for VLA policies.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2306.03310) (NeurIPS 2023 D&B) | [Website](https://libero-project.github.io/) | [Code](https://github.com/Lifelong-Robot-Learning/LIBERO) ★2.6k | [Data](https://libero-project.github.io/datasets)

- <a id="mimicgen"></a>**MimicGen** (2023) `Sim + Real`: Data-generation system that adapts about 200 human demonstrations into 50K+ demonstrations across 18 tasks, including long-horizon and high-precision ones such as multi-part assembly and coffee preparation. The released robosuite task variants and datasets are often used as an imitation-learning benchmark.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2310.17596) (CoRL 2023) | [Website](https://mimicgen.github.io/) | [Code](https://github.com/NVlabs/mimicgen) ★672 | [Data](https://huggingface.co/datasets/amandlek/mimicgen_datasets)

- <a id="gembench"></a>**GemBench** (2024) `Sim`: RLBench-based generalization benchmark for language-conditioned manipulation. Policies train on 16 tasks (31 variations) and are tested on 44 tasks (92 variations) at four levels: new placements, new rigid objects, new articulated objects and new long-horizon tasks.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2410.01345) (ICRA 2025) | [Website](https://www.di.ens.fr/willow/research/gembench/) | [Code](https://github.com/vlc-robot/robot-3dlotus) ★134 | [Data](https://huggingface.co/datasets/rjgpinel/GEMBench)

- <a id="vlabench"></a>**VLABench** (2024) `Sim`: 100 task categories (60 primitive, 40 composite) with 2,000+ objects, built to test what VLAs and VLM-based agents need beyond motor skill: common-sense and world knowledge, implicit instructions, spatial and physical reasoning, and multi-step long-horizon plans.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2412.18194) (ICCV 2025) | [Website](https://vlabench.github.io/) | [Code](https://github.com/OpenMOSS/VLABench) ★482 | [Data](https://huggingface.co/VLABench)

- <a id="autobio"></a>**AutoBio** (2025) `Sim`: MuJoCo simulation and benchmark for biology-lab automation: 16 tasks at three difficulty levels on digitized instruments (centrifuge, thermal cycler, pipette, thermal mixer), with plugins for threads, detents and liquids and rendering of displays and transparent labware. Tests VLAs on precise protocol steps.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2505.14030) (ICLR 2026) | [Code](https://github.com/autobio-bench/AutoBio) ★101 | [Data](https://huggingface.co/autobio-bench)

- <a id="labutopia"></a>**LabUtopia** (2025) `Sim`: Isaac Sim suite for laboratory robots: LabSim simulates liquids and chemical reactions, LabScene generates lab scenes, and LabBench defines 30 tasks at five levels, from atomic actions to long-horizon and mobile manipulation, with over 200 scene and instrument assets.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2505.22634) (NeurIPS 2025) | [Website](https://rui-li023.github.io/labutopia-site/) | [Code](https://github.com/Rui-li023/LabUtopia) ★62 | [Data](https://huggingface.co/datasets/Ruinwalker/Labutopia-Dataset)

- <a id="robocerebra"></a>**RoboCerebra** (2025) `Sim`: Long-horizon benchmark built on LIBERO that evaluates the planning, reflection and memory of a VLM planner paired with a VLA controller. 1,000 human-teleoperated trajectories of about 3,000 steps each, with LLM-generated subtask decompositions; evaluation on 60 tasks, 10 trials each.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2506.06677) (NeurIPS 2025) | [Website](https://robocerebra.github.io/) | [Code](https://github.com/buaa-colalab/RoboCerebra) ★80 | [Data](https://huggingface.co/datasets/qiukingballball/RoboCerebra)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| **[RLBench](#rlbench)** | table-top, multi-task, few-shot | 100 | 1 (success rate) | 1 (Franka Panda) | RGB, depth, segmentation, proprioceptive, language | CoppeliaSim (PyRep) | Planner | unlimited demos, generated on demand by waypoint motion planning |
| **[Meta-World](#meta-world)** | table-top, multi-task RL, meta-RL | 50 | 1 (success rate) | 1 (Sawyer) | state, proprioceptive | MuJoCo | - | N/A |
| **[Franka Kitchen](#franka-kitchen)** | kitchen, long-horizon, multi-task | 7 sub-tasks, combined into multi-task sequences | 1 | 1 (9-DoF Franka) | state, proprioceptive | MuJoCo | Human demos | 400 VR-teleoperated demo sequences; also in D4RL / Minari kitchen datasets |
| [robosuite](#robosuite) | table-top, single- and two-arm | 9 | 2 | 10 built-in models | RGB, depth, proprioceptive, state | MuJoCo | - | N/A (teleoperation tools included; datasets ship with robomimic) |
| [Ravens](#ravens-transporter-networks) | table-top, pick-and-place, rearrangement | 10 | 1 | 1 (UR5 with suction gripper or spatula) | RGB, depth | PyBullet | Planner | scripted oracle demos, generated on demand |
| **[robomimic](#robomimic)** | table-top, imitation learning | 5 sim + 3 real | 1 (success rate) | 1 (Franka Panda) | RGB, depth, proprioceptive, state | robosuite (MuJoCo) + real | Mixed | 200 proficient-human demos per task; 300 multi-human; machine-generated sets |
| [CLIPort](#cliport) | table-top | 10 sim task families + 9 real | 1 | 1 in sim (UR5 with suction gripper) | RGB, depth, language | PyBullet (Ravens) + real | Planner | scripted oracle demos, generated on demand (1-1,000 per task in the paper) |
| **[CALVIN](#calvin)** | table-top, language-conditioned | 34 | 2 | 1 (Franka Panda) | RGB, depth, tactile, proprioceptive, language | PyBullet | Human demos | ~24 h of teleoperated play data (6 h per environment), 20K language directives |
| [VIMA-Bench](#vima-bench) | table-top, multimodal prompts | 17 task templates | 1 | 1 (UR5 with suction cup or spatula) | RGB, segmentation, language | PyBullet (Ravens) | Planner | 650K expert trajectories from scripted oracles |
| [Push-T](#push-t-diffusion-policy) | planar pushing, contact-rich | 1 | 1 | 1 (2D circular end-effector) | RGB, state | pymunk (2D physics) | Human demos | 206 human demonstrations (25,650 frames) |
| [ARNOLD](#arnold) | language-grounded | 8 | 1 (success rate) | 1 (Franka Panda) | RGB, depth, proprioceptive, language | NVIDIA Isaac Sim | Planner | 10k expert demos from a keypoint-based motion planner, template language |
| **[LIBERO](#libero)** | table-top, lifelong learning | 130 | 3 (FWT, NBT, AUC) | 1 (Franka Panda) | RGB, proprioceptive, language | robosuite (MuJoCo) | Human demos | 50 human demos per task (6,500 total) |
| [MimicGen](#mimicgen) | table-top, data generation | 18 in the paper | 1 (success rate) | 4 (Panda, Sawyer, IIWA, UR5e) | RGB, proprioceptive, state | robosuite (MuJoCo); Isaac Gym Factory for some tasks + real | Mixed | 50K+ generated demos from ~200 human demos (48K+ released) |
| [GemBench](#gembench) | table-top, language-conditioned | 16 train, 44 test | 1 | 1 (Franka Panda) | RGB, depth, pointcloud, proprioceptive, language | CoppeliaSim (RLBench) | Planner | scripted RLBench demonstrations (train / val / test sets on Hugging Face) |
| [VLABench](#vlabench) | table-top, language-conditioned | 100 categories | 2 | 1 in standard evaluation (Franka Panda) | RGB, proprioceptive, language | MuJoCo (dm_control) | Planner | auto-generated fine-tuning trajectories (heuristic skills + RRT planning) |
| [AutoBio](#autobio) | biology lab automation, language-guided | 16 (three difficulty levels) | 1 (success rate) | 2 (UR5e, ALOHA) | RGB, proprioceptive, language | MuJoCo (optional Blender rendering) | Planner | 100 synthesized demos per task, in MuJoCo and Blender renderings |
| [LabUtopia](#labutopia) | chemistry lab, hierarchical benchmark | 30 (five levels) | 1 (success rate) | 3 | RGB, proprioceptive | NVIDIA Isaac Sim | Planner | expert demos from a built-in planner-based collector (on Hugging Face) |
| [RoboCerebra](#robocerebra) | long-horizon | 60 evaluation tasks | 4 | 1 (Franka Panda) | RGB, proprioceptive, language | LIBERO (robosuite / MuJoCo) | Human demos | 1,000 human-teleoperated trajectories, 2,972 steps on average |

### <a id="manipulation-bimanual"></a>Bimanual

- <a id="aloha-sim-act"></a>**ALOHA Sim (ACT)** (2023) `Sim`: The two simulated bimanual tasks released with ACT and the ALOHA system: Transfer Cube and Bimanual Insertion, in MuJoCo with scripted and human demonstrations. Small, but reported in many imitation-learning papers; packaged as gym-aloha in LeRobot.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2304.13705) (RSS 2023) | [Website](https://tonyzhaozh.github.io/aloha/) | [Code](https://github.com/tonyzhaozh/act) ★2.4k

- <a id="peract2-rlbench2-twin"></a>**PerAct2 (RLBench2 / TWIN)** (2024) `Sim`: Bimanual extension of RLBench: 13 language-conditioned two-arm tasks with 23 variations for two Franka Panda arms, with demonstrations generated automatically from waypoints. Often called RLBench2; published at ICRA 2025 under the name TWIN.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2407.00278) (ICRA 2025 (as TWIN)) | [Website](https://bimanual.github.io/) | [Code](https://github.com/markusgrotz/peract_bimanual) ★132 | [Data](https://dataset.cs.washington.edu/fox/bimanual/)

- <a id="bigym"></a>**BiGym** (2024) `Sim`: Mobile bimanual benchmark with a Unitree H1 humanoid: 40 household tasks, from target reaching to dishwasher loading, each with sparse rewards and 50 VR-teleoperated human demonstrations. Built for imitation learning and demo-driven reinforcement learning.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2407.07788) (CoRL 2024) | [Website](https://chernyadev.github.io/bigym/) | [Code](https://github.com/NeuracoreAI/bigym) ★231

- <a id="robotwin"></a>**RoboTwin** (2024) `Sim + Real`: Dual-arm benchmark that builds object digital twins with 3D generative models and has LLMs write the expert programs. Version 1.0 has 17 tasks for the AgileX COBOT Magic platform in SAPIEN, with real teleoperated data for sim-to-real studies. Succeeded by RoboTwin 2.0.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2409.02920) (ECCV 2024 Workshop; CVPR 2025) | [Website](https://robotwin-platform.github.io/) | [Code](https://github.com/RoboTwin-Platform/RoboTwin/tree/RoboTwin-1.0) ★3.1k | [Leaderboard](https://robotwin-benchmark.github.io/cvpr-2025-challenge/)

- <a id="robofactory"></a>**RoboFactory** (2025) `Sim`: Multi-arm collaboration benchmark on ManiSkill: 11 tasks in which one to four Franka Panda arms must cooperate under logical, spatial and temporal constraints. Expert data is generated automatically; the tasks were used in the MARS Challenge at NeurIPS 2025.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2503.16408) (ICCV 2025) | [Website](https://iranqin.github.io/robofactory/) | [Code](https://github.com/MARS-EAI/RoboFactory) ★152 | [Data](https://huggingface.co/datasets/FACEONG/RoboFactory_Dataset)

- <a id="robotwin-2-0"></a>**RoboTwin 2.0** (2025) `Sim` `widely used`: Bimanual benchmark and data generator with strong domain randomization: 50 dual-arm tasks, 5 robot embodiments and a 731-object library. Policies train on clean demonstrations and are tested in clean and randomized scenes (clutter, lighting, background, table height, language). Public leaderboard.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2506.18088) (ICML 2026) | [Website](https://robotwin-platform.github.io/) | [Code](https://github.com/RoboTwin-Platform/RoboTwin) ★3.1k | [Data](https://huggingface.co/datasets/TianxingChen/RoboTwin2.0) | [Leaderboard](https://robotwin-platform.github.io/leaderboard)

- <a id="roboeval"></a>**RoboEval** (2025) `Sim`: Bimanual benchmark that scores how a task is done, not only whether it succeeds: 8 tasks with 30 controlled variations and 3,000+ VR-teleoperated demonstrations, instrumented with stage-wise progress, efficiency, coordination and safety metrics. Has a leaderboard and hosted a CoRL 2026 challenge track.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2507.00435) | [Website](https://robo-eval.github.io/) | [Code](https://github.com/Robo-Eval/RoboEval) ★67 | [Leaderboard](https://robo-eval.github.io/#leaderboard)

- <a id="bicoord"></a>**BiCoord** (2026) `Sim` `new`: Bimanual benchmark built on RoboTwin 2.0 for long-horizon tasks in which the two arms stay tightly coupled. 18 tasks with stage-wise sub-goal annotations, and statistics that quantify temporal, spatial and spatio-temporal coordination between the arms.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2604.05831) | [Website](https://buaa-colalab.github.io/BiCoord/) | [Code](https://github.com/buaa-colalab/BiCoord-Bench) ★16 | [Data](https://huggingface.co/datasets/GradiusTwinbee/BiCoord)

- <a id="duobench"></a>**DuoBench** (2026) `Sim + Real` `new`: Reproducible bimanual benchmark on the Franka FR3 Duo: 11 MuJoCo tasks in four coordination categories, four of them replicated on real hardware with 3D-printable assets. Stage-based evaluation shows where a policy fails, not only whether it succeeds.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2606.11901) | [Website](https://duobench.github.io/) | [Code](https://github.com/RobotControlStack/duobench) ★27 | [Data](https://huggingface.co/datasets/RobotControlStack/duobench)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| [ALOHA Sim](#aloha-sim-act) | bimanual, fine manipulation | 2 | 1 (success rate) | 1 (ALOHA: two 6-DoF arms with grippers) | RGB, proprioceptive | MuJoCo (dm_control) | Mixed | 50 demos per task, in scripted and human-teleoperated variants |
| [PerAct2](#peract2-rlbench2-twin) | bimanual, language-conditioned | 13 (23 variations) | 1 (success rate) | 1 (two Franka Panda arms) | RGB, depth, proprioceptive, language | CoppeliaSim (RLBench / PyRep) | Planner | scripted waypoint demos (100 per task in the paper); more can be generated |
| [BiGym](#bigym) | mobile bimanual, humanoid, demo-driven | 40 | 1 (success rate) | 1 (Unitree H1) | RGB, depth, proprioceptive | MuJoCo | Human demos | 50 human demos per task (VR teleoperation) |
| [RoboTwin](#robotwin) | dual-arm, generative digital twins | 17 | 1 (success rate) | 1 (AgileX COBOT Magic dual-arm) | RGB, depth, pointcloud, proprioceptive | SAPIEN + real | Mixed | scripted expert demos (20-100 per task in the paper) + real teleop data |
| [RoboFactory](#robofactory) | multi-arm collaboration | 11 | 1 (success rate) | 1 (Franka Panda, 1-4 arms per task) | RGB, proprioceptive | ManiSkill3 (SAPIEN) | Planner | auto-generated expert demos (50-150 per task used in the paper) |
| **[RoboTwin 2.0](#robotwin-2-0)** | dual-arm, domain randomization | 50 | 1 | 5 dual-arm embodiments | RGB, depth, proprioceptive, language | SAPIEN | Planner | 100,000+ scripted expert trajectories (50 tasks, 5 embodiments) |
| [RoboEval](#roboeval) | bimanual, behavioural metrics | 8 task families (30 variations) | 4 groups | 1 (bimanual Franka Panda) | RGB, proprioceptive | MuJoCo | Human demos | 3,000+ human demonstrations (VR teleoperation) |
| [BiCoord](#bicoord) | bimanual, long-horizon | 18 | 3 | 1 (dual-arm robot from RoboTwin 2.0) | RGB, proprioceptive, language | SAPIEN (RoboTwin 2.0) | Planner | 100 scripted trajectories per task (1,800 total), with stage annotations |
| [DuoBench](#duobench) | bimanual, sim and real | 11 in simulation | 3 | 1 | RGB, proprioceptive, language | MuJoCo (Robot Control Stack) + real | Human demos | 750 teleoperated episodes (50 per task: 11 sim + 4 real) |

### <a id="manipulation-mobile"></a>Mobile & Household

- <a id="habitat-2-0-hab-home-assistant-benchmark"></a>**Habitat 2.0 HAB (Home Assistant Benchmark)** (2021) `Sim`: Home Assistant Benchmark of Habitat 2.0: a Fetch mobile manipulator rearranges objects in ReplicaCAD apartments in three long-horizon tasks (Tidy House, Prepare Groceries, Set Table). Used to compare end-to-end RL, hierarchical skill chaining and sense-plan-act pipelines.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2106.14405) (NeurIPS 2021) | [Website](https://aihabitat.org/docs/habitat2/) | [Code](https://github.com/facebookresearch/habitat-lab) ★3.2k

- <a id="behavior-1k"></a>**BEHAVIOR-1K** (2022) `Sim`: 1,000 everyday household activities, chosen from a survey of what people want robots to do, defined in BDDL and instantiated in 50 interactive scenes with 9,000+ annotated objects. Runs in OmniGibson, which simulates rigid and deformable bodies and liquids. Basis of the annual BEHAVIOR Challenge and of benchmarks such as BEHAVIOR-Spatial, IS-Bench and ManiGuard.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2403.09227) (CoRL 2022) | [Website](https://behavior.stanford.edu/) | [Code](https://github.com/StanfordVL/BEHAVIOR-1K) ★1.8k

- <a id="homerobot-ovmm"></a>**HomeRobot OVMM** (2023) `Sim + Real`: Open-vocabulary mobile manipulation: a Hello Robot Stretch must find a named object in an unseen home, pick it up and place it on a target receptacle. Habitat simulation on HSSD scenes plus a real-world software stack; basis of the NeurIPS 2023 and CVPR 2024 challenges.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2306.11565) (CoRL 2023) | [Website](https://ovmm.github.io/) | [Code](https://github.com/facebookresearch/home-robot) ★1.3k | [Leaderboard](https://aihabitat.org/challenge/2023_homerobot_ovmm/)

- <a id="robocasa"></a>**RoboCasa** (2024) `Sim` `widely used`: Kitchen simulation built on robosuite and MuJoCo, with 120 scenes and 2,500+ objects. 100 tasks (25 atomic, 75 LLM-guided composite) for a mobile manipulator, with human demonstrations and 100K+ MimicGen-generated trajectories. Extended by RoboCasa365 in 2026.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2406.02523) (RSS 2024) | [Website](https://robocasa.ai/) | [Code](https://github.com/robocasa/robocasa) ★1.9k

- <a id="maniskill-hab"></a>**ManiSkill-HAB** (2024) `Sim`: GPU-accelerated ManiSkill3 version of the Home Assistant Benchmark with realistic low-level grasping in place of magical grasps. Three long-horizon home rearrangement tasks, RL and imitation baselines, and a demonstration dataset generated from RL policies with rule-based trajectory filtering.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2412.13211) (ICLR 2025) | [Website](https://arth-shukla.github.io/mshab/) | [Code](https://github.com/arth-shukla/mshab) ★211 | [Data](https://arth-shukla.github.io/mshab/#dataset-section)

- <a id="behavior-challenge"></a>**BEHAVIOR Challenge** (2025) `Sim`: Annual challenge on BEHAVIOR-1K: a policy must complete full-length household activities with a bimanual mobile manipulator in OmniGibson, from onboard RGB-D and proprioception. 50 tasks at NeurIPS 2025; 100 tasks in 7 scenes at CoRL 2026, scored on hidden test instances.<br>
  *Resources*: [Website](https://behavior.stanford.edu/challenge/) | [Code](https://github.com/StanfordVL/BEHAVIOR-1K) ★1.8k | [Data](https://huggingface.co/datasets/behavior-1k/2026-challenge-demos) | [Leaderboard](https://huggingface.co/spaces/behavior-1k/2026-challenge-leaderboard)

- <a id="robobenchmart"></a>**RoboBenchMart** (2025) `Sim` `new`: Retail dark-store benchmark: a Fetch mobile manipulator picks grocery items into a basket, moves them between shelves and opens or closes fridges and showcases in procedurally generated stores. Tests whether generalist VLAs fine-tuned on motion-planned data cope with dense shelf clutter.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2511.10276) | [Website](https://emb-ai.github.io/RoboBenchMart/) | [Code](https://github.com/emb-ai/RoboBenchMart) ★86 | [Data](https://huggingface.co/datasets/emb-ai/RoboBenchMart_demo_envs)

- <a id="molmospaces"></a>**MolmoSpaces** (2026) `Sim` `new`: Open ecosystem of 230k indoor scenes and 130k annotated objects (48k manipulable, 42M grasps), usable in MuJoCo, Isaac and ManiSkill. Its MolmoSpaces-Bench evaluates policies zero-shot on 8 navigation and manipulation tasks in unseen scenes and reports strong sim-to-real correlation; public leaderboard.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2602.11337) (RSS 2026) | [Website](https://molmospaces.allen.ai/) | [Code](https://github.com/allenai/molmospaces) ★526 | [Data](https://huggingface.co/datasets/allenai/molmospaces) | [Leaderboard](https://molmospaces.allen.ai/leaderboard)

- <a id="robocasa365"></a>**RoboCasa365** (2026) `Sim` `new`: Second generation of RoboCasa: 365 kitchen tasks (65 atomic, 300 composite) across 2,500 kitchen scenes, with 600+ hours of human demonstrations and 1,600+ hours of MimicGen data. Benchmarks multi-task training, foundation-model training and lifelong learning; public leaderboard on a 50-task split.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2603.04356) (ICLR 2026) | [Website](https://robocasa.ai/) | [Code](https://github.com/robocasa/robocasa) ★1.9k | [Leaderboard](https://robocasa.ai/leaderboard.html)

- <a id="ebench"></a>**EBench** (2026) `Sim` `new`: Diagnostic benchmark for generalist policies on a dual-arm mobile robot in Isaac Sim. 26 tasks across mobile pick-and-place, long-horizon and precise manipulation are tagged on 5 capability and 4 generalization axes, so one score becomes a capability profile. Held-out test split with an online leaderboard.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2606.18239) | [Website](https://internrobotics.github.io/EBench-home/) | [Code](https://github.com/InternRobotics/EBench) ★149 | [Data](https://huggingface.co/datasets/InternRobotics/EBench-Dataset) | [Leaderboard](https://internrobotics.shlab.org.cn/eval/evaluation-list)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| [Habitat 2.0 HAB](#habitat-2-0-hab-home-assistant-benchmark) | home rearrangement, mobile manipulation | 3 long-horizon tasks | 1 | 1 (Fetch) | RGB, depth, proprioceptive | Habitat-Sim (Bullet physics) | - | N/A (ReplicaCAD: 111 layouts of one apartment, 92 objects; no demos) |
| [BEHAVIOR-1K](#behavior-1k) | household activities, long-horizon | 1,000 activities | 2 | multiple | RGB, depth, segmentation, proprioceptive | OmniGibson (NVIDIA Omniverse / PhysX 5) | - | N/A (teleoperated demos are released with the BEHAVIOR Challenge) |
| [HomeRobot OVMM](#homerobot-ovmm) | open-vocabulary mobile manipulation | 1 | 3 | 1 (Hello Robot Stretch) | RGB, depth, proprioceptive, language | Habitat (HSSD scenes) + real | - | N/A (episodes in HSSD homes; no demonstrations) |
| **[RoboCasa](#robocasa)** | household kitchen, mobile manipulation | 100 (25 atomic + 75 composite) | 1 (success rate) | 1 in datasets | RGB, proprioceptive | robosuite (MuJoCo) | Mixed | 50 human demos per task + 100K+ MimicGen-generated trajectories |
| [ManiSkill-HAB](#maniskill-hab) | home rearrangement, low-level control | 3 long-horizon tasks | 1 | 1 (Fetch) | RGB, depth, proprioceptive, state | ManiSkill3 (SAPIEN) | RL policy | 44K RGB-D episodes, 8.8M transitions (TidyHouse, PrepareGroceries, SetTable) |
| [BEHAVIOR Challenge](#behavior-challenge) | household activities, long-horizon | 100 household tasks (2026) | 1 | 1 by default | RGB, depth, proprioceptive | OmniGibson (NVIDIA Omniverse / PhysX 5) | Human demos | 20,000 teleoperated demos, 1,950 h (2026); 10,000 demos, 1,200+ h (2025) |
| [RoboBenchMart](#robobenchmart) | retail dark store, mobile manipulation | 10 (7 atomic + 3 composite) | 1 (success rate) | 1 (Fetch) | RGB, proprioceptive, language | ManiSkill3 (SAPIEN) | Planner | 2,976 motion-planned demonstrations (248 per task-item-fixture triplet) |
| [MolmoSpaces](#molmospaces) | large-scale scenes | 8 base tasks | 1 (success rate) | 2 plus floating grippers | RGB, proprioceptive, language | MuJoCo for the benchmark (assets also for Isaac and ManiSkill) | Synthetic | 230k scenes, 130k objects, 42M grasps (assets; no trajectories) |
| [RoboCasa365](#robocasa365) | household kitchen, mobile manipulation | 365 (65 atomic + 300 composite) | 1 (task success rate) | 1 in datasets | RGB, proprioceptive, language | robosuite (MuJoCo) | Mixed | 612 h human teleoperation (30k pretraining demos) + 1,615 h MimicGen-generated |
| [EBench](#ebench) | mobile bimanual | 26 | 2, split by 5 capability and 4 generalization axes | 1 (ARX Lift 2 dual-arm mobile robot) | RGB, proprioceptive, language | NVIDIA Isaac Sim (GenManip) | Mixed | 6,600 episodes, 91.4 h (teleoperation + cuRobo motion planning) |

### <a id="manipulation-contact-rich"></a>Assembly & Contact-Rich

- <a id="nist-assembly-task-boards"></a>**NIST Assembly Task Boards** (2018) `Real` `widely used`: Low-cost physical task boards from NIST for measuring robotic small-part assembly: peg and connector insertion, gear meshing and nut threading (board 1), belt drives, cable routing, wire harnesses and bolt threading (boards 2-5). Public designs and test methods; used in the IROS/ICRA manipulation competitions.<br>
  *Resources*: [Paper](https://doi.org/10.1109/LRA.2020.2965869) (IEEE RA-L 2020) | [Website](https://www.nist.gov/el/intelligent-systems-division-73500/robotic-grasping-and-manipulation-assembly/assembly)

- <a id="robothon-grand-challenge-task-board"></a>**Robothon Grand Challenge Task Board** (2021) `Real`: Internet-connected electronic task board (the 'Digital Robot Judge') whose microcontroller times and verifies manipulation sub-tasks such as localisation, insertion and disassembly and publishes each trial to a web dashboard. It is the shared test object of the Robothon Grand Challenge (four editions by 2025) and the euROBIN manipulation challenge.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2201.09565) | [Website](https://automatica-munich.com/en/munich-i/robothon/) | [Code](https://github.com/peterso/robotlearningblock) ★24 | [Leaderboard](https://github.com/peterso/robothon-grand-challenge)

- <a id="factory"></a>**Factory** (2022) `Sim`: GPU-accelerated contact simulation and RL environments for robotic assembly: 60 part models from NIST Task Board 1 and three Franka scenes (nut-and-bolt, peg and connector insertion, gears). Its peg-insert, gear-mesh and nut-thread tasks now ship with Isaac Lab; IndustReal and AutoMate (100 assemblies) followed from the same group.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2205.03532) (RSS 2022) | [Website](https://research.nvidia.com/publication/2022-05_factory-fast-contact-robotic-assembly) | [Code](https://github.com/isaac-sim/IsaacGymEnvs) ★2.9k

- <a id="furniturebench"></a>**FurnitureBench** (2023) `Sim + Real`: Reproducible real-world furniture assembly benchmark with a standardized Franka setup, 3D-printable furniture parts, a large teleoperation dataset and a matching simulator (FurnitureSim); tests long-horizon, contact-rich skills such as inserting and screwing.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2305.12821) (RSS 2023) | [Website](https://clvrai.github.io/furniture-bench/) | [Code](https://github.com/clvrai/furniture-bench) ★244 | [Data](https://clvrai.github.io/furniture-bench/docs/tutorials/dataset.html)

- <a id="fmb"></a>**FMB** (2024) `Real`: Functional Manipulation Benchmark: real-world multi-stage tasks combining grasping, repositioning and insertion on 66 procedurally generated, 3D-printable objects with a Franka arm, meant to test generalisation across object shapes. Ships CAD files, 22,550 demonstrations and baseline imitation policies.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2401.08553) (IJRR 2024) | [Website](https://functional-manipulation-benchmark.github.io/) | [Code](https://github.com/rail-berkeley/fmb) ★92 | [Data](https://functional-manipulation-benchmark.github.io/dataset/index.html)

- <a id="reassemble"></a>**REASSEMBLE** (2025) `Real`: Multimodal dataset for contact-rich assembly and disassembly on NIST Task Board 1: 4,551 haptically teleoperated demonstrations of pick, insert, remove and place on 17 objects, recorded with multi-view RGB, an event camera, force-torque, audio and proprioception. Benchmarked on action segmentation, motion policy learning and execution monitoring.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2502.05086) (RSS 2025) | [Website](https://tuwien-asl.github.io/REASSEMBLE_page/) | [Code](https://github.com/TUWIEN-ASL/REASSEMBLE) ★38 | [Data](https://researchdata.tuwien.ac.at/records/0ewrv-8cb44)

- <a id="roco-challenge"></a>**RoCo Challenge** (2025) `Sim + Real` `new`: Challenge on long-horizon planetary gearbox assembly with Galaxea dual-arm robots, scored step by step in three scenarios (from scratch, resuming a partial assembly, error recovery), first in Isaac Sim and then on real hardware. The first edition drew 60+ teams; a second was organised for IROS 2026.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2603.15469) (AAAI 2026 workshop challenge) | [Website](https://rocochallenge.github.io/RoCo-AAAI2026/) | [Code](https://github.com/rocochallenge/gearboxAssembly) ★34 | [Leaderboard](https://rocochallenge.github.io/RoCo-AAAI2026/leaderboard.html)

- <a id="contactbench-1-0"></a>**ContactBench 1.0** (2026) `Sim + Real` `new`: Benchmark of 36 everyday contact-rich tasks built around eight skills (thin-object, multi-object and clutter grasping, constrained placing, in-hand repositioning, extrinsic contact, articulated mechanisms, insertion). Over 40 3D-printable assets each have a matching simulation model, so tasks can be reproduced across labs and in simulation.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2610.24512) | [Website](https://jingyi-xiang.github.io/contactbench/) | [Code](https://github.com/Michaelwyx/contactbench-sim) ★21

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| **[NIST Assembly Task Boards](#nist-assembly-task-boards)** | physical task boards | 5 task boards | 2 | robot-agnostic | N/A | Real world | - | N/A |
| [Robothon Grand Challenge Task Board](#robothon-grand-challenge-task-board) | electronic task board | 5 tasks per board (2025 edition) | 2, plus jury scoring | robot-agnostic | N/A | Real world | - | N/A |
| [Factory](#factory) | simulated assembly, RL | 3 assembly scenes | 1 (success rate) | 1 (Franka Panda) | state, proprioceptive | Isaac Gym (PhysX); tasks ported to Isaac Lab | - | N/A |
| [FurnitureBench](#furniturebench) | furniture assembly, long-horizon | 8 furniture models | 2 | 1 (Franka Panda) | RGB, proprioceptive | FurnitureSim (Isaac Gym, built on Factory) + real | Human demos | 219.6 hours, 5,100 teleoperated demonstrations |
| [FMB](#fmb) | real-world, multi-stage assembly | 2 task families, 6 skills | 1 (success rate) | 1 (Franka Panda) | RGB, depth, proprioceptive, force-torque | Real world | Human demos | 22,550 demonstration trajectories (about 5 s each) |
| [REASSEMBLE](#reassemble) | real-world dataset | 4 actions on 17 objects | task-specific | 1 (Franka Research 3) | RGB, event camera, force-torque, audio, proprioceptive | Real world | Human demos | 4,551 demonstrations (4,035 successful), 781 minutes |
| [RoCo Challenge](#roco-challenge) | challenge, gearbox assembly, dual-arm | 3 | 1 | 2 (Galaxea R1, R1 Lite) | RGB, depth, proprioceptive | Isaac Sim / Isaac Lab + real | Mixed | 300+ scripted simulation demos and 300+ teleoperated real demos |
| [ContactBench 1.0](#contactbench-1-0) | everyday contact-rich skills | 36 | 4 | 2 | RGB, tactile, force-torque, proprioceptive | Newton (MuJoCo Warp solver) + real | - | N/A (printable assets, task definitions, scripted sim policies) |

### <a id="manipulation-articulated"></a>Articulated Objects

- <a id="partnet-mobility-sapien"></a>**PartNet-Mobility (SAPIEN)** (2020) `Sim` `widely used`: Set of 2,346 articulated 3D objects in 46 household categories with part-level motion annotations, released with the SAPIEN simulator. It remains the most used asset source for articulated-object benchmarks; GAPartNet, UniDoorManip and GarmentLab all draw on it.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2003.08515) (CVPR 2020) | [Code](https://github.com/haosulab/SAPIEN) ★872

- <a id="gapartnet"></a>**GAPartNet** (2022) `Sim + Real`: Part-centric dataset of 1,166 articulated objects in 27 categories with 8,489 instances of nine generalizable and actionable part classes (handles, lids, buttons, doors and others), built from PartNet-Mobility and AKB-48. Defines three cross-category tasks: part segmentation, part pose estimation and part-based manipulation.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2211.05272) (CVPR 2023 (Highlight)) | [Website](https://pku-epic.github.io/GAPartNet/) | [Code](https://github.com/PKU-EPIC/GAPartNet) ★164

- <a id="artvip"></a>**ArtVIP** (2025) `Sim`: Open set of 992 artist-made digital-twin articulated objects (9 categories, 37 subcategories) and six scenes in USD, with tuned joint dynamics, embedded interaction behaviours such as latching and self-closing, and pixel-level affordance labels. Validated against motion capture and in imitation- and reinforcement-learning experiments in Isaac Sim.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2506.04941) (ICLR 2026) | [Website](https://x-humanoid-artvip.github.io/) | [Data](https://huggingface.co/datasets/X-Humanoid/ArtVIP)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| **[PartNet-Mobility](#partnet-mobility-sapien)** | articulated-object assets | N/A (asset dataset) | N/A | N/A | 3D assets | SAPIEN (URDF assets, also used in other simulators) | Human labels | 2,346 articulated objects, 46 categories |
| [GAPartNet](#gapartnet) | part-centric perception and manipulation | 3 | 3 | 2 (Franka, Kinova) | RGB, depth, pointcloud, segmentation | Isaac Gym (released manipulation code) + real | Human labels | 1,166 objects, 8,489 part instances, rendered point clouds |
| [ArtVIP](#artvip) | articulated-object assets, digital twins | N/A | N/A | N/A | 3D assets | Isaac Sim (USD; convertible to URDF / MJCF) | Human labels | 992 articulated objects, 6 scenes |

### <a id="manipulation-deformable"></a>Deformable Objects & Garments

- <a id="softgym"></a>**SoftGym** (2020) `Sim` `widely used`: Gym-style simulated benchmark for manipulating rope, cloth and fluids: ten tasks (six in SoftGym-Medium, four in SoftGym-Hard) with an abstract picker action space, plus variants with a Sawyer or Franka arm. Widely reused as the simulation base for later cloth-manipulation work.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2011.07215) (CoRL 2020) | [Website](https://sites.google.com/view/softgym) | [Code](https://github.com/Xingyu-Lin/softgym) ★357

- <a id="plasticinelab"></a>**PlasticineLab** (2021) `Sim`: Differentiable-physics benchmark of 10 soft-body manipulation tasks (50 configurations) in which kinematic manipulators pinch, roll, chop and mould plasticine into target shapes. Its Taichi-based simulator provides gradients, so the benchmark compares reinforcement learning with gradient-based planning.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2104.03311) (ICLR 2021 (Spotlight)) | [Website](https://plasticinelab.csail.mit.edu/) | [Code](https://github.com/hzaskywalker/PlasticineLab) ★152

- <a id="icra-2024-cloth-competition"></a>**ICRA 2024 Cloth Competition** (2024) `Real`: Benchmark and dataset from a head-to-head competition on choosing the grasp that best unfolds a garment hanging in the air, executed on a shared dual-arm UR5e setup from RGB-D input. Released data: 679 real unfolding attempts on 34 garments, including 176 competition trials from 11 teams.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2508.16749) (ICRA 2024 competition; IJRR 2026) | [Website](https://airo.ugent.be/cloth_competition/) | [Code](https://github.com/Victorlouisdg/cloth-competition) ★24 | [Data](https://zenodo.org/records/14621179)

- <a id="garmentlab"></a>**GarmentLab** (2024) `Sim + Real`: Isaac Sim environment and benchmark for garment manipulation: 20 tasks in five groups covering garment interaction with rigid, articulated and fluid objects and human avatars, with garments from ClothesNet, PBD and FEM simulation, teleoperation tools, sim-to-real methods and a real-world benchmark protocol.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2411.01200) (NeurIPS 2024) | [Website](https://garmentlab.github.io/) | [Code](https://github.com/GarmentLab/GarmentLab) ★189

- <a id="lehome"></a>**LeHome** (2026) `Sim + Real` `new`: Isaac Lab environment for household deformable-object manipulation (garments, food, liquids, granular and linear objects) with low-cost LeRobot-family robots. It hosted the LeHome Challenge at ICRA 2026: garment folding across four clothing categories, ranked in simulation (62 teams) and then on real SO-ARM101 robots.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2604.22363) (ICRA 2026) | [Website](https://lehome-web.github.io/) | [Code](https://github.com/lehome-official/lehome) ★54 | [Data](https://huggingface.co/datasets/lehome/lehome_release) | [Leaderboard](https://lehome-challenge.com/2026/)

- <a id="softvtbench"></a>**SoftVTBench** (2026) `Sim` `new`: Visuo-tactile benchmark for deformable-object manipulation that scores physical safety as well as task completion: a successful rollout must also keep the object from dropping or deforming beyond a calibrated limit read from hidden FEM states. Four matched suites (deformable vs. rigid twins, object vs. spatial variation) in Isaac Sim.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2607.04234) | [Website](https://softvtbench.github.io/) | [Code](https://github.com/TuojingAI/SoftVTBench) ★248 | [Data](https://huggingface.co/datasets/Arthur12137/SoftVTBench)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| **[SoftGym](#softgym)** | rope, cloth and fluid; RL | 10, plus robot variants | 1 | abstract pickers | RGB, state | NVIDIA FleX | - | N/A |
| [PlasticineLab](#plasticinelab) | soft-body, differentiable physics | 10 tasks, 50 configurations | 1 | task-specific kinematic manipulators | state | Taichi / DiffTaichi (differentiable MPM) | - | N/A |
| [ICRA 2024 Cloth Competition](#icra-2024-cloth-competition) | real-world cloth unfolding | 1 | 2 | 1 | RGB, depth, pointcloud | Real world | Mixed | 679 unfolding attempts on 34 garments (83 GB) |
| [GarmentLab](#garmentlab) | garments, sim-to-real | 20 (5 groups) | 1 (success rate) | several | RGB, depth, pointcloud, proprioceptive | Isaac Sim (PhysX 5; PBD and FEM) + real | - | N/A (assets only: 20 scenes, 9,000+ object models) |
| [LeHome](#lehome) | household deformables, low-cost robots | 6 evaluated tasks | 1 (success rate) | 3 (LeRobot SO-101, LeKiwi, XLeRobot) | RGB, depth, proprioceptive, language | Isaac Sim / Isaac Lab (PBD, FEM, fluid simulation) + real | Human demos | teleoperated demos (50 per task in the paper; challenge sets on Hugging Face) |
| [SoftVTBench](#softvtbench) | visuo-tactile, safety-aware | 4 task suites | 2 | 1 | RGB, tactile, proprioceptive, language | Isaac Sim (FEM deformable objects) | Planner | 4,000 scripted-expert demos (1,628 in the first public release) |

### <a id="manipulation-tactile"></a>Tactile

- <a id="objectfolder-benchmark"></a>**ObjectFolder Benchmark** (2023) `Sim + Real`: Suite of 10 multisensory object-centric tasks across recognition, reconstruction and manipulation with sight, sound and touch. Evaluated on 1,000 simulated neural objects from ObjectFolder and on ObjectFolder Real, which holds meshes, videos, impact sounds and GelSight readings of 100 household objects.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2306.00956) (CVPR 2023) | [Website](https://objectfolder.stanford.edu/) | [Code](https://github.com/objectfolder)

- <a id="maniskill-vitac-challenge"></a>**ManiSkill-ViTac Challenge** (2024) `Sim + Real`: Annual challenge on contact-rich manipulation with vision-based tactile sensing. The 2024 and 2025 editions train in an IPC-based tactile simulator (peg insertion, lock opening; 2025 added tactile-vision fusion and sensor-design tracks) with sim-to-real evaluation; the 2026 edition moved to real-robot bimanual visuo-tactile tasks.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2411.12503) (ICRA ViTac Workshop 2024-2025; CVPR 2026 Embodied AI Workshop) | [Website](https://ai-workshops.github.io/maniskill-vitac-challenge-2025/) | [Code](https://github.com/chuanyune/ManiSkill-ViTac2025) ★61 | [Leaderboard](https://callmeray.github.io/Mani_ViTac_Challenge_2026_page/)

- <a id="manifeel"></a>**ManiFeel** (2025) `Sim + Real`: Simulation benchmark for supervised visuotactile policy learning on Isaac Gym with TacSL: nine tasks in three groups (insertion, screwing, exploration under occlusion or dim light), teleoperated demonstrations, and a modular pipeline over sensing modalities, tactile encoders and policy heads. One task per group is replicated on a real Franka.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2505.18472) | [Website](https://zhengtongxu.github.io/manifeel-website/) | [Code](https://github.com/purdue-mars/manifeel) ★68 | [Data](https://huggingface.co/datasets/purdue-mars/manifeel)

- <a id="univtac"></a>**UniVTAC** (2026) `Sim` `new`: Simulation platform and benchmark for visuo-tactile manipulation on Isaac Lab and TacEx, supporting GelSight Mini, ViTai GF225 and Xense WS sensors with automated data generation. The UniVTAC Benchmark has eight contact-rich tasks such as HDMI and tube insertion, key extraction and grasp-and-classify, each with 100 generated demonstrations.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2602.10093) (CoRL 2026) | [Website](https://univtac.github.io/) | [Code](https://github.com/univtac/UniVTAC) ★196 | [Data](https://huggingface.co/datasets/byml/UniVTAC)

- <a id="tabero"></a>**Tabero** (2026) `Sim` `new`: Benchmark for gentle, language-conditioned manipulation with touch: the LIBERO suites are rebuilt in Isaac Lab with a tactile-equipped Franka gripper (Taxim / FOTS simulation) by replaying open-source demonstrations, and policies are scored on task success together with grip and applied forces under gentle versus firm instructions.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2605.27886) (ICML 2026) | [Website](https://nathanwu7.github.io/Tabero/) | [Code](https://github.com/NathanWu7/Tabero) ★64 | [Data](https://huggingface.co/datasets/NathanWu7/Isaaclab_Libero)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| [ObjectFolder Benchmark](#objectfolder-benchmark) | multisensory: vision, audio, touch | 10 | task-specific | 1 (Franka Panda with GelSight finger) | RGB, audio, tactile | ObjectFolder neural objects (PyBullet for object dynamics) + real | Mixed | 1,000 neural objects; 100 real objects with multisensory recordings |
| [ManiSkill-ViTac Challenge](#maniskill-vitac-challenge) | challenge, visuo-tactile insertion | 2 tasks (2024) | 1 | organiser platform | tactile, depth, RGB, proprioceptive, language | SAPIEN with IPC-based tactile sensor simulation + real | Human demos | none for 2024-2025 (RL in simulation); teleoperated real data in 2026 |
| [ManiFeel](#manifeel) | visuotactile imitation learning | 9 in simulation | 1 (success rate) | 1 (Franka Panda with GelSight sensor) | RGB, tactile, proprioceptive | Isaac Gym + TacSL + real | Human demos | SpaceMouse-teleoperated demos, about 50-80 per task |
| [UniVTAC](#univtac) | visuo-tactile simulation platform | 8 | 1 (success rate) | 2 arm models (Franka Panda, UR5e) | RGB, tactile, proprioceptive | Isaac Lab + TacEx (UIPC tactile simulation) | Planner | 100 generated demos per task (800), plus contact-pretraining data |
| [Tabero](#tabero) | tactile LIBERO | 4 LIBERO suites with force-level instructions | 5 | 1 | RGB, tactile, proprioceptive, language | Isaac Lab with Taxim / FOTS tactile simulation | Human demos | LIBERO demonstrations replayed with tactile sensing (count not stated) |

### <a id="manipulation-grasping"></a>Grasping

- <a id="cornell-grasping-dataset"></a>**Cornell Grasping Dataset** (2011) `Real`: Early real RGB-D dataset for planar grasp detection: 885 images of 240 objects hand-labelled with 8,019 grasp rectangles (about 5.1k positive). Results are reported as accuracy under the rectangle metric (orientation and IoU thresholds); long the standard test for parallel-jaw grasp detectors.<br>
  *Resources*: [Paper](https://doi.org/10.1109/ICRA.2011.5980145) (ICRA 2011) | [Data](https://www.kaggle.com/datasets/oneoneliu/cornell-grasp)

- <a id="ycb-object-and-model-set"></a>**YCB Object and Model Set** (2015) `Real` `widely used`: Standard physical object set for manipulation research: 77 everyday items varying in shape, size, texture, weight and rigidity, shipped to labs worldwide, with high-resolution RGB-D scans, meshes and physical properties, plus a framework of task protocols so that results can be compared across robots and labs.<br>
  *Resources*: [Paper](https://arxiv.org/abs/1502.03143) (IEEE RAM 2015) | [Website](https://www.ycbbenchmarks.org/) | [Data](http://ycb-benchmarks.s3-website-us-east-1.amazonaws.com/)

- <a id="graspnet-1billion"></a>**GraspNet-1Billion** (2020) `Real` `widely used`: Large real-world benchmark for 6-DoF parallel-jaw grasp detection in clutter: 97,280 RGB-D images of 190 scenes with 88 objects from RealSense and Kinect cameras, annotated with 6D poses and over 1.1 billion grasp poses. A unified evaluation scores predicted grasps analytically and reports AP across friction coefficients.<br>
  *Resources*: [Paper](https://openaccess.thecvf.com/content_CVPR_2020/html/Fang_GraspNet-1Billion_A_Large-Scale_Benchmark_for_General_Object_Grasping_CVPR_2020_paper.html) (CVPR 2020) | [Website](https://graspnet.net/) | [Code](https://github.com/graspnet/graspnetAPI) ★371 | [Data](https://graspnet.net/datasets.html)

- <a id="acronym"></a>**ACRONYM** (2020) `Sim`: Simulation-labelled dataset of 17.7 million parallel-jaw grasps on 8,872 ShapeNetSem objects from 262 categories, each tested in the FleX physics simulator with a Franka Panda gripper model. Comes with tools to build cluttered scenes; a common training source for learned 6-DoF grasp generators.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2011.09584) (ICRA 2021) | [Code](https://github.com/NVlabs/acronym) ★158

- <a id="graspclutter6d"></a>**GraspClutter6D** (2025) `Real`: Real-world dataset for perception and grasping in dense clutter: 1,000 scenes averaging 14.1 objects and 62.6% occlusion, 200 objects in 75 bin, shelf and table settings, four RGB-D cameras, 736K 6D poses and 9.3 billion grasp labels. Benchmarks instance segmentation, pose estimation and 6-DoF grasp detection.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2504.06866) (IEEE RA-L 2025) | [Website](https://sites.google.com/view/graspclutter6d) | [Code](https://github.com/SeungBack/graspclutter6dAPI) ★33 | [Data](https://huggingface.co/datasets/GraspClutter6D/GraspClutter6D)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| [Cornell Grasping Dataset](#cornell-grasping-dataset) | planar grasp rectangles, real RGB-D | 1 (grasp-rectangle detection) | 1 | N/A (parallel-jaw gripper assumed) | RGB, depth | Real world | Human labels | 885 RGB-D images, 240 objects, 8,019 grasp rectangles |
| **[YCB Object and Model Set](#ycb-object-and-model-set)** | physical object set | N/A | protocol-specific | robot-agnostic | RGB, depth, pointcloud | Real world | - | 77-object set; RGB-D scans and meshes for most objects |
| **[GraspNet-1Billion](#graspnet-1billion)** | 6-DoF grasp detection, clutter | 1 | 1 | N/A (parallel-jaw gripper model) | RGB, depth, pointcloud | Real world | Mixed | 97,280 RGB-D images, 190 scenes, 88 objects, 1.1B grasp poses |
| [ACRONYM](#acronym) | 6-DoF grasps, simulation-labelled | N/A (grasp dataset) | N/A | 1 (Franka Panda gripper) | 3D assets, grasp poses | NVIDIA FleX | Synthetic | 17.7M grasps, 8,872 objects, 262 categories |
| [GraspClutter6D](#graspclutter6d) | 6-DoF grasping, heavy clutter | 3 | task-specific | N/A | RGB, depth, pointcloud, segmentation | Real world | Mixed | 52K RGB-D images, 1,000 scenes, 736K 6D poses, 9.3B grasps |

<p align="right"><a href="#contents">Back to contents ↑</a></p>

---

## <a id="dexterous-manipulation"></a>Dexterous Manipulation

Multi-finger hands: in-hand skills, two-handed dexterity, grasp synthesis, and the human hand-object data that robot hands learn from. **41 entries.**

**Sub-areas:** [In-Hand & Dexterous Skills](#dexterous-manipulation-dex-manipulation) (12) · [Bimanual Dexterity](#dexterous-manipulation-dex-bimanual) (11) · [Dexterous Grasping](#dexterous-manipulation-dex-grasping) (8) · [Human Hand-Object Data](#dexterous-manipulation-hand-object-data) (10)

### <a id="dexterous-manipulation-dex-manipulation"></a>In-Hand & Dexterous Skills

- <a id="adroit-hand-dapg"></a>**Adroit Hand (DAPG)** (2017) `Sim` `widely used`: Four MuJoCo tasks for a 24-DoF Shadow Hand on a free-moving arm (door, hammer, pen, relocate), introduced with the DAPG paper together with human demonstrations. Later packaged in D4RL and Gymnasium-Robotics; the standard testbed for demonstration-augmented and offline RL with a dexterous hand.<br>
  *Resources*: [Paper](https://arxiv.org/abs/1709.10087) (RSS 2018) | [Website](https://robotics.farama.org/envs/adroit_hand/) | [Code](https://github.com/aravindr93/hand_dapg) ★330 | [Data](https://minari.farama.org/datasets/D4RL/)

- <a id="shadow-dexterous-hand-gymnasium-robotics"></a>**Shadow Dexterous Hand (Gymnasium-Robotics)** (2018) `Sim` `widely used`: OpenAI's goal-conditioned, sparse-reward tasks for a simulated 24-DoF Shadow Dexterous Hand: fingertip reaching and in-hand reorientation of a block, an egg and a pen. Now maintained in Gymnasium-Robotics, with optional readings from 92 touch sensors.<br>
  *Resources*: [Paper](https://arxiv.org/abs/1802.09464) | [Website](https://robotics.farama.org/envs/shadow_dexterous_hand/) | [Code](https://github.com/Farama-Foundation/Gymnasium-Robotics) ★1.9k

- <a id="trifinger-real-robot-challenge"></a>**TriFinger Real Robot Challenge** (2020) `Sim + Real`: Open-source three-finger robot and a series of challenges (2020-2022) in which submitted policies were run remotely on a cluster of real TriFinger platforms. The 2022 edition and the follow-up ICLR 2023 benchmark provide real and simulated offline-RL datasets for cube pushing and lifting.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2008.03596) (NeurIPS 2022 Competition Track) | [Website](https://real-robot-challenge.com/) | [Code](https://github.com/open-dynamic-robot-initiative/trifinger_simulation) ★43 | [Data](https://github.com/rr-learning/trifinger_rl_datasets) | [Leaderboard](https://real-robot-challenge.com/leaderboard)

- <a id="dexmv"></a>**DexMV** (2021) `Sim`: Platform that pairs three MuJoCo tasks for an Adroit hand (relocate, pour, place inside) with videos of people doing the same tasks. 3D hand and object poses are estimated from the videos and retargeted into robot demonstrations, which are used to benchmark imitation learning.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2108.05877) (ECCV 2022) | [Code](https://github.com/yzqin/dexmv-sim) ★209

- <a id="isaacgymenvs-hand-tasks"></a>**IsaacGymEnvs Hand Tasks** (2021) `Sim`: The dexterous-hand environments shipped with NVIDIA Isaac Gym: Shadow Hand and Allegro Hand object reorientation, TriFinger cube manipulation, DeXtreme, and the Allegro-Kuka arm-hand tasks from DexPBT. A common starting point for GPU-parallel in-hand RL; the repository is now archived.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2108.10470) | [Website](https://developer.nvidia.com/isaac-gym) | [Code](https://github.com/isaac-sim/IsaacGymEnvs) ★2.9k

- <a id="myosuite"></a>**MyoSuite** (2022) `Sim`: MuJoCo suite of physiologically detailed musculoskeletal models (finger, hand, arm, elbow, leg) with contact-rich tasks such as key turning, pen twirling and Baoding balls, plus muscle fatigue and sarcopenia variants. It hosts the MyoChallenge competition tasks; version 3 adds GPU backends.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2205.13600) (L4DC 2022) | [Website](https://www.myosuite.org) | [Code](https://github.com/MyoHub/myosuite) ★1.3k

- <a id="dexart"></a>**DexArt** (2023) `Sim`: Benchmark of four articulated-object tasks (faucet, bucket, laptop, toilet) for an Allegro Hand on an XArm6 in SAPIEN, with point-cloud observations. Policies are trained on a set of object instances and scored on instances not seen in training.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2305.05706) (CVPR 2023) | [Website](https://www.chenbao.tech/dexart/) | [Code](https://github.com/Kami-code/dexart-release) ★154

- <a id="vtdexmanip"></a>**VTDexManip** (2025) `Sim`: Visual-tactile dataset of people performing 10 daily manipulation tasks on 182 objects, paired with an Isaac Gym benchmark of six dexterous tasks (bottle-cap turning, faucet screwing, lever sliding, table and in-hand reorientation, bimanual handover) on which 18 pretrained and non-pretrained visual-tactile models are compared.<br>
  *Resources*: [Paper](https://openreview.net/forum?id=jf7C7EGw21) (ICLR 2025) | [Website](https://lqts.github.io/VTDexManip/) | [Code](https://github.com/LQTS/VTDexManip) ★94

- <a id="pomdar"></a>**POMDAR** (2026) `Sim + Real` `new`: Performance-based dexterity benchmark for anthropomorphic robot hands: 18 tasks derived from human motor-control taxonomies (12 in-hand manipulation patterns, 6 grasps) on 3D-printable, mechanically scaffolded fixtures. Scores combine correctness and speed against a human baseline; real hardware plus MuJoCo models.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2604.09294) | [Website](https://srl-ethz.github.io/POMDAR/) | [Code](https://github.com/srl-ethz/pomdar_benchmark) ★17

- <a id="dexjoco"></a>**DexJoCo** (2026) `Sim` `new`: MuJoCo benchmark and toolkit of 11 functional tasks for Franka arms with Allegro Hands, covering tool use, bimanual coordination, long-horizon execution and reasoning. Ships 1.1K glove-teleoperated demonstrations and visual and dynamics randomisation for testing imitation and VLA policies.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2605.16257) | [Website](https://dexjoco.github.io) | [Code](https://github.com/brave-eai/dexjoco) ★289 | [Data](https://huggingface.co/datasets/DexJoCo/DexJoCo-Datasets-LeRobot)

- <a id="dexverse"></a>**DexVerse** (2026) `Sim` `new`: Isaac Lab benchmark of 100 dexterous tasks in eight categories (primitive, functional, articulation, non-prehensile, contact-rich, bimanual, multi-goal, long-horizon) with support for 3 arms and 6 hands, configurable visual variation, and 3,180 VR-teleoperated demonstrations.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2607.08751) | [Website](https://ycyao216.github.io/DexVerse.site) | [Code](https://github.com/ycyao216/DexVerse) ★122 | [Data](https://huggingface.co/datasets/dexverse/DexVerse_release)

- <a id="handson"></a>**HandsOn** (2026) `Sim` `new`: Isaac Sim benchmark for dexterous manipulation on a bimanual arm-hand platform, with support for 5 arms and 6 hands. Its 66 human-verified tasks split into Core-50, backed by 18,000 demonstrations, and Transfer-16, which tests asset transfer, skill composition and deformables without target-task demonstrations.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2610.26765) | [Website](https://llltttwww.github.io/HandsOn-website/) | [Code](https://github.com/TsinghuaC3I/HandsOn) ★82 | [Data](https://huggingface.co/datasets/Cyan666/HandsOn-Datasets) | [Leaderboard](https://llltttwww.github.io/HandsOn-website/leaderboard.html)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| **[Adroit Hand](#adroit-hand-dapg)** | single hand, RL with demonstrations | 4 (door, hammer, pen, relocate) | 1 (success rate) | 1 (Adroit: Shadow Hand on a free arm) | state, proprioceptive | MuJoCo | Human demos | 25 human demos per task (DAPG); larger D4RL / Minari sets |
| **[Shadow Dexterous Hand](#shadow-dexterous-hand-gymnasium-robotics)** | in-hand manipulation | 4 + touch-sensor variants | 1 (success rate) | 1 (Shadow Dexterous Hand) | state, proprioceptive, tactile | MuJoCo | - | N/A |
| [TriFinger Real Robot Challenge](#trifinger-real-robot-challenge) | real robot, remote evaluation | 2 in the 2022 edition | 1 | 1 (TriFinger) | RGB, proprioceptive, state | PyBullet (trifinger_simulation) + real | RL policy | Dozens of hours of real and simulated robot data (push, lift) |
| [DexMV](#dexmv) | human video to robot, imitation learning | 3 (relocate, pour, place inside) | 1 (success rate) | 1 (Adroit hand) | video, hand pose, state | MuJoCo | Human demos | Human videos retargeted to robot demonstrations (count N/A) |
| [IsaacGymEnvs Hand Tasks](#isaacgymenvs-hand-tasks) | in-hand reorientation, GPU-parallel RL | 5 families | 1 | 4 | state, proprioceptive | Isaac Gym (PhysX) | - | N/A |
| [MyoSuite](#myosuite) | musculoskeletal control, MyoChallenge | 8 MyoChallenge tasks + pose / reach / manipulation families | 1 (success rate) | 5 model families | state, proprioceptive | MuJoCo (CPU), mjlab and MJX (GPU) | - | N/A |
| [DexArt](#dexart) | articulated objects, point-cloud RL | 4 | 1 | 1 (XArm6 + Allegro Hand) | pointcloud, proprioceptive | SAPIEN | - | N/A |
| [VTDexManip](#vtdexmanip) | visual-tactile, pretraining, RL | 6 benchmark tasks | N/A | N/A | RGB, tactile, proprioceptive | Isaac Gym | Human demos | 2,032 human visual-tactile sequences, 10 tasks, 182 objects |
| [POMDAR](#pomdar) | hand hardware evaluation, taxonomy-based | 18 | 1 | Any anthropomorphic hand | state | MuJoCo + real | - | N/A |
| [DexJoCo](#dexjoco) | task-oriented, tool use, VLA evaluation | 11 | 1 (success rate) | 1 (Franka Panda + Allegro Hand) | RGB, proprioceptive, state | MuJoCo | Human demos | 1.1K human demonstration trajectories |
| [DexVerse](#dexverse) | multi-task, multi-embodiment | 100 | 1 (success rate) | 3 arms x 6 dexterous hands | RGB, depth, pointcloud, proprioceptive, state | Isaac Lab (Isaac Sim) | Human demos | 3,180 VR-teleoperated demonstrations |
| [HandsOn](#handson) | cross-embodiment, generalisation | 66 (Core-50 + Transfer-16) | 1 | 5 arms, 6 hands | RGB, proprioceptive, language | Isaac Sim 5.1 (PhysX) | Human demos | 18,000 human demonstrations (6.05M timesteps) |

### <a id="dexterous-manipulation-dex-bimanual"></a>Bimanual Dexterity

- <a id="bi-dexhands"></a>**Bi-DexHands** (2022) `Sim` `widely used`: Isaac Gym benchmark of 20 bimanual tasks for two Shadow Hands (handover, catch, lift, door, bottle cap, scissors and others), graded against stages of human motor development. Covers over 2,000 objects and supports single-agent, multi-agent, multi-task, meta and offline RL.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2206.08686) (NeurIPS 2022 D&B) | [Website](https://pku-marl.github.io/DexterousHands/) | [Code](https://github.com/PKU-MARL/DexterousHands) ★1.1k

- <a id="robopianist"></a>**RoboPianist** (2023) `Sim`: MuJoCo benchmark in which two simulated Shadow Hands learn to play piano pieces from MIDI files with fingering annotations. A repertoire of 150 pieces tests spatial and temporal precision, finger coordination and planning, scored by key-press precision, recall and F1.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2304.04150) (CoRL 2023) | [Website](https://kzakka.com/robopianist/) | [Code](https://github.com/google-research/robopianist) ★738

- <a id="dexmimicgen"></a>**DexMimicGen** (2024) `Sim`: Nine robosuite tasks for bimanual imitation learning across three embodiments (two Panda arms with grippers, two Panda arms with dexterous hands, a GR-1 humanoid with dexterous hands), with about 21K demonstrations generated automatically from 60 human teleoperated demos.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2410.24185) (ICRA 2025) | [Website](https://dexmimicgen.github.io/) | [Code](https://github.com/NVlabs/dexmimicgen) ★301 | [Data](https://huggingface.co/datasets/MimicGen/dexmimicgen_datasets)

- <a id="dexmanipnet-maniptrans"></a>**DexManipNet (ManipTrans)** (2025) `Sim`: Dataset of 3.3K dexterous-hand manipulation episodes (61 tasks, about 600 bimanual sequences) executed in Isaac Gym with Inspire Hands. Produced by ManipTrans, a two-stage residual-learning method that transfers human hand-object motion from OakInk-V2 and FAVOR to robot hands.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2503.21860) (CVPR 2025) | [Website](https://maniptrans.github.io) | [Code](https://github.com/ManipTrans/ManipTrans) ★350 | [Data](https://huggingface.co/datasets/LiKailin/DexManipNet)

- <a id="dexgarmentlab"></a>**DexGarmentLab** (2025) `Sim`: Isaac Sim environment for dexterous, mostly bimanual, garment manipulation with two UR10e arms and Shadow Hands: 15 task scenarios (fling, fold, hang, wear, store) over 2,500+ garments. Demonstrations are collected automatically using category-level garment correspondence.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2505.11032) (NeurIPS 2025) | [Website](https://wayrise.github.io/DexGarmentLab/) | [Code](https://github.com/wayrise/DexGarmentLab) ★168 | [Data](https://huggingface.co/datasets/wayrise/DexGarmentLab)

- <a id="teleopbench"></a>**TeleOpBench** (2025) `Sim + Real`: Isaac Sim benchmark for comparing bimanual dexterous teleoperation interfaces: 30 tasks on humanoids with dexterous hands and four reference modalities (motion capture, VR, exoskeleton, monocular vision). Mirrored real-robot runs on 10 tasks correlate with the simulated results.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2505.12748) | [Website](https://gorgeous2002.github.io/TeleOpBench/) | [Code](https://github.com/cyjdlhy/TeleOpBench) ★54

- <a id="dexmachina"></a>**DexMachina** (2025) `Sim`: Benchmark and curriculum-RL method for functional retargeting: two dexterous hands must reproduce the object motion of ARCTIC human demonstrations on long-horizon tasks with articulated objects. Six robot hands share the same clips in Genesis, which allows hardware designs to be compared.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2505.24853) (ICML 2026) | [Website](https://project-dexmachina.github.io) | [Code](https://github.com/MandiZhao/dexmachina) ★283

- <a id="humanoidgen"></a>**HumanoidGen** (2025) `Sim`: Automated task-creation and demonstration-collection framework for humanoid bimanual dexterous manipulation, in which an LLM planner writes chains of spatial constraints that a solver turns into actions. Its HGen-Bench has 20 tabletop tasks for a Unitree H1-2 with Inspire hands, with 2D and 3D diffusion-policy baselines.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2507.00833) (NeurIPS 2025) | [Website](https://openhumanoidgen.github.io/) | [Code](https://github.com/TeleHuman/HumanoidGen) ★149 | [Data](https://huggingface.co/datasets/TeleEmbodied/humanoidgen_dataset)

- <a id="bench2dex"></a>**Bench2Dex** (2026) `Sim` `new`: Isaac Lab benchmark of 26 multi-stage bimanual tasks (tool use, articulated objects) across 12 arm-hand embodiments that share one simulated fingertip visuo-tactile interface. Comes with about 1.3K teleoperated demonstrations and a robustness protocol built from seven scene perturbations.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2609.15726) | [Website](https://bench2dex.github.io/) | [Code](https://github.com/Bench2Dex/Bench2Dex) ★108 | [Data](https://huggingface.co/Bench2Dex) | [Leaderboard](https://bench2dex.github.io/Bench2Dex-Leaderboard/)

- <a id="v2d-challenge-video-to-data"></a>**V2D Challenge (Video to Data)** (2026) `Sim` `new`: NVIDIA challenge on turning human video into robot skills, with three coupled tracks: monocular 4D human-object reconstruction, robotic grounding (tracking policies for a Unitree G1 with Dex3 hands from clean, corrupted or reconstructed references) and egocentric video-to-policy. Submissions are scored on Kaggle.<br>
  *Resources*: [Website](https://nvidia-isaac.github.io/video_to_data/v2d_challenge/) | [Code](https://github.com/nvidia-isaac/video_to_data) ★1k | [Data](https://huggingface.co/datasets/nvidia/video_to_data_challenge) | [Leaderboard](https://nvidia-isaac.github.io/video_to_data/v2d_challenge/#leaderboard)

- <a id="bidex-100"></a>**BiDex-100** (2026) `Sim` `new`: MuJoCo benchmark of 106 bimanual dexterous tasks organised along five capability axes (generalisation, instruction following, limited demonstrations, long horizon, memory), each paired with an out-of-domain variant. Provides 8,080 teleoperated demonstrations on two platforms with 22-DoF hands.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2610.25459) | [Website](https://robbyant-research.github.io/BiDex-100/) | [Code](https://github.com/robbyant-research/BiDex-100) ★11 | [Data](https://huggingface.co/datasets/Robbyant-Research/BiDex-100) | [Leaderboard](https://robbyant-research.github.io/BiDex-100/leaderboard.html)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| **[Bi-DexHands](#bi-dexhands)** | two Shadow Hands, RL and multi-agent RL | 20 | 1 | 1 (two Shadow Hands) | state, proprioceptive, pointcloud, RGB | Isaac Gym | RL policy | Offline-RL datasets collected with PPO policies |
| [RoboPianist](#robopianist) | piano playing, high-dimensional control | 150 piano pieces | 3 | 1 (two Shadow Hands) | state, proprioceptive | MuJoCo | - | N/A (pieces come from the PIG piano-fingering dataset) |
| [DexMimicGen](#dexmimicgen) | data generation, imitation learning | 9 | 1 (success rate) | 3 | RGB, proprioceptive | robosuite (MuJoCo) | Mixed | ~21K generated demos from 60 human source demos |
| [DexManipNet](#dexmanipnet-maniptrans) | human-to-robot transfer | 61 | N/A | 1 | state, hand pose | Isaac Gym | RL policy | 3.3K episodes, 1.34M frames, 1.2K objects |
| [DexGarmentLab](#dexgarmentlab) | garments, bimanual dexterous hands | 15 | 1 (success rate) | 1 (two UR10e arms + Shadow Hands) | RGB, pointcloud, proprioceptive | Isaac Sim 4.5 | Planner | 100 automatically collected demonstrations per task |
| [TeleOpBench](#teleopbench) | teleoperation systems, humanoid | 30 | 2 | 3 | RGB, hand pose, mocap | Isaac Sim + real | - | N/A |
| [DexMachina](#dexmachina) | functional retargeting | 7 ARCTIC demonstration clips | 1 | 6 hands | state, hand pose | Genesis | Human demos | 7 curated ARCTIC clips plus processed hand assets |
| [HumanoidGen](#humanoidgen) | humanoid bimanual dexterous manipulation | 20 | 1 (success rate) | 1 (Unitree H1-2 with Inspire hands) | RGB, pointcloud, proprioceptive | ManiSkill (SAPIEN) | Planner | Generated demonstrations for the 20 tasks (count not stated) |
| [Bench2Dex](#bench2dex) | visuo-tactile, cross-hand, long-horizon | 26 | 3 | 12 arm-hand embodiments | RGB, tactile, proprioceptive, state | Isaac Lab (Isaac Sim) | Human demos | ~1.3K human-teleoperated demonstrations |
| [V2D Challenge](#v2d-challenge-video-to-data) | human video to robot, challenge | 3 tracks | Track 2: 4 | 1 in Track 2 (Unitree G1 + Dex3 hands) | video, RGB, mocap, state | Isaac Lab (starter toolkit) | Human demos | 30 human-object interaction episodes each for Tracks 1 and 2 |
| [BiDex-100](#bidex-100) | VLA evaluation, high-DoF hands | 106 | 2 | 2 | RGB, depth, proprioceptive, language | MuJoCo | Human demos | 8,080 teleoperated demonstrations (6.25M frames) |

### <a id="dexterous-manipulation-dex-grasping"></a>Dexterous Grasping

- <a id="multidex-gendexgrasp"></a>**MultiDex (GenDexGrasp)** (2022) `Sim`: Multi-hand grasp dataset released with GenDexGrasp: 436,000 force-closure grasps of 58 household objects (YCB, ContactDB) for five hands with two to five fingers (EZGripper, Barrett, Robotiq-3F, Allegro, Shadow Hand). A common test bed for grasp generation that transfers across hands.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2210.00722) (ICRA 2023) | [Website](https://sites.google.com/view/gendexgrasp/multidex) | [Code](https://github.com/tengyu-liu/GenDexGrasp) ★213

- <a id="dexgraspnet"></a>**DexGraspNet** (2022) `Sim` `widely used`: Synthetic dataset of 1.32 million Shadow Hand grasps on 5,355 objects from more than 133 categories, generated with an accelerated differentiable force-closure estimator and validated in Isaac Gym. The usual training and comparison set for dexterous grasp synthesis.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2210.02697) (ICRA 2023) | [Website](https://pku-epic.github.io/DexGraspNet/) | [Code](https://github.com/PKU-EPIC/DexGraspNet) ★483

- <a id="unidexgrasp"></a>**UniDexGrasp** (2023) `Sim`: Table-top grasp-and-lift setting for a Shadow Hand from point-cloud input in Isaac Gym, with 3,200 training objects and held-out test sets of seen-category and unseen-category objects. The follow-up UniDexGrasp++ uses the same setting.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2303.00938) (CVPR 2023) | [Website](https://pku-epic.github.io/UniDexGrasp/) | [Code](https://github.com/PKU-EPIC/UniDexGrasp) ★276

- <a id="dexgraspnet-2-0"></a>**DexGraspNet 2.0** (2024) `Sim`: Synthetic benchmark for dexterous grasping in clutter: 427 million LEAP Hand grasp labels over 8,270 scenes built from 1,319 objects. Models receive a single-view depth point cloud and are scored by grasp success in Isaac Gym; the paper also reports zero-shot real-world transfer.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2410.23004) (CoRL 2024) | [Website](https://pku-epic.github.io/DexGraspNet2.0/) | [Code](https://github.com/PKU-EPIC/DexGraspNet2) ★165 | [Data](https://huggingface.co/datasets/lhrlhr/DexGraspNet2.0)

- <a id="dexgraspbench-bodex"></a>**DexGraspBench (BODex)** (2024) `Sim`: MuJoCo benchmark that replays open-loop dexterous grasps so that synthesis methods and datasets can be compared on equal terms, reporting simulation success, force-closure, penetration, contact and diversity metrics. Released with the BODex bilevel-optimisation pipeline and its grasp dataset.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2412.16490) (ICRA 2025) | [Website](https://pku-epic.github.io/BODex/) | [Code](https://github.com/JYChen18/DexGraspBench) ★67 | [Data](https://huggingface.co/datasets/JiayiChenPKU/BODex)

- <a id="dexonomy"></a>**Dexonomy** (2025) `Sim`: Grasp dataset that covers the GRASP taxonomy: 9.5 million simulation-validated grasps of 31 grasp types on 10.7k objects, synthesised from one human-annotated template per hand and grasp type. The released pipeline supports Shadow, Allegro, LEAP, MANO and Unitree G1 hands.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2504.18829) (RSS 2025) | [Website](https://pku-epic.github.io/Dexonomy) | [Code](https://github.com/JYChen18/Dexonomy) ★170 | [Data](https://huggingface.co/datasets/JiayiChenPKU/Dexonomy)

- <a id="dexh2r"></a>**DexH2R** (2025) `Real`: Real-world dataset and benchmark for dynamic dexterous grasping in human-to-robot handover: 4,282 teleoperated handover trials (456K frames) from 39 participants and 56 objects with a Shadow Hand on a UR10e, recorded with multi-view RGB-D. Baselines cover autoregressive and diffusion-policy motion generation.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2506.23152) (ICCV 2025) | [Website](https://dexh2r.github.io/) | [Code](https://github.com/4DVLab/DexH2R) ★30

- <a id="hrdexdb"></a>**HRDexDB** (2026) `Real` `new`: Real-world 4D grasping dataset in which a human hand and four robot end-effectors (Allegro, two Inspire hands, Robotiq 2F-85) grasp the same 100 objects: 3.2K trials, with robot grasps teleoperated after a human reference, captured by a synchronised multi-camera rig with 3D trajectories and success labels.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2604.14944) | [Website](https://snuvclab.github.io/HRDexDB/) | [Code](https://github.com/snuvclab/HRDexDB) ★47 | [Data](https://huggingface.co/datasets/HRDexDB/HRDexDB)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| [MultiDex](#multidex-gendexgrasp) | multi-hand grasp dataset | N/A | 3 | 5 | pointcloud, state | Isaac Gym (grasp validation) | Synthetic | 436,000 grasps, 58 objects, 5 hands |
| **[DexGraspNet](#dexgraspnet)** | grasp dataset, Shadow Hand | N/A | N/A | 1 | state | Isaac Gym (grasp validation) | Synthetic | 1.32M grasps on 5,355 objects |
| [UniDexGrasp](#unidexgrasp) | grasp policy learning, point clouds | 1 (grasp and lift) | 1 (success rate) | 1 (Shadow Hand) | pointcloud, proprioceptive | Isaac Gym | Synthetic | Synthesised grasp labels; 3,200 train + 141 + 100 test objects |
| [DexGraspNet 2.0](#dexgraspnet-2-0) | cluttered scenes, grasp benchmark | N/A | 1 | 1 (LEAP Hand) | depth, pointcloud | Isaac Gym | Synthetic | 427M grasps, 8,270 scenes, 1,319 objects |
| [DexGraspBench](#dexgraspbench-bodex) | grasp synthesis benchmark | 2 settings | 5+ | 4 | state, pointcloud | MuJoCo | Synthetic | BODex: 4.09M floating + 3.08M tabletop grasps, 2,397 objects |
| [Dexonomy](#dexonomy) | grasp taxonomy, type-conditioned grasps | N/A | N/A | 5 hands | state, pointcloud | MuJoCo | Synthetic | 9.5M grasps, 10.7k objects, 31 grasp types |
| [DexH2R](#dexh2r) | human-to-robot handover | 1 | 3 | 1 (UR10e + Shadow Hand) | RGB, depth, pointcloud, proprioceptive | Real world | Human demos | 4,282 handover trials, 456K frames, 56 objects, 39 people |
| [HRDexDB](#hrdexdb) | paired human-robot grasps, real world | N/A | N/A | 5 embodiments | RGB, hand pose, proprioceptive, tactile | Real world | Human demos | 3.2K trials, 43.5M frames, 100 objects (about 1.6 TB) |

### <a id="dexterous-manipulation-hand-object-data"></a>Human Hand-Object Data

- <a id="ho-3d"></a>**HO-3D** (2019) `Real` `widely used`: Markerless RGB-D dataset of a hand manipulating YCB objects, with 3D hand and object pose annotations produced by the HOnnotate optimisation method. Version 3 holds 103,462 annotated images; CodaLab servers score hand pose on the held-out test set.<br>
  *Resources*: [Paper](https://arxiv.org/abs/1907.01481) (CVPR 2020) | [Website](https://www.tugraz.at/index.php?id=40231) | [Code](https://github.com/shreyashampali/ho3d) ★252 | [Leaderboard](https://codalab.lisn.upsaclay.fr/competitions/4318)

- <a id="grab"></a>**GRAB** (2020) `Real` `widely used`: Motion-capture dataset of whole-body grasps: 10 subjects interacting with 51 everyday objects under four motion intents, with full 3D body, hand and face meshes, object pose and contact maps. A main data source for grasp synthesis and for retargeting human grasps to robot hands.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2008.11200) (ECCV 2020) | [Website](https://grab.is.tue.mpg.de) | [Code](https://github.com/otaheri/GRAB) ★406

- <a id="dexycb"></a>**DexYCB** (2021) `Real` `widely used`: Multi-camera RGB-D dataset of 10 subjects grasping YCB objects, with 3D hand pose and 6D object pose labels. Defines benchmarks for 2D detection, 6D object pose, 3D hand pose and safe human-to-robot handover, and is a standard test set for hand-object reconstruction.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2104.04631) (CVPR 2021) | [Website](https://dex-ycb.github.io) | [Code](https://github.com/NVlabs/dex-ycb-toolkit) ★215

- <a id="hoi4d"></a>**HOI4D** (2022) `Real`: Egocentric RGB-D dataset for category-level human-object interaction: 2.4M frames in over 4,000 sequences covering 800 object instances from 16 categories in 610 indoor rooms, annotated with panoptic and motion segmentation, 3D hand pose, category-level object pose and hand actions.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2203.01577) (CVPR 2022) | [Website](https://hoi4d.github.io/) | [Code](https://github.com/leolyliu/HOI4D-Instructions) ★98

- <a id="oakink"></a>**OakInk** (2022) `Real`: Hand-object interaction repository in two parts: Oak, 1,800 household objects annotated with affordances, and Ink, 50,000 intent-oriented interactions recorded on 100 of the objects and transferred to the rest. Benchmarked on hand-object pose estimation and grasp generation.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2203.15709) (CVPR 2022) | [Website](https://oakink.net) | [Code](https://github.com/oakink/OakInk) ★153

- <a id="arctic"></a>**ARCTIC** (2022) `Real` `widely used`: Dataset of two hands dexterously manipulating articulated objects such as scissors and laptops: 2.1M video frames from eight static views and one egocentric view, with motion-capture ground truth for SMPL-X bodies, MANO hands, articulated objects and contact. A main human source for bimanual dexterous retargeting.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2204.13662) (CVPR 2023) | [Website](https://arctic.is.tue.mpg.de) | [Code](https://github.com/zc-alexfan/arctic) ★533 | [Leaderboard](https://arctic-leaderboard.is.tuebingen.mpg.de/)

- <a id="taco"></a>**TACO** (2024) `Real`: Bimanual tool-action-object dataset: about 2.5K motion sequences of two hands using a tool on a target object, with third-person and egocentric video, precise hand-object meshes and action labels. Benchmarks compositional action recognition, motion forecasting and cooperative grasp synthesis.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2401.08399) (CVPR 2024) | [Website](https://taco2024.github.io) | [Code](https://github.com/leolyliu/TACO-Instructions) ★79 | [Data](https://huggingface.co/datasets/leolyliu/TACO)

- <a id="oakink2"></a>**OakInk2** (2024) `Real`: Bimanual hand-object manipulation dataset organised in three levels (object affordance, primitive task, complex task), with multi-view image streams and pose annotations for body, hands and objects. Used as a human-motion source for bimanual dexterous transfer, for example in ManipTrans.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2403.19417) (CVPR 2024) | [Website](https://oakink.net/v2) | [Code](https://github.com/oakink/OakInk2) ★115 | [Data](https://huggingface.co/datasets/kelvin34501/OakInk-v2)

- <a id="hot3d"></a>**HOT3D** (2024) `Real`: Egocentric dataset for 3D hand and object tracking recorded with Project Aria glasses and Quest 3 headsets: 833 minutes (3.7M+ images) of 19 subjects handling 33 rigid objects, with motion-capture ground-truth poses. A curated subset was used in the BOP Challenge 2024.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2411.19167) (CVPR 2025) | [Website](https://facebookresearch.github.io/hot3d/) | [Code](https://github.com/facebookresearch/hot3d) ★298 | [Data](https://huggingface.co/datasets/bop-benchmark/hot3d)

- <a id="gigahands"></a>**GigaHands** (2024) `Real`: Markerless multi-view capture of bimanual hand activities: 34 hours from 56 subjects and 417 objects, giving 14k motion clips (183M frames) with 3D hand and object poses and 84k text annotations. Supports text-driven motion synthesis and captioning, and serves as retargeting data.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2412.04244) (CVPR 2025) | [Website](https://ivl.cs.brown.edu/research/gigahands.html) | [Code](https://github.com/brown-ivl/GigaHands) ★140 | [Data](https://huggingface.co/datasets/freddie007/GigaHands)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| **[HO-3D](#ho-3d)** | hand-object pose, markerless | 1 | N/A | N/A | RGB, depth, hand pose | Real world | Human demos | v2: 77,558 frames, 68 sequences, 10 objects; v3: 103,462 images |
| **[GRAB](#grab)** | whole-body grasping, contact | N/A | N/A | N/A | mocap, hand pose | Real world | Human demos | 10 subjects, 51 objects, 4 motion intents |
| **[DexYCB](#dexycb)** | hand-object pose, handover | 4 | 4 protocols | N/A | RGB, depth, hand pose | Real world | Human demos | 10 subjects, 8 RGB-D views, YCB objects (119 GB) |
| [HOI4D](#hoi4d) | egocentric RGB-D, category-level | 3 | N/A | N/A | RGB, depth, pointcloud, hand pose | Real world | Human demos | 2.4M RGB-D frames, 4,000+ sequences, 800 objects |
| [OakInk](#oakink) | affordance-aware hand-object interaction | 2 | N/A | N/A | RGB, hand pose, mocap | Real world | Mixed | 50,000 interactions, 1,800 objects; 792 clips (230K images) |
| **[ARCTIC](#arctic)** | bimanual, articulated objects | 2 | N/A | N/A | RGB, hand pose, mocap | Real world | Human demos | 2.1M frames from 9 views (8 static + 1 egocentric) |
| [TACO](#taco) | bimanual tool use | 3 | N/A | N/A | RGB, hand pose, mocap | Real world | Human demos | 2.5K sequences (v1 release: 2,317 over 151 triplets) |
| [OakInk2](#oakink2) | bimanual, long-horizon tasks | N/A | N/A | N/A | RGB, hand pose, mocap, language | Real world | Human demos | Multi-view sequences, 1M-10M frames (dataset card) |
| [HOT3D](#hot3d) | egocentric multi-view | 3 | N/A | N/A | RGB, hand pose, mocap | Real world | Human demos | 833 min, 3.7M+ images, 19 subjects, 33 objects |
| [GigaHands](#gigahands) | bimanual activities, text annotations | N/A | N/A | N/A | RGB, hand pose, language | Real world | Human demos | 34 h, 14k clips, 183M frames, 417 objects, 84k captions |

<p align="right"><a href="#contents">Back to contents ↑</a></p>

---

## <a id="generalist"></a>Generalist Policies & VLA Evaluation

How generalist robot policies and vision-language-action models (VLAs) are evaluated: multi-domain suites, real robots, simulated stand-ins for real setups, and stress tests. **27 entries.**

**Sub-areas:** [Multi-Domain Suites](#generalist-multi-domain) (5) · [Real-World Evaluation](#generalist-real-eval) (6) · [Real-to-Sim Evaluation](#generalist-real2sim) (6) · [Generalization, Robustness & Memory Probes](#generalist-probes) (10)

### <a id="generalist-multi-domain"></a>Multi-Domain Suites

- <a id="maniskill"></a>**ManiSkill** (2021) `Sim` `widely used`: SAPIEN-based benchmark family for generalisable manipulation skills. ManiSkill (2021) tested generalisation over object geometry, ManiSkill2 (2023) grew to 20 task families, and ManiSkill3 (2024), the current version, is a GPU-parallelised simulator and benchmark with 12 task categories and 20+ robots.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2410.00425) (NeurIPS 2021 D&B (ManiSkill3: RSS 2025)) | [Website](https://maniskill.ai/) | [Code](https://github.com/mani-skill/ManiSkill) ★3.5k | [Data](https://huggingface.co/datasets/haosulab/ManiSkill_Demonstrations)

- <a id="robocasa-gr-1-tabletop-tasks"></a>**RoboCasa GR-1 Tabletop Tasks** (2025) `Sim`: Simulation suite released with GR00T N1: 24 language-conditioned tabletop tasks (18 rearrangement, 6 with articulated objects) for a Fourier GR-1 humanoid with dexterous hands, observed through one egocentric head camera. Later humanoid VLA papers report on it.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2503.14734) | [Code](https://github.com/robocasa/robocasa-gr1-tabletop-tasks) ★167 | [Data](https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-GR00T-Teleop-Sim)

- <a id="genie-sim"></a>**Genie Sim** (2025) `Sim`: AgiBot's open simulation platform and benchmark for its Genie robots. Version 3.0 (January 2026) added LLM-generated scenes and evaluation configurations with VLM-based scoring; the benchmark now backs the RoboColiseum leaderboard, with instruction, robustness, manipulation and spatial boards.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2601.02078) | [Website](https://agibot-world.com/genie-sim) | [Code](https://github.com/AgibotTech/genie_sim) ★1.7k | [Data](https://modelscope.cn/datasets/agibot_world/GenieSim3.0-Dataset) | [Leaderboard](https://robocoliseum.ai/)

- <a id="vla-eval"></a>**vla-eval** (2026) `Sim` `new`: Open evaluation harness hosted by AllenAI that runs any VLA on many simulation benchmarks through one model interface and Docker-isolated environments. It maintains a leaderboard aggregating published VLA results under fixed per-benchmark protocols.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2603.13966) | [Website](https://allenai.github.io/vla-evaluation-harness/) | [Code](https://github.com/allenai/vla-evaluation-harness) ★682 | [Leaderboard](https://allenai.github.io/vla-evaluation-harness/leaderboard/)

- <a id="robodojo"></a>**RoboDojo** (2026) `Sim + Real` `new`: Unified sim-and-real benchmark for generalist manipulation policies: 42 Isaac Sim tasks grouped into generalisation, memory, precision, long-horizon and open-vocabulary instruction following, plus 18 real-world tasks on three bimanual platforms run remotely through the RoboDojo-RealEval system.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2607.04434) | [Website](https://robodojo-benchmark.com/) | [Code](https://github.com/RoboDojo-Benchmark/RoboDojo) ★942 | [Leaderboard](https://robodojo-benchmark.com/leaderboard)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| **[ManiSkill](#maniskill)** | GPU-parallel simulation benchmark | 12 task categories | 1 (task success rate) | 20+ | RGB, depth, pointcloud, segmentation, proprioceptive, state | SAPIEN (PhysX, GPU-parallel) | Mixed | demonstrations for many tasks (motion planning, RL and teleoperation) |
| [RoboCasa GR-1 Tabletop Tasks](#robocasa-gr-1-tabletop-tasks) | humanoid dexterous tabletop | 24 | 1 (success rate) | 1 (Fourier GR-1 with dexterous hands) | RGB, proprioceptive, language | RoboCasa / robosuite (MuJoCo) | Mixed | 1,000 demos per task (24,000), generated with DexMimicGen |
| [Genie Sim](#genie-sim) | simulation platform and benchmark | 200+ tasks, 100,000+ generated scenarios | N/A | 2 (AgiBot Genie G1, G2) | RGB, proprioceptive, language | Isaac Sim (PhysX); Newton and MuJoCo for some tasks | Mixed | 10,000+ hours of synthetic data over 200+ tasks |
| [vla-eval](#vla-eval) | cross-benchmark harness | 18+ integrated simulation benchmarks | N/A | N/A (per benchmark) | RGB, proprioceptive, language | per benchmark (LIBERO, SimplerEnv, CALVIN, RoboTwin, ...) | - | N/A (leaderboard of published results; no trajectories) |
| [RoboDojo](#robodojo) | simulation plus remote real-robot evaluation | 60 | 2 | 3 (ARX X5, Piper, Piper X; all bimanual) | RGB, depth, proprioceptive, language | Isaac Sim + real | Mixed | 3,500 sim trajectories (20.7 h) and 1,800 real teleop demos (17.9 h) |

### <a id="generalist-real-eval"></a>Real-World Evaluation

- <a id="autoeval"></a>**AutoEval** (2025) `Real`: System for around-the-clock real-robot evaluation with automatic success detection and scene resets. Users submit policies to a job queue served by public WidowX cells in the BridgeData setup and receive evaluation reports; the four launch tasks were scheduled to run through 2025.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2503.24278) (CoRL 2025) | [Website](https://auto-eval.github.io/) | [Code](https://github.com/zhouzypaul/auto_eval) ★109 | [Data](https://huggingface.co/datasets/zhouzypaul/auto_eval)

- <a id="agibot-world-challenge"></a>**AgiBot World Challenge** (2025) `Sim + Real`: Competition series run by AgiBot (IROS 2025 with OpenDriveLab, ICRA 2026). Teams in the manipulation track train on AgiBot World data, qualify online on 10 Genie Sim tasks, and finalists are ranked by task success on real AgiBot robots. A second track scores world models.<br>
  *Resources*: [Website](https://agibot-world.com/challenge2026) | [Code](https://github.com/AgibotTech/genie_sim) ★1.7k | [Data](https://huggingface.co/datasets/agibot-world/AgiBotWorldChallenge-2026)

- <a id="roboarena"></a>**RoboArena** (2025) `Real`: Crowd-sourced real-world evaluation of generalist policies on the DROID platform: evaluators at seven universities pick their own scenes and tasks and run double-blind A/B comparisons of two policies, which are aggregated into a global ranking.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2506.18123) (CoRL 2025) | [Website](https://robo-arena.github.io/) | [Code](https://github.com/robo-arena/roboarena) ★117 | [Leaderboard](https://robo-arena.github.io/)

- <a id="robochallenge-table30"></a>**RoboChallenge (Table30)** (2025) `Real`: Online real-robot testing service from Dexmal and Hugging Face. Users fine-tune on released demonstrations and control a hosted fleet of robots remotely; the first benchmark, Table30, has 30 tabletop tasks, and Table30 v2 followed in 2026.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2510.17950) | [Website](https://robochallenge.ai) | [Code](https://github.com/RoboChallenge/RoboChallengeInference) ★158 | [Data](https://huggingface.co/datasets/RoboChallenge/Table30) | [Leaderboard](https://robochallenge.ai)

- <a id="manipulationnet"></a>**ManipulationNet** (2026) `Real` `new`: NIST-supported infrastructure for real-world manipulation benchmarking: registered teams receive standard object kits, run tasks on their own robots through a common software client, and are judged centrally. Tasks form a Physical Skills track and an Embodied Reasoning track.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2603.04363) | [Website](https://manipulation-net.org/) | [Code](https://github.com/ManipulationNet/mnet_client) ★37 | [Leaderboard](https://manipulation-net.org/leaderboards.html)

- <a id="maniparena"></a>**ManipArena** (2026) `Real` `new`: Standardised real-robot benchmark from X Square Robot run in green-screen booths: 20 bimanual tasks for execution reasoning, semantic reasoning and mobile manipulation, with in-domain, visual-shift and semantic out-of-distribution trials and partial-credit scoring. Models are served remotely.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2603.28545) (CVPR 2026 Embodied AI Workshop challenge) | [Code](https://github.com/maniparena/maniparena-repo) ★57 | [Data](https://huggingface.co/datasets/ManipArena/maniparena-dataset)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| [AutoEval](#autoeval) | autonomous real-robot evaluation | 4 | 1 (success rate) | 1 (WidowX; two public cells) | RGB, proprioceptive, language | Real world | - | N/A (rollout logs are public; policies train on BridgeData) |
| [AgiBot World Challenge](#agibot-world-challenge) | competition series | 10 per edition | 1 (task success rate) | 1 per edition | RGB, depth, proprioceptive, language | Genie Sim (Isaac Sim) + real | Human demos | simulated and real-robot trajectories for each of the 10 tasks |
| [RoboArena](#roboarena) | distributed real-robot evaluation | open-ended | 3 | 1 (DROID Franka setup) | RGB, proprioceptive, language | Real world | - | N/A (no training set; policies train on DROID) |
| [RoboChallenge](#robochallenge-table30) | online real-robot testing | 30 (Table30) | 2 | 4 | RGB, proprioceptive, language | Real world | Human demos | up to 1,000 demonstration episodes per task |
| [ManipulationNet](#manipulationnet) | distributed real-world benchmarking | 5 released, 2 announced | N/A | any (teams use their own robots) | RGB, language | Real world | - | N/A |
| [ManipArena](#maniparena) | remote real-robot evaluation | 20 | 2 | 2 | RGB, proprioceptive, language | Real world | Human demos | 10,812 teleoperated trajectories (~188 h, 13.5M frames) |

### <a id="generalist-real2sim"></a>Real-to-Sim Evaluation

- <a id="simplerenv-simpler"></a>**SimplerEnv (SIMPLER)** (2024) `Sim` `widely used`: Simulated counterparts of the Google Robot and WidowX (Bridge) setups, built so that policies trained on real data can be scored in simulation; paired sim and real evaluations show strong correlation. A standard simulation testbed for VLA policies.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2405.05941) (CoRL 2024) | [Website](https://simpler-env.github.io/) | [Code](https://github.com/simpler-env/SimplerEnv) ★1.2k

- <a id="robotarena"></a>**RobotArena ∞** (2025) `Sim`: Converts demonstration videos from Bridge V2, DROID and RH20T into simulated environments automatically, then scores VLA policies there with VLM-based progress scoring and crowd-sourced pairwise preferences. Controlled perturbations of background, colour and object pose probe robustness.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2510.23571) (ICLR 2026) | [Website](https://robotarenainf.github.io/) | [Code](https://github.com/offjangir/RobotArena) ★20 | [Data](https://huggingface.co/datasets/sourlreapwr/RobotArena-Benchmark)

- <a id="polaris"></a>**PolaRiS** (2025) `Sim` `new`: Real-to-sim framework that reconstructs a real scene from a short video scan with Gaussian splatting and evaluates DROID policies in it after light simulation co-training. Reported scores correlate with real-world results and with RoboArena rankings.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2512.16881) (RSS 2026) | [Website](https://polaris-evals.github.io/) | [Code](https://github.com/arhanjain/polaris) ★252 | [Data](https://huggingface.co/datasets/owhan/PolaRiS-Hub)

- <a id="realm"></a>**REALM** (2025) `Sim` `new`: Simulation benchmark for VLA generalisation with high-fidelity rendering and robot control aligned to the DROID setup: 10 tasks tested under 15 visual, semantic and behavioural perturbations. Simulated task progress was validated against paired real-world rollouts.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2512.19562) (RA-L 2026) | [Website](https://martin-sedlacek.com/realm) | [Code](https://github.com/martin-sedlacek/REALM) ★72

- <a id="robolab"></a>**RoboLab** (2026) `Sim` `new`: NVIDIA simulation benchmark for policies trained only on real-world data. RoboLab-120 has 120 language-specified tasks along visual, procedural and relational axes at three difficulty levels, with graded subtask scores and sensitivity analysis under controlled perturbations.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2604.09860) (RSS 2026) | [Website](https://research.nvidia.com/labs/srl/projects/robolab/) | [Code](https://github.com/NVlabs/RoboLab) ★633 | [Leaderboard](https://research.nvidia.com/labs/srl/projects/robolab/leaderboard.html)

- <a id="x2real"></a>**X2Real** (2026) `Sim` `new`: Simulation benchmark from X Square Robot built on Isaac Lab-Arena and calibrated visually and physically against real hardware (0.84 sim-real correlation reported): 44 hierarchical long-horizon tasks over 10 capability dimensions, with domain randomisation and separate training and evaluation pipelines.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2609.27449) | [Website](https://x2robot.com/en/pages/x2real) | [Code](https://github.com/X-Square-Robot/x2real) ★33 | [Data](https://huggingface.co/datasets/x-square-robot/X2Real-Dataset)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| **[SimplerEnv](#simplerenv-simpler)** | real-to-sim proxy | 10 prepackaged, plus variants | 3 | 2 (Google Robot, WidowX) | RGB, proprioceptive, language | SAPIEN (ManiSkill2); GPU port in ManiSkill3 | - | N/A (policies are trained on real-robot data) |
| [RobotArena ∞](#robotarena) | automatic real-to-sim translation | hundreds of generated environments | 2 | 3 source setups | RGB, language | Genesis | - | N/A (8,749 human pairwise votes collected on BridgeSim) |
| [PolaRiS](#polaris) | real-to-sim via Gaussian splatting | 6 ready-made evaluation environments | 2 | 1 (DROID Franka setup) | RGB, proprioceptive, language | Isaac Lab (Isaac Sim) with Gaussian-splat rendering | Human demos | ~350 teleoperated simulation demos for co-training |
| [REALM](#realm) | real-to-sim validated | 10 x 15 perturbations | 2 | 1 (DROID Franka setup) | RGB, proprioceptive, language | Isaac Sim (OmniGibson) | - | N/A (policies train on DROID) |
| [RoboLab](#robolab) | simulation benchmark for real-world-trained policies | 120 (RoboLab-120) | 3+ | 1 by default (DROID Franka) | RGB, proprioceptive, language | Isaac Lab (Isaac Sim) | - | N/A (policies train on real data such as DROID) |
| [X2Real](#x2real) | calibrated simulation proxy | 44 (10 capability dimensions) | 2 | 4 | RGB, proprioceptive, language | Isaac Lab-Arena (Isaac Sim) | Mixed | ~300 h of annotated simulation trajectories |

### <a id="generalist-probes"></a>Generalization, Robustness & Memory Probes

- <a id="the-colosseum"></a>**THE COLOSSEUM** (2024) `Sim`: RLBench-based generalisation benchmark: 20 manipulation tasks evaluated under 14 perturbation factors covering object, table and background colour, texture and size, lighting, distractors, physical properties and camera pose. A matching real-world setup with 3D-printable objects is provided.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2402.08191) (RSS 2024) | [Website](https://robot-colosseum.github.io/) | [Code](https://github.com/robot-colosseum/robot-colosseum) ★162 | [Data](https://huggingface.co/datasets/colosseum/colosseum-challenge)

- <a id="memorybench-sam2act"></a>**MemoryBench (SAM2Act)** (2025) `Sim`: Three RLBench tasks introduced with SAM2Act (reopen drawer, put block back, rearrange block). An intermediate step breaks the Markov property, so the policy must recall earlier object locations and its own past actions.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2501.18564) (ICML 2025) | [Website](https://sam2act.github.io/) | [Code](https://github.com/sam2act/sam2act) ★253 | [Data](https://huggingface.co/datasets/hqfang/memorybench)

- <a id="mikasa-robo"></a>**MIKASA-Robo** (2025) `Sim`: Memory-intensive tabletop manipulation tasks on ManiSkill3 in which the cue for the correct action disappears from view. The original release has 32 tasks for memory RL; the 2026 rebuild, MIKASA-Robo-VLA, has 90 language-conditioned tasks over 10 memory types.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2502.10550) (ICLR 2026) | [Website](https://mikasarobo.github.io/) | [Code](https://github.com/CognitiveAISystems/MIKASA-Robo) ★146 | [Data](https://huggingface.co/mikasa-robo)

- <a id="int-act"></a>**INT-ACT** (2025) `Sim`: Probing suite that extends SimplerEnv's Bridge setup from 4 to 50 tasks across object diversity, language complexity and vision-language reasoning. An added intention metric separates whether a policy goes for the right object from whether it completes the task.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2506.09930) | [Website](https://ai4ce.github.io/INT-ACT/) | [Code](https://github.com/ai4ce/INT-ACT) ★34

- <a id="libero-pro"></a>**LIBERO-PRO** (2025) `Sim`: Evaluation extension of LIBERO that perturbs manipulated objects, initial positions, instructions, task goals and environments on the four standard suites; models above 90% on standard LIBERO fall to near zero. LIBERO-Pro2.0 (October 2026) widens this to 1,648 shifted task instances with runtime interventions.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2510.03827) | [Website](https://zxy-mllab.github.io/LIBERO-PRO-Webpage/) | [Code](https://github.com/Zxy-MLlab/LIBERO-PRO) ★362 | [Data](https://huggingface.co/datasets/zhouxueyang/LIBERO-Pro) | [Leaderboard](https://racingemperor.github.io/LIBERO-Pro2.0/leaderboard.html)

- <a id="libero-plus"></a>**LIBERO-Plus** (2025) `Sim`: Robustness extension of LIBERO: 10,030 task variants generated by perturbing object layout, camera viewpoint, robot initial state, language instruction, lighting, background texture and sensor noise at graded difficulty levels. Installs as a drop-in replacement for LIBERO.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2510.13626) (CVPR 2026) | [Website](https://sylvestf.github.io/LIBERO-plus/) | [Code](https://github.com/sylvestf/LIBERO-plus) ★502 | [Data](https://huggingface.co/datasets/Sylvest/LIBERO-plus)

- <a id="vla-arena"></a>**VLA-Arena** (2025) `Sim` `new`: Benchmark that grades VLA capability along task structure, language and vision: 170 tasks in 11 suites covering safety, distractors, extrapolation and long horizons at three difficulty levels, with optional language and visual perturbations. Models are fine-tuned on the easiest level only.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2512.22539) (ICML 2026) | [Website](https://vla-arena.github.io/) | [Code](https://github.com/PKU-Alignment/VLA-Arena) ★224 | [Data](https://huggingface.co/vla-arena) | [Leaderboard](https://vla-arena.github.io/#leaderboard)

- <a id="robomme"></a>**RoboMME** (2026) `Sim` `new`: Sixteen long-horizon, history-dependent manipulation tasks in four suites targeting temporal, spatial, object and procedural memory, used to compare memory designs for VLA policies. Maintains a public leaderboard and ran a CVPR 2026 challenge.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2603.04639) (ICML 2026) | [Website](https://robomme.github.io/) | [Code](https://github.com/RoboMME/robomme_benchmark) ★201 | [Data](https://huggingface.co/datasets/Yinpei/robomme_data_h5) | [Leaderboard](https://robomme.github.io/leaderboard.html)

- <a id="libero-para"></a>**LIBERO-Para** (2026) `Sim` `new`: Diagnostic benchmark for instruction paraphrasing in VLAs: over 4,000 paraphrases of LIBERO-Goal instructions that vary action expressions and object references independently across 43 paraphrase types, scored with the difficulty-aware PRIDE metric. A CALVIN version is included.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2603.28301) (EMNLP 2026) | [Website](https://cau-hai-lab.github.io/LIBERO-Para/) | [Code](https://github.com/cau-hai-lab/LIBERO-Para) ★52 | [Data](https://huggingface.co/datasets/HAI-Lab/LIBERO-Para)

- <a id="colosseum-v2"></a>**Colosseum V2** (2026) `Sim` `new`: Successor to THE COLOSSEUM, rebuilt on ManiSkill for GPU-parallel evaluation of VLAs: 28 tasks in 13 categories for single-arm and bimanual Franka setups, tested under 19 visual, language and action perturbations. Simulated trends are checked on real hardware.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2605.27759) (RA-L 2026) | [Website](https://colosseum-v2.github.io/) | [Code](https://github.com/jstmn/ColosseumV2) ★15

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| [THE COLOSSEUM](#the-colosseum) | generalisation under perturbations | 20 tasks x 14 perturbation factors | 1 | 1 (Franka Panda, RLBench default) | RGB, depth, proprioceptive, language | CoppeliaSim (PyRep / RLBench) | Planner | 100 training demos per task; 25 test episodes per task and factor |
| [MemoryBench](#memorybench-sam2act) | spatial memory, RLBench | 3 | 1 (success rate) | 1 (Franka Panda, RLBench default) | RGB, depth, proprioceptive, language | CoppeliaSim (RLBench) | Planner | 100 training and 25 test scripted demos per task |
| [MIKASA-Robo](#mikasa-robo) | memory, partial observability | 32 (original) | 1 (success rate) | 1 by default (Franka Panda) | RGB, proprioceptive, language, state | ManiSkill3 (SAPIEN) | Mixed | 22,500 oracle trajectories (RLDS and LeRobot formats) |
| [INT-ACT](#int-act) | generalisation probing | 50 | 3 | 1 (WidowX) | RGB, proprioceptive, language | SAPIEN (ManiSkill2, via SimplerEnv) | - | N/A (policies train on BridgeData V2) |
| [LIBERO-PRO](#libero-pro) | VLA generalisation versus memorisation | 4 LIBERO suites x 5 perturbation types | 1 (success rate) | 1 (Franka Panda) | RGB, proprioceptive, language | robosuite (MuJoCo) | Mixed | N/A for LIBERO-PRO (evaluation only); 39,390 trajectories in Pro2.0 |
| [LIBERO-Plus](#libero-plus) | VLA robustness | 10,030 perturbed task variants | 1 | 1 (Franka Panda) | RGB, proprioceptive, language | robosuite (MuJoCo) | Human demos | 20,000+ trajectories (LIBERO demos replayed in perturbed scenes) |
| [VLA-Arena](#vla-arena) | graded difficulty, safety | 170 | 2 | 1 (Franka Panda) | RGB, proprioceptive, language | robosuite (MuJoCo) | Human demos | 5,750 human demos (50 each for 115 L0/L1 tasks) |
| [RoboMME](#robomme) | memory, long-horizon, history-dependent | 16 (4 suites x 4 tasks) | 1 (success rate) | 1 (Franka Panda) | RGB, proprioceptive, language, video | ManiSkill (SAPIEN) | Planner | 1,600 demonstrations (100 per task, 770k timesteps) |
| [LIBERO-Para](#libero-para) | paraphrase robustness | 10 LIBERO-Goal scenarios, 4,000+ paraphrased instructions | 2 (success rate, PRIDE) | 1 (Franka Panda) | RGB, proprioceptive, language | robosuite (MuJoCo) | Synthetic | 4,000+ LLM-generated, verified paraphrases; no new trajectories |
| [Colosseum V2](#colosseum-v2) | VLA generalisation under perturbations | 28 tasks x 19 perturbations | 1 | 2 | RGB, proprioceptive, language | ManiSkill (SAPIEN, GPU-parallel) | Planner | 100 perturbation-free demos per task |

<p align="right"><a href="#contents">Back to contents ↑</a></p>

---

## <a id="world-models"></a>World Models & World-Action Models

Benchmarks for learned simulators of the physical world, for world models that score robot policies, and for the physical plausibility of generated video. **26 entries.**

**Sub-areas:** [Embodied World Models](#world-models-wm-embodied) (12) · [Policy Evaluation with World Models & WAM Benchmarks](#world-models-wm-policy-eval) (7) · [Physical Plausibility of Generated Video](#world-models-wm-physics) (7)

### <a id="world-models-wm-embodied"></a>Embodied World Models

- <a id="1x-world-model-challenge"></a>**1X World Model Challenge** (2024) `Real`: Challenge by 1X on predicting future first-person observations of its EVE humanoid from about 100 hours of real robot video and states. Sampling (future frames) and compression (future tokens) tracks ran in the Autonomous Grand Challenge 2025; a policy-evaluation track is planned.<br>
  *Resources*: [Website](https://huggingface.co/spaces/1x-technologies/1X_World_Model_Challenge_Home) | [Code](https://github.com/1x-technologies/1xgpt) ★568 | [Data](https://huggingface.co/datasets/1x-technologies/worldmodel) | [Leaderboard](https://huggingface.co/spaces/1x-technologies/1X_World_Model_Challenge_Compression)

- <a id="worldsimbench"></a>**WorldSimBench** (2024) `Sim + Real`: Evaluates video generation models as world simulators in two ways: a human-preference evaluator trained on 35,701 annotated videos scores visual and embodied quality, and closed-loop tests convert generated video into actions in Minecraft, driving (CARLA) and robot manipulation (CALVIN).<br>
  *Resources*: [Paper](https://arxiv.org/abs/2410.18072) (ICML 2025) | [Website](https://iranqin.github.io/WorldSimBench.github.io)

- <a id="ewmbench"></a>**EWMBench** (2025) `Real`: Scores embodied world models on robot manipulation video generated from AgiBot World scenes along three axes: scene consistency, end-effector motion against ground-truth trajectories, and semantic alignment. Its toolkit supplies the metrics of the AgiBot World Challenge world-model track.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2505.09694) | [Code](https://github.com/AgibotTech/EWMBench) ★132 | [Data](https://huggingface.co/datasets/agibot-world/EWMBench)

- <a id="dreamgen-bench"></a>**DreamGen Bench** (2025) `Sim + Real`: Video-generation benchmark from NVIDIA's DreamGen (GR00T-Dreams) work: video models adapted to a robot must generate unseen objects, behaviours and environments, and VLM judges score instruction following and physics alignment. Scores correlate with downstream policy success on RoboCasa.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2505.12705) | [Website](https://research.nvidia.com/labs/gear/dreamgen/) | [Code](https://github.com/NVIDIA/GR00T-Dreams) ★633

- <a id="agibot-world-challenge-world-model-track"></a>**AgiBot World Challenge (World Model track)** (2025) `Real`: Competition track in which models generate robot video from a first frame and an action sequence on AgiBot World scenes such as kitchens, workbenches and dining tables. Submissions are ranked on a Hugging Face server by PSNR, scene consistency and nDTW using EWMBench.<br>
  *Resources*: [Website](https://agibot-world.com/challenge2026) | [Code](https://github.com/AgibotTech/AgiBotWorldChallengeICRA2026-WorldModelBaseline) ★51 | [Data](https://huggingface.co/datasets/agibot-world/AgiBotWorldChallenge-2026) | [Leaderboard](https://huggingface.co/spaces/agibot-world/ICRA26WM)

- <a id="world-in-world"></a>**World-in-World** (2025) `Sim`: Closed-loop platform that plugs video world models into an online planner through a unified action API and ranks them by task success instead of visual quality, across active recognition, image-goal navigation, embodied question answering and RLBench manipulation.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2510.18135) (ICLR 2026 (Oral)) | [Website](https://world-in-world.github.io/) | [Code](https://github.com/World-In-World/world-in-world) ★215 | [Data](https://huggingface.co/datasets/zonszer/WIW_datasets) | [Leaderboard](https://world-in-world.github.io/subpages/leaderboard.html)

- <a id="wow-world-eval"></a>**WoW-World-Eval** (2026) `Real` `new`: Embodied Turing test for video world models: 609 robot manipulation samples scored with 22 metrics on perception, planning, prediction, generalisation and execution, plus an inverse-dynamics test that executes generated videos on a real robot. Builds on WoWBench from the WoW world model.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2601.04137) | [Data](https://huggingface.co/datasets/WoW-world-model/WoW-1-Benchmark-Samples)

- <a id="rbench"></a>**RBench** (2026) `Real` `new`: Benchmark for robot video generation from the paper 'Rethinking Video Generation Model for the Embodied World': 650 image-text pairs over five task types and four embodiment types, scored automatically for task completion and visual quality. Released with the 4M-clip RoVid-X dataset.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2601.15282) (ICML 2026) | [Website](https://dagroup-pku.github.io/ReVidgen.github.io/) | [Code](https://github.com/DAGroup-PKU/ReVidgen) ★103 | [Data](https://huggingface.co/datasets/DAGroup-PKU/RBench) | [Leaderboard](https://huggingface.co/spaces/DAGroup-PKU/RBench-Leaderboard)

- <a id="worldarena"></a>**WorldArena** (2026) `Sim + Real` `new`: Benchmark and leaderboard for embodied world models: 16 video-quality metrics plus functional tests of the model as data engine, policy evaluator and action planner on RoboTwin 2.0. Version 2.0 adds visuotactile prediction, RL-environment use, LIBERO and a real ALOHA robot.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2602.08971) | [Website](https://world-arena.ai) | [Code](https://github.com/tsinghua-fib-lab/WorldArena) ★274 | [Data](https://huggingface.co/datasets/WorldArena/WorldArena_Robotwin2.0) | [Leaderboard](https://huggingface.co/spaces/WorldArena/WorldArena)

- <a id="wr-arena"></a>**WR-Arena** (2026) `Real` `new`: World Reasoning Arena from the PAN team (MBZUAI): tests general world models such as PAN, Cosmos and V-JEPA 2 on following multi-step instructions with counterfactual rollouts, staying coherent over long horizons, and supporting a VLM planner that simulates candidate actions on household and tabletop robot tasks.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2603.25887) | [Code](https://github.com/MBZUAI-IFM/WR-Arena) ★26

- <a id="robowm-bench"></a>**RoboWM-Bench** (2026) `Sim` `new`: Tests whether manipulation videos generated by world models are physically executable: human-hand videos are retargeted and robot videos passed through an inverse dynamics model, then replayed in simulation scenes reconstructed from real setups and scored by task and step success.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2604.19092) (CVPR 2026 Workshop (WMAS)) | [Website](https://robowm-bench.github.io/RoboWM-Bench/) | [Code](https://github.com/fffstrong/RoboWM-Bench) ★42

- <a id="worldoracle"></a>**WorldOracle** (2026) `Real` `new`: Compares rollouts of action-conditioned world models with paired real executions given the same first frame and low-level actions. Episodes are long and multi-segment, include failed attempts and policy rollouts, and span AgiBot G2, YAM arms and human hands; a public leaderboard is maintained.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2610.18826) | [Website](https://worldoracle-benchmark.github.io/) | [Code](https://github.com/WorldOracle-benchmark/WorldOracle) ★29 | [Data](https://huggingface.co/datasets/WorldOracle/worldoracle-validation) | [Leaderboard](https://worldoracle-benchmark.github.io/leaderboard.html)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| [1X World Model Challenge](#1x-world-model-challenge) | humanoid, future-frame prediction | 2 tracks (sampling, compression) | 2 | 1 (1X EVE humanoid) | video, RGB, proprioceptive | Real world | Not stated | about 100 hours of tokenised robot video with states; 450-sample test set |
| [WorldSimBench](#worldsimbench) | video generation as world simulator | 3 scenarios | 20 perceptual dimensions + closed-loop task metrics per scenario | 3 | video, RGB, language | MineRL, CARLA, CALVIN + real | Human labels | HF-Embodied dataset: 35,701 scored video-instruction tuples |
| [EWMBench](#ewmbench) | embodied video generation | 10 manipulation tasks | 3 groups | 1 (AgiBot G1) | video, RGB, language | Real world | Human demos | 10 tasks from AgiBot World, 10 diverse trajectories selected per task |
| [DreamGen Bench](#dreamgen-bench) | video world model as data generator | 4 evaluation sets | 2 | 2 | video, RGB, language | RoboCasa + real | Human labels | about 50 start frames per set (48 RoboCasa; 50 / 47 / 30 GR1) |
| [AgiBot World Challenge (World Model track)](#agibot-world-challenge-world-model-track) | action-conditioned video prediction | 10 real-world task scenarios | 3 | 1 (AgiBot World robot) | video, RGB, proprioceptive | Real world | Human demos | 30,000+ training trajectories over 10 tasks; 30 validation + 30 hidden test samples (2025) |
| [World-in-World](#world-in-world) | closed-loop, world model for planning | 4 | task success as primary | 2 | RGB, video, language | Habitat-Sim, CoppeliaSim (RLBench) | Mixed | 551 AR + 144 ImageNav episodes, 184 A-EQA questions, 4 RLBench tasks x 50 episodes |
| [WoW-World-Eval](#wow-world-eval) | embodied Turing test, video generation | 5 abilities | 22 metrics in 5 groups + human and inverse-dynamics Turing tests | 4 (Franka, UR5e, AgileX, humanoid) | video, RGB, language | Real world | Mixed | 609 samples (instruction, first frame, ground-truth video) |
| [RBench](#rbench) | robot video generation, task completion | 5 task categories + 4 embodiment categories | 5 | 4 types | video, RGB, language | Real world | Human labels | 650 image-text pairs (250 task-oriented, 400 embodiment-specific) |
| [WorldArena](#worldarena) | perception + functional utility | video quality + 3 functional roles, on 50 RoboTwin 2.0 tasks | 16 video metrics in 6 sub-dimensions + task success, correlation | 3 | video, RGB, language, proprioceptive, tactile | RoboTwin 2.0; LIBERO and UniVTAC in 2.0 + real | Planner | RoboTwin 2.0 Clean-50: 2,500 videos (2,000 train / 500 test) |
| [WR-Arena](#wr-arena) | general world models, action simulation | 3 dimensions | VLM-judged action fidelity, smoothness and consistency, planning success | 2 | video, RGB, language | Real world | Mixed | 100 scenes x 10-round prompts (forecast); 15 AgiBot + 47 Language Table planning cases |
| [RoboWM-Bench](#robowm-bench) | executability of generated video | 24 | 2 | 2 | video, RGB, language | Isaac Lab (LeHome) | - | 10 initial object configurations per task |
| [WorldOracle](#worldoracle) | action-conditioned world models | 4 | 4 | 3 | video, RGB, proprioceptive | Real world | Mixed | 335 evaluation episodes (275 human-operated, 60 policy rollouts); 1,779 G2 training episodes |

### <a id="world-models-wm-policy-eval"></a>Policy Evaluation with World Models & WAM Benchmarks

- <a id="worldeval"></a>**WorldEval** (2025) `Real`: Pipeline that evaluates real-world manipulation policies inside a video world model driven by the policy's own latent actions (Policy2Vec). Validated on a bimanual AgileX robot against 1,000+ real trials of Diffusion Policy, OpenVLA, DexVLA and pi0; dWorldEval is its 2026 follow-up.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2505.19017) | [Website](https://worldeval.github.io) | [Code](https://github.com/liyaxuanliyaxuan/Worldeval) ★31

- <a id="worldgym"></a>**WorldGym** (2025) `Real`: Policy evaluation environment built on an autoregressive action-conditioned video model: policies are rolled out from real first frames and a VLM judges success. Success rates of RT-1-X, Octo and OpenVLA inside the model track real-robot results on the OpenVLA Bridge tasks (r = 0.78).<br>
  *Resources*: [Paper](https://arxiv.org/abs/2506.00613) | [Website](https://world-model-eval.github.io/abstract.html) | [Code](https://github.com/world-model-eval/world-model-eval) ★117

- <a id="ctrl-world"></a>**Ctrl-World** (2025) `Real`: Open multi-view world model trained on DROID and built for policy-in-the-loop rollouts with generalist policies. Its imagined rollouts reproduce the real-world ranking of pi0, pi0-FAST and pi0.5, and later benchmarks such as WorldArena and WorldFailBench use it as a learned evaluator baseline.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2510.10125) (ICLR 2026) | [Website](https://ctrl-world.github.io) | [Code](https://github.com/Robert-gyj/Ctrl-World) ★586

- <a id="robotwin-2-0-plus"></a>**RoboTwin 2.0-Plus** (2026) `Sim` `new`: Perturbation suite on RoboTwin 2.0 from the study 'Do World Action Models Generalize Better than VLAs?'. It measures how the success of world action models and VLAs degrades under seven kinds of perturbation (noise, lighting, camera, robot state, background, layout, language), alongside LIBERO-Plus.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2603.22078) | [Website](https://robot-robustness.github.io/RoboTwin2.0-Plus/) | [Code](https://github.com/Robot-Robustness/RoboTwin2.0-Plus) ★18

- <a id="wmbench"></a>**WMBench** (2026) `Real` `new`: Benchmark from the GigaWorld-1 paper for world models as policy evaluators: a model rolls out a policy closed-loop from held-out real episodes and is scored on whether it reproduces the real outcome. Official benchmark of the CVPR 2026 GigaBrain Challenge world-model track.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2607.02642) | [Website](https://open-gigaai.github.io/giga-world-1/) | [Code](https://github.com/open-gigaai/giga-world-1) ★1.1k | [Data](https://huggingface.co/datasets/open-gigaai/CVPR-2026-WorldModel-Track-Dataset) | [Leaderboard](https://huggingface.co/spaces/open-gigaai/CVPR-2026-WorldModel-Track-LeaderBoard)

- <a id="robotwin-phys"></a>**RoboTwin-Phys** (2026) `Sim` `new`: Extends the 50 RoboTwin 2.0 tasks with per-episode sampling of 13 physical attributes such as mass, friction, restitution, joint damping and table tilt, to test whether world action models and VLAs stay robust when physics changes. All five models evaluated drop to 32-44% success.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2609.26292) | [Website](https://yefeng00.github.io/RoboTwinPhysTest/) | [Code](https://github.com/yefeng00/RoboTwin-Phys) ★6 | [Leaderboard](https://yefeng00.github.io/RoboTwinPhysTest/#leaderboard)

- <a id="worldfailbench"></a>**WorldFailBench** (2026) `Sim + Real` `new`: Tests whether world models used as policy evaluators reproduce how policies fail: the error type, the stage where it occurs, and the scene change at which success turns into failure. Reference rollouts come from LIBERO, RoboTwin and a real G1 humanoid.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2610.33565) | [Code](https://github.com/DAXIAORobotics/WorldFailBench) ★3 | [Data](https://huggingface.co/datasets/ACERobotics/WorldFailBench)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| [WorldEval](#worldeval) | world model as real-robot policy evaluator | 5 | 2 | 1 (bimanual AgileX, ALOHA-style) | RGB, video, language | Real world | Human demos | 1,400 real trajectories to train the world model; 1,000+ real evaluation trials |
| [WorldGym](#worldgym) | world model as policy evaluation environment | 17 Bridge tasks from the OpenVLA evaluation, plus Google Robot and OOD tasks | 2 | 2 evaluated (Bridge robot, Google Robot) | RGB, video, language | Real world | - | real first frames of the evaluated tasks; no new dataset |
| [Ctrl-World](#ctrl-world) | controllable multi-view world model | 7 task types | correlation of imagined and real instruction-following and success rates | 1 | RGB, video, language, proprioceptive | Real world | Human demos | trained on DROID (95,599 trajectories, 564 scenes); no separate evaluation set |
| [RoboTwin 2.0-Plus](#robotwin-2-0-plus) | WAM vs VLA robustness | 50 bimanual tasks x 8 configs | 1 | 1 (Aloha-AgileX dual-arm) | RGB, language, proprioceptive | RoboTwin 2.0 | - | 50 episodes per config per task; 21 perturbation sub-dimensions |
| [WMBench](#wmbench) | world models as policy evaluators | 8 manipulation task families | WMES + automatic video diagnostics | N/A (platform not named) | video, RGB, language, proprioceptive | Real world | Mixed | 2,989 paired trajectories (teleoperation and policy rollouts, about 1:1); 7,200 s test split |
| [RoboTwin-Phys](#robotwin-phys) | WAM and VLA robustness | 50 bimanual tasks, 13 varied physical attributes | 1 | 1 (RoboTwin 2.0 dual-arm) | RGB, language, proprioceptive | RoboTwin 2.0 | Planner | 5,000 expert demonstrations (50 tasks x 100) with ground-truth physical parameters |
| [WorldFailBench](#worldfailbench) | world models as policy evaluators | 3 over 32 manipulation tasks | failure-frequency error, cross-policy correlation, boundary agreement | 3 | video, RGB, language, proprioceptive | LIBERO, RoboTwin + real | Human labels | 6,900 reference rollouts (1,500 LIBERO, 5,000 RoboTwin, 400 real G1); 120 boundary pairs |

### <a id="world-models-wm-physics"></a>Physical Plausibility of Generated Video

- <a id="phygenbench"></a>**PhyGenBench** (2024) `Real` `widely used`: 160 hand-written text-to-video prompts covering 27 physical laws in mechanics, optics, thermal phenomena and material properties. The PhyGenEval pipeline scores generated videos with VLMs and an LLM in a three-tier hierarchy designed to agree with human judgement.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2410.05363) (ICML 2025) | [Website](https://phygenbench123.github.io/) | [Code](https://github.com/OpenGVLab/PhyGenBench) ★170

- <a id="physics-iq"></a>**Physics-IQ** (2025) `Real` `widely used`: Real-video benchmark from Google DeepMind: a model sees the start of a filmed physical event and must continue it; the output is compared with the true footage. 396 clips cover 66 scenarios in mechanics, fluids, optics, thermodynamics and magnetism. A Verified variant keeps a public leaderboard.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2501.09038) | [Website](https://physics-iq.github.io) | [Code](https://github.com/google-deepmind/physics-IQ-benchmark) ★394 | [Leaderboard](https://physics-iq-verified.anates.ai)

- <a id="worldmodelbench"></a>**WorldModelBench** (2025) `Real`: Judges video generators as world models in seven application domains including robotics and driving. 350 text or image-plus-text conditions are scored for instruction following, physics adherence (five violation types) and commonsense by a judge model fine-tuned on 67K human labels.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2502.20694) (CVPR 2025 Workshop) | [Website](https://worldmodelbench-team.github.io) | [Code](https://github.com/WorldModelBench-Team/WorldModelBench) ★53 | [Data](https://huggingface.co/datasets/Efficient-Large-Model/worldmodelbench) | [Leaderboard](https://worldmodelbench-team.github.io/#leaderboard)

- <a id="videophy-2"></a>**VideoPhy-2** (2025) `Real` `widely used`: Action-centric physical-commonsense benchmark for video generation and successor to VideoPhy (ICLR 2025): prompts built from about 200 real-world actions with a hard subset. Humans rate semantic adherence, physical commonsense and violated physical rules; VideoPhy-2-AutoEval gives automatic scores.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2503.06800) (ICLR 2026) | [Website](https://videophy2.github.io/) | [Code](https://github.com/Hritikbansal/videophy) ★216 | [Data](https://huggingface.co/datasets/videophysics/videophy2_test) | [Leaderboard](https://videophy2.github.io/)

- <a id="intphys-2"></a>**IntPhys 2** (2025) `Sim`: Meta's intuitive-physics video benchmark: a model must tell possible from impossible events in matched synthetic videos testing object permanence, immutability, spatio-temporal continuity and solidity. Used to probe predictive world models such as V-JEPA 2 and multimodal LLMs, which mostly score near chance.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2506.09849) | [Code](https://github.com/facebookresearch/IntPhys2) ★117 | [Data](https://huggingface.co/datasets/facebook/IntPhys2) | [Leaderboard](https://huggingface.co/spaces/facebook/physical_reasoning_leaderboard)

- <a id="phyworldbench"></a>**PhyWorldBench** (2025) `Real`: 1,050 text-to-video prompts organised as 10 physics categories, 5 subcategories each, 7 scenarios and 3 prompt styles, from basic motion to rigid-body and human or animal motion, plus an anti-physics set that asks models to break physical laws. Judged by humans and a zero-shot MLLM protocol.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2507.13428) (ICLR 2026) | [Website](https://research.nvidia.com/labs/cosmos-lab/phyworldbench/) | [Code](https://github.com/ashwin-333/phy-world-bench) ★8

- <a id="pai-bench"></a>**PAI-Bench** (2025) `Real` `new`: Physical AI Bench: three tracks on real-world video from physical-AI domains such as driving, robotics, industry and egocentric scenes. It scores video generation for quality and physical plausibility, control-conditioned generation, and video understanding by multimodal LLMs, with a public leaderboard.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2512.01989) (CVPR 2026 (Oral)) | [Code](https://github.com/SHI-Labs/physical-ai-bench) ★108 | [Data](https://huggingface.co/datasets/shi-labs/physical-ai-bench-generation) | [Leaderboard](https://huggingface.co/spaces/shi-labs/physical-ai-bench-leaderboard)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| **[PhyGenBench](#phygenbench)** | physical commonsense, text-to-video | 27 physical laws in 4 domains | 1 | N/A | video, language | Real world | Human labels | 160 prompts |
| **[Physics-IQ](#physics-iq)** | physical understanding | 66 scenarios in 5 physics categories | 4 -> Physics-IQ score | N/A | video, RGB, language | Real world | Human labels | 396 videos of 8 s (66 scenarios x 3 camera views x 2 takes) |
| [WorldModelBench](#worldmodelbench) | physics adherence, instruction following | 7 domains, 56 subdomains | 3 | N/A | video, RGB, language | Real world | Human labels | 350 image and text conditions; 67K human labels on videos from 14 models |
| **[VideoPhy-2](#videophy-2)** | physical commonsense, action-centric | 197 actions + hard subset | 3 | N/A | video, language | Real world | Human labels | 20 LLM-written prompts per action; human-rated test set on Hugging Face |
| [IntPhys 2](#intphys-2) | intuitive physics | 4 physical principles | 1 | N/A | video | Unreal Engine 5.4 | Synthetic | 1,416 videos in 3 splits (main 1,012; held-out 344; rest debug) |
| [PhyWorldBench](#phyworldbench) | physical realism, text-to-video | 10 physics categories, 50 subcategories | 1 | N/A | video, language | Real world | Human labels | 1,050 prompts |
| [PAI-Bench](#pai-bench) | physical AI | 3 tracks | per track | N/A | video, RGB, language, depth | Real world | Human labels | 2,808 real-world cases (1,044 in the generation track) |

<p align="right"><a href="#contents">Back to contents ↑</a></p>

---

## <a id="embodied-reasoning"></a>Embodied Reasoning

Benchmarks that test vision-language models and LLMs as the reasoning and planning layer of a robot. **24 entries.**

**Sub-areas:** [Spatial & Physical Reasoning](#embodied-reasoning-spatial) (11) · [Task Planning & Agents](#embodied-reasoning-planning) (9) · [Embodied Question Answering](#embodied-reasoning-eqa) (4)

### <a id="embodied-reasoning-spatial"></a>Spatial & Physical Reasoning

- <a id="where2place-robopoint"></a>**Where2Place (RoboPoint)** (2024) `Real`: Free-space pointing benchmark introduced with RoboPoint: 100 real photos of cluttered homes and offices, each with an instruction describing a vacant region relative to other objects. A model succeeds when its predicted points fall inside the human-annotated mask.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2406.10721) (CoRL 2024) | [Website](https://robo-point.github.io) | [Code](https://github.com/wentaoyuan/RoboPoint) ★233 | [Data](https://huggingface.co/datasets/wentao-yuan/where2place)

- <a id="robospatial"></a>**RoboSpatial** (2024) `Real`: Spatial-understanding dataset for robotics built from 3D scans and egocentric images of indoor and tabletop scenes, with ego-, object- and world-centric reference frames. Its human-annotated test set RoboSpatial-Home (350 questions) was the basis of a CVPR 2026 challenge.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2411.16537) (CVPR 2025) | [Website](https://chanh.ee/RoboSpatial/) | [Code](https://github.com/NVlabs/RoboSpatial) ★156 | [Data](https://huggingface.co/datasets/chanhee-luke/RoboSpatial-Home)

- <a id="vsi-bench"></a>**VSI-Bench** (2024) `Real` `widely used`: Video QA benchmark for visual-spatial intelligence: after watching an egocentric walkthrough of a real indoor scene (ScanNet, ScanNet++, ARKitScenes), a model answers questions on configuration, measurement and spatiotemporal order. Widely reported by spatial VLMs and embodied-reasoning models.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2412.14171) (CVPR 2025) | [Website](https://vision-x-nyu.github.io/thinking-in-space.github.io/) | [Code](https://github.com/vision-x-nyu/thinking-in-space) ★753 | [Data](https://huggingface.co/datasets/nyu-visionx/VSI-Bench)

- <a id="cosmos-reason1-benchmark"></a>**Cosmos-Reason1 Benchmark** (2025) `Real`: Video QA benchmark released with NVIDIA's Cosmos-Reason1. A physical common sense part covers space, time and fundamental physics; an embodied reasoning part asks about task completion, action affordance and the next action in robot, human and driving videos. Later became the understanding track of PAI-Bench.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2503.15558) | [Code](https://github.com/nvidia-cosmos/cosmos-reason1) ★965 | [Data](https://huggingface.co/datasets/nvidia/Cosmos-Reason1-Benchmark) | [Leaderboard](https://huggingface.co/spaces/shi-labs/physical-ai-bench-leaderboard)

- <a id="erqa-gemini-robotics"></a>**ERQA (Gemini Robotics)** (2025) `Real` `widely used`: Embodied Reasoning Question Answering benchmark released with Gemini Robotics: 400 multiple-choice visual questions on spatial, trajectory, action, state, pointing, multi-view and task reasoning, 28% of them over several images. Now a standard yardstick in embodied-reasoning model reports.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2503.20020) | [Code](https://github.com/embodiedreasoning/ERQA) ★341

- <a id="pointarena"></a>**PointArena** (2025) `Real`: Evaluation platform for language-guided pointing in three stages: Point-Bench (982 image-question pairs with masks), Point-Battle (a blind pairwise arena with human votes) and Point-Act (pointing used to command a real robot arm).<br>
  *Resources*: [Paper](https://arxiv.org/abs/2505.09990) | [Website](https://pointarena.github.io/) | [Code](https://github.com/pointarena/pointarena) ★41 | [Data](https://huggingface.co/datasets/PointArena/pointarena-data)

- <a id="refspatial-bench"></a>**RefSpatial-Bench** (2025) `Real`: Spatial-referring benchmark from RoboRefer. In real cluttered scenes the model must point to the object (Location) or the free space (Placement) picked out by an expression that can need up to five reasoning steps; 77 samples use relation combinations unseen in training.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2506.04308) (NeurIPS 2025) | [Website](https://zhoues.github.io/RoboRefer/) | [Code](https://github.com/Zhoues/RoboRefer) ★270 | [Data](https://huggingface.co/datasets/BAAI/RefSpatial-Bench)

- <a id="bear"></a>**BEAR** (2025) `Sim + Real`: Skill-level benchmark that splits embodied tasks into 14 atomic skills in six categories (pointing, bounding box, trajectory reasoning, spatial reasoning, task planning, long-horizon), so failures of multimodal LLMs can be traced from planning back to perception.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2510.08759) (ICML 2026) | [Website](https://bear-official66.github.io/) | [Code](https://github.com/yqi19/BEAR-official) ★26 | [Data](https://huggingface.co/datasets/yqi19/BEAR-benchmark)

- <a id="robobench"></a>**RoboBench** (2025) `Real`: Evaluates multimodal LLMs as the 'embodied brain' of a manipulation robot along five dimensions: instruction comprehension, perception reasoning, generalized planning, affordance prediction and failure analysis. Long-horizon plans are judged by an MLLM acting as a world simulator instead of by text matching.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2510.17801) (ECCV 2026) | [Website](https://robo-bench.github.io/) | [Code](https://github.com/yulin-luo/RoboBench) ★28 | [Data](https://huggingface.co/datasets/LeoFan01/RoboBench)

- <a id="esi-bench"></a>**ESI-Bench** (2026) `Sim` `new`: Embodied spatial intelligence benchmark where the model acts instead of only watching: in OmniGibson scenes it chooses perception, locomotion and manipulation actions to reveal occlusion, containment or dynamics before answering. Compares passive single-view, passive multi-view and active exploration.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2605.18746) | [Website](https://esi-bench.github.io/) | [Code](https://github.com/ESI-Bench/ESI-Bench) ★144 | [Data](https://huggingface.co/datasets/esi-bench/ESI-Bench)

- <a id="behavior-spatial"></a>**BEHAVIOR-Spatial** (2026) `Sim` `new`: Spatial-understanding benchmark built on BEHAVIOR-1K that tests the same scenes and relations three ways: VLM spatial question answering, pointing to the instructed target, and VLA policies acting in OmniGibson. The baseline policy reaches 41.6% on held-out layouts but 16.1% when the instruction changes within a training layout.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2610.34051) | [Code](https://github.com/arielchen07/BEHAVIOR-Spatial-benchmark) ★2 | [Data](https://huggingface.co/datasets/behavior-spatial-benchmark/BEHAVIOR-Spatial)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| [Where2Place](#where2place-robopoint) | pointing, free-space reference | 100 image-instruction pairs | 1 | N/A | RGB, language | Real world | Human labels | 100 real-world images with instructions and masks |
| [RoboSpatial](#robospatial) | spatial relations, reference frames | 3 question types | 1 (success rate) | N/A | RGB, depth, language | Real world | Mixed | 1M images, 5k 3D scans, 3M spatial relations; RoboSpatial-Home: 350 questions |
| **[VSI-Bench](#vsi-bench)** | visual-spatial intelligence, video QA | 8 tasks | 2 | N/A | video, language | Real world | Mixed | 5,000+ QA pairs from 288 egocentric videos |
| [Cosmos-Reason1 Benchmark](#cosmos-reason1-benchmark) | physical common sense | 9 sub-benchmarks | 1 | 4 embodiment types | video, language | Real world | Human labels | 1,214 questions: 604 common sense (426 videos), 610 embodied reasoning |
| **[ERQA](#erqa-gemini-robotics)** | embodied reasoning VQA, multiple-choice | 400 multiple-choice questions | 1 | N/A | RGB, language | Real world | Human labels | 400 manually labeled questions over robot and egocentric images |
| [PointArena](#pointarena) | pointing, grounding | 982 Point-Bench tasks in 5 categories | 3 | 1 (robot arm, Point-Act stage only) | RGB, language | Real world | Human labels | 982 image-question pairs with masks; 4,500+ arena votes |
| [RefSpatial-Bench](#refspatial-bench) | spatial referring, pointing | 2 tasks, 100 samples each | 1 | N/A | RGB, language | Real world | Human labels | 200 annotated samples; companion RefSpatial training set has 20M QA pairs |
| [BEAR](#bear) | atomic embodied skills | 14 skills in 6 categories | 2 | N/A | RGB, video, language | AI2-THOR (35 long-horizon episodes) + real | Mixed | 4,469 image-video-text samples from 13 data sources |
| [RoboBench](#robobench) | embodied brain: perception, planning | 25 tasks in 5 dimensions | 5 evaluators | N/A | RGB, video, language | Real world | Mixed | 6,092 QA pairs from open-source and in-house robot data |
| [ESI-Bench](#esi-bench) | active spatial reasoning | 10 task categories | 1 (answer accuracy) | 1 | RGB, language | OmniGibson (BEHAVIOR) | Synthetic | 3,081 question instances, GPT-4o-proposed and human-verified |
| [BEHAVIOR-Spatial](#behavior-spatial) | spatial QA, pointing, VLA action | 3,256 QA + 1,240 pointing + 24 action tasks | 6 | 1 | RGB, language | OmniGibson (BEHAVIOR-1K) | Mixed | 3,256 questions over 49 activities; 1,240 pointing queries; 1,570 sim-eval episodes |

### <a id="embodied-reasoning-planning"></a>Task Planning & Agents

- <a id="alfworld"></a>**ALFWorld** (2020) `Sim` `widely used`: TextWorld games aligned with ALFRED household tasks in AI2-THOR, so an agent can learn or plan in text and then act in the embodied scene. Its text tasks became a standard testbed for LLM agents.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2010.03768) (ICLR 2021) | [Website](https://alfworld.github.io) | [Code](https://github.com/alfworld/alfworld) ★921

- <a id="egoplan-bench"></a>**EgoPlan-Bench** (2023) `Real`: Multiple-choice planning benchmark from the egocentric view: given a task goal, a video of progress so far and the current frame, pick the next action. Built from Epic-Kitchens and Ego4D; EgoPlan-Bench2 extends it to 24 everyday scenarios.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2312.06722) (IJCV) | [Website](https://chenyi99.github.io/ego_plan/) | [Code](https://github.com/ChenYi99/EgoPlan) ★89 | [Leaderboard](https://huggingface.co/spaces/ChenYi99/EgoPlan-Bench_Leaderboard)

- <a id="embodied-agent-interface"></a>**Embodied Agent Interface** (2024) `Sim`: Standard interface for testing LLMs on embodied decision making. Splits the problem into four modules (goal interpretation, subgoal decomposition, action sequencing, transition modeling) on BEHAVIOR and VirtualHome tasks and reports fine-grained error types such as hallucination, affordance and planning errors.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2410.07166) (NeurIPS 2024 D&B) | [Website](https://embodied-agent-interface.github.io/) | [Code](https://github.com/embodied-agent-interface/embodied-agent-interface) ★302 | [Data](https://huggingface.co/datasets/Inevitablevalor/EmbodiedAgentInterface) | [Leaderboard](https://eai-challenge-cvpr2026.github.io)

- <a id="partnr"></a>**PARTNR** (2024) `Sim`: Planning And Reasoning Tasks in humaN-Robot collaboration: 100,000 natural-language household tasks, generated with LLMs and grounded in simulation, in which an LLM-planned robot works with a human partner under spatial, temporal and agent-capability constraints.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2411.00081) (ICLR 2025) | [Website](https://aihabitat.org/partnr/) | [Code](https://github.com/facebookresearch/partnr-planner) ★409

- <a id="embodiedbench"></a>**EmbodiedBench** (2025) `Sim`: Benchmark for multimodal LLMs as vision-driven embodied agents in four simulated environments: EB-ALFRED and EB-Habitat (high-level household tasks), EB-Navigation and EB-Manipulation (low-level navigation and manipulation). Six capability subsets probe commonsense, complex instructions, spatial awareness, visual perception and long-horizon planning.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2502.09560) (ICML 2025) | [Website](https://embodiedbench.github.io) | [Code](https://github.com/EmbodiedBench/EmbodiedBench) ★361 | [Data](https://huggingface.co/EmbodiedBench) | [Leaderboard](https://embodiedbench.github.io/#leaderboard-findings)

- <a id="robofac"></a>**RoboFAC** (2025) `Sim + Real`: Video QA benchmark on manipulation failures. Given a failed attempt, models must describe the task, detect and locate the failure, explain it (task planning, motion planning or execution control) and propose a correction; covers ManiSkill simulation and a real SO-100 arm.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2505.12224) | [Website](https://mint-sjtu.github.io/RoboFAC.io/) | [Code](https://github.com/MINT-SJTU/RoboFAC) ★50 | [Data](https://huggingface.co/datasets/MINT-SJTU/RoboFAC-dataset)

- <a id="roboreward"></a>**RoboReward** (2026) `Real` `new`: Tests whether VLMs can serve as reward models for real robots: given a task and an episode video, predict a 1-5 progress score. RoboRewardBench holds about 2,800 human-verified episodes from Open X-Embodiment and RoboArena, including generated failures and near-misses.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2601.00675) | [Website](https://crfm.stanford.edu/helm/robo-reward-bench) | [Data](https://huggingface.co/datasets/teetone/RoboReward) | [Leaderboard](https://crfm.stanford.edu/helm/robo-reward-bench/latest/#/leaderboard)

- <a id="cap-x"></a>**CaP-X** (2026) `Sim + Real` `new`: Framework for testing LLMs and VLMs as code-writing robot controllers. In CaP-Gym the agent writes programs that call perception and control primitives; CaP-Bench varies abstraction level, feedback and visual grounding over eight tiers to show how much models depend on human-designed scaffolding.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2603.22435) (ICML 2026) | [Website](https://capgym.github.io) | [Code](https://github.com/capgym/cap-x) ★935

- <a id="embodied-first-exam"></a>**Embodied First Exam** (2026) `Sim` `new`: Agentic-robotics exam for coding agents: on each task the agent may command the robot directly, write control code or train a policy. Covers 1,156 simulated tasks in 35 suites on 47 robots, including nine new suites beyond pick-and-place.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2611.12177) | [Website](https://www.embodied-first-exam.ai) | [Code](https://github.com/mll-lab-nu/embodied-first-exam) ★307 | [Data](https://huggingface.co/datasets/MLL-Lab/embodied-exam-data) | [Leaderboard](https://www.embodied-first-exam.ai/leaderboard/)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| **[ALFWorld](#alfworld)** | text and embodied household tasks | 6 task types | 2 | 1 (AI2-THOR agent) | language, RGB | TextWorld + AI2-THOR | Synthetic | 3,553 training games generated from ALFRED tasks |
| [EgoPlan-Bench](#egoplan-bench) | egocentric video, next-action planning | 4,939 multiple-choice questions | 1 (accuracy) | N/A (human egocentric video) | video, language | Real world | Mixed | EgoPlan-Val 3,355 and EgoPlan-Test 1,584 questions; EgoPlan-Bench2 adds 1,321 |
| [Embodied Agent Interface](#embodied-agent-interface) | LLM decision making, household planning | 4 modules on 438 task instructions | 3 plus error-type rates | N/A (symbolic agent) | language, state | BEHAVIOR, VirtualHome | Human labels | 438 annotated task plans with goals, trajectories and transition models |
| [PARTNR](#partnr) | human-robot collaboration | 4 task types | 4 | 1 (Spot) with a simulated human partner | RGB, depth, language, state | Habitat 3.0 | Synthetic | 100,000 train, 1,000 validation and 1,000 test episodes in 60 HSSD houses |
| [EmbodiedBench](#embodiedbench) | MLLM agents, high- and low-level control | 1,128 test instances across 4 environments | 3 | 3 | RGB, language | AI2-THOR (EB-ALFRED, EB-Navigation), Habitat 2.0, CoppeliaSim (EB-Manipulation) | Mixed | 1,128 test instances (300 / 300 / 300 / 228 per environment) |
| [RoboFAC](#robofac) | failure analysis, failure correction | 8 question types | 2 | 2 (simulated arm in ManiSkill, SO-100) | video, language | ManiSkill (SAPIEN) + real | Mixed | 9,440 failure trajectories; 78,623 QA pairs (70K simulated, 8K real) |
| [RoboReward](#roboreward) | reward model, progress estimation | about 2,800 scored episodes | 1 | 14 embodiments | video, language | Real world | Mixed | 45,072 training and about 2,800 benchmark episode-reward pairs |
| [CaP-X](#cap-x) | coding agents, code-as-policy | 187 CaP-Gym tasks | 1 (task success rate) | sim: single-arm, bimanual, R1Pro | RGB, depth, state, language | Robosuite (MuJoCo), LIBERO-PRO, BEHAVIOR (OmniGibson / Isaac Sim) + real | - | N/A |
| [Embodied First Exam](#embodied-first-exam) | coding agents, agentic robot control | 1,156 tasks in 35 suites | 1 | 47 robots | RGB, state, language | MuJoCo, Isaac Sim, OmniGibson, SAPIEN, Genesis | - | N/A |

### <a id="embodied-reasoning-eqa"></a>Embodied Question Answering

- <a id="sqa3d"></a>**SQA3D** (2022) `Real`: Situated question answering in 3D scenes: the agent is told its position and orientation in a ScanNet scan and must answer questions that depend on that viewpoint. A standard evaluation for 3D vision-language models.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2210.07474) (ICLR 2023) | [Website](https://sqa3d.github.io/) | [Code](https://github.com/SilongYong/SQA3D) ★173 | [Data](https://zenodo.org/record/7792397)

- <a id="robovqa"></a>**RoboVQA** (2023) `Real`: Video question answering for long-horizon robot reasoning, recorded in three office buildings with a robot, a human arm and a human using a grasping tool. Questions are generated from crowd-sourced hindsight labels and cover planning, success detection, affordances, and past and future steps.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2311.00899) (ICRA 2024) | [Website](https://robovqa.github.io) | [Code](https://github.com/google-deepmind/robovqa) ★37 | [Data](https://huggingface.co/datasets/Tianli/robovqa)

- <a id="hm-eqa"></a>**HM-EQA** (2024) `Sim`: Active embodied question answering: 500 multiple-choice questions about 267 Habitat-Matterport 3D homes, where a robot must explore until it is confident of the answer. Released with the 'Explore until Confident' method.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2403.15941) (RSS 2024) | [Website](https://explore-eqa.github.io/) | [Code](https://github.com/Stanford-ILIAD/explore-eqa) ★89 | [Data](https://github.com/Stanford-ILIAD/explore-eqa/tree/master/data)

- <a id="openeqa"></a>**OpenEQA** (2024) `Sim + Real` `widely used`: Open-vocabulary embodied question answering on real environments: 1,636 human-written questions about ScanNet and HM3D scenes, answered from an episodic memory of a tour (EM-EQA) or by actively exploring (A-EQA), and scored by an LLM judge.<br>
  *Resources*: [Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Majumdar_OpenEQA_Embodied_Question_Answering_in_the_Era_of_Foundation_Models_CVPR_2024_paper.html) (CVPR 2024) | [Website](https://open-eqa.github.io) | [Code](https://github.com/facebookresearch/open-eqa) ★363 | [Data](https://github.com/facebookresearch/open-eqa/tree/main/data)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| [SQA3D](#sqa3d) | situated QA in 3D scenes | 33.4k questions over 6.8k situations in 650 ScanNet scenes | 1 | N/A | pointcloud, RGB, video, language | Real world | Human labels | 26,623 / 3,261 / 3,519 train / val / test questions; 20.4k descriptions |
| [RoboVQA](#robovqa) | robot video QA, long-horizon reasoning | 10 question-answer types | 2 | 3 embodiments | video, language | Real world | Mixed | 829,502 (video, text) pairs; 238 hours; 29,520 unique instructions |
| [HM-EQA](#hm-eqa) | active exploration EQA | 500 multiple-choice questions in 5 categories | 2 | 1 | RGB, depth, language | Habitat-Sim (HM3D) | Synthetic | 500 questions over 267 HM3D scenes, GPT4-V-generated and manually filtered |
| **[OpenEQA](#openeqa)** | open-vocabulary EQA, episodic memory | 1,636 questions in 7 categories | 1 | N/A | RGB, depth, video, language | Habitat (HM3D scenes) + real | Human labels | 1,636 question-answer pairs over 180+ environments |

<p align="right"><a href="#contents">Back to contents ↑</a></p>

---

## <a id="navigation"></a>Navigation

Goal-driven, language-guided, social and outdoor navigation. **35 entries.**

**Sub-areas:** [Point, Object & Image-Goal Navigation](#navigation-goal-nav) (7) · [Vision-Language Navigation (VLN)](#navigation-vln) (16) · [Interactive Instruction Following](#navigation-interactive) (2) · [Social Navigation](#navigation-social) (5) · [Outdoor, Urban & Aerial](#navigation-outdoor) (5)

### <a id="navigation-goal-nav"></a>Point, Object & Image-Goal Navigation

- <a id="ai2-thor"></a>**AI2-THOR** (2017) `Sim` `widely used`: Open-source Unity-based embodied AI platform with interactive indoor scenes: iTHOR rooms, RoboTHOR sim-to-real apartments, ManipulaTHOR arm manipulation and procedurally generated ProcTHOR houses. It underlies ObjectNav, rearrangement and instruction-following benchmarks such as ALFRED and TEACh.<br>
  *Resources*: [Paper](https://arxiv.org/abs/1712.05474) | [Website](https://ai2thor.allenai.org/) | [Code](https://github.com/allenai/ai2thor) ★1.8k

- <a id="habitat-navigation-challenge-pointnav-objectnav-imagenav"></a>**Habitat Navigation Challenge (PointNav / ObjectNav / ImageNav)** (2019) `Sim` `widely used`: Photorealistic embodied navigation benchmarks run in Habitat-Sim on real-building scans: PointNav, ObjectNav and instance ImageNav, scored by Success and SPL. The yearly challenge ran from 2019 to 2023; HM3D-Semantics ObjectNav remains the standard object-goal benchmark.<br>
  *Resources*: [Paper](https://arxiv.org/abs/1904.01201) (ICCV 2019) | [Website](https://aihabitat.org/challenge/2023/) | [Code](https://github.com/facebookresearch/habitat-lab) ★3.2k | [Data](https://github.com/facebookresearch/habitat-lab/blob/main/DATASETS.md) | [Leaderboard](https://eval.ai/web/challenges/challenge-page/1992/overview)

- <a id="procthor"></a>**ProcTHOR** (2022) `Sim`: Procedural generator of interactive AI2-THOR houses. The released ProcTHOR-10K set of 10,000 houses is a common training ground for object-goal navigation, with evaluation on the artist-designed ArchitecTHOR houses and on RoboTHOR, iTHOR and Habitat ObjectNav.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2206.06994) (NeurIPS 2022) | [Website](https://procthor.allenai.org/) | [Code](https://github.com/allenai/procthor) ★487 | [Data](https://github.com/allenai/procthor-10k)

- <a id="goat-bench"></a>**GOAT-Bench** (2024) `Sim`: Go-to-Anything benchmark: in one episode the agent visits 5 to 10 goals in an unseen HM3D-Semantics home, each given as a category name, a language description or an image, testing open-vocabulary goals and reuse of memory across subtasks.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2404.06609) (CVPR 2024) | [Website](https://mukulkhanna.github.io/goat-bench/) | [Code](https://github.com/Ram81/goat-bench) ★171

- <a id="hm3d-ovon"></a>**HM3D-OVON** (2024) `Sim`: Open-vocabulary object-goal navigation on HM3D-Semantics scans: goals are free-form category names drawn from 379 categories instead of a fixed set of 6 to 20, with validation splits for seen categories, their synonyms, and unseen categories.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2409.14296) (IROS 2024) | [Website](https://naoki.io/portfolio/ovon.html) | [Code](https://github.com/naokiyokoyama/ovon) ★152

- <a id="langmap"></a>**LangMap** (2026) `Sim` `new`: Benchmark for the HieraNav task: language goals at four levels (scene, room, region, instance) on HM3D scans, with region labels and discriminative descriptions written and cross-checked by people rather than generated by a VLM. Has single-goal and multi-goal episodes.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2602.02220) (NeurIPS 2026) | [Website](https://bo-miao.github.io/LangMap) | [Code](https://github.com/bo-miao/LangMap) ★62 | [Data](https://huggingface.co/datasets/bo-miao/LangMap)

- <a id="omninavbench"></a>**OmniNavBench** (2026) `Sim` `new`: Benchmark for general-purpose navigation: each composite instruction interleaves at least two of six skills (PointNav, VLN, ObjectNav, SocialNav, human following, EQA) and runs on humanoid, quadruped and wheeled robots in Isaac Sim. Reference trajectories are human-teleoperated; test scoring goes through a public leaderboard.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2605.09441) (RSS 2026) | [Website](https://omninavbench.cloud-ip.cc/) | [Code](https://github.com/AutoLab-SAI-SJTU/OmniNavBench) ★110 | [Data](https://huggingface.co/datasets/AutoLab-SJTU/OmniNavBench) | [Leaderboard](https://omninavbench.cloud-ip.cc/)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| **[AI2-THOR](#ai2-thor)** | interactive indoor platform | N/A (platform) | N/A | 3 | RGB, depth, segmentation | Unity 3D | - | iTHOR: 120 rooms, 2,000+ objects; RoboTHOR: 89 apartments, 600+ objects |
| **[Habitat Navigation Challenge](#habitat-navigation-challenge-pointnav-objectnav-imagenav)** | PointNav, ObjectNav | 3 | 2 (Success, SPL) | 1 | RGB, depth, GPS_IMU | Habitat-Sim | Synthetic | 2023 edition: HM3D-Semantics v0.2, 216 scenes (145/36/35), 6 goal categories |
| [ProcTHOR](#procthor) | procedurally generated houses, ObjectNav | ObjectNav | 2 for ObjectNav | 1 (AI2-THOR navigation agent) | RGB, depth, segmentation | AI2-THOR (Unity) | Synthetic | 10,000 generated houses; 1,633 interactive objects in 108 categories |
| [GOAT-Bench](#goat-bench) | lifelong multi-modal goal navigation | 1 | 2 (SR, SPL) | 1 (Stretch-like agent) | RGB, depth, language | Habitat-Sim | Synthetic | 181 HM3D-Sem scenes, 312 object categories, about 680k episodes |
| [HM3D-OVON](#hm3d-ovon) | open-vocabulary ObjectNav | 1 | 2 (SR, SPL) | 1 (Stretch-like agent) | RGB, depth, language | Habitat-Sim | Synthetic | 15k+ annotated object instances, 379 categories, 181 scenes (145 train / 36 val) |
| [LangMap](#langmap) | hierarchical open-vocabulary goal navigation | 18,479 tasks at 4 goal levels | 3 (SR, SPL, SeqSR@k) | 1 (simulated agent) | RGB, depth, language | Habitat-Sim | Human labels | 36 HM3D-Sem validation scenes, 414 object categories, 926 region descriptions |
| [OmniNavBench](#omninavbench) | unified multi-skill navigation | 6 skill families combined in 1,779 composite episodes | 9 | 3 | RGB, depth, lidar, language | Isaac Sim | Human demos | 1,779 teleoperated trajectories (1,187 train / 592 test) in 170 scenes |

### <a id="navigation-vln"></a>Vision-Language Navigation (VLN)

- <a id="r2r-room-to-room"></a>**R2R (Room-to-Room)** (2017) `Sim` `widely used`: The original vision-and-language navigation benchmark: an agent follows crowd-sourced English instructions through Matterport3D buildings by hopping between panoramic viewpoints on a navigation graph. Still reported by nearly every VLN paper, and the starting point for RxR, REVERIE and VLN-CE.<br>
  *Resources*: [Paper](https://arxiv.org/abs/1711.07280) (CVPR 2018) | [Website](https://bringmeaspoon.org/) | [Code](https://github.com/peteanderson80/Matterport3DSimulator) ★720 | [Leaderboard](https://eval.ai/web/challenges/challenge-page/97/overview)

- <a id="touchdown"></a>**Touchdown** (2018) `Sim`: Street-level language navigation in Google Street View panoramas of New York City: follow written directions through the street graph, then resolve a spatial description to locate a hidden target. The reference benchmark for outdoor ground-level VLN.<br>
  *Resources*: [Paper](https://arxiv.org/abs/1811.12354) (CVPR 2019) | [Code](https://github.com/lil-lab/touchdown) ★116

- <a id="reverie"></a>**REVERIE** (2019) `Sim`: Remote object grounding in Matterport3D buildings: from a short high-level instruction (for example a household request), the agent must navigate to the right place and identify the target object among distractors. The standard goal-oriented companion to R2R, with an active leaderboard.<br>
  *Resources*: [Paper](https://arxiv.org/abs/1904.10151) (CVPR 2020) | [Website](https://yuankaiqi.github.io/REVERIE_Challenge/index.html) | [Code](https://github.com/YuankaiQi/REVERIE) ★162 | [Data](https://github.com/YuankaiQi/REVERIE/tree/master/tasks/REVERIE/data_v2) | [Leaderboard](https://yuankaiqi.github.io/REVERIE_Challenge/leaderboard2026.html)

- <a id="vln-ce-vision-and-language-navigation-in-continuous-environments"></a>**VLN-CE (Vision-and-Language Navigation in Continuous Environments)** (2020) `Sim` `widely used`: R2R and RxR instructions transferred from the panorama graph to continuous Habitat scenes, where the agent takes low-level actions (0.25 m forward, 15 degree turns) with no nav-graph or oracle localisation. R2R-CE and RxR-CE are the standard testbeds for learned and VLM-based instruction followers.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2004.02857) (ECCV 2020) | [Website](https://jacobkrantz.github.io/vlnce/) | [Code](https://github.com/jacobkrantz/VLN-CE) ★905 | [Data](https://jacobkrantz.github.io/vlnce/data) | [Leaderboard](https://eval.ai/web/challenges/challenge-page/719)

- <a id="rxr-room-across-room"></a>**RxR (Room-Across-Room)** (2020) `Sim` `widely used`: Multilingual VLN dataset on Matterport3D: longer and more varied paths than R2R, with instructions in English, Hindi and Telugu whose words are time-aligned to the annotator's pose trace. Its continuous port RxR-CE is a standard test of long-instruction following.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2010.07954) (EMNLP 2020) | [Website](https://ai.google.com/research/rxr/) | [Code](https://github.com/google-research-datasets/RxR) ★188 | [Leaderboard](https://ai.google.com/research/rxr/competition?active_tab=leaderboard)

- <a id="aerialvln"></a>**AerialVLN** (2023) `Sim`: First large UAV vision-and-language navigation benchmark: a drone follows long natural-language flight instructions through 25 near-realistic city-level scenes with continuous 3D motion. Paths were flown by licensed human pilots and described by crowd workers.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2308.06735) (ICCV 2023) | [Code](https://github.com/AirVLN/AirVLN) ★404 | [Data](https://www.kaggle.com/datasets/shuboliu/aerialvln)

- <a id="citynav"></a>**CityNav** (2024) `Sim`: Language-goal aerial navigation over 3D scans of two real cities (Cambridge and Birmingham): a drone must reach an object described relative to real landmarks. Ships human-flown demonstration trajectories and a geographic landmark map as an extra input.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2406.14240) (ICCV 2025) | [Website](https://water-cookie.github.io/city-nav-proj/) | [Code](https://github.com/water-cookie/citynav) ★150

- <a id="ha-vln-2-0"></a>**HA-VLN 2.0** (2024) `Sim`: Human-aware VLN: Matterport3D scenes populated with moving, interacting people (HAPS 2.0 motions), in both discrete and continuous settings. Scores goal reaching together with human collisions, and offers a public leaderboard plus real-robot validation on a Unitree Go2.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2503.14229) (NeurIPS 2024 D&B; v2.0 at IROS 2026) | [Website](https://uwmilab.github.io/HA-VLN-webpage/) | [Code](https://github.com/UWMILab/HA-VLN) ★525 | [Data](https://huggingface.co/datasets/fly1113/HA-VLN) | [Leaderboard](https://www.codabench.org/competitions/18135/)

- <a id="openuav-traveluav-uav-need-help"></a>**OpenUAV (TravelUAV / UAV-Need-Help)** (2024) `Sim`: UAV navigation platform with realistic flight control rather than discrete steps, and the UAV-Need-Help benchmark: a drone searches for a described target object while an assistant gives guidance at different levels. Trajectories were flown by human experts.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2410.07087) | [Website](https://prince687028.github.io/OpenUAV/) | [Code](https://github.com/prince687028/TravelUAV) ★300 | [Data](https://huggingface.co/datasets/wangxiangyu0814/TravelUAV)

- <a id="vln-ce-isaac"></a>**VLN-CE-Isaac** (2024) `Sim`: Isaac Lab port of R2R-CE introduced with NaVILA: 1,077 val-unseen trajectories run with physically simulated Unitree Go2 and H1 robots, so a navigation model's commands must be executed by a learned locomotion policy over the real scene geometry.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2412.04453) (RSS 2025) | [Website](https://navila-bot.github.io/) | [Code](https://github.com/yang-zj1026/NaVILA-Bench) ★348 | [Data](https://huggingface.co/datasets/Zhaojing/VLN-CE-Isaac)

- <a id="lh-vln-lhpr-vln"></a>**LH-VLN (LHPR-VLN)** (2024) `Sim`: Long-horizon VLN: each task chains several navigation subtasks in one HM3D scene (about 150 steps on average), testing long-term planning and consistency across stages. Adds per-subtask metrics (ISR, CSR, CGT) and ships the NavGen task generator.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2412.09082) (CVPR 2025) | [Website](https://hcplab-sysu.github.io/LH-VLN/) | [Code](https://github.com/HCPLab-SYSU/LH-VLN) ★271 | [Data](https://huggingface.co/datasets/Starry123/LHPR-VLN)

- <a id="openfly"></a>**OpenFly** (2025) `Sim`: Aerial VLN platform that renders 18 outdoor scenes through four engines (Unreal Engine, GTA V, Google Earth, 3D Gaussian Splatting) and generates trajectories and instructions automatically, yielding a 100k-trajectory dataset with seen and unseen test splits.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2502.18041) (ICLR 2026) | [Website](https://shailab-ipec.github.io/openfly/) | [Code](https://github.com/SHAILAB-IPEC/OpenFly-Platform) ★386 | [Data](https://huggingface.co/datasets/IPEC-COMMUNITY/OpenFly)

- <a id="octonav-bench"></a>**OctoNav-Bench** (2025) `Sim`: Benchmark for generalist navigation agents: each free-form instruction combines several capabilities (ObjNav, PointNav, ImgNav, Ins-ImgNav, VLN) and modalities (text, image, coordinates) in continuous Habitat scenes. Includes the TBA-CoT dataset of think-before-action reasoning traces.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2506.09839) (CVPR 2026) | [Website](https://buaa-colalab.github.io/OctoNav/) | [Code](https://github.com/buaa-colalab/OctoNav-R1) ★78

- <a id="vln-pe"></a>**VLN-PE** (2025) `Sim`: Physically realistic VLN on GRUtopia / Isaac Sim: instruction following is re-run with humanoid, quadruped and wheeled robots under real locomotion controllers, exposing failures from falls, collisions, low viewpoints and lighting that idealised VLN-CE agents never encounter.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2507.13019) (ICCV 2025) | [Website](https://crystalsixone.github.io/vln_pe.github.io/) | [Code](https://github.com/InternRobotics/InternNav) ★1.2k

- <a id="navitrace"></a>**NaviTrace** (2025) `Real`: VQA-style probe of navigation ability in vision-language models: given a real-world image, an instruction and an embodiment (human, legged robot, wheeled robot, bicycle), the model draws a 2D path in image space, scored against expert traces.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2510.26909) (ICRA 2026) | [Website](https://leggedrobotics.github.io/navitrace_webpage/) | [Code](https://github.com/leggedrobotics/navitrace_evaluation) ★36 | [Data](https://huggingface.co/datasets/leggedrobotics/navitrace) | [Leaderboard](https://huggingface.co/spaces/leggedrobotics/navitrace_leaderboard)

- <a id="vlnverse"></a>**VLNVerse** (2025) `Sim` `new`: Large VLN benchmark on Isaac Sim with 263 hand-built interactive USD scenes and physically simulated agents instead of teleporting cameras. One framework covers fine-grained, coarse-grained, visual-reference, long-horizon and dialogue navigation; used for the ECCV 2026 EMR workshop challenge.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2512.19021) | [Website](https://sihaoevery.github.io/vlnverse/) | [Code](https://github.com/sihaoevery/vlnverse_emr) ★25 | [Data](https://huggingface.co/datasets/Eyz/VLNVerse_scene) | [Leaderboard](https://www.codabench.org/competitions/17009/)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| **[R2R](#r2r-room-to-room)** | discrete VLN, indoor, panorama graph | 1 | 5 (TL, NE, OSR, SR, SPL) | 1 | RGB, language | Matterport3D Simulator | Human labels | about 22k instructions (3 per path, 29 words on average) in 90 buildings |
| [Touchdown](#touchdown) | outdoor street-level VLN | 2 | 6 | 1 (panoramic agent on a street graph) | RGB, language | StreetLearn (Google Street View panoramas) | Human labels | 9,326 instruction examples over 29,641 panoramas of New York City |
| [REVERIE](#reverie) | discrete VLN, remote object grounding | 1 | 5 | 1 | RGB, language | Matterport3D Simulator | Human labels | 21,702 instructions, 4,140 target objects, 10,567 panoramas in 90 buildings |
| **[VLN-CE](#vln-ce-vision-and-language-navigation-in-continuous-environments)** | continuous VLN, low-level actions | 2 (R2R-CE, RxR-CE) | 5 (TL, NE, OS, SR, SPL) | 1 | RGB, depth, language | Habitat-Sim | Human labels | R2R-CE: 10,819 train / 778 val-seen / 1,839 val-unseen / 3,408 test episodes |
| **[RxR](#rxr-room-across-room)** | discrete VLN, multilingual | 1 | 6 | 1 | RGB, language | Matterport3D Simulator | Human labels | 126k instructions over 16.5k paths, 3 languages, 90 buildings |
| [AerialVLN](#aerialvln) | aerial VLN, city-scale | 1 | 4 (NE, SR, OSR, SDTW) | 1 (simulated multirotor UAV) | RGB, depth, language | AirSim (Unreal Engine 4) | Human demos | 8,446 flight paths, 25,338 instructions, 25 city scenes (plus AerialVLN-S) |
| [CityNav](#citynav) | aerial VLN, real-city scans | 1 | 4 (NE, SR, OSR, SPL) | 1 (simulated UAV) | RGB, depth, language | CityFlight (SensatUrban point clouds) | Human demos | 32,637 human trajectories with descriptions (22,002/2,498/2,826/5,311), 4.65 km2 |
| [HA-VLN 2.0](#ha-vln-2-0) | human-aware VLN, discrete and continuous | 2 | 4 (NE, SR, TCR, CR) | 1 simulated agent | RGB, depth, language | HA-VLN Simulator (HA-VLN-DE and HA-VLN-CE; the CE side runs on Habitat) | Mixed | 16,844 instructions; HAPS 2.0: 486 motion sequences, 172 activities, 90 scans |
| [OpenUAV](#openuav-traveluav-uav-need-help) | aerial VLN, realistic flight control | 1 | 4 (NE, SR, OSR, SPL) | 1 | RGB, depth, lidar, language | AirSim (Unreal Engine 4) | Human demos | 12,149 trajectories, 22 scenes, 89 object categories |
| [VLN-CE-Isaac](#vln-ce-isaac) | legged-robot VLN, low-level control | 1,077 episodes | 4 (NE, OS, SR, SPL) | 2 (Unitree Go2, Unitree H1) | RGB, lidar, proprioceptive, language | Isaac Lab (Isaac Sim) | Human labels | 1,077 trajectories selected from the 1,839 of R2R val-unseen |
| [LH-VLN](#lh-vln-lhpr-vln) | long-horizon multi-stage VLN | 3,260 multi-stage tasks in 216 scenes | 7 | 2 | RGB, depth, language | Habitat-Sim (HM3D scenes) | Mixed | 3,260 tasks, about 150 steps each |
| [OpenFly](#openfly) | aerial VLN, multi-engine | 1 (aerial instruction following) | 4 (NE, SR, OSR, SPL) | 1 (simulated UAV) | RGB, language | Unreal Engine / AirSim, GTA V, Google Earth, 3D Gaussian Splatting | Mixed | 100k trajectories in 18 scenes; test sets of 1,800 seen and 1,200 unseen |
| [OctoNav-Bench](#octonav-bench) | generalist navigation | 5 capabilities combined within single instructions | 3 (SR, OSR, SPL) | 1 | RGB, language | Habitat-Sim | Mixed | 45k+ instruction-trajectory pairs in 400+ scenes; 10k+ TBA-CoT reasoning pairs |
| [VLN-PE](#vln-pe) | physically realistic VLN | 3 datasets | 7 | 4 | RGB, depth, language | GRUtopia (Isaac Sim) | Human labels | R2R 8,679/658/1,347 episodes; GRU-VLN10 441/111/1,287; 3DGS-Lab-VLN 160/640 |
| [NaviTrace](#navitrace) | VLM navigation probe, real-world images | 1,000 scenarios | 1 | 4 embodiments | RGB, language | Real world | Human labels | 1,000 scenarios, 3,000+ expert traces; validation split and hidden test split |
| [VLNVerse](#vlnverse) | unified multi-task VLN | 5 | 7 | configurable agent footprint | RGB, depth, language | Isaac Sim | Mixed | 263 scenes (177/33/53); coarse-grained task: 11,895 train / 3,975 test episodes |

### <a id="navigation-interactive"></a>Interactive Instruction Following

- <a id="alfred"></a>**ALFRED** (2019) `Sim` `widely used`: Household instruction-following benchmark that maps egocentric vision and language (a high-level goal plus step-by-step instructions) to long action sequences with irreversible state changes in AI2-THOR. The long-standing reference for interactive instruction following.<br>
  *Resources*: [Paper](https://arxiv.org/abs/1912.01734) (CVPR 2020) | [Website](https://askforalfred.com/) | [Code](https://github.com/askforalfred/alfred) ★533 | [Data](https://github.com/askforalfred/alfred/tree/master/data) | [Leaderboard](https://askforalfred.com/leaderboard/leaderboard.html)

- <a id="teach"></a>**TEACh** (2021) `Sim`: Human-human dialogues for household tasks in AI2-THOR: a Commander with oracle task knowledge guides a Follower who navigates and manipulates objects, on tasks from Make Coffee to Prepare Breakfast. Defines three benchmarks: EDH, TfD and TATC.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2110.00534) (AAAI 2022) | [Website](https://teachingalfred.github.io/) | [Code](https://github.com/alexa/teach) ★146

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| **[ALFRED](#alfred)** | household instruction following | 7 task types | 4 | 1 (AI2-THOR agent) | RGB, language | AI2-THOR 2.1.0 | Mixed | 25k language directives over 8k+ expert demonstrations |
| [TEACh](#teach) | dialogue-guided household tasks | 12 task types; 3 benchmarks | 4 | 1 (AI2-THOR agent) | RGB, language | AI2-THOR | Human demos | 3,047 human-human gameplay sessions, 45k+ utterances |

### <a id="navigation-social"></a>Social Navigation

- <a id="socnavbench"></a>**SocNavBench** (2021) `Sim`: Simulation test bed for social navigation: a robot crosses 33 curated scenarios in which pedestrians replay recorded real-world trajectories (ETH and UCY), with optional photorealistic rendering. A fixed metric suite covers path quality, motion quality and pedestrian disruption.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2103.00047) (ACM THRI) | [Code](https://github.com/CMU-TBD/SocNavBench) ★58

- <a id="scand"></a>**SCAND** (2022) `Real`: Socially Compliant Navigation Dataset: human-teleoperated demonstrations of polite robot driving through indoor and outdoor crowds at UT Austin, recorded on a Spot and a Jackal. A common real-world source for learning and evaluating social navigation.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2203.15041) (RA-L 2022) | [Website](https://www.cs.utexas.edu/~xiao/SCAND/SCAND.html) | [Data](https://dataverse.tdl.org/dataset.xhtml?persistentId=doi:10.18738/T8/0PRYRH)

- <a id="socialgym-2-0"></a>**SocialGym 2.0** (2023) `Sim`: Lightweight 2D ROS-based simulator and benchmark for multi-agent social navigation in constrained layouts (doorways, hallways, intersections, roundabouts), with a Python API built on PettingZoo and Stable Baselines3 and MARL baselines.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2303.05584) | [Website](https://amrl.cs.utexas.edu/social_gym/index.html) | [Code](https://github.com/ut-amrl/SocialGym2) ★63

- <a id="habitat-3-0-social-navigation"></a>**Habitat 3.0 Social Navigation** (2023) `Sim`: Social Navigation task of Habitat 3.0: a Spot robot must find a simulated humanoid walking through an unseen HSSD home, then follow it at 1-2 m without colliding. Policies can also be evaluated with real people controlling the avatar.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2310.13724) | [Website](https://aihabitat.org/habitat3/) | [Code](https://github.com/facebookresearch/habitat-lab) ★3.2k

- <a id="socialnav-sub"></a>**SocialNav-SUB** (2025) `Real`: Visual question answering benchmark testing whether VLMs understand real social-navigation scenes drawn from SCAND, with spatial, spatiotemporal and social-reasoning questions scored against human answers. Current VLMs fall below a human oracle and a rule-based baseline.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2509.08757) (CoRL 2025) | [Website](https://larg.github.io/socialnav-sub) | [Code](https://github.com/LARG/SocialNavSUB) ★26 | [Data](https://huggingface.co/datasets/michaelmunje/SocialNav-SUB)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| [SocNavBench](#socnavbench) | social navigation | 33 curated scenarios | 4 groups | 1 | RGB, depth, state | SocNavBench simulator (Swiftshader rendering of S3DIS building meshes) | - | N/A (scenarios replay pedestrian recordings from ETH and UCY) |
| [SCAND](#scand) | social navigation demonstrations | N/A | N/A | 2 | RGB, lidar, GPS_IMU, proprioceptive | Real world | Human demos | 8.7 hours, 138 trajectories, 25 miles |
| [SocialGym 2.0](#socialgym-2-0) | multi-agent social navigation, 2D | 4 scenario types | N/A | multi-robot, configurable kinematic constraints | state, lidar | ROS-based 2D simulator (PettingZoo / Stable Baselines3 interface) | - | N/A (simulated training and evaluation) |
| [Habitat 3.0 Social Navigation](#habitat-3-0-social-navigation) | find and follow a humanoid, home scenes | 1 | 4 | 1 (Boston Dynamics Spot) | RGB, depth, state | Habitat-Sim (Habitat 3.0) | - | HSSD scenes: 37 train / 12 val / 10 test |
| [SocialNav-SUB](#socialnav-sub) | VLM scene understanding for social navigation | about 5k questions in 3 categories | 2 | N/A | RGB, language | Real world | Human labels | 4,968 unique questions with human responses |

### <a id="navigation-outdoor"></a>Outdoor, Urban & Aerial

- <a id="barn-challenge"></a>**BARN Challenge** (2020) `Sim + Real`: Benchmark for Autonomous Robot Navigation: 300 cluttered Gazebo obstacle courses of graded difficulty that a Clearpath Jackal with a 2D LiDAR must cross quickly and without collision. Held as an ICRA competition every year since 2022, with physical finals at the venue.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2008.13315) (SSRR 2020; ICRA competition since 2022) | [Website](https://people.cs.gmu.edu/~xiao/Research/BARN_Challenge/BARN_Challenge26.html) | [Code](https://github.com/Daffan/the-barn-challenge) ★73 | [Data](https://www.cs.utexas.edu/~xiao/BARN/BARN.html) | [Leaderboard](https://people.cs.gmu.edu/~xiao/Research/BARN_Challenge/BARN_Challenge26.html)

- <a id="metaurban"></a>**MetaUrban** (2024) `Sim`: Compositional simulator that generates unlimited urban street scenes with pedestrians, vehicles and street furniture for sidewalk robots. Its PointNav and SocialNav benchmarks train on the MetaUrban-12K scene set and test RL and imitation baselines on held-out and unseen scenes.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2407.08725) (ICLR 2025) | [Website](https://metadriverse.github.io/metaurban/) | [Code](https://github.com/metadriverse/metaurban) ★262

- <a id="earth-rover-challenge"></a>**Earth Rover Challenge** (2024) `Real`: Real-world navigation competition in which AI policies and human gamers remotely drive the same small sidewalk rovers through GPS and image-goal missions in cities around the world. Scored by mission difficulty and time; the FrodoBots driving datasets support training.<br>
  *Resources*: [Website](https://earth-rover-challenge.github.io/) | [Code](https://github.com/frodobots-org/earth-rovers-sdk) ★66 | [Data](https://huggingface.co/datasets/BitRobot/FrodoBots-2K)

- <a id="urban-sim-urban-bench"></a>**URBAN-SIM / URBAN-BENCH** (2025) `Sim`: GPU-parallel robot-learning platform for city scenes on Isaac Sim, with URBAN-BENCH: eight tasks covering urban locomotion, urban navigation and a long urban traverse, evaluated on wheeled, quadruped, wheeled-legged and humanoid robots.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2505.00690) (CVPR 2025) | [Website](https://metadriverse.github.io/urban-sim/) | [Code](https://github.com/metadriverse/urban-sim) ★198

- <a id="sidewalkbench"></a>**SidewalkBench** (2026) `Sim` `new`: Benchmark for visual navigation models on urban sidewalks, built on Isaac Sim with procedurally generated and real-world scanned (3DGS) scenes and reactive pedestrians. Nine navigation models are compared on unit-test, pedestrian-reactive and long-horizon scenarios.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2606.16953) (CoRL 2026) | [Website](https://vail.cs.ucla.edu/SidewalkBench/) | [Code](https://github.com/VAIL-UCLA/SidewalkBench) ★36

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| [BARN Challenge](#barn-challenge) | ground-robot obstacle courses | 300 simulated environments, 50 new held-out ones for scoring, physical courses | 1 | 1 (Clearpath Jackal with 2D LiDAR) | lidar, state | Gazebo (ROS) + real | Synthetic | 300 generated navigation environments ordered by difficulty |
| [MetaUrban](#metaurban) | urban micromobility | 2 (PointNav, SocialNav) | 4 | 3 | lidar, state | MetaUrban (MetaDrive-based) | Synthetic | MetaUrban-12K: 12,800 training scenes, 1,000 test scenes, 100 unseen scenes |
| [Earth Rover Challenge](#earth-rover-challenge) | real-world urban navigation competition | 4 tracks in 2026 | 1 | 1 (Earth Rover Mini+ 4WD rover in 2026) | RGB, GPS_IMU | Real world | Human demos | FrodoBots-2K: about 2,000 h of driving; Berkeley-FrodoBots-7K: about 7,000 h |
| [URBAN-SIM / URBAN-BENCH](#urban-sim-urban-bench) | urban micromobility | 8 | task-specific | 4 | RGB, depth, proprioceptive | Isaac Sim (Omniverse, PhysX 5) | - | N/A (procedurally generated scenes) |
| [SidewalkBench](#sidewalkbench) | urban sidewalk visual navigation | 1,235 scenarios | 4 | 4 | RGB | Isaac Sim | - | 100 procedurally generated environments and 11 real-world scanned scenes |

<p align="right"><a href="#contents">Back to contents ↑</a></p>

---

## <a id="locomotion"></a>Locomotion & Humanoids

Continuous-control suites, legged locomotion, humanoid whole-body control, and the motion data behind humanoid tracking. **28 entries.**

**Sub-areas:** [Classic Continuous Control](#locomotion-continuous-control) (3) · [Legged Locomotion](#locomotion-legged) (5) · [Humanoid & Whole-Body Control](#locomotion-humanoid) (11) · [Motion Data for Humanoids](#locomotion-motion-data) (9)

### <a id="locomotion-continuous-control"></a>Classic Continuous Control

- <a id="gymnasium-mujoco-openai-gym"></a>**Gymnasium MuJoCo (OpenAI Gym)** (2016) `Sim` `widely used`: Canonical MuJoCo continuous-control tasks widely used as RL baselines (Ant, HalfCheetah, Hopper, Walker2d, Humanoid and others). Introduced with OpenAI Gym in 2016 and now maintained by the Farama Foundation in Gymnasium.<br>
  *Resources*: [Paper](https://arxiv.org/abs/1606.01540) | [Website](https://gymnasium.farama.org/environments/mujoco/) | [Code](https://github.com/Farama-Foundation/Gymnasium) ★12.8k

- <a id="deepmind-control-suite"></a>**DeepMind Control Suite** (2018) `Sim` `widely used`: Set of MuJoCo continuous-control tasks with a standardised structure and interpretable rewards, from pendulum and cartpole to walker, quadruped, dog and humanoid. A standard testbed for both state-based and pixel-based reinforcement learning.<br>
  *Resources*: [Paper](https://arxiv.org/abs/1801.00690) | [Code](https://github.com/google-deepmind/dm_control) ★4.7k

- <a id="brax"></a>**Brax** (2021) `Sim`: JAX-based differentiable physics engine reproducing classic MuJoCo-style tasks for massively parallel training on accelerators. Since version 0.13 only its training code is maintained: the environments are superseded by MuJoCo Playground and the physics by MJX.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2106.13281) (NeurIPS 2021 D&B) | [Code](https://github.com/google/brax) ★3.3k

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| **[Gymnasium MuJoCo](#gymnasium-mujoco-openai-gym)** | classic control, RL baselines | 11 | 1 (episode return) | 10 (simulated bodies) | state, RGB | MuJoCo | - | N/A |
| **[DeepMind Control Suite](#deepmind-control-suite)** | classic control, state and pixel RL | 28 benchmark tasks | 1 (episode return) | 19 (simulated bodies, one per domain) | state, RGB | MuJoCo | - | N/A |
| [Brax](#brax) | GPU-parallel, differentiable physics | 12 | 1 (episode return) | 11 (simulated bodies) | state | Brax (JAX); pipelines: MJX, generalized, positional, spring | - | N/A |

### <a id="locomotion-legged"></a>Legged Locomotion

- <a id="legged-gym"></a>**legged_gym** (2021) `Sim` `widely used`: Isaac Gym environments from 'Learning to Walk in Minutes': rough-terrain locomotion trained with thousands of parallel robots, a terrain curriculum and the randomisation needed for sim-to-real transfer. Later codebases such as Unitree RL Gym and Humanoid-Gym build on it; the tasks have since moved to Isaac Lab.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2109.11978) (CoRL 2021) | [Website](https://leggedrobotics.github.io/legged_gym/) | [Code](https://github.com/leggedrobotics/legged_gym) ★3.2k

- <a id="icra-quadruped-robot-challenge-qrc"></a>**ICRA Quadruped Robot Challenge (QRC)** (2023) `Real`: Real-robot competition held at ICRA and IROS since 2023 that tests autonomous traversal of varied terrain; later stages added inspection missions and multi-robot collaboration. At ICRA 2026 it was extended to humanoids as the Legged Robot Challenges.<br>
  *Resources*: [Paper](https://doi.org/10.1109/MRA.2023.3293296) (ICRA / IROS competition (since ICRA 2023)) | [Website](https://quadruped-robot-challenges.notion.site/) | [Leaderboard](https://quadruped-robot-challenges.notion.site/ICRA-2026-Legged-Robot-Challenges-286ec5124feb805eb1c1cc14261a7fdf)

- <a id="barkour"></a>**Barkour** (2023) `Real`: Obstacle course for measuring quadruped agility, modelled on dog agility competitions: weave poles, an A-frame, a broad jump and a pause table in a 5 m x 5 m area, scored from 0 to 1 against the roughly 10 s a small dog needs.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2305.14654) | [Website](https://research.google/blog/barkour-benchmarking-animal-level-agility-with-quadruped-robots/) | [Code](https://github.com/google-deepmind/barkour_robot) ★386

- <a id="unitree-rl-gym"></a>**Unitree RL Gym** (2023) `Sim + Real`: Unitree's reinforcement-learning environments for Go2, H1, H1-2 and G1 with a train, play, sim-to-sim, sim-to-real workflow: training in Isaac Gym, a MuJoCo check, then deployment on the robot. Built on legged_gym; Unitree's newer repositories are unitree_rl_lab (Isaac Lab) and unitree_rl_mjlab (MuJoCo).<br>
  *Resources*: [Code](https://github.com/unitreerobotics/unitree_rl_gym) ★3.7k

- <a id="robogauge"></a>**RoboGauge** (2026) `Sim` `new`: Assessment suite that scores a quadruped locomotion policy in MuJoCo sim-to-sim tests before hardware deployment: terrains at ten difficulty levels, domain randomisation and proprioception-based metrics chosen to predict sim-to-real transfer. Released with a mixture-of-experts policy for the Unitree Go2.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2602.00678) (RSS 2026) | [Website](https://robogauge.github.io/complete/) | [Code](https://github.com/wty-yy/RoboGauge) ★90

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| **[legged_gym](#legged-gym)** | quadruped / biped, rough terrain | 5 | N/A | 4 | proprioceptive | Isaac Gym (PhysX) | - | N/A |
| [ICRA Quadruped Robot Challenge](#icra-quadruped-robot-challenge-qrc) | real-robot competition | N/A | N/A | Teams bring their own quadruped | onboard sensors (team's choice) | Real world | - | N/A |
| [Barkour](#barkour) | quadruped agility, obstacle course | 1 course (4 obstacles) | 1 | 1 (custom-built Barkour quadruped) | proprioceptive | Real world | - | N/A |
| [Unitree RL Gym](#unitree-rl-gym) | quadruped / humanoid, sim-to-real | 4 | N/A | 4 (Unitree Go2, G1, H1, H1-2) | proprioceptive | Isaac Gym; MuJoCo (sim-to-sim) + real | - | N/A |
| [RoboGauge](#robogauge) | quadruped, sim-to-real prediction | 5 terrain types x 10 difficulty levels | 6 | 1 (Unitree Go2) | proprioceptive | MuJoCo (policies trained in Isaac Gym) | - | N/A |

### <a id="locomotion-humanoid"></a>Humanoid & Whole-Body Control

- <a id="locomujoco"></a>**LocoMuJoCo** (2023) `Sim`: Imitation-learning benchmark for whole-body control with 9 humanoid robots, 3 (musculo-)skeletal human models and 4 quadrupeds on MuJoCo, MJX and MjWarp. Ships motion-capture data retargeted to each humanoid, trajectory-comparison metrics and JAX baselines; a November 2026 paper describes the current release.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2311.02496) (NeurIPS 2023 Robot Learning Workshop) | [Website](https://loco-mujoco.readthedocs.io/) | [Code](https://github.com/robfiras/loco-mujoco) ★1.5k

- <a id="humanoidbench"></a>**HumanoidBench** (2024) `Sim`: Simulated humanoid benchmark with dexterous hands spanning whole-body manipulation and locomotion: 15 manipulation and 12 locomotion tasks for a Unitree H1 with two dexterous hands, designed for high-DoF reinforcement-learning research.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2403.10506) (RSS 2024) | [Website](https://humanoid-bench.github.io/) | [Code](https://github.com/carlosferrazza/humanoid-bench) ★806

- <a id="humanoid-gym"></a>**Humanoid-Gym** (2024) `Sim + Real`: Isaac Gym framework for training humanoid locomotion policies with zero-shot sim-to-real transfer, with a MuJoCo sim-to-sim step to check policies before deployment. Verified on RobotEra's XBot-S and XBot-L and reused as a base by later humanoid RL code.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2404.05695) | [Website](https://sites.google.com/view/humanoid-gym/) | [Code](https://github.com/roboterax/humanoid-gym) ★2.1k

- <a id="smplolympics"></a>**SMPLOlympics** (2024) `Sim`: Sports environments for physically simulated humanoids compatible with SMPL and SMPL-X: individual events (golf, javelin, high jump, long jump, hurdling) and competitive 1v1 or 2v2 games (table tennis, tennis, fencing, boxing, soccer, basketball), with baselines that combine motion priors and simple rewards.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2407.00187) | [Website](https://smplolympics.github.io/SMPLOlympics) | [Code](https://github.com/SMPLOlympics/SMPLOlympics) ★257

- <a id="mimicking-bench"></a>**Mimicking-Bench** (2024) `Sim`: Benchmark for learning humanoid-scene interaction from human references: six household tasks (sitting on a chair or sofa, lying on a bed or sofa, touching points, lifting a box) over 11K object shapes. Compares pipelines of motion retargeting, motion tracking and imitation learning.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2412.17730) (CVPR 2025 Workshop on Humanoid Agents) | [Website](https://mimicking-bench.github.io/)

- <a id="skillbench-skillblender"></a>**SkillBench (SkillBlender)** (2025) `Sim`: Parallel, cross-embodiment simulation benchmark released with SkillBlender: four primitive skills (walking, reaching, squatting, stepping) and eight loco-manipulation tasks such as button press, box push and package carry on three Unitree humanoids, with metrics that balance accuracy and feasibility.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2506.09366) | [Website](https://psi-lab.ai/SkillBlender-web/) | [Code](https://github.com/Humanoid-SkillBlender/SkillBlender) ★118

- <a id="leverb-bench"></a>**LeVERB-Bench** (2025) `Sim`: Vision-language, closed-loop benchmark for humanoid whole-body control: over 150 tasks in 10 categories (navigation, locomotion, sitting, reaching), rendered photorealistically in Isaac Sim from retargeted motion capture and built to be sim-to-real ready. Released with LeVERB, a hierarchical vision-language-action model shown on a Unitree G1.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2506.13751) | [Website](https://ember-center-berkeley.github.io/LeVERB-Website/) | [Data](https://huggingface.co/datasets/ember-lab-berkeley/LeVERB-Bench-Dataset)

- <a id="simple"></a>**SIMPLE** (2026) `Sim` `new`: Simulation testbed for training and evaluating humanoid loco-manipulation policies that couples MuJoCo contact dynamics with Isaac Sim rendering: whole-body Unitree G1 tasks in 50 indoor scenes with over 1,000 objects. Benchmarks imitation, VLA and world-action models and reports agreement with real-robot results.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2606.08278) (CoRL 2026) | [Website](https://psi-lab.ai/SIMPLE/) | [Code](https://github.com/physical-superintelligence-lab/SIMPLE) ★374 | [Data](https://huggingface.co/collections/USC-PSI-Lab/simple) | [Leaderboard](https://psi-lab.ai/SIMPLE/leaderboard.html)

- <a id="humanoidarena"></a>**HumanoidArena** (2026) `Sim` `new`: Simulation benchmark for hierarchical humanoid control: a high-level policy maps egocentric vision, proprioception and instructions to whole-body actions that a general motion tracker (TWIST2 or SONIC) executes. Seven leg-critical object and scene interaction tasks, tested under visual, semantic and execution shifts and across trackers.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2606.17833) (NeurIPS 2026 Evaluations & Datasets) | [Website](https://humanoidarena.github.io) | [Code](https://github.com/William-wAng618/HumanoidArena) ★120 | [Data](https://www.modelscope.cn/datasets/Twang2026/HumanoidArenaV3.1) | [Leaderboard](https://humanoidarena.github.io/#leaderboard)

- <a id="humantracker"></a>**HumanTracker** (2026) `Sim` `new`: Benchmark for humanoid motion trackers: about 153 hours of newly captured optical mocap from 24 performers in four families (daily, highly dynamic, interaction, ground), retargeted to the Unitree G1, plus HumanScore, a metric trained on 12K human preference pairs. Trackers are evaluated zero-shot in MuJoCo.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2608.13555) (ECCV 2026) | [Website](https://dairuliu.github.io/humantracker) | [Code](https://github.com/GalaxyGeneralRobotics/HumanTracker) ★55 | [Data](https://huggingface.co/datasets/GalaxyGeneralRobotics/HumanTracker)

- <a id="locomanilab"></a>**LocoManiLab** (2026) `Sim + Real` `new`: Testbed for humanoid loco-manipulation spanning data collection, policy training, evaluation and deployment: 234 atomic and compositional household tasks for a Unitree G1 with Dex3-1 hands. Twelve policies are compared with a shared controller, two across five whole-body controllers, on unseen-task, unseen-scene and visual-perturbation splits.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2610.30876) | [Website](https://locomanilab.github.io/) | [Code](https://github.com/Gamma-Robot/LocoManiLab) ★26 | [Data](https://huggingface.co/datasets/GammaRobotics/LocoManiLab) | [Leaderboard](https://locomanilab.github.io/leaderboard.html)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| [LocoMuJoCo](#locomujoco) | imitation learning, whole-body control | 16 embodiments | 2+ | 16 | state, proprioceptive, mocap | MuJoCo (CPU); MJX and MjWarp (GPU) | Human demos | Native mocap set per humanoid; AMASS and LAFAN1 can be retargeted |
| [HumanoidBench](#humanoidbench) | whole-body RL, dexterous hands | 27 | 1 (episode return) | 2 | state, proprioceptive, RGB, tactile | MuJoCo (MJX training code included) | - | N/A |
| [Humanoid-Gym](#humanoid-gym) | humanoid locomotion, sim-to-real | 1 (humanoid locomotion) | N/A | 2 (RobotEra XBot-S, XBot-L) | proprioceptive | Isaac Gym; MuJoCo (sim-to-sim) + real | - | N/A |
| [SMPLOlympics](#smplolympics) | simulated humanoid sports | 11 sports named in the paper | N/A | 1 (simulated SMPL / SMPL-X humanoid) | state, mocap | Isaac Gym | Human demos | Human motion from mocap and videos, used as motion priors (size not stated) |
| [Mimicking-Bench](#mimicking-bench) | humanoid-scene interaction | 6 | 1 | 1 (Unitree H1) | RGB, depth, segmentation, proprioceptive | Isaac Gym | Mixed | 23K human skill references (20K synthetic, 3K real); 11K object shapes |
| [SkillBench](#skillbench-skillblender) | humanoid loco-manipulation | 8 loco-manipulation tasks + 4 primitive skills | 2 groups | 3 (Unitree H1, G1, H1-2) | state, RGB | Isaac Gym | - | N/A |
| [LeVERB-Bench](#leverb-bench) | vision-language whole-body control | 154 vision-language + 460 language-only tasks | 1 (success rate) | 1 (Unitree G1) | RGB, language, proprioceptive | Isaac Sim | Human demos | 17.1 h rendered rollouts + 2.7 h language-only data (5,996 demos) |
| [SIMPLE](#simple) | humanoid loco-manipulation | 60 whole-body tasks on the project page | 1 | 1 for the benchmark (Unitree G1) | RGB, proprioceptive, language | MuJoCo physics with Isaac Sim rendering | Mixed | Motion-planned and VR-teleoperated demos on Hugging Face (size not stated) |
| [HumanoidArena](#humanoidarena) | egocentric hierarchical whole-body learning | 7 | 3 | 1 (Unitree G1) | RGB, proprioceptive, language | Isaac Lab (Isaac Sim) | Human demos | 1,400 VR-teleoperated demos (100 per task per tracker) |
| [HumanTracker](#humantracker) | humanoid motion-tracking evaluation | 25K motion clips in 4 families | 4 | 1 (Unitree G1) | mocap, proprioceptive, language | MuJoCo | Human demos | 153 h optical mocap, 25K clips with text labels |
| [LocoManiLab](#locomanilab) | humanoid loco-manipulation, household | 234 in 5 scene categories | 1 | 1 (Unitree G1 with Dex3-1 hands) | RGB, proprioceptive, language | MuJoCo (RoboCasa-based) + real | Human demos | 51.5 h of simulated teleoperation (about 14k episodes) |

### <a id="locomotion-motion-data"></a>Motion Data for Humanoids

- <a id="amass"></a>**AMASS** (2019) `Real` `widely used`: Archive that unifies optical marker-based motion-capture datasets (15 at release) in one SMPL body parameterisation using MoSh++. The usual source of human reference motion for physics-based character control and humanoid motion tracking, after retargeting to the robot; many trackers are also tested on AMASS subsets.<br>
  *Resources*: [Paper](https://arxiv.org/abs/1904.03278) (ICCV 2019) | [Website](https://amass.is.tue.mpg.de/) | [Code](https://github.com/nghorbani/amass) ★1k | [Data](https://amass.is.tue.mpg.de/)

- <a id="lafan1"></a>**LAFAN1** (2020) `Real` `widely used`: Ubisoft La Forge motion-capture set released with 'Robust Motion In-betweening': 77 sequences from 5 subjects covering walking, running, obstacles, dancing, fighting, jumps and falls. A version retargeted to the Unitree H1, H1-2 and G1 is widely used as reference motion for humanoid tracking.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2102.04942) (SIGGRAPH 2020) | [Code](https://github.com/ubisoft/ubisoft-laforge-animation-dataset) ★1.7k | [Data](https://huggingface.co/datasets/lvhaidong/LAFAN1_Retargeting_Dataset)

- <a id="omomo"></a>**OMOMO** (2023) `Real`: Human-object interaction dataset released with Object MOtion guided human MOtion synthesis: about 10 hours of full-body humans manipulating 15 large objects, with 3D object geometry and object motion. A common source of carrying references for humanoid loco-manipulation, for example in the OmniRetarget set.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2309.16237) (SIGGRAPH Asia 2023) | [Website](https://lijiaman.github.io/projects/omomo/) | [Code](https://github.com/lijiaman/omomo_release) ★326

- <a id="humanoid-x"></a>**Humanoid-X** (2024) `Real`: Dataset of over 20 million humanoid robot poses (163,800 motion samples) mined from internet videos; each sample pairs a video clip with a text description, estimated 3D human pose, retargeted robot keypoints and RL-generated robot actions. Released with UH-1, a text-conditioned humanoid control model.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2412.14172) (Humanoids 2025) | [Website](https://psi-lab.ai/UH-1/) | [Code](https://github.com/sihengz02/UH-1) ★171 | [Data](https://huggingface.co/datasets/USC-PSI-Lab/Humanoid-X)

- <a id="motionmillion"></a>**MotionMillion** (2025) `Real`: Human motion dataset of over 2,000 hours and 2 million text-annotated SMPL sequences, reconstructed from web videos and merged with existing motion sets. Comes with MotionMillion-Eval, 126 prompts in 7 categories for zero-shot text-to-motion, and has been used as a source corpus for large humanoid motion trackers.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2507.07095) (ICCV 2025) | [Website](https://vankouf.github.io/MotionMillion/) | [Code](https://github.com/VankouF/MotionMillion-Codes) ★327 | [Data](https://huggingface.co/datasets/InternRobotics/MotionMillion)

- <a id="omniretarget-dataset"></a>**OmniRetarget Dataset** (2025) `Real`: Unitree G1 reference trajectories produced by OmniRetarget, an interaction-mesh retargeting engine that preserves contacts between robot, objects and terrain: object carrying retargeted from OMOMO, plus terrain climbing and object-terrain motions from in-house mocap. Built for training whole-body tracking policies for loco-manipulation and scene interaction.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2509.26633) (ICRA 2026) | [Website](https://omniretarget.github.io) | [Code](https://github.com/amazon-far/holosoma) ★1.7k | [Data](https://huggingface.co/datasets/omniretarget/OmniRetarget_Dataset)

- <a id="phuma"></a>**PHUMA** (2025) `Real`: Physically reliable humanoid locomotion dataset: 73 hours of motion from motion capture and internet video, cleaned by physics-aware curation and retargeted to the Unitree G1 and H1-2 with a physics-constrained method (PhySINK) that removes floating, penetration and foot skating. Supported natively in NVIDIA ProtoMotions.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2510.26236) (CoRL 2026) | [Website](https://davian-robotics.github.io/PHUMA) | [Code](https://github.com/DAVIAN-Robotics/PHUMA) ★253 | [Data](https://huggingface.co/datasets/DAVIAN-Robotics/PHUMA)

- <a id="bones-seed"></a>**BONES-SEED** (2026) `Real` `new`: Open motion-capture dataset from Bones Studio for humanoid robotics: 142,220 annotated motions (71,132 captured plus mirrored copies, about 288 hours) from 522 actors, each with up to six text descriptions, in NVIDIA SOMA (BVH) and Unitree G1 (MuJoCo-compatible) formats. Used to train NVIDIA's SONIC tracker and Kimodo.<br>
  *Resources*: [Website](https://bones.studio/datasets/seed) | [Code](https://github.com/bones-studio/seed-viewer) ★106 | [Data](https://huggingface.co/datasets/bones-studio/seed)

- <a id="hiphi"></a>**HiPHI** (2026) `Real` `new`: Optical-mocap dataset of whole-body human motion and object interaction, organised by FrameNet action frames: 617.5 hours (308.7 captured) from 132 performers with 40 tracked objects, in BVH with object meshes and trajectories. Its benchmark suite covers motion diversity, interaction quality and humanoid tracking on a Unitree G1.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2608.16222) (CoRL 2026) | [Website](https://noitom-robotics.github.io/hiphi/) | [Code](https://github.com/noitom-robotics/hiphi) ★107 | [Data](https://huggingface.co/datasets/noitomrobotics/HiPHI)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| **[AMASS](#amass)** | human mocap archive, SMPL | N/A (dataset) | N/A | N/A (human SMPL body) | mocap | Real world | Human demos | 40+ hours, 300+ subjects, 11,000+ motions at release |
| **[LAFAN1](#lafan1)** | human mocap; version retargeted to Unitree robots | N/A | N/A | 3 in the retargeted set | mocap | Real world | Human demos | 496,672 frames at 30 fps (about 4.6 h), BVH |
| [OMOMO](#omomo) | full-body human-object interaction mocap | N/A (dataset) | N/A | N/A (human body) | mocap | Real world | Human demos | About 10 hours, 15 objects |
| [Humanoid-X](#humanoid-x) | video-derived humanoid motion with text | N/A (dataset) | N/A | 1 (Unitree H1-2) | video, language, mocap, proprioceptive | Real world | Mixed | 163,800 motion samples, 20M+ robot poses |
| [MotionMillion](#motionmillion) | web-scale human motion with text | 126 evaluation prompts in 7 categories | 3 | N/A (human SMPL body) | mocap, video, language | Real world | Mixed | 2,000+ hours, 2M motion sequences with text |
| [OmniRetarget Dataset](#omniretarget-dataset) | retargeted humanoid loco-manipulation references | N/A (dataset) | N/A | 1 (Unitree G1) | state, mocap | Real world | Mixed | 4.0 hours (3.0 h object carrying, 1.0 h terrain and object-terrain) |
| [PHUMA](#phuma) | physically filtered humanoid locomotion data | N/A (dataset) | N/A | 2 (Unitree G1, H1-2) | mocap, video | Real world | Mixed | 73 hours of retargeted humanoid motion |
| [BONES-SEED](#bones-seed) | large mocap set with Unitree G1 retargets | N/A (dataset) | N/A | 1 | mocap, language | Real world | Human demos | 142,220 motions, about 288 hours at 120 fps, 522 actors |
| [HiPHI](#hiphi) | human motion and object-interaction mocap | 4 benchmark groups | Several per group | 1 | mocap, language | Real world | Human demos | 617.5 h released (308.7 h captured), 200.1M frames, 132 performers |

<p align="right"><a href="#contents">Back to contents ↑</a></p>

---

## <a id="datasets"></a>Robot Learning Datasets

Large open datasets that policies are trained and compared on. **32 entries.**

**Sub-areas:** [Robot Datasets](#datasets-robot-data) (23) · [Egocentric & Human Data](#datasets-human-data) (9)

### <a id="datasets-robot-data"></a>Robot Datasets

- <a id="language-table"></a>**Language-Table** (2022) `Sim + Real`: Language-annotated block rearrangement on a tabletop arm, released with the Interactive Language paper together with a matching simulated benchmark: 442,226 real and 181,020 simulated teleoperated episodes relabelled with natural-language instructions.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2210.06407) | [Website](https://interactive-language.github.io/) | [Code](https://github.com/google-research/language-table) ★368 | [Data](https://github.com/google-research/language-table#datasets)

- <a id="rt-1-robot-action-fractal"></a>**RT-1 Robot Action (Fractal)** (2022) `Real` `widely used`: Training data of Google's RT-1, listed as fractal20220817_data in Open X-Embodiment: over 130k teleoperated episodes covering 700+ language instructions, collected with a fleet of 13 mobile manipulators over 17 months.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2212.06817) (RSS 2023) | [Website](https://robotics-transformer1.github.io/) | [Code](https://github.com/google-research/robotics_transformer) ★1.7k | [Data](https://console.cloud.google.com/storage/browser/gresearch/rt-1-data-release)

- <a id="rh20t"></a>**RH20T** (2023) `Real`: Over 110,000 contact-rich manipulation sequences across 147 tasks and 7 robot configurations, recorded with multi-view RGB-D, force-torque, audio and action data. Each robot sequence comes with a human demonstration video and a language description.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2307.00595) (ICRA 2024) | [Website](https://rh20t.github.io/) | [Code](https://github.com/rh20t/rh20t_api) ★117 | [Data](https://rh20t.github.io/)

- <a id="bridgedata-v2"></a>**BridgeData V2** (2023) `Real` `widely used`: 60,096 trajectories on a low-cost WidowX 250 arm across 24 environments and 13 skills, each labelled with a natural-language instruction. Built for goal-image- and language-conditioned multi-task learning.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2308.12952) (CoRL 2023) | [Website](https://rail-berkeley.github.io/bridgedata/) | [Code](https://github.com/rail-berkeley/bridge_data_v2) ★295 | [Data](https://rail.eecs.berkeley.edu/datasets/bridge_release/data/)

- <a id="open-x-embodiment"></a>**Open X-Embodiment** (2023) `Real` `widely used`: Pool of existing real-robot datasets from 34 labs converted to one RLDS format: over 1M trajectories, 22 embodiments and 527 skills at release. The usual pretraining corpus for generalist manipulation policies, starting with RT-X.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2310.08864) (ICRA 2024) | [Website](https://robotics-transformer-x.github.io/) | [Code](https://github.com/google-deepmind/open_x_embodiment) ★2.1k | [Data](https://docs.google.com/spreadsheets/d/1rPBD77tk60AEIGZrGSODwyyzs5FgCU9Uz3h-3_t2A9g)

- <a id="droid"></a>**DROID** (2024) `Real` `widely used`: In-the-wild manipulation data collected by 13 institutions with one shared Franka Panda setup: 76k teleoperated trajectories (350 hours) over 564 scenes and 84 tasks, with three stereo cameras and language annotations.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2403.12945) (RSS 2024) | [Website](https://droid-dataset.github.io/) | [Code](https://github.com/droid-dataset/droid) ★474 | [Data](https://droid-dataset.github.io/droid/the-droid-dataset)

- <a id="robomind"></a>**RoboMIND** (2024) `Real`: Teleoperated manipulation data collected under one protocol: 107k trajectories over 479 tasks on four embodiments (Franka, UR5e, AgileX dual-arm, a humanoid with dexterous hands), plus 5k annotated failures. RoboMIND 2.0 (Dec 2025) extends it to 310k+ dual-arm trajectories on six embodiments.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2412.13877) (RSS 2025) | [Website](https://x-humanoid-robomind.github.io/) | [Code](https://github.com/x-humanoid-robomind/x-humanoid-robomind.github.io) ★143 | [Data](https://huggingface.co/datasets/x-humanoid-robomind/RoboMIND)

- <a id="agibot-world"></a>**AgiBot World** (2024) `Real` `widely used`: Real-world bimanual manipulation data from about 100 AgiBot G1 robots in home, retail, industrial, restaurant and office scenes: over 1M trajectories (2,976 hours), 217 tasks and 87 atomic skills, including dexterous-hand and visuo-tactile episodes. Released as an Alpha subset and the full Beta set.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2503.06669) (IROS 2025) | [Website](https://agibot-world.com/) | [Code](https://github.com/OpenDriveLab/AgiBot-World) ★3.2k | [Data](https://huggingface.co/datasets/agibot-world/AgiBotWorld-Beta)

- <a id="fourier-actionnet"></a>**Fourier ActionNet** (2025) `Real`: Teleoperated bimanual tabletop manipulation on Fourier GR-1 and GR-2 humanoids with 6- and 12-DoF dexterous hands: over 30k trajectories (about 140 hours) of pick-and-place, pouring and insertion with language prompts.<br>
  *Resources*: [Website](https://action-net.org/) | [Code](https://github.com/FFTAI/fourier-lerobot) ★83 | [Data](https://huggingface.co/datasets/FourierIntelligence/ActionNet)

- <a id="lerobot-community-datasets"></a>**LeRobot Community Datasets** (2025) `Real`: Curated bundles of datasets that community contributors recorded with LeRobot, mostly on SO-100 and SO-101 arms. Versions 1 and 2 build on the data used to pretrain SmolVLA; version 3 (Dec 2025) holds 791 datasets from 235 contributors across 46 robot types.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2506.01844) | [Website](https://huggingface.co/blog/smolvla) | [Code](https://github.com/huggingface/lerobot) ★29k | [Data](https://huggingface.co/datasets/HuggingFaceVLA/community_dataset_v3)

- <a id="interndata-a1"></a>**InternData-A1** (2025) `Sim`: Synthetic data generated in Isaac Sim by composing skills and planning motions: 630k trajectories (7,433 hours) over 70 tasks, 18 skills and 227 scenes on four embodiments, with rigid, articulated, deformable and fluid objects. Built to test whether synthetic data alone can pretrain VLA policies.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2511.16651) | [Website](https://internrobotics.github.io/interndata-a1.github.io/) | [Code](https://github.com/InternRobotics/InternDataEngine) ★150 | [Data](https://huggingface.co/datasets/InternRobotics/InternData-A1)

- <a id="galaxea-open-world-dataset"></a>**Galaxea Open-World Dataset** (2025) `Real`: 500 hours (about 100k trajectories) of mobile bimanual manipulation recorded with a single robot, the Galaxea R1 Lite, in 50 real scenes across homes, restaurants, shops and offices. Covers 150 task categories and 58 skills with subtask-level language annotations.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2509.00576) | [Website](https://opengalaxea.github.io/GalaxeaVLA/) | [Code](https://github.com/OpenGalaxea/GalaxeaVLA) ★825 | [Data](https://huggingface.co/datasets/OpenGalaxea/Galaxea-Open-World-Dataset)

- <a id="fastumi-100k"></a>**FastUMI-100K** (2025) `Real`: Demonstrations recorded with FastUMI handheld grippers instead of a robot: 100K+ trajectories over 54 household tasks in single- and dual-arm form, with wrist fisheye video, end-effector states and text annotations.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2510.08022) | [Code](https://github.com/MrKeee/FastUMI-100K) ★57 | [Data](https://huggingface.co/datasets/IPEC-COMMUNITY/FastUMI_100k_lerobot)

- <a id="humanoid-everyday"></a>**Humanoid Everyday** (2025) `Real`: Teleoperated humanoid data on Unitree G1 and H1 with dexterous hands: 10.3k trajectories (3M+ frames) over 260 tasks in 7 categories, including human-humanoid interaction and loco-manipulation. Comes with a cloud platform that runs submitted policies on the real robots.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2510.08807) | [Website](https://humanoideveryday.github.io/) | [Code](https://github.com/physical-superintelligence-lab/Humanoid-Everyday) ★173 | [Data](https://huggingface.co/datasets/USC-PSI-Lab/humanoid-everyday)

- <a id="robocoin"></a>**RoboCOIN** (2025) `Real` `new`: Bimanual manipulation data from 15 robot platforms: over 180,000 demonstrations of 421 tasks in 16 residential, commercial and industrial environments, annotated from trajectory-level concepts down to subtasks and frame-level kinematics.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2511.17441) | [Website](https://flagopen.github.io/RoboCOIN/) | [Code](https://github.com/FlagOpen/RoboCOIN) ★217 | [Data](https://huggingface.co/RoboCOIN)

- <a id="10kh-realomni"></a>**10Kh RealOmni** (2025) `Real` `new`: GenRobot's open household dataset recorded with handheld Gen DAS grippers instead of robots: long bimanual chores from 3,000+ homes with fisheye video, IMU, tactile arrays and reconstructed trajectories. Uploaded in stages; the dataset card reports 13,000+ hours and 5M+ clips.<br>
  *Resources*: [Website](https://www.genrobot.ai/) | [Code](https://github.com/genrobot-ai/das-datakit) ★63 | [Data](https://huggingface.co/datasets/genrobot2025/10Kh-RealOmin-OpenData)

- <a id="agibot-world-2026"></a>**AgiBot World 2026** (2026) `Sim + Real` `new`: Successor to AgiBot World, collected on the AgiBot G2 in real commercial and home scenes with free-form (unscripted) teleoperation and whole-body control. Released in parts for imitation learning, rich interaction, reinforcement learning and physical reasoning, with digital-twin simulation data.<br>
  *Resources*: [Website](https://agibot-world.com/) | [Data](https://huggingface.co/datasets/agibot-world/AgiBotWorld2026)

- <a id="open-h-embodiment"></a>**Open-H-Embodiment** (2026) `Real` `new`: Community-built dataset of medical robot video with synchronized kinematics, hosted by NVIDIA: about 750 hours and 120,000 trajectories from more than 50 institutions, covering surgical manipulation, robotic ultrasound and endoscopy on platforms such as da Vinci, dVRK and CMR Versius.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2604.21017) | [Website](https://www.open-h.org/) | [Code](https://github.com/open-h/open-h-embodiment) ★160 | [Data](https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-Open-H-Embodiment)

- <a id="hiw-500"></a>**HIW-500** (2026) `Real` `new`: Humanoids In-the-Wild: whole-body teleoperation of a Unitree G1 with grippers in real homes in Southeast Asia, covering mobile and bimanual household chores. Version 1 offers 500+ hours with head and wrist stereo cameras, joint states, odometry and fine-grained subtask labels.<br>
  *Resources*: [Website](https://bitrobot-foundation.github.io/humanoids-in-the-wild-500-hours/) | [Data](https://huggingface.co/datasets/BitRobot/HIW-500-LeRobot)

- <a id="abc-130k"></a>**ABC-130K** (2026) `Real` `new`: Teleoperation dataset at the core of the open ABC behaviour-cloning stack: 3,500+ hours and 130k episodes over 195 tasks on one low-cost bimanual YAM station, part of it with subtask labels. Released with the hardware design, training code and 400 hours of simulated teleoperation.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2606.27375) | [Website](https://abc.bot/) | [Code](https://github.com/amazon-far/abc) ★401 | [Data](https://huggingface.co/datasets/XDOF/ABC-130k)

- <a id="hifi-umi-2k"></a>**HiFi-UMI-2K** (2026) `Real` `new`: 2,000 hours of robot-free bimanual demonstrations captured with the HiFi-UMI handheld system: six hardware-synchronized camera views, about 3 mm end-effector accuracy and replay-validated trajectories from 480+ scenes. A curated subset of a 20,000-hour corpus, aimed at training deployable policies without robot data.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2607.25895) | [Website](https://cloud.simpleai.tech/simple-world-lab/hifi-umi/) | [Data](https://huggingface.co/datasets/simple-world-lab/HiFi-UMI-2K)

- <a id="tacverse"></a>**TacVerse** (2026) `Real` `new`: Bimanual visuo-tactile dataset from Xense Robotics, recorded with handheld UMI grippers that carry a visuotactile sensor on each finger, so every frame has four tactile streams next to the camera views. Released so far: 1,400+ hours and 75,000+ episodes over 150+ contact-rich tasks.<br>
  *Resources*: [Website](https://huggingface.co/datasets/TacVerse/TacVerse) | [Data](https://huggingface.co/datasets/TacVerse/TacVerse)

- <a id="fineart"></a>**FineART** (2026) `Real` `new`: Bimanual manipulation dataset from Scale AI and Hugging Face LeRobot in which every episode carries human-written subtask annotations: 40,543 teleoperated episodes (1,718 hours), 533,913 subtask labels and 151 tasks on a Trossen Stationary AI robot.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2609.36416) | [Code](https://github.com/huggingface/lerobot) ★29k | [Data](https://huggingface.co/datasets/lerobot/FineART)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| [Language-Table](#language-table) | language-conditioned, tabletop pushing | N/A | 1 | 1 (xArm) | RGB, proprioceptive, language | PyBullet + real | Mixed | 442,226 real and 181,020 sim teleoperated episodes; 1M scripted sim episodes |
| **[RT-1 Robot Action](#rt-1-robot-action-fractal)** | single embodiment, mobile manipulator | 700+ language instructions | N/A | 1 (Google Robot mobile manipulator) | RGB, proprioceptive, language | Real world | Human demos | 130k+ episodes (73,499 in the Open X-Embodiment copy) |
| [RH20T](#rh20t) | contact-rich, force-torque, multi-view | 147 | N/A | 7 | RGB, depth, proprioceptive, force-torque, audio, tactile, language | Real world | Human demos | 110,000+ robot sequences with paired human demonstration videos |
| **[BridgeData V2](#bridgedata-v2)** | single embodiment, low-cost arm | 13 skills, 24 environments | N/A | 1 (WidowX 250) | RGB, depth, proprioceptive, language | Real world | Mixed | 60,096 trajectories (50,365 teleoperated, 9,731 scripted) |
| **[Open X-Embodiment](#open-x-embodiment)** | cross-embodiment, aggregated, real robot | 527 skills (160,266 tasks) | N/A | 22 | RGB, depth, proprioceptive, language | Real world | Mixed | 1M+ trajectories (60 datasets) at release; now 72 datasets, 2.4M episodes |
| **[DROID](#droid)** | single embodiment, in-the-wild | 84 tasks, 564 scenes | N/A | 1 (Franka Panda) | RGB, depth, proprioceptive, language | Real world | Human demos | 76k trajectories, 350 hours |
| [RoboMIND](#robomind) | multi-embodiment | 479 (v1); 739 (v2.0) | N/A | 4 (v1); 6 (v2.0) | RGB, proprioceptive, tactile, language | Real world | Human demos | 107k trajectories (v1); 310k+ real and 20k simulated (v2.0) |
| **[AgiBot World](#agibot-world)** | bimanual, large-scale, long-horizon | 217 tasks, 87 atomic skills | N/A | 1 (AgiBot G1) | RGB, depth, proprioceptive, tactile, language | Real world | Human demos | 1,003,672 trajectories, 2,976 hours (Beta); 92,214 trajectories (Alpha) |
| [Fourier ActionNet](#fourier-actionnet) | humanoid, dexterous hands | N/A | N/A | 3 (Fourier GR1-T1, GR1-T2, GR2) | RGB, depth, proprioceptive, language | Real world | Human demos | 30k+ trajectories, about 140 hours |
| [LeRobot Community Datasets](#lerobot-community-datasets) | crowdsourced, low-cost arms | N/A | N/A | 46 robot types in v3 | RGB, proprioceptive, language | Real world | Human demos | v3: 50,622 episodes, 251.5 hours; v1 + v2: 17,457 episodes, 93.5 hours |
| [InternData-A1](#interndata-a1) | synthetic, multi-embodiment | 70 tasks, 18 skills | N/A | 4 | RGB, proprioceptive, language | NVIDIA Isaac Sim (InternDataEngine) | Planner | 630k+ trajectories, 7,433 hours |
| [Galaxea Open-World Dataset](#galaxea-open-world-dataset) | mobile bimanual, single embodiment | 150 task categories, 58 skills | N/A | 1 (Galaxea R1 Lite) | RGB, proprioceptive, language | Real world | Human demos | 500 hours, about 100k trajectories |
| [FastUMI-100K](#fastumi-100k) | UMI-style, handheld gripper, robot-free | 54 tasks | N/A | N/A | RGB, proprioceptive, language | Real world | Human demos | 100K+ trajectories |
| [Humanoid Everyday](#humanoid-everyday) | humanoid, dexterous hands | 260 tasks in 7 categories | N/A | 2 (Unitree G1, Unitree H1) | RGB, depth, lidar, tactile, GPS_IMU, proprioceptive, language | Real world | Human demos | 10.3k trajectories, 3M+ frames |
| [RoboCOIN](#robocoin) | bimanual, multi-embodiment | 421 tasks | N/A | 15 | RGB, proprioceptive, language | Real world | Human demos | 180,000+ demonstrations |
| [10Kh RealOmni](#10kh-realomni) | UMI-style, handheld gripper | 30 core skills in 10 household scenarios | N/A | N/A (handheld Gen DAS Gripper, bimanual) | RGB, tactile, GPS_IMU, proprioceptive | Real world | Human demos | 13,000+ hours, 5M+ clips, 95 TB |
| [AgiBot World 2026](#agibot-world-2026) | whole-body mobile manipulation | N/A | N/A | 1 (AgiBot G2) | RGB, depth, tactile, lidar, GPS_IMU, proprioceptive, language | Genie Sim (digital twins of the real scenes) + real | Human demos | Hundreds of hours in the first (imitation-learning) part; total not stated |
| [Open-H-Embodiment](#open-h-embodiment) | medical robotics, surgical | N/A | N/A | Multiple | RGB, proprioceptive, language | Real world | Mixed | About 750 hours, 120,000 trajectories (v1) |
| [HIW-500](#hiw-500) | humanoid, in-the-wild homes | 11 tasks, 161 subtask labels | N/A | 1 (Unitree G1) | RGB, proprioceptive, GPS_IMU, language | Real world | Human demos | 500+ hours (V1); 23,743 episodes in the LeRobot-format release |
| [ABC-130K](#abc-130k) | bimanual, teleoperation, low-cost arms | 195 tasks | N/A | 1 (bimanual YAM station) | RGB, proprioceptive, language | Real world | Human demos | 130,703 episodes, 3,590.7 hours (42,980 episodes with subtask labels) |
| [HiFi-UMI-2K](#hifi-umi-2k) | UMI-style, handheld bimanual, robot-free | N/A | N/A | N/A | RGB, proprioceptive, language | Real world | Human demos | 2,000 hours released (from a 20,000+ hour, 4.32M-episode corpus) |
| [TacVerse](#tacverse) | visuo-tactile, UMI-style, bimanual | 150+ released (350+ planned) | N/A | N/A (handheld XTac-UMI-G1 gripper pair) | RGB, tactile, proprioceptive, language | Real world | Human demos | 75,000+ episodes, 1,400+ hours released (10,000+ hours planned) |
| [FineART](#fineart) | bimanual, dense subtask language | 151 tasks | N/A | 1 (Trossen Stationary AI) | RGB, proprioceptive, language | Real world | Human demos | 40,543 episodes, 1,718 hours, 533,913 subtask labels |

### <a id="datasets-human-data"></a>Egocentric & Human Data

- <a id="epic-kitchens-100"></a>**EPIC-KITCHENS-100** (2020) `Real` `widely used`: 100 hours of unscripted head-mounted video in 45 home kitchens with 90K densely annotated action segments. Runs yearly challenges on action recognition, detection, anticipation, retrieval and domain adaptation, and is a long-standing source of human manipulation video.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2006.13256) (IJCV 2022) | [Website](https://epic-kitchens.github.io/) | [Code](https://github.com/epic-kitchens/epic-kitchens-100-annotations) ★175 | [Data](https://github.com/epic-kitchens/epic-kitchens-download-scripts) | [Leaderboard](https://epic-kitchens.github.io/2026)

- <a id="ego4d"></a>**Ego4D** (2021) `Real` `widely used`: 3,670 hours of unscripted daily-life egocentric video from 931 camera wearers in 74 locations and 9 countries, with narrations and five benchmark families: episodic memory, hands and objects, audio-visual diarization, social interaction and forecasting. A common source of human video for robot pretraining.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2110.07058) (CVPR 2022) | [Website](https://ego4d-data.org/) | [Code](https://github.com/facebookresearch/Ego4d) ★665 | [Data](https://ego4d-data.org/docs/start-here/) | [Leaderboard](https://ego4d-data.org/docs/challenge/)

- <a id="ego-exo4d"></a>**Ego-Exo4D** (2023) `Real`: Time-synchronized first- and third-person video of skilled activities such as cooking, bike repair, sports and music: 1,286 hours from 740 participants in 13 cities, with audio, gaze, IMU, point clouds and expert commentary. Benchmarks cover activity understanding, proficiency, cross-view translation and 3D hand/body pose.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2311.18259) (CVPR 2024) | [Website](https://ego-exo4d-data.org/) | [Code](https://github.com/facebookresearch/Ego4d) ★665 | [Data](https://docs.ego-exo4d-data.org/)

- <a id="nymeria"></a>**Nymeria** (2024) `Real`: 300 hours of in-the-wild daily activity from 264 participants in 50 locations, recorded with Project Aria devices and a motion-capture suit, so egocentric video is paired with full-body ground-truth motion and 301.5K motion-language sentences. NymeriaPlus (2026) adds object boxes, 3D shapes and SMPL motion.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2406.09905) (ECCV 2024) | [Website](https://explorer.projectaria.com/nymeria) | [Code](https://github.com/facebookresearch/nymeria_dataset) ★270 | [Data](https://explorer.projectaria.com/nymeria)

- <a id="ph2d"></a>**PH2D** (2025) `Real`: Physical Human-Humanoid Data: about 27k task-oriented egocentric human demonstrations with 3D head, hand and finger poses and language, recorded with consumer VR headsets and aligned with humanoid teleoperation data so that both can train one policy.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2503.13441) (CoRL 2025) | [Website](https://human-as-robot.github.io/) | [Code](https://github.com/RogerQi/human-policy) ★258 | [Data](https://huggingface.co/datasets/RogerQi/PH2D)

- <a id="egodex"></a>**EgoDex** (2025) `Real`: 829 hours of egocentric tabletop manipulation recorded with Apple Vision Pro, with 3D pose of the head, upper body and every finger joint tracked at capture time, plus language labels, across 194 tasks. Includes a train/test split and a hand-trajectory prediction benchmark.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2505.11709) (ICLR 2026) | [Code](https://github.com/apple-aiml-research/ml-egodex) ★416 | [Data](https://github.com/apple-aiml-research/ml-egodex)

- <a id="egocentric-10k"></a>**Egocentric-10K** (2025) `Real` `new`: 10,000 hours of head-mounted video of workers in 85 real factories, released by Build AI under Apache 2.0 as raw 1080p clips with camera intrinsics; the card stresses high hand visibility and manipulation density. The follow-up Egocentric-100K adds 100,405 hours at 256p.<br>
  *Resources*: [Website](https://www.build.ai/) | [Data](https://huggingface.co/datasets/builddotai/Egocentric-10K)

- <a id="egoverse"></a>**EgoVerse** (2026) `Real` `new`: Consortium-run, continuously growing egocentric dataset built for robot learning, with per-frame 3D hand poses, head poses and language annotation in a shared format. The paper release has 1,362 hours (80k episodes) over 1,965 tasks from 2,087 demonstrators and a multi-lab study of human-to-robot transfer.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2604.07607) (RSS 2026) | [Website](https://egoverse.ai/) | [Code](https://github.com/GaTech-RL2/EgoVerse) ★584 | [Data](https://egoverse-research-workbench.vercel.app/)

- <a id="humannet"></a>**HumanNet** (2026) `Real` `new`: Curated human-centric video corpus of about one million hours, first- and third-person, with captions, motion descriptions and hand/body signals for embodied pretraining. Public so far: HumanNet Ego (about 200,000 egocentric hours) and Open-HumanWAM-50K, a 50,000-hour multi-source mix with hand-motion and language labels.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2605.06747) | [Website](https://dagroup-pku.github.io/HumanNet/) | [Code](https://github.com/DAGroup-PKU/HumanNet) ★370 | [Data](https://huggingface.co/datasets/DAGroup-PKU/HumanNet)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| **[EPIC-KITCHENS-100](#epic-kitchens-100)** | egocentric video, kitchens | 6 challenges | N/A | N/A (human) | video, audio, language | Real world | Human demos | 100 hours, 700 videos, 20M frames, 90K action segments |
| **[Ego4D](#ego4d)** | egocentric video, daily activities | 5 benchmark families | N/A | N/A (human) | video, audio, language | Real world | Human demos | 3,670 hours of video, 931 camera wearers |
| [Ego-Exo4D](#ego-exo4d) | ego and exo video, skilled activities | 4 benchmark families | N/A | N/A (human) | video, audio, GPS_IMU, pointcloud, hand pose, language | Real world | Human demos | 1,286 hours of video, 740 participants, 123 scenes |
| [Nymeria](#nymeria) | egocentric video, full-body motion | N/A | N/A | N/A (human) | video, mocap, GPS_IMU, pointcloud, language | Real world | Human demos | 300 hours, 264 participants, 50 locations |
| [PH2D](#ph2d) | egocentric video, hand pose | N/A | N/A | N/A | video, hand pose, language | Real world | Human demos | About 27k demonstrations (dozens of hours) |
| [EgoDex](#egodex) | egocentric video, 3D hand pose | 194 tasks | 1 family | N/A (human) | video, hand pose, language | Real world | Human demos | 829 hours (about 725 train, 7 test, 97 additional) |
| [Egocentric-10K](#egocentric-10k) | egocentric video, factory work | N/A | N/A | N/A (human) | video | Real world | Human demos | 10,000 hours, 192,900 clips, 1.08B frames (Egocentric-100K: 100,405 hours) |
| [EgoVerse](#egoverse) | egocentric video | 1,965 tasks, 240 scenes | N/A | N/A | video, hand pose, language | Real world | Human demos | 1,362 hours, 80k episodes (paper); 4,003 hours on the site (Nov 2026) |
| [HumanNet](#humannet) | human video, million-hour scale | N/A | N/A | N/A (human) | video, hand pose, language | Real world | Human demos | 1M hours described; 200K-hour egocentric subset and 50K-hour mix released |

<p align="right"><a href="#contents">Back to contents ↑</a></p>

---

## <a id="simulation"></a>Simulators

The engines and frameworks the benchmarks above are built on. This section compares capabilities instead of tasks. **30 simulators.**

**Sub-areas:** [Physics Engines & General Simulators](#simulation-physics) (13) · [Robot-Learning Frameworks](#simulation-learning-framework) (6) · [Embodied-AI Platforms](#simulation-embodied-platform) (4) · [Specialized Simulators](#simulation-specialized) (7)

### <a id="simulation-physics"></a>Physics Engines & General Simulators

- <a id="webots"></a>**Webots** (1998): Open-source desktop robot simulator with a large library of robot, sensor and actuator models, used in research, teaching and robot contests. Designed at EPFL in 1996, commercialised by Cyberbotics from 1998 and open-sourced in December 2018.<br>
  *Resources*: [Paper](https://arxiv.org/abs/cs/0412052) | [Website](https://cyberbotics.com/) | [Code](https://github.com/cyberbotics/webots) ★4.8k | [Docs](https://cyberbotics.com/doc/guide/index)

- <a id="gazebo"></a>**Gazebo** (2002) `widely used`: Modular open-source robot simulator with plugin-based physics, rendering and sensor libraries. Development began in 2002; the rewritten Gazebo (formerly Ignition) first shipped in 2019 and Gazebo Classic reached end of life in January 2025. Physics runs on CPU.<br>
  *Resources*: [Paper](https://ieeexplore.ieee.org/document/1389727) (IROS 2004) | [Website](https://gazebosim.org) | [Code](https://github.com/gazebosim/gz-sim) ★1.6k | [Docs](https://gazebosim.org/docs)

- <a id="coppeliasim-v-rep"></a>**CoppeliaSim (V-REP)** (2010): General-purpose robot simulator (V-REP until 2019) with a distributed control architecture: each object can be driven by embedded scripts, plugins or remote API clients. Offers five interchangeable physics engines; RLBench runs on it through PyRep.<br>
  *Resources*: [Paper](https://ieeexplore.ieee.org/document/6696520) (IROS 2013) | [Website](https://www.coppeliarobotics.com/) | [Code](https://github.com/CoppeliaRobotics/coppeliaSimLib) ★154 | [Docs](https://manual.coppeliarobotics.com/)

- <a id="mujoco"></a>**MuJoCo** (2012) `widely used`: General-purpose physics engine for articulated bodies in contact, maintained by Google DeepMind; the backend of many manipulation and locomotion benchmarks. Batched GPU simulation comes through MJX (JAX) and MuJoCo Warp (with NVIDIA); version 4.0 was released in November 2026.<br>
  *Resources*: [Paper](https://ieeexplore.ieee.org/document/6386109) (IROS 2012) | [Website](https://mujoco.org/) | [Code](https://github.com/google-deepmind/mujoco) ★18.4k | [Docs](https://mujoco.readthedocs.io/)

- <a id="drake"></a>**Drake** (2014): C++ toolbox with Python bindings for analysing robot dynamics and building controllers: multibody simulation with contact plus optimisation-based planning and control design. Started at MIT's Robot Locomotion Group; development is now led by Toyota Research Institute.<br>
  *Resources*: [Website](https://drake.mit.edu/) | [Code](https://github.com/RobotLocomotion/drake) ★4.3k | [Docs](https://drake.mit.edu/installation.html)

- <a id="pybullet"></a>**PyBullet** (2016) `widely used`: Official Python interface to the Bullet physics SDK, aimed at robotics simulation and reinforcement learning. Lightweight and CPU-based; the base of many earlier manipulation, drone and assistive benchmarks such as CALVIN, safe-control-gym and Assistive Gym.<br>
  *Resources*: [Website](https://pybullet.org) | [Code](https://github.com/bulletphysics/bullet3) ★14.9k | [Docs](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/edit)

- <a id="raisim"></a>**RaiSim** (2018): Closed-source rigid-body physics engine from RaiSim Tech, built around a per-contact iteration solver and used for legged-robot learning. Free for academics, paid for commercial use. The original raisimLib was retired in 2026 in favour of RaiSim2, distributed as binaries with the rayrai renderer.<br>
  *Resources*: [Paper](https://ieeexplore.ieee.org/document/8255551) (RA-L 2018) | [Website](https://raisim.com/) | [Code](https://github.com/raisimTech/raisim2Lib) ★48 | [Docs](https://raisim.com/)

- <a id="sapien"></a>**SAPIEN** (2020): Physics-rich simulator for robotics and embodied AI built on PhysX, released together with the PartNet-Mobility articulated-object dataset. SAPIEN 3 added GPU-parallel PhysX 5 simulation and is the engine underneath ManiSkill.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2003.08515) (CVPR 2020) | [Website](https://sapien-sim.github.io/docs/) | [Code](https://github.com/haosulab/SAPIEN) ★872 | [Docs](https://sapien-sim.github.io/docs/)

- <a id="isaac-sim"></a>**Isaac Sim** (2021) `widely used`: NVIDIA's robotics simulator on Omniverse with RTX-rendered sensors, synthetic data generation and ROS 2 bridges; the base of Isaac Lab and of many embodied-AI platforms. Open-sourced under Apache-2.0 with version 5.0 (2025); version 6 (2026) adds Newton as a second physics backend next to PhysX.<br>
  *Resources*: [Website](https://developer.nvidia.com/isaac/sim) | [Code](https://github.com/isaac-sim/IsaacSim) ★4.5k | [Docs](https://docs.isaacsim.omniverse.nvidia.com/latest/index.html)

- <a id="isaac-gym"></a>**Isaac Gym** (2021) `widely used`: NVIDIA's standalone GPU physics simulator: simulation and policy training stay on one GPU with direct tensor access, enabling massively parallel RL for legged and dexterous robots. Deprecated in favour of Isaac Lab (last release Preview 4) but still the backend of many published benchmarks.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2108.10470) (NeurIPS 2021 D&B) | [Website](https://developer.nvidia.com/isaac-gym) | [Code](https://github.com/isaac-sim/IsaacGymEnvs) ★2.9k

- <a id="genesis-genesis-world"></a>**Genesis (Genesis World)** (2024): Multi-physics simulation platform with a Python interface: rigid, FEM, MPM, SPH, PBD and IPC solvers share one scene and run as batched GPU environments. Started as an academic project in December 2024; renamed Genesis World, with a 1.0 release in May 2026 backed by Genesis AI.<br>
  *Resources*: [Website](https://genesis-world.readthedocs.io/) | [Code](https://github.com/Genesis-Embodied-AI/genesis-world) ★30.3k | [Docs](https://genesis-world.readthedocs.io/)

- <a id="newton"></a>**Newton** (2025): Open-source GPU physics engine built on NVIDIA Warp and OpenUSD, started by Disney Research, Google DeepMind and NVIDIA and hosted by the Linux Foundation. MuJoCo Warp is its main rigid-body backend, next to Kamino, VBD, XPBD and MPM solvers; 1.0 shipped in March 2026.<br>
  *Resources*: [Website](https://newton-physics.github.io/newton/stable/) | [Code](https://github.com/newton-physics/newton) ★6k | [Docs](https://newton-physics.github.io/newton/stable/)

- <a id="unreal-robotics-lab-urlab"></a>**Unreal Robotics Lab (URLab)** (2025): Unreal Engine 5 plugin that embeds MuJoCo physics in the editor and runtime, pairing MuJoCo contact dynamics with Unreal rendering, cameras and effects such as smoke, fire and water, with Python and ROS 2 control. Paper in April 2025; code released in April 2026.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2504.14135) (ICRA 2026) | [Website](https://urlab-sim.github.io/UnrealRoboticsLab/) | [Code](https://github.com/URLab-Sim/UnrealRoboticsLab) ★578 | [Docs](https://urlab-sim.github.io/UnrealRoboticsLab/)

**Summary comparison**

| Simulator | Physics Engine | Renderer | GPU Support | OS | License |
|---|---|---|:---:|---|---|
| [Webots](#webots) | ODE | WREN (OpenGL 3.3) | ✗ | Linux, Windows, macOS | Apache-2.0 |
| **[Gazebo](#gazebo)** | gz-physics plugins: DART (reference), Bullet, Bullet Featherstone, TPE | gz-rendering: OGRE 1.x, OGRE-Next 2.x | ✗ | Linux, macOS, Windows | Apache-2.0 |
| [CoppeliaSim](#coppeliasim-v-rep) | Bullet, ODE, MuJoCo, Vortex, Newton Dynamics (selectable) | OpenGL; POV-Ray plugin | ✗ | Linux, Windows, macOS | Proprietary (free Edu licence, paid Pro); core library GPL-3.0 |
| **[MuJoCo](#mujoco)** | MuJoCo (CPU); MJX (JAX) and MuJoCo Warp for GPU | OpenGL, Filament; MuJoCo Warp batch ray tracer | ✓ | Linux, Windows, macOS | Apache-2.0 |
| [Drake](#drake) | Drake multibody dynamics (CPU) | RenderEngineVtk, RenderEngineGl (OpenGL), glTF render client | ✗ | Linux, macOS | BSD-3-Clause |
| **[PyBullet](#pybullet)** | Bullet (rigid and soft bodies) | OpenGL visualizer; TinyRenderer (CPU) | ✗ | Linux, Windows, macOS | zlib |
| [RaiSim](#raisim) | RaiSim (per-contact iteration solver, multithreaded CPU) | rayrai (RGB, depth, LiDAR); RaisimUnity / RaisimOgre for legacy RaiSim | ✗ | Linux, Windows, macOS | Proprietary (free academic licence; paid commercial) |
| [SAPIEN](#sapien) | NVIDIA PhysX 5 (CPU and GPU) | SapienRenderer (Vulkan rasterisation and ray tracing) | ✓ | Linux, Windows, macOS | Apache-2.0 |
| **[Isaac Sim](#isaac-sim)** | PhysX 5 (GPU); Newton backend since 6.0 | Omniverse RTX (ray tracing / path tracing) | ✓ | Linux, Windows | Apache-2.0 (code); Omniverse Kit and assets under NVIDIA terms |
| **[Isaac Gym](#isaac-gym)** | NVIDIA PhysX (GPU) | Built-in Vulkan renderer; camera images as GPU tensors | ✓ | Linux | Free binary under NVIDIA licence; IsaacGymEnvs is BSD-3-Clause |
| [Genesis](#genesis-genesis-world) | Genesis multi-physics (rigid, FEM, MPM, SPH, PBD, IPC) | Nyx; LuisaRender ray tracer; PyRender rasteriser | ✓ | Linux, Windows, macOS | Apache-2.0 |
| [Newton](#newton) | Newton solvers: MuJoCo Warp, Kamino, Featherstone, XPBD, VBD, implicit MPM | Warp ray-traced tiled camera sensor; OpenGL, USD, Rerun, Viser viewers | ✓ | Linux, Windows, macOS | Apache-2.0 |
| [Unreal Robotics Lab](#unreal-robotics-lab-urlab) | MuJoCo | Unreal Engine 5 | ✗ | Windows, Linux | Apache-2.0 |

### <a id="simulation-learning-framework"></a>Robot-Learning Frameworks

- <a id="isaac-lab"></a>**Isaac Lab** (2023) `widely used`: NVIDIA's open-source GPU-accelerated framework for robot learning (reinforcement and imitation learning), grown out of Orbit, with 30+ ready-to-train environments and 16+ robot models. Version 3.0 (October 2026) is multi-backend: PhysX through Isaac Sim, or Newton without Isaac Sim.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2511.04831) | [Website](https://developer.nvidia.com/isaac/lab) | [Code](https://github.com/isaac-sim/IsaacLab) ★8.7k | [Docs](https://isaac-sim.github.io/IsaacLab/)

- <a id="mujoco-playground"></a>**MuJoCo Playground** (2025): Google DeepMind's suite of robot-learning environments and sim-to-real workflows on MuJoCo: quadrupeds, humanoids, dexterous hands and arms trained in minutes on one GPU. The RSS 2025 release used JAX/MJX; version 1.0 (November 2026) moved to PyTorch on reaf-sim and MuJoCo Warp.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2502.08844) (RSS 2025) | [Website](https://playground.mujoco.org/) | [Code](https://github.com/google-deepmind/mujoco_playground) ★2.3k | [Docs](https://reaf-sim.readthedocs.io/en/latest/playground/index.html)

- <a id="roboverse-metasim"></a>**RoboVerse (MetaSim)** (2025): Simulation platform, synthetic dataset and unified imitation- and reinforcement-learning benchmarks built on MetaSim, a layer that exposes many simulators through one configuration system and API. Integrates tasks and data from suites such as LIBERO, ManiSkill, RLBench and Meta-World.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2504.18904) (RSS 2025) | [Website](https://roboverseorg.github.io/) | [Code](https://github.com/RoboVerseOrg/RoboVerse) ★1.9k | [Docs](https://roboverse.wiki/)

- <a id="mjlab"></a>**mjlab** (2025): Lightweight robot-learning framework that pairs Isaac Lab's manager-based API with MuJoCo Warp, with few dependencies and direct access to native MuJoCo data structures. Ships velocity-tracking, motion-imitation and manipulation tasks; training needs an NVIDIA GPU.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2601.22074) | [Website](https://mujocolab.github.io/mjlab/) | [Code](https://github.com/mujocolab/mjlab) ★3.4k | [Docs](https://mujocolab.github.io/mjlab/)

- <a id="isaac-lab-arena"></a>**Isaac Lab-Arena** (2025) `new`: NVIDIA's open-source extension of Isaac Lab, co-developed with Lightwheel, for authoring benchmarks and evaluating generalist policies: environments are composed from scene, embodiment and task parts and evaluated in parallel on GPU through a policy server. Still alpha software.<br>
  *Resources*: [Website](https://developer.nvidia.com/blog/simplify-generalist-robot-policy-evaluation-in-simulation-with-nvidia-isaac-lab-arena/) | [Code](https://github.com/isaac-sim/IsaacLab-Arena) ★665 | [Docs](https://isaac-sim.github.io/IsaacLab-Arena/)

- <a id="gs-playground"></a>**GS-Playground** (2026) `new`: Simulator for vision-based robot learning that couples its own batched physics engine (MotrixSim) with batch 3D Gaussian Splatting rendering, reporting about 10^4 FPS at 640x480, plus a Real2Sim pipeline for photorealistic scenes. From the DISCOVERSE team at Tsinghua AIR with Motphys; the public repository is a preview release.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2604.25459) (RSS 2026) | [Website](https://gsplayground.github.io/) | [Code](https://github.com/discoverse-dev/gs_playground) ★508

**Summary comparison**

| Simulator | Physics Engine | Renderer | GPU Support | OS | License |
|---|---|---|:---:|---|---|
| **[Isaac Lab](#isaac-lab)** | PhysX 5 (Isaac Sim) or Newton (MuJoCo Warp, Kamino, XPBD, VBD) | Omniverse RTX (Isaac Sim), OVRTX, Newton Warp renderer | ✓ | Linux, Windows | BSD-3-Clause (isaaclab_mimic: Apache-2.0); Isaac Sim licensed separately |
| [MuJoCo Playground](#mujoco-playground) | MuJoCo Warp (v1.0); MJX for the RSS 2025 environments | MuJoCo Warp batch renderer; MuJoCo viewer | ✓ | Linux, macOS | Apache-2.0 |
| [RoboVerse](#roboverse-metasim) | Multi-backend: Isaac Lab, Isaac Gym, MuJoCo, SAPIEN, Genesis, PyBullet, Newton | Per backend (e.g. Isaac RTX, SAPIEN, MuJoCo); Blender | ✓ | Linux | Apache-2.0 |
| [mjlab](#mjlab) | MuJoCo Warp | MuJoCo Warp ray-traced cameras; native MuJoCo and Viser viewers | ✓ | Linux, macOS | Apache-2.0 |
| [Isaac Lab-Arena](#isaac-lab-arena) | PhysX 5 or Newton (through Isaac Lab 3) | Omniverse RTX (Isaac Sim) | ✓ | Linux | Apache-2.0 |
| [GS-Playground](#gs-playground) | MotrixSim (CPU/GPU batched backends) | Batch 3D Gaussian Splatting | ✓ | Linux | MIT |

### <a id="simulation-embodied-platform"></a>Embodied-AI Platforms

- <a id="habitat-sim"></a>**Habitat-Sim** (2019) `widely used`: Fast 3D simulator for embodied AI on scanned and CAD indoor scenes (HM3D, HSSD, Matterport3D, Gibson, ReplicaCAD) with Bullet rigid-body physics; with Habitat-Lab it underlies the PointNav, ObjectNav and rearrangement benchmarks. Meta ended official maintenance after v0.3.4 and archived the repository in 2026.<br>
  *Resources*: [Paper](https://arxiv.org/abs/1904.01201) (ICCV 2019) | [Website](https://aihabitat.org/) | [Code](https://github.com/facebookresearch/habitat-sim) ★3.8k | [Docs](https://aihabitat.org/docs/habitat-sim/)

- <a id="omnigibson"></a>**OmniGibson** (2022): Simulator behind the BEHAVIOR-1K benchmark, built on NVIDIA Isaac Sim: realistic physics and rendering of rigid bodies, deformable bodies and liquids in household scenes for 1,000 everyday activities. From the Stanford lab behind iGibson; now developed inside the BEHAVIOR-1K repository.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2403.09227) (CoRL 2022) | [Website](https://behavior.stanford.edu/) | [Code](https://github.com/StanfordVL/BEHAVIOR-1K) ★1.8k | [Docs](https://behavior.stanford.edu/omnigibson/overview.html)

- <a id="internutopia-grutopia"></a>**InternUtopia (GRUtopia)** (2024): Isaac Sim-based platform (GRUtopia until its 2025 renaming) for general robots in city-scale interactive scenes: GRScenes with 100k annotated scenes in 89 categories, LLM-driven NPCs for social interaction, and GRBench tasks for loco-navigation, social navigation and loco-manipulation.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2407.10943) | [Website](https://internrobotics.github.io/user_guide/internutopia/) | [Code](https://github.com/InternRobotics/InternUtopia) ★1.3k | [Docs](https://internrobotics.github.io/user_guide/internutopia/)

- <a id="unrealzoo"></a>**UnrealZoo** (2024): Collection of 100+ photo-realistic Unreal Engine worlds with playable humans, animals, robots, vehicles and drones, exposed through UnrealCV and a Gym interface for navigation, tracking and multi-agent tasks. Version 3.1 adds MuJoCo-driven robots, LiDAR and 3DGS scenes.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2412.20977) (ICCV 2025) | [Website](https://unrealzoo.site/) | [Code](https://github.com/UnrealZoo/unrealzoo-gym) ★380 | [Docs](https://docs.unrealcv.org/en/latest/)

**Summary comparison**

| Simulator | Physics Engine | Renderer | GPU Support | OS | License |
|---|---|---|:---:|---|---|
| **[Habitat-Sim](#habitat-sim)** | Bullet | Magnum (OpenGL) | ✗ | Linux, macOS | MIT |
| [OmniGibson](#omnigibson) | PhysX 5 (Isaac Sim) | Omniverse RTX | ✗ | Linux, Windows | MIT (Isaac Sim licensed separately) |
| [InternUtopia](#internutopia-grutopia) | PhysX 5 (Isaac Sim 4.5) | Omniverse RTX | ✗ | Linux | MIT |
| [UnrealZoo](#unrealzoo) | Unreal Engine Chaos; MuJoCo for robot physics (v3.1) | Unreal Engine 5 | ✗ | Linux, Windows, macOS | Apache-2.0 |

### <a id="simulation-specialized"></a>Specialized Simulators

- <a id="airsim"></a>**AirSim** (2017): Microsoft's Unreal Engine simulator for drones and cars with PX4/ArduPilot software- and hardware-in-the-loop support, widely used for aerial autonomy and learning research. Microsoft stopped updating it; its successor Project AirSim is maintained by IAMAI, and community forks include Colosseum and Cosys-AirSim.<br>
  *Resources*: [Paper](https://arxiv.org/abs/1705.05065) (FSR 2017) | [Website](https://microsoft.github.io/AirSim/) | [Code](https://github.com/microsoft/AirSim) ★18.6k | [Docs](https://microsoft.github.io/AirSim/)

- <a id="gym-pybullet-drones"></a>**gym-pybullet-drones** (2021): Gymnasium environments for single- and multi-agent quadcopter control on PyBullet, with realistic collisions and aerodynamic effects such as downwash, PID and RL examples, and Betaflight SITL support. A common lightweight baseline for drone reinforcement learning.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2103.02142) (IROS 2021) | [Code](https://github.com/learnsyslab/gym-pybullet-drones) ★2.2k

- <a id="holoocean"></a>**HoloOcean** (2022): Underwater robotics simulator from BYU's Field Robotic Systems Lab on Unreal Engine, with imaging, profiling and sidescan sonar, DVL, IMU, camera and depth sensors, multi-agent support and ROS 2. HoloOcean 2.0 (2025) moved to Unreal Engine 5.3 with Fossen vehicle dynamics. The source repository needs an Epic-linked GitHub account.<br>
  *Resources*: [Paper](https://ieeexplore.ieee.org/document/9812353) (ICRA 2022) | [Website](https://byu-holoocean.github.io/holoocean-docs/) | [Docs](https://byu-holoocean.github.io/holoocean-docs/v2.4.0/index.html)

- <a id="aerial-gym-simulator"></a>**Aerial Gym Simulator** (2023): Highly parallel simulator for multirotors built on NVIDIA Isaac Gym: under-, fully- and over-actuated platforms with GPU geometric controllers and a custom Warp ray-casting renderer for depth, segmentation and lidar. Used to train state- and vision-based flight policies with demonstrated sim-to-real transfer.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2503.01471) (RA-L 2025) | [Website](https://ntnu-arl.github.io/aerial_gym_simulator/) | [Code](https://github.com/ntnu-arl/aerial_gym_simulator) ★781 | [Docs](https://ntnu-arl.github.io/aerial_gym_simulator/)

- <a id="orbit-surgical"></a>**ORBIT-Surgical** (2024): Surgical-robot simulation framework on Isaac Lab and Isaac Sim with 14 benchmark tasks for the da Vinci Research Kit (dVRK) and the STAR robot, GPU-parallel reinforcement and imitation learning, synthetic data generation, and demonstrated sim-to-real transfer to a physical dVRK.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2404.16027) (ICRA 2024) | [Website](https://orbit-surgical.github.io/) | [Code](https://github.com/orbit-surgical/orbit-surgical) ★186

- <a id="oceansim"></a>**OceanSim** (2025): Underwater perception simulator built as an NVIDIA Isaac Sim extension: physics-based underwater camera rendering and GPU-accelerated imaging sonar with real-time output, plus ROS 2 support, for synthetic data generation and testing of underwater perception algorithms.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2503.01074) (IROS 2025) | [Website](https://umfieldrobotics.github.io/OceanSim/) | [Code](https://github.com/umfieldrobotics/OceanSim) ★514

- <a id="carla-air"></a>**CARLA-Air** (2026) `new`: Runs CARLA urban driving and AirSim multirotor flight in a single Unreal Engine process, keeping both native Python APIs and ROS 2 interfaces, so cars, pedestrians and drones share one world, physics tick and sensor suite (up to 18 modalities). Aimed at air-ground cooperation research.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2603.28032) | [Website](https://carla-air.com/) | [Code](https://github.com/louiszengCN/CarlaAir) ★1.1k

**Summary comparison**

| Simulator | Physics Engine | Renderer | GPU Support | OS | License |
|---|---|---|:---:|---|---|
| [AirSim](#airsim) | Custom high-frequency vehicle physics inside Unreal Engine | Unreal Engine 4 (experimental Unity build) | ✗ | Linux, Windows, macOS | MIT |
| [gym-pybullet-drones](#gym-pybullet-drones) | PyBullet (Bullet) with added aerodynamic effects | PyBullet (OpenGL visualizer; TinyRenderer) | ✗ | Linux, macOS | MIT |
| [HoloOcean](#holoocean) | Unreal Engine 5 with Fossen-model vehicle dynamics | Unreal Engine 5.3 | ✗ | Linux, Windows | MIT (client code); Unreal Engine EULA |
| [Aerial Gym Simulator](#aerial-gym-simulator) | PhysX through Isaac Gym (GPU) | Isaac Gym cameras; custom NVIDIA Warp ray casting | ✓ | Linux | BSD-3-Clause |
| [ORBIT-Surgical](#orbit-surgical) | PhysX 5 (Isaac Lab) | Omniverse RTX | ✓ | Linux | BSD-3-Clause |
| [OceanSim](#oceansim) | PhysX 5 (Isaac Sim) | Omniverse RTX with custom underwater camera and sonar models | ✗ | Linux | BSD-3-Clause |
| [CARLA-Air](#carla-air) | Unreal Engine 4.26 (CARLA 0.9.16 vehicles, AirSim multirotor dynamics) | Unreal Engine 4.26 | ✗ | Linux, Windows | Custom non-commercial licence (README states MIT for CARLA-Air code) |

<p align="right"><a href="#contents">Back to contents ↑</a></p>

---

## <a id="hri"></a>Human-Robot Interaction

Assistive robots, handovers, and collaboration between people and robots. **11 entries.**

**Sub-areas:** [Assistive & Physical HRI](#hri-assistive) (4) · [Handover](#hri-handover) (3) · [Human-Robot Collaboration](#hri-collaboration) (4)

### <a id="hri-assistive"></a>Assistive & Physical HRI

- <a id="assistive-gym"></a>**Assistive Gym** (2019) `Sim` `widely used`: Physics-based assistive robotics framework with human models and six activities of daily living (itch scratching, bed bathing, feeding, drinking, dressing, arm manipulation). The human is static or actively cooperating, and policies are compared across four commercial robots.<br>
  *Resources*: [Paper](https://arxiv.org/abs/1910.04700) (ICRA 2020) | [Code](https://github.com/Healthcare-Robotics/assistive-gym) ★414

- <a id="rcareworld"></a>**RCareWorld** (2022) `Sim`: Unity-based simulation world for physical and social caregiving robots, with SMPL-X care-recipient avatars that model mobility limitations, accessible home scenes and assistive devices. Proposes six caregiving benchmark tasks and was the platform of the 2024-25 PhyRC caregiving challenge.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2210.10821) (IROS 2022) | [Website](https://emprise.cs.cornell.edu/rcareworld/) | [Code](https://github.com/empriselab/RCareWorld) ★133

- <a id="assistax"></a>**Assistax** (2025) `Sim`: GPU-accelerated assistive-robotics benchmark in JAX and MuJoCo MJX where a robot arm and an active simulated human are trained together with multi-agent RL. Tests ad-hoc teamwork with held-out human policies that differ in disability and preference.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2507.21638) (RLC 2026) | [Website](https://leohinckeldey.dev/assistax-project/) | [Code](https://github.com/assistive-autonomy/assistax) ★28 | [Data](https://huggingface.co/datasets/leohink/assistax-zoo)

- <a id="openrobocare"></a>**OpenRoboCare** (2025) `Real` `new`: Multimodal real-world dataset of expert caregiving: 21 occupational therapists perform 15 activities-of-daily-living tasks (bathing, dressing, transfers, toileting, grooming) on two manikins, recorded with RGB-D, motion capture, eye gaze, tactile skin and annotations. Used to test pose estimation and task recognition for assistive robots.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2511.13707) (IROS 2025) | [Website](https://emprise.cs.cornell.edu/robo-care/) | [Data](https://registry.opendata.aws/open-robo-care/)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| **[Assistive Gym](#assistive-gym)** | physical assistance | 6 | 2 | 4 (PR2, Jaco, Baxter, Sawyer) | proprioceptive, force-torque, state | PyBullet | - | N/A |
| [RCareWorld](#rcareworld) | caregiving simulation | 6 | 1 (task success rate) | 10 | RGB, depth, force-torque, proprioceptive | Unity (interfaces with several physics engines) | - | N/A |
| [Assistax](#assistax) | multi-agent RL, ad-hoc teamwork | 5 in paper | 3 | 1 plus a simulated humanoid partner | proprioceptive, force-torque, state | MuJoCo MJX (Brax, JAX) | - | No trajectories; zoo of pre-trained humanoid partner policies |
| [OpenRoboCare](#openrobocare) | caregiving dataset | 15 ADL tasks | 2 | N/A (human caregivers on manikins) | RGB, depth, mocap, tactile, eye gaze | Real world | Human demos | 315 sessions, 19.8 hours, 31,185 samples from 21 therapists |

### <a id="hri-handover"></a>Handover

- <a id="handoversim"></a>**HandoverSim** (2022) `Sim`: Simulation benchmark for human-to-robot object handover: a simulated hand replays motion-captured grasps from DexYCB and a Franka Panda must take the object without touching the hand. Standard splits test unseen subjects, handedness and objects.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2205.09747) (ICRA 2022) | [Website](https://handover-sim.github.io) | [Code](https://github.com/NVlabs/handover-sim) ★126

- <a id="hoh"></a>**HOH** (2023) `Real`: Markerless multimodal dataset of 2,720 human-to-human object handovers with 136 objects and 40 participants, captured with multi-view RGB-D and annotated with segmentations, grasp type, handedness and comfort ratings. Intended for learning grasp, orientation and trajectory prediction for robot handover.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2310.00723) (NeurIPS 2023 D&B) | [Website](https://tars-home.github.io/hohdataset/)

- <a id="genh2r"></a>**GenH2R** (2024) `Sim`: Framework and simulator (GenH2R-Sim) for learning human-to-robot handover at scale: about one million procedurally generated handover scenes over 3,266 ShapeNet objects with synthetic hand grasps and trajectories, plus test sets built from HandoverSim and HOI4D.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2401.00929) (CVPR 2024) | [Website](https://genh2r.github.io/) | [Code](https://github.com/chenjy2003/genh2r) ★51

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| [HandoverSim](#handoversim) | human-to-robot handover | 1,000 handover scenes | 3 | 1 (Franka Panda) | pointcloud, state | PyBullet | Human demos | 1,000 motion-captured handover sequences from DexYCB |
| [HOH](#hoh) | human-human handover dataset | 3 demo tasks | N/A | N/A (human-human data) | RGB, depth, pointcloud, segmentation | Real world | Human demos | 2,720 handovers, 136 objects, 40 participants (20 pairs) |
| [GenH2R](#genh2r) | human-to-robot handover | ~1M training scenes | 3 | 1 (Franka Panda) | pointcloud, depth | PyBullet (built on HandoverSim) | Planner | ~1M automatically generated demonstrations |

### <a id="hri-collaboration"></a>Human-Robot Collaboration

- <a id="overcooked-ai"></a>**Overcooked-AI** (2019) `Sim` `widely used`: Two-player cooperative cooking gridworld based on the game Overcooked, in which agents must split sub-tasks on the fly to deliver soups. The standard testbed for human-AI and zero-shot coordination, evaluated with human proxy models and real human partners.<br>
  *Resources*: [Paper](https://arxiv.org/abs/1910.05789) (NeurIPS 2019) | [Website](https://bair.berkeley.edu/blog/2019/10/21/coordination/) | [Code](https://github.com/HumanCompatibleAI/overcooked_ai) ★1k

- <a id="watch-and-help"></a>**Watch-And-Help** (2020) `Sim`: Challenge for social intelligence in the VirtualHome-Social simulator: an AI agent watches one demonstration of a human-like agent doing a household task, infers the goal, then helps complete it faster in a new apartment. Evaluated with a planner-based human model and with real humans.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2010.09890) (ICLR 2021) | [Code](https://github.com/xavierpuigf/watch_and_help) ★110

- <a id="chaic"></a>**CHAIC** (2024) `Sim`: Constrained Human-AI Cooperation challenge in ThreeDWorld: a helper with egocentric RGB-D must infer the goals and physical limits of a human partner (child, wheelchair user, cyclist, frail person) and help with long-horizon indoor and outdoor transport tasks.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2411.01796) (NeurIPS 2024 D&B) | [Website](https://umass-embodied-agi.github.io/CHAIC/) | [Code](https://github.com/UMass-Embodied-AGI/CHAIC) ★27

- <a id="habit"></a>**HABIT** (2026) `Real` `new`: Real-robot demonstration dataset recorded with a person in the workspace: a bimanual Franka setup acts as collaborator, coworker or supervised robot across 60 tasks. Policies trained on it are scored on manipulation, workflow compliance and human safety.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2606.31682) (NeurIPS 2026 E&D (oral)) | [Website](https://habit-dataset.github.io) | [Code](https://github.com/HABIT-dataset/HABIT-policy-training) ★25 | [Data](https://huggingface.co/datasets/configinc/HABIT)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| **[Overcooked-AI](#overcooked-ai)** | human-AI coordination | 5 standard layouts | 1 | N/A (gridworld agents) | state | custom 2D gridworld | Human demos | Human-human gameplay, about 16 trajectories per layout; human-AI study data |
| [Watch-And-Help](#watch-and-help) | social perception, household assistance | 5 household activity types | 3 | N/A (humanoid avatars) | state, RGB, depth, segmentation | VirtualHome-Social | Planner | Planner-generated Watch demonstrations in 5 training apartments |
| [CHAIC](#chaic) | embodied social intelligence | 8 tasks, 4 constrained human agents, 12 test episodes per task | 4 | N/A (simulated helper avatar) | RGB, depth, state | ThreeDWorld (TDW) | - | N/A |
| [HABIT](#habit) | human-present robot dataset, bimanual | 60 | 1 | 1 | RGB, proprioceptive | Real world | Human demos | 10,563 episodes, 164 hours |

<p align="right"><a href="#contents">Back to contents ↑</a></p>

---

## <a id="safety"></a>Safety

Safe reinforcement learning and control, and the safety of LLM- and VLA-driven robots. **16 entries.**

**Sub-areas:** [Safe RL & Control](#safety-safe-rl) (6) · [Safety of LLM / VLA Agents](#safety-embodied-safety) (10)

### <a id="safety-safe-rl"></a>Safe RL & Control

- <a id="safety-gym"></a>**Safety Gym** (2019) `Sim` `widely used`: Constrained-RL benchmark with hazard/constraint costs across goal, button and push tasks and three robots. The original safe-exploration suite from OpenAI; the repository is archived and Safety-Gymnasium is its maintained successor.<br>
  *Resources*: [Paper](https://cdn.openai.com/safexp-short.pdf) (OpenAI preprint 2019) | [Website](https://openai.com/index/safety-gym/) | [Code](https://github.com/openai/safety-gym) ★602

- <a id="safe-control-gym"></a>**safe-control-gym** (2021) `Sim`: Unified safe learning-based control suite with constraints and disturbances on cart-pole and quadrotor systems. Extends the Gym API with symbolic (CasADi) prior dynamics and constraint specification so that control-theoretic and RL methods can be compared on safety and robustness.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2109.06325) (IEEE RA-L 2022) | [Website](https://www.dynsyslab.org/safe-robot-learning/) | [Code](https://github.com/learnsyslab/safe-control-gym) ★937

- <a id="dsrl-datasets-for-offline-safe-rl"></a>**DSRL (Datasets for Offline Safe RL)** (2023) `Sim`: Datasets for offline safe RL with a D4RL-style API: 38 tasks from Safety-Gymnasium, Bullet-Safety-Gym and MetaDrive with reward and cost labels, filters that change data density and noise, and companion baseline implementations (OSRL).<br>
  *Resources*: [Paper](https://arxiv.org/abs/2306.09303) (DMLR 2024) | [Website](https://www.offline-saferl.org/) | [Code](https://github.com/liuzuxin/DSRL) ★141

- <a id="safety-gymnasium"></a>**Safety-Gymnasium** (2023) `Sim` `widely used`: Unified safe-RL environment suite on MuJoCo with the Gymnasium API: Safety Gym-style navigation, velocity-constrained locomotion, multi-agent and vision tasks, plus Isaac Gym manipulation. Ships with the SafePO library of 16 constrained-RL algorithms and is the maintained successor to Safety Gym.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2310.12567) (NeurIPS 2023 D&B) | [Website](https://safety-gymnasium.readthedocs.io/en/latest/) | [Code](https://github.com/PKU-Alignment/safety-gymnasium) ★602

- <a id="robust-gymnasium"></a>**Robust-Gymnasium** (2025) `Sim`: Modular benchmark for robust RL that wraps over sixty control, manipulation, dexterous-hand, humanoid, safe-RL and multi-agent tasks and injects disturbances into observations, actions, rewards or dynamics, in random, adversarial or LLM-generated form.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2502.19652) (ICLR 2025) | [Website](https://robust-gym.github.io/) | [Code](https://github.com/SAIL-Research-Lab/Robust-Gymnasium) ★106

- <a id="crax"></a>**CRAX** (2026) `Sim` `new`: Hardware-accelerated safe-RL benchmark on MuJoCo MJX in JAX: eight constrained tasks at three difficulty levels with vector or pixel observations, reported as up to 200x faster to train on than CPU-based safety suites.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2606.20376) | [Website](https://ttomilin.github.io/CRAX/) | [Code](https://github.com/TTomilin/CRAX) ★19

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| **[Safety Gym](#safety-gym)** | constrained RL, safe exploration | 18, plus 9 unconstrained | 3 | 3 (Point, Car, Doggo) | lidar, proprioceptive | MuJoCo (mujoco-py) | - | N/A |
| [safe-control-gym](#safe-control-gym) | safe learning-based control, robustness | 2 on 3 systems | 3 | 3 | state | PyBullet | - | N/A |
| [DSRL](#dsrl-datasets-for-offline-safe-rl) | offline safe RL datasets | 38 datasets | 2 | N/A (agents of the three source suites) | state | MuJoCo, PyBullet, MetaDrive | RL policy | 38 offline datasets with reward and cost labels |
| **[Safety-Gymnasium](#safety-gymnasium)** | constrained RL, single- and multi-agent | 54 environments benchmarked in the paper | 2 | 10+ | state, lidar, RGB, depth | MuJoCo; Isaac Gym for the manipulation tasks | - | N/A |
| [Robust-Gymnasium](#robust-gymnasium) | robust RL, disturbances | 60+ task bases from 11 suites | 1 | Many | state, RGB | MuJoCo, Box2D, robosuite | - | N/A |
| [CRAX](#crax) | GPU-accelerated constrained RL | 8 tasks x 3 difficulty levels | 2 | 8 | state, lidar, RGB | MuJoCo MJX (JAX) | - | N/A |

### <a id="safety-embodied-safety"></a>Safety of LLM / VLA Agents

- <a id="badrobot"></a>**BadRobot** (2024) `Sim + Real`: Jailbreak study of embodied LLM agents that ships a benchmark of malicious physical-action requests in seven categories (physical harm, privacy, fraud, sabotage and others) and three attack types. Evaluated on Code as Policies, VoxPoser, ProgPrompt and VisProg and on real robot arms.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2407.20242) (ICLR 2025) | [Website](https://embodied-llms-safety.github.io) | [Code](https://github.com/Rookie143/BadRobot) ★50 | [Data](https://huggingface.co/datasets/Hangtao/badrobot-malicious-queries)

- <a id="llm-physical-safety-benchmark"></a>**LLM Physical Safety Benchmark** (2024) `Sim`: Benchmark for the physical safety of LLMs that write drone-control code: about 400 instructions covering deliberate attacks, unintentional attacks, regulation violations and benign utility tasks. Responses are scored by two LLM judges and generated code is run in AirSim to detect collisions.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2411.02317) (Communications of the ACM 2026) | [Website](https://huggingface.co/spaces/TrustSafeAI/LLM-physical-safety) | [Data](https://huggingface.co/datasets/TrustSafeAI/llm_physical_safety_benchmark)

- <a id="safeagentbench"></a>**SafeAgentBench** (2024) `Sim`: Benchmark for safety-aware task planning of embodied LLM agents in AI2-THOR: 750 executable tasks (450 hazardous, 300 safe) covering 10 hazard types as detailed, abstract and long-horizon instructions. Measures whether agents refuse or carry out hazardous tasks.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2412.13178) | [Website](https://safeagentbench.github.io) | [Code](https://github.com/shengyin1224/SafeAgentBench) ★80 | [Data](https://huggingface.co/datasets/safeagentbench/SafeAgentBench)

- <a id="safety-chores"></a>**Safety-CHORES** (2025) `Sim`: Safety benchmark for vision-language-action policies released with SafeVLA: long-horizon navigation, pick-up and fetch tasks in procedurally generated ProcTHOR houses, with costs for safety-critical cases such as corners, blind spots, fragile collections, critical points and dangerous equipment.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2503.03480) (NeurIPS 2025) | [Website](https://pku-safevla.github.io/) | [Code](https://github.com/PKU-Alignment/SafeVLA) ★167 | [Data](https://huggingface.co/datasets/SafetyEmbodiedAI/safety-chores)

- <a id="asimov"></a>**ASIMOV** (2025) `Real`: Google DeepMind datasets for the semantic safety of foundation models used as robot brains: undesirable situations generated from real robot images (RoboVQA), hospital injury reports (NEISS) and dilemmas, scored by agreement with human labels. ASIMOV-2.0 (September 2025) adds injury-risk reasoning, risk perception in video and embodiment constraints.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2503.08663) (CoRL 2025) | [Website](https://asimov-benchmark.github.io/v1/) | [Code](https://github.com/asimov-benchmark/code) ★27 | [Data](https://github.com/asimov-benchmark/code/blob/main/ASIMOV_Datasets.ipynb)

- <a id="is-bench"></a>**IS-Bench** (2025) `Sim`: Multimodal benchmark for the interactive safety of VLM-driven household agents in OmniGibson: 161 scenarios with 388 safety risks built on BEHAVIOR-1K scenes. A process-oriented evaluation checks that risk-mitigation steps happen before or after the risky action, not only the final state.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2506.16402) (AAAI 2026) | [Website](https://ursulalujun.github.io/isbench.github.io/) | [Code](https://github.com/AI45Lab/IS-Bench) ★57 | [Data](https://huggingface.co/datasets/Ursulalala/IS_Bench_dataset)

- <a id="robojailbench"></a>**RoboJailBench** (2026) `Real` `new`: Standardized evaluation of jailbreak attacks and defenses for embodied VLMs: an 18-category security taxonomy derived from ISO standards, regulations and incidents, paired adversarial and benign goals over robot and driving scenes, and a leaderboard that tracks both security and benign-task utility.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2605.19328) | [Website](https://purseclab.github.io/benchmark-for-robotics-security/) | [Code](https://github.com/purseclab/benchmark-for-robotics-security) ★3 | [Leaderboard](https://purseclab.github.io/benchmark-for-robotics-security/)

- <a id="touchsafebench"></a>**TouchSafeBench** (2026) `Sim` `new`: Physics-grounded benchmark of collision grounding for VLMs used as safety monitors in human-robot collaboration: 2,940 simulated indoor co-presence episodes from social navigation and social rearrangement in Habitat 3.0, with multi-view RGB-D and simulator contact labels. Models classify the current safety state and warn of imminent collisions.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2605.31196) (CoRL 2026) | [Website](https://jun25336-bit.github.io/TouchSafeBench/) | [Code](https://github.com/jun25336-bit/TouchSafeBench) ★0 | [Data](https://huggingface.co/datasets/face12345/TouchSafeBench)

- <a id="libero-safety"></a>**LIBERO-Safety** (2026) `Sim` `new`: Safety benchmark for vision-language-action models built on LIBERO: five suites (affordance-aware grasping, human-robot interaction, tabletop avoidance, free-space hand-object avoidance, semantic safety reasoning) at three difficulty levels, with procedurally randomized scenes and collision-free planner demonstrations.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2606.23686) (ECCV 2026) | [Website](https://libero-safety.github.io/) | [Code](https://github.com/LIBERO-SAFETY/LIBERO-Safety) ★74 | [Data](https://huggingface.co/datasets/LIBERO-Safety/libero_safety)

- <a id="maniguard"></a>**ManiGuard** (2026) `Sim + Real` `new`: Specification-grounded safety benchmark for foundation-model manipulation policies: 200 contact-rich household base tasks in six families (clutter, lid, cabinet, jar, stack, dusty), each run in-distribution and under four shifts. Every rollout is checked by LTLf automaton monitors, in simulation and on a real Franka.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2608.17386) | [Website](https://nu-ideas-lab.github.io/ManiGuard/) | [Code](https://github.com/NU-IDEAS-Lab/ManiGuard) ★5 | [Data](https://huggingface.co/collections/IDEAS-Lab-Northwestern/maniguard-benchmark-and-datasets)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| [BadRobot](#badrobot) | jailbreak, malicious instructions | 277 malicious queries in the paper | 2 | 2 real arms plus simulated agents | language, RGB | PyBullet, RLBench, VirtualHome (through the attacked systems) + real | Not stated | Malicious queries and ready-made jailbreak prompts |
| [LLM Physical Safety Benchmark](#llm-physical-safety-benchmark) | LLM drone control, physical harm | 408 instructions | 6 | 1 (simulated drone) | language | AirSim (Unreal Engine) | Mixed | 408 text instructions |
| [SafeAgentBench](#safeagentbench) | LLM task planning | 750 (450 hazardous, 300 safe) | 4 | 1 | RGB, language, state | AI2-THOR | Mixed | 750 task instructions with reference plans |
| [Safety-CHORES](#safety-chores) | VLA safety, mobile manipulation | 3 | 2 | 1 (simulated mobile manipulator) | RGB, proprioceptive, language | AI2-THOR (ProcTHOR houses, Objaverse assets) | - | Task definition files for the three task types |
| [ASIMOV](#asimov) | semantic safety, robot constitutions | 5 datasets | 2 | N/A (image and text questions) | RGB, language | Real world | Mixed | Validation: 310 contexts, 2,273 actions; all splits: 513,679 contexts |
| [IS-Bench](#is-bench) | interactive safety, household tasks | 161 scenarios with 388 safety risks | 4 | N/A (agent with 18 primitive skills) | RGB, language | OmniGibson (BEHAVIOR-1K) | Mixed | 161 scenarios with human-verified reference plans |
| [RoboJailBench](#robojailbench) | jailbreak attacks and defenses | 990 paired instructions, 1,408 scene images, 18 security categories | 4 | N/A | RGB, language | Real world | Mixed | New 90-scene set plus augmented DROID, RH20T, RoboVQA, Robo2VLM, PhysicalAI-AV |
| [TouchSafeBench](#touchsafebench) | VLM safety monitors | 2 | 2 | 1 (mobile manipulator in Habitat 3.0) | RGB, depth | Habitat 3.0 | Mixed | 2,940 episodes with multi-view RGB-D and contact labels |
| [LIBERO-Safety](#libero-safety) | VLA safety, physical and semantic | 75 | 5 | 1 (Franka Panda, as in LIBERO) | RGB, proprioceptive, language | LIBERO (robosuite / MuJoCo) | Planner | 19,664 collision-free demonstrations over 40 tasks |
| [ManiGuard](#maniguard) | manipulation safety | 200 base tasks in 6 families | 4 | 1 (Franka Panda, simulated and real) | RGB, proprioceptive, language | OmniGibson / Isaac Sim (BEHAVIOR-1K) + real | Mixed | 8,000 safety-annotated demonstrations (40 per base task) |

<p align="right"><a href="#contents">Back to contents ↑</a></p>

---

## <a id="autonomous-driving"></a>Autonomous Driving

The driving benchmarks that robotics work most often borrows from. Kept short on purpose. **11 entries.**

**Sub-areas:** [Datasets & Open-Loop Benchmarks](#autonomous-driving-driving-data) (7) · [Closed-Loop Simulation](#autonomous-driving-driving-closed-loop) (4)

### <a id="autonomous-driving-driving-data"></a>Datasets & Open-Loop Benchmarks

- <a id="kitti"></a>**KITTI** (2012) `Real` `widely used`: Driving benchmark suite recorded around Karlsruhe from a station wagon with stereo cameras, a Velodyne lidar and GPS/IMU. Its online leaderboards for stereo, optical flow, depth, odometry, 3D object detection and tracking are a long-standing reference for perception and SLAM.<br>
  *Resources*: [Paper](https://www.cvlibs.net/publications/Geiger2012CVPR.pdf) (CVPR 2012) | [Website](https://www.cvlibs.net/datasets/kitti/) | [Data](https://www.cvlibs.net/datasets/kitti/raw_data.php) | [Leaderboard](https://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark=3d)

- <a id="nuscenes"></a>**nuScenes** (2019) `Real` `widely used`: Multimodal driving dataset of 1,000 20-second scenes from Boston and Singapore with the full sensor suite (6 cameras, 1 lidar, 5 radars) and 3D boxes for 23 classes. Standard benchmark for 3D detection, tracking, prediction and lidar segmentation, and widely reused for open-loop planning.<br>
  *Resources*: [Paper](https://arxiv.org/abs/1903.11027) (CVPR 2020) | [Website](https://www.nuscenes.org/nuscenes) | [Code](https://github.com/nutonomy/nuscenes-devkit) ★2.8k | [Data](https://www.nuscenes.org/download) | [Leaderboard](https://www.nuscenes.org/object-detection)

- <a id="waymo-open-dataset"></a>**Waymo Open Dataset** (2019) `Real` `widely used`: Waymo's public data in three parts: Perception (lidar and camera with 2D/3D labels), Motion (103,354 scenes with object tracks and maps) and, since 2025, End-to-End Driving (4,021 long-tail segments scored by rater feedback). Leaderboards for motion prediction, sim agents and end-to-end driving remain open.<br>
  *Resources*: [Paper](https://arxiv.org/abs/1912.04838) (CVPR 2020) | [Website](https://waymo.com/open/) | [Code](https://github.com/waymo-research/waymo-open-dataset) ★3.4k | [Data](https://waymo.com/open/download/) | [Leaderboard](https://waymo.com/open/challenges/)

- <a id="argoverse-2"></a>**Argoverse 2** (2021) `Real`: Four datasets from six US cities, all with HD maps: 1,000 annotated multi-sensor sequences, 20,000 unlabeled lidar sequences, 250,000 motion-forecasting scenarios and 1,000 map-change scenarios. Its CVPR challenges continue, in 2026 on scenario mining and lidar scene flow.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2301.00493) (NeurIPS 2021 D&B) | [Website](https://www.argoverse.org/av2.html) | [Code](https://github.com/argoverse/av2-api) ★419 | [Leaderboard](https://www.argoverse.org/tasks.html)

- <a id="drivelm"></a>**DriveLM** (2023) `Sim + Real`: Graph visual question answering for driving: perception, prediction and planning questions about key objects are linked by logical dependencies. DriveLM-nuScenes has 4,871 annotated frames with about 91 QA pairs each; DriveLM-CARLA is generated by a rule-based expert. Basis of the CVPR 2024 Driving-with-Language challenge.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2312.14150) (ECCV 2024) | [Website](https://opendrivelab.com/DriveLM/) | [Code](https://github.com/OpenDriveLab/DriveLM) ★1.4k | [Data](https://huggingface.co/datasets/OpenDriveLab/DriveLM) | [Leaderboard](https://huggingface.co/spaces/AGC2024/driving-with-language-official)

- <a id="navsim"></a>**NAVSIM** (2024) `Sim + Real`: Benchmark for sensor-based driving policies on real nuPlan/OpenScene logs: each planned trajectory is unrolled in a non-reactive bird's-eye-view simulation and scored with the PDM Score. NAVSIM v2 (2025) adds pseudo-simulation with 3D Gaussian Splatting views and the extended EPDMS; public leaderboards cover navtest and navhard.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2406.15349) (NeurIPS 2024 D&B) | [Code](https://github.com/autonomousvision/navsim) ★1.1k | [Leaderboard](https://huggingface.co/spaces/AGC2025/e2e-driving-navhard)

- <a id="nureasoning"></a>**nuReasoning** (2026) `Real` `new`: Motional and UCLA's reasoning-centric driving dataset in the nuScenes/nuPlan lineage: 20,000 long-tail 20-second clips (105 h) with 8 cameras, lidar, HD maps and human-verified spatial, decision and counterfactual reasoning annotations. Its 2026 challenge scores planning and multiple-choice reasoning on a private test set.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2605.31572) (NeurIPS 2026 E&D) | [Website](https://nureasoning.github.io/) | [Code](https://github.com/nureasoning/nureasoning-devkit) ★27 | [Data](https://huggingface.co/datasets/nureasoning/nuReasoning) | [Leaderboard](https://huggingface.co/spaces/nureasoning/nureasoning-challenge-2026)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| **[KITTI](#kitti)** | perception, odometry | 9 families, incl. stereo, flow, depth, odometry, object detection, tracking | Task-specific | 1 | RGB, lidar, GPS_IMU | Real world | Human labels | 7,481 training and 7,518 test frames for object detection; 22 stereo sequences for odometry |
| **[nuScenes](#nuscenes)** | 3D perception, prediction | 5 leaderboards | Task-specific | 1 | RGB, lidar, radar, GPS_IMU | Real world | Human labels | 1,000 scenes of 20 s (about 15 h); 1.4M camera images and 1.4M 3D boxes on 40k keyframes |
| **[Waymo Open Dataset](#waymo-open-dataset)** | perception, motion forecasting | 17 challenge tasks since 2020 | Task-specific | 1 | RGB, lidar | Real world | Human labels | Perception: 1,150 scenes of 20 s (v1 paper); Motion: 103,354 scenes; End-to-End: 4,021 segments |
| [Argoverse 2](#argoverse-2) | 3D perception, motion forecasting | 6 | Task-specific | 1 | RGB, lidar | Real world | Human labels | 1,000 sensor, 20,000 lidar and 1,000 map-change sequences; 250,000 motion scenarios |
| [DriveLM](#drivelm) | driving VQA, vision-language | 1 | 4 in the challenge | 1, plus the CARLA ego vehicle | RGB, language | CARLA (DriveLM-CARLA split) + real | Mixed | DriveLM-nuScenes: 4,871 frames (avg. 91.4 QAs each); DriveLM-CARLA: 64,285 frames (avg. 24.4) |
| [NAVSIM](#navsim) | end-to-end planning | 2 public test splits | PDMS in v1 | 1 | RGB, lidar, state | Non-reactive BEV simulation on real logs (3DGS views in v2) + real | Human demos | navtrain 103k samples, navtest 12k samples, drawn from 120 h of OpenScene (nuPlan at 2 Hz) |
| [nuReasoning](#nureasoning) | long-tail reasoning, planning | 2 | 2 | 1 (vehicle with 8 cameras and lidar) | RGB, lidar, language, state | Real world | Mixed | 20,000 clips of 20 s at 10 Hz (105 h): 17K train, 2K validation, 1K private test |

### <a id="autonomous-driving-driving-closed-loop"></a>Closed-Loop Simulation

- <a id="carla"></a>**CARLA** (2017) `Sim` `widely used`: Open-source driving simulator on Unreal Engine with configurable sensors, weather and traffic; CARLA 1.0 (November 2026) runs on UE 5.8. Its Autonomous Driving Leaderboard, long the standard closed-loop test, is now permanently closed; routes and metrics remain for local evaluation.<br>
  *Resources*: [Paper](https://arxiv.org/abs/1711.03938) (CoRL 2017) | [Website](https://carla.org/) | [Code](https://github.com/carla-simulator/carla) ★14.7k | [Leaderboard](https://leaderboard.carla.org/)

- <a id="nuplan"></a>**nuPlan** (2021) `Sim + Real`: Planning benchmark built on more than 1,200 hours of human driving in Boston, Pittsburgh, Las Vegas and Singapore, with a lightweight simulator, reactive agents and planning metrics. Planners are scored open-loop and in non-reactive and reactive closed-loop simulation; the challenge server closed in November 2025.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2106.11810) | [Website](https://www.nuplan.org/) | [Code](https://github.com/motional/nuplan-devkit) ★1.1k | [Data](https://www.nuscenes.org/nuplan)

- <a id="bench2drive"></a>**Bench2Drive** (2024) `Sim`: Closed-loop benchmark for end-to-end driving in CARLA: 220 routes covering 44 interactive scenarios, 23 weathers and 12 towns, with results split by five driving abilities. Training data come from the Think2Drive RL expert; VL, Speed and Robust variants and the v0.0.4 data followed in 2025-2026.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2406.03877) (NeurIPS 2024 D&B) | [Website](https://thinklab-sjtu.github.io/Bench2Drive/) | [Code](https://github.com/Thinklab-SJTU/Bench2Drive) ★2k | [Data](https://huggingface.co/datasets/rethinklab/Bench2Drive)

- <a id="alpasim"></a>**AlpaSim** (2025) `Sim`: NVIDIA's open-source closed-loop simulator for end-to-end driving policies, replaying real drives as neural reconstructions (NuRec) with a pluggable renderer. The 2026 AlpaSim End-to-End Closed-Loop Challenge scores submitted driver containers on private scenes in two tracks, Physical AI AV and nuPlan.<br>
  *Resources*: [Website](https://opendrivelab.com/alpasim2026) | [Code](https://github.com/NVlabs/alpasim) ★1.3k | [Data](https://huggingface.co/datasets/nvidia/PhysicalAI-Autonomous-Vehicles-NuRec) | [Leaderboard](https://huggingface.co/spaces/nvidia/AlpasimE2EClosedLoopChallenge2026)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| **[CARLA](#carla)** | driving simulator | 2 leaderboard tracks | 3 | 1 | RGB, depth, segmentation, lidar, radar, GPS_IMU | CARLA (Unreal Engine 5.8 in 1.0; Unreal Engine 4.26 in 0.9.x) | - | N/A |
| [nuPlan](#nuplan) | closed-loop planning on real logs | 3 challenges | 3 overall scores, one per challenge, aggregated from planning metrics | 1 | state, RGB, lidar | nuPlan simulator (replay of real logs with optional reactive agents) + real | Human demos | More than 1,200 h of driving logs with auto-labelled tracks; 120 h with raw sensor data |
| [Bench2Drive](#bench2drive) | closed-loop end-to-end driving | 220 routes over 44 interactive scenarios | 4 plus 5 ability scores | 1 | RGB, depth, lidar, radar, GPS_IMU | CARLA 0.9.15 (Leaderboard 2.0 scenarios) | RL policy | 13,638 clips (about 2M annotated frames); v0.0.4 adds 1,100 scenario-uniform routes |
| [AlpaSim](#alpasim) | neural-reconstruction simulator | 2 challenge tracks | 2 | 1 | RGB, state | AlpaSim (NuRec neural reconstructions; MTGS rendering on the nuPlan track) | Not stated | 2,523 public reconstructed 20 s clips; challenge split of 1,761 train and 441 validation scenes |

<p align="right"><a href="#contents">Back to contents ↑</a></p>

---

## <a id="other"></a>Other Areas

Smaller areas that sit next to the domains above. **16 entries.**

**Sub-areas:** [Offline RL & Data-Driven Control](#other-offline-rl) (4) · [Aerial Robotics](#other-aerial) (3) · [Multi-Robot](#other-multi-robot) (4) · [Competitions](#other-competition) (5)

### <a id="other-offline-rl"></a>Offline RL & Data-Driven Control

- <a id="d4rl"></a>**D4RL** (2020) `Sim` `widely used`: Offline RL benchmark with fixed datasets and an evaluation protocol across seven simulated domains (Maze2D, AntMaze, Gym-MuJoCo locomotion, Adroit hand, Franka Kitchen, Flow, CARLA), scored by normalized return. Still the default offline RL testbed; development has moved to Minari, which now hosts its datasets.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2004.07219) | [Website](https://sites.google.com/view/d4rl/home) | [Code](https://github.com/Farama-Foundation/D4RL) ★1.7k | [Data](https://github.com/Farama-Foundation/D4RL/wiki/Tasks)

- <a id="minari"></a>**Minari** (2022) `Sim`: Farama Foundation's standard format, API and hosting for offline RL datasets, and the maintained successor to D4RL. Its reference collections re-create the D4RL robot tasks (AntMaze, PointMaze, Adroit hand, Franka Kitchen) on current Gymnasium environments and add MuJoCo, Atari and MiniGrid sets.<br>
  *Resources*: [Website](https://minari.farama.org/) | [Code](https://github.com/Farama-Foundation/Minari) ★1.7k | [Data](https://huggingface.co/farama-minari)

- <a id="d5rl"></a>**D5RL** (2024) `Sim`: Offline RL benchmark built on realistic simulations of real robot systems: Unitree A1 legged locomotion, image-based Franka Kitchen (standard and randomized) and WidowX bin sorting. Data mix scripted policies and human-teleoperated play, and tasks are evaluated both offline and after online fine-tuning.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2408.08441) (RLC 2024) | [Website](https://sites.google.com/view/d5rl/) | [Code](https://github.com/d5rlbenchmark/d5rl) ★32

- <a id="ogbench"></a>**OGBench** (2024) `Sim`: Benchmark for offline goal-conditioned RL with 8 environment types (maze navigation with point, Ant and humanoid agents, Ant soccer, UR5e cube, scene and puzzle manipulation, and drawing) and 85 datasets, in state and pixel versions. Single-task variants give 410 standard offline RL tasks.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2410.20092) (ICLR 2025) | [Website](https://seohong.me/projects/ogbench/) | [Code](https://github.com/seohongpark/ogbench) ★523

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| **[D4RL](#d4rl)** | offline RL datasets | 7 domains | 1 | Several | state, RGB | MuJoCo; also CARLA, Flow (SUMO), MiniGrid and PyBullet variants | Mixed | One fixed dataset per task, in variants such as random, medium, expert, human and play |
| [Minari](#minari) | offline RL dataset standard | 6 hosted collections with about 340 datasets | 1 | Several | state, RGB | MuJoCo via Gymnasium and Gymnasium-Robotics; Atari and MiniGrid | Mixed | About 340 datasets (D4RL 31, MuJoCo 28, Atari 57, MiniGrid 170, community 52, web agents 1) |
| [D5RL](#d5rl) | offline RL | 4 | Task return or success, offline and after online fine-tuning | 3 (Unitree A1, Franka arm, WidowX) | RGB, proprioceptive | MuJoCo and PyBullet | Mixed | Per-domain datasets, including over 20 h of teleoperated play for Randomized Kitchen |
| [OGBench](#ogbench) | offline goal-conditioned RL | 8 environment types, 85 datasets | 1 | 4 | state, RGB | MuJoCo | Mixed | 85 datasets (navigate, stitch, explore, play and noisy types) |

### <a id="other-aerial"></a>Aerial Robotics

- <a id="uzh-fpv-drone-racing-dataset"></a>**UZH-FPV Drone Racing Dataset** (2019) `Real`: Visual-inertial dataset of aggressive first-person-view quadrotor flights by an expert pilot, indoors and outdoors, with frame cameras, an event camera, IMU and laser-tracker ground truth. A leaderboard on sequences with withheld ground truth ranks state estimators; race-track sequences added in 2023 reach 100 km/h.<br>
  *Resources*: [Paper](https://rpg.ifi.uzh.ch/docs/ICRA19_Delmerico.pdf) (ICRA 2019) | [Website](https://fpv.ifi.uzh.ch/) | [Data](https://fpv.ifi.uzh.ch/datasets/) | [Leaderboard](https://fpv.ifi.uzh.ch/uzh/leader-board/)

- <a id="tii-ratm-race-against-the-machine"></a>**TII-RATM (Race Against the Machine)** (2023) `Real`: Open-design drone racing dataset from the Technology Innovation Institute with fast (over 21 m/s) autonomous and human-piloted flights. It provides high-rate camera, IMU and motion-capture data, control inputs and corner-level labels of racing gates; a 2025 update adds flights by a world-class FPV pilot.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2311.02667) (IEEE RA-L 2024) | [Code](https://github.com/tii-racing/drone-racing-dataset) ★153

- <a id="a2rl-drone-championship"></a>**A2RL Drone Championship** (2025) `Real`: Autonomous drone racing series of the Abu Dhabi Autonomous Racing League. Teams fly a standard drone with one forward camera and an IMU through gate courses at over 130 km/h in AI speed, multi-drone and AI-versus-human races (April 2025 and January 2026, Abu Dhabi).<br>
  *Resources*: [Website](https://a2rl.io/autonomous-drone-race)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| [UZH-FPV Drone Racing Dataset](#uzh-fpv-drone-racing-dataset) | drone racing, visual-inertial odometry | 1 | 2 | 1 (FPV racing quadrotor) | RGB, event, IMU | Real world | Human demos | 31 sequences (16 with public ground truth; 9 used for the leaderboard) |
| [TII-RATM](#tii-ratm-race-against-the-machine) | drone racing dataset | N/A | N/A | 1 | RGB, IMU, mocap | Real world | Mixed | 18 autonomous and 18 piloted flights on 3 track shapes; 6 more piloted flights in v3.0.0 |
| [A2RL Drone Championship](#a2rl-drone-championship) | autonomous drone racing competition | 3 race formats in 2026 | Lap time and race results | 1 | RGB, IMU | Real world | - | N/A |

### <a id="other-multi-robot"></a>Multi-Robot

- <a id="multi-agent-mujoco-mamujoco"></a>**Multi-Agent MuJoCo (MaMuJoCo)** (2020) `Sim`: Cooperative continuous-control benchmark that splits single MuJoCo robots (Ant, HalfCheetah, Humanoid, Walker2d and others) into several agents, each controlling a subset of the joints from local observations. Introduced with FACMAC and now maintained in Gymnasium-Robotics with the PettingZoo API.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2003.06709) | [Website](https://robotics.farama.org/envs/MaMuJoCo/) | [Code](https://github.com/Farama-Foundation/Gymnasium-Robotics) ★1.9k

- <a id="vmas"></a>**VMAS** (2022) `Sim`: Vectorized Multi-Agent Simulator: a 2D physics engine in PyTorch with multi-robot coordination scenarios for multi-agent RL, such as transport, flocking, passage and navigation. Thousands of environments step in parallel on accelerators, and the MPE scenarios are ported; BenchMARL is the companion training library.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2207.03530) (DARS 2022) | [Website](https://vmas.readthedocs.io) | [Code](https://github.com/proroklab/VectorizedMultiAgentSimulator) ★631

- <a id="rocobench"></a>**RoCoBench** (2023) `Sim`: Six tabletop tasks in MuJoCo where two or three robots with different embodiments and reach (UR5e, Franka Panda, a humanoid) must coordinate: sweeping, sorting cubes, packing groceries, making a sandwich, moving a rope, arranging a cabinet. Introduced with RoCo to test LLM-based multi-robot planning.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2307.04738) | [Website](https://project-roco.github.io) | [Code](https://github.com/MandiZhao/robot-collab) ★267

- <a id="jaxrobotarium"></a>**JaxRobotarium** (2025) `Sim + Real`: JAX-based multi-robot RL platform and benchmark for the Robotarium, Georgia Tech's remotely accessible multi-robot testbed. Eight coordination scenarios train in parallel on accelerators, and policies can be deployed on the physical robots through the Robotarium's open remote access; it succeeds MARBLER.<br>
  *Resources*: [Paper](https://arxiv.org/abs/2505.06771) (CoRL 2025) | [Website](https://star-lab.cc.gatech.edu/papers/jain-jaxrobotarium/) | [Code](https://github.com/GT-STAR-Lab/JaxRobotarium) ★28

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| [Multi-Agent MuJoCo](#multi-agent-mujoco-mamujoco) | cooperative continuous control | 11 robot environments with configurable agent factorizations | 1 (team episode return) | 11 MuJoCo robots, each partitioned into agents by joints | state, proprioceptive | MuJoCo (Gymnasium-Robotics) | - | N/A |
| [VMAS](#vmas) | multi-agent RL, vectorized 2D simulation | 12 scenarios in the paper | 1 | Holonomic 2D agents with configurable shapes and sensors | state, lidar | VMAS (vectorized 2D physics engine in PyTorch) | - | N/A |
| [RoCoBench](#rocobench) | multi-arm collaboration, LLM planning | 6 | 3 | 3, 2 or 3 robots per task | state, language | MuJoCo (dm_control) | Not stated | RoCoBench-Text: a text-only question set on agent representation and reasoning |
| [JaxRobotarium](#jaxrobotarium) | multi-robot RL, sim-to-real | 8 coordination scenarios | Scenario-specific | 1 (Robotarium ground robots) | state | JaxRobotarium (JAX version of the Robotarium simulator) + real | - | N/A |

### <a id="other-competition"></a>Competitions

- <a id="robocup"></a>**RoboCup** (1997) `Sim + Real`: Annual robot competition, established in 1997 with the goal of a robot team beating the human soccer world champions by 2050. Leagues span soccer, rescue, home service (RoboCup@Home) and industrial robots; RoboCup 2026 in Incheon held the first championship of the merged Humanoid Soccer League.<br>
  *Resources*: [Website](https://www.robocup.org/)

- <a id="roboracer-formerly-f1tenth"></a>**RoboRacer (formerly F1TENTH)** (2016) `Sim + Real`: Open-source 1:10-scale autonomous racing platform and competition series, formerly F1TENTH and running since 2016. Teams build a standardized car and race in time trials and head-to-head knockouts at robotics conferences (27th edition at ICRA 2026, 31st at IROS 2026), alongside a remote Sim Racing League.<br>
  *Resources*: [Paper](https://proceedings.mlr.press/v123/o-kelly20a.html) (NeurIPS 2019 Competition Track) | [Website](https://roboracer.ai/) | [Code](https://github.com/f1tenth/f1tenth_gym) ★255

- <a id="robotic-grasping-and-manipulation-competition-rgmc"></a>**Robotic Grasping and Manipulation Competition (RGMC)** (2016) `Sim + Real`: Yearly manipulation competition, first held at IROS 2016 and now hosted at ICRA: the 11th edition ran at ICRA 2026 and the 12th is set for ICRA 2027 in Seoul. Tracks cover picking in clutter, human-to-robot handover, cloud robotics, mobile manipulation and simulated sorting.<br>
  *Resources*: [Paper](https://doi.org/10.1109/LRA.2021.3129134) (IEEE RA-L 2021) | [Website](https://sites.google.com/view/rgmcomp) | [Leaderboard](https://sites.google.com/view/rgmcomp/leaderboards)

- <a id="what-bimanuals-can-do-wbcd"></a>**What Bimanuals Can Do (WBCD)** (2025) `Real`: Bimanual manipulation competition at ICRA built around teleoperated data collection and learned policies on industry-style tasks. The second edition (ICRA 2026, Vienna) ran four tracks on sponsor robots: logistics picking, logistics packing, lab experiments and deformable manipulation. The 2025 edition drew 88 registered teams.<br>
  *Resources*: [Website](https://wbcdcompetition.github.io/)

- <a id="world-humanoid-robot-games"></a>**World Humanoid Robot Games** (2025) `Real`: Multi-sport event for humanoid robots, held in Beijing each August since 2025. The 2026 edition drew 666 teams and 2,056 robots from 16 countries to 51 events: 30 competitive (athletics, football, combat and more) and 21 scenario-based (such as hotel service and emergency response).<br>
  *Resources*: [Website](https://en.wikipedia.org/wiki/World_Humanoid_Robot_Games)

**Summary comparison**

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---|---|---|---|---|---|---|
| [RoboCup](#robocup) | robot soccer, rescue, home service | 5 domains | League-specific | League-specific | RGB, depth, lidar, audio, language | League simulators (Soccer Simulation and Rescue Simulation leagues) + real | - | N/A |
| [RoboRacer](#roboracer-formerly-f1tenth) | 1:10-scale autonomous racing | 2 formats | Lap time and race results | 1 | lidar, proprioceptive | F1TENTH Gym; AutoDRIVE for the Sim Racing League + real | - | N/A |
| [Robotic Grasping and Manipulation Competition](#robotic-grasping-and-manipulation-competition-rgmc) | grasping and manipulation competition | 5 tracks announced for the 2027 edition | Track-specific scoring rules | Team-provided robots | RGB, depth, proprioceptive | MATLAB/Simulink (simulation sorting track) + real | - | N/A |
| [What Bimanuals Can Do](#what-bimanuals-can-do-wbcd) | bimanual manipulation competition | 4 tracks in 2026 | Track-specific | 4 sponsor platforms in 2026 | RGB, proprioceptive | Real world | - | N/A |
| [World Humanoid Robot Games](#world-humanoid-robot-games) | humanoid sports and service events | 51 events in 2026 | Event-specific | 2,056 humanoid robots from 666 teams in 2026 | RGB, proprioceptive | Real world | - | N/A |

<p align="right"><a href="#contents">Back to contents ↑</a></p>

---

## <a id="contributing"></a>Contributing

Additions and corrections are both welcome.

This README is generated. Each entry is one YAML file in [`benchmarks/`](benchmarks/), the sections come from [`taxonomy.yaml`](taxonomy.yaml), and [`scripts/build_readme.py`](scripts/build_readme.py) writes the page. To add or fix an entry, edit the YAML file and rebuild; do not edit the README by hand. [CONTRIBUTING.md](CONTRIBUTING.md) has the template and the steps.

Found a wrong number or a dead link? Open an issue or a pull request with the source.
