# Awesome Robotics Benchmarks

A curated collection of robotics benchmarks organized by domain with concise, comparable tables.

Counts (tasks / metrics / robot configs) are recorded as numbers; modalities are listed in detail; SIM shows the simulator backend (e.g., CoppeliaSim, SAPIEN, MuJoCo).

_For the **Simulation** domain, the summary table compares capabilities: physics engine, renderer, GPU support, OS, and license._

**human_demonstration** — trajectories recorded from a human controlling the robot/simulator (e.g., teleop, VR).

**motion_planner** — trajectories generated/executed by a planner/IK/trajectory optimizer (e.g., MoveIt, RRT, CHOMP).

**synthetic** — trajectories or episodes created programmatically or by generative scripts/LLMs without a physics-aware planner or human.

**NOTE: Currently this repo is underdevelopment and any pr is welcomed**.

## Domains
- [Manipulation](#manipulation)
- [Locomotion](#locomotion)
- [Navigation](#navigation)
- [HRI](#hri)
- [Safety](#safety)
- [Simulation](#simulation)
- [Generalist](#generalist)
- [Other](#other)

---

## Manipulation

- **RLBench** (2019): A large-scale learning environment featuring 100 unique vision-guided manipulation tasks of varying difficulty. RLBench provides multimodal observations (RGB, depth, segmentation, proprioception) from multiple camera angles and an *infinite* supply of demonstration trajectories generated via built-in motion planners.
  
  *Resources*: [Paper](https://arxiv.org/abs/1909.12271 ) | [Website](https://sites.google.com/view/rlbench ) | [Code](https://github.com/stepjam/RLBench )

- **Meta-World** (2019): Open-source benchmark of diverse single-arm tabletop manipulation tasks for multi-task and meta-RL.
  
  *Resources*: [Paper](https://arxiv.org/abs/1910.10897) | [Website](https://meta-world.github.io/) | [Code](https://github.com/Farama-Foundation/Metaworld)

- **RoboSuite** (2020): Modular MuJoCo-based simulator and benchmark suite for robot manipulation with standardized tasks and multi-robot support.
  
  *Resources*: [Paper](https://arxiv.org/abs/2009.12293) | [Website](https://robosuite.ai/) | [Code](https://github.com/ARISE-Initiative/robosuite)

- **CALVIN** (2021): An open-source simulated benchmark for learning long-horizon language-conditioned robot manipulation tasks. It features a Franka Emika Panda arm in four tabletop environments and 34 distinct manipulation tasks with unconstrained language instructions
  
  *Resources*: [Paper](https://arxiv.org/abs/2112.03227 ) | [Website](https://calvin.cs.uni-freiburg.de (offline, see GitHub)) | [Code](https://github.com/mees/calvin ) | [Data](https://github.com/mees/calvin/tree/main/dataset (download scripts))

- **FurnitureBench** (2023): Reproducible real-world furniture assembly benchmark with standardized hardware/setup, 3D-printed parts, large teleoperation dataset, and a matching simulator (FurnitureSim).
  
  *Resources*: [Paper](https://arxiv.org/abs/2305.12821) | [Website](https://clvrai.github.io/furniture-bench/) | [Code](https://github.com/clvrai/furniture-bench) | [Data](https://clvrai.github.io/furniture-bench/docs/tutorials/dataset.html)

- **LIBERO** (2023): A benchmark for lifelong robot learning featuring multitask manipulation with language conditioning. Focuses on knowledge transfer and generalization across diverse manipulation tasks.
  
  *Resources*: [Paper](https://arxiv.org/abs/2310.08531) | [Website](https://libero-project.github.io/) | [Code](https://github.com/Lifelong-Robot-Learning/LIBERO) | [Data](https://libero-project.github.io/)

- **RoboCasa** (2024): A large-scale simulation framework for generalist household robots, focusing on diverse kitchen environments.
  
  *Resources*: [Paper](https://arxiv.org/abs/2406.02523) | [Website](https://robocasa.ai ) | [Code](https://github.com/robocasa/robocasa (coming soon))

- **RoboTwin** (2024): A dual-arm manipulation benchmark and data-generation framework that uses generative 3D models and LLMs to create diverse bimanual task scenarios. RoboTwin provides a real-to-sim “digital twin” pipeline to generate varied object models and expert demonstrations, and an evaluation platform aligned with a real dual-arm robot (COBOT Magic platform). It combines simulated expert data with real-world teleoperated demos for coordinated two-arm tasks.
  
  *Resources*: [Paper](https://arxiv.org/abs/2409.02920 ) | [Website](https://robotwin-platform.github.io/) | [Code](https://github.com/RoboTwin-Platform/RoboTwin) | [Data](https://github.com/RoboTwin-Platform/RoboTwin/tree/main/data (simulated & real data))

- **VLABench** (2024): Language-conditioned manipulation benchmark with 100 categories emphasizing long-horizon reasoning and world knowledge.
  
  *Resources*: [Paper](https://arxiv.org/abs/2412.18194) | [Website](https://vlabench.github.io/) | [Code](https://github.com/OpenMOSS/VLABench)

- **RoboCerebra** (2025): A benchmark for evaluating high-level reasoning in long-horizon manipulation. RoboCerebra provides a large-scale simulation dataset of complex household tasks with extended subtask sequences, generated by GPT-based instruction decomposition and executed by human operators in simulatio. It emphasizes “System 2” planning skills (deliberative, goal-directed thinking) in vision-language-conditioned manipulation.
  
  *Resources*: [Paper](https://arxiv.org/abs/2506.06677) | [Website](https://robocerebra.github.io) | [Data](https://huggingface.co/datasets/qiukingballball/RoboCerebra )

### Summary Comparison

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---:|---:|---:|---|---|---|---|
| RLBench | table-top | 100 | 1 (task success rate) | 1 | RGB, depth, segmentation, proprioceptive | CoppeliaSim (V-REP) | motion_planner | 100 tasks × infinite demos (motion planner can generate unlimited trajectories) |
| Meta-World | table-top | 50 | 1 | 1 | proprioceptive | MuJoCo | unknown | N/A |
| RoboSuite | table-top, mobile-manipulation | 9 | 2 | 10 | RGB, depth, proprioceptive | MuJoCo | human_demonstration | N/A |
| CALVIN | table-top | 34 | 1 (primary metric: success rate) | 1 | RGB, depth, proprioceptive, language, tactile | PyBullet | human_demonstration | Hours of teleoperated play data (20K language instructions); 4 environments (A–D) with ~23K trajectories for training |
| FurnitureBench | table-top | 8 | 2 | 1 | RGB, proprioceptive | NVIDIA Isaac Gym / PhysX (Factory) via FurnitureSim | human_demonstration | ≈219.6 hours, 5100 successful demonstrations |
| LIBERO | table-top | 130 | 4 | 3 | RGB, depth, proprioceptive, language | RoboSuite (MuJoCo) | human_demonstration | 130+ tasks, 2500+ demonstrations |
| RoboCasa | mobile-manipulation (household) | 100 (25 atomic + 75 composite) | 1 (success rate for task completion) | 3 (supports single-arm mobiles, humanoids, quadruped-with-arm) | RGB, proprioceptive | PhysX (NVIDIA Omniverse) | both | 100+K demonstration trajectories (e.g. 50 human demos ×25 skills + 72K generated) |
| RoboTwin | dual-arm | 50 | 1 (task success rate) | 1 | RGB, depth, language | sapien | both | Synthetic dataset (hundreds of expert demos) + limited real demos per task |
| VLABench | table-top | 100 | 2 | 1 | RGB, language | MuJoCo (dm_control) | unknown | not specified |
| RoboCerebra | table-top | 1,000 training tasks + 60 held-out tasks (1,060 total) | 2 (sequence success rate and subtask completion) | 1 | RGB, language, proprioceptive | RoboSuite (MuJoCo) | both | 100k+ trajectories (e.g. 50 human demos ×25 skills + synthetic expansions) |


## Locomotion

- **Gymnasium MuJoCo Locomotion (classic subset)** (2016): Canonical MuJoCo continuous-control locomotion tasks widely used as RL baselines (e.g., Ant, HalfCheetah, Hopper, Walker2d, Humanoid).
  
  *Resources*: [Paper](https://arxiv.org/abs/1606.01540) | [Website](https://gymnasium.farama.org/environments/mujoco/) | [Code](https://github.com/Farama-Foundation/Gymnasium)

- **Brax** (2021): JAX-based differentiable physics engine reproducing classic MuJoCo-style tasks for massively parallel training.
  
  *Resources*: [Paper](https://arxiv.org/abs/2106.13281) | [Website](https://github.com/google/brax) | [Code](https://github.com/google/brax)

- **HumanoidBench** (2024): Simulated humanoid benchmark with dexterous hands spanning whole-body manipulation and locomotion; designed for high-DoF control research.
  
  *Resources*: [Paper](https://arxiv.org/abs/2403.10506) | [Website](https://humanoid-bench.github.io/) | [Code](https://humanoid-bench.github.io/)

### Summary Comparison

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---:|---:|---:|---|---|---|---|
| Gymnasium MuJoCo Locomotion (classic subset) | - | 11 | 1 | 6 | RGB, depth, proprioceptive | MuJoCo | unknown | N/A |
| Brax | - | 5 | 1 | 5 | proprioceptive | Brax (JAX) | unknown | N/A |
| HumanoidBench | humanoid, whole-body | 27 | 1 | 4 | proprioceptive, RGB, tactile | MuJoCo | unknown | N/A |


## Navigation

- **KITTI** (2012): Large-scale real-world autonomous driving dataset and benchmark suite for perception and odometry.
  
  *Resources*: [Paper](https://www.cvlibs.net/publications/Geiger2012CVPR.pdf) | [Website](https://www.cvlibs.net/datasets/kitti/) | [Data](https://www.cvlibs.net/datasets/kitti/)

- **AI2-THOR** (2017): Open-source Unity-based embodied AI platform with interactive indoor scenes; supports navigation (iTHOR/RoboTHOR) and manipulation (ManipulaTHOR).
  
  *Resources*: [Paper](https://arxiv.org/abs/1712.05474) | [Website](https://ai2thor.allenai.org/) | [Code](https://github.com/allenai/ai2thor) | [Data](https://ai2thor.allenai.org/robothor/cvpr-2021-challenge/)

- **Habitat Navigation (PointNav/ObjectNav/ImageNav)** (2019): Photoreal embodied navigation benchmarks (PointNav, ObjectNav, ImageNav) run in Habitat-Sim with standard metrics like Success and SPL.
  
  *Resources*: [Paper](https://arxiv.org/abs/1904.01201) | [Website](https://aihabitat.org/) | [Code](https://github.com/facebookresearch/habitat-challenge) | [Data](https://github.com/facebookresearch/habitat-challenge#dataset)

- **ALFRED** (2020): Household instruction-following benchmark that maps egocentric vision + language to action sequences in AI2-THOR.
  
  *Resources*: [Paper](https://openaccess.thecvf.com/content_CVPR_2020/papers/Shridhar_ALFRED_A_Benchmark_for_Interpreting_Grounded_Instructions_for_Everyday_Tasks_CVPR_2020_paper.pdf) | [Website](https://askforalfred.com/) | [Code](https://github.com/askforalfred/alfred) | [Data](https://github.com/askforalfred/alfred-data)

- **SocialGym 2.0** (2023): 2D ROS-based multi-agent social navigation simulator/benchmark with Python API and MARL baselines.
  
  *Resources*: [Paper](https://arxiv.org/abs/2303.05584) | [Website](https://amrl.cs.utexas.edu/SocialGym2/) | [Code](https://github.com/ut-amrl/SocialGym2)

### Summary Comparison

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---:|---:|---:|---|---|---|---|
| KITTI | - | 8 | 8 | 1 | RGB, lidar, GPS_IMU | - | human_demonstration | Varies by task; multi-sensor vehicle platform |
| AI2-THOR | navigation+manipulation | N/A | N/A | 2 | RGB, depth, semantic | Unity 3D | synthetic | iTHOR: 120 rooms; 2000+ objects; RoboTHOR: sim-real apartments |
| Habitat Navigation (PointNav/ObjectNav/ImageNav) | - | 3 | 2 | 1 | RGB, depth, semantic | Habitat-Sim | synthetic | large-scale episodes from HM3D/MP3D/Gibson splits (varies by year) |
| ALFRED | navigation+manipulation | 7 | 2 | 1 | RGB, depth, semantic, language | AI2-THOR 2.0 | both | 25,743 directives; 8,055 expert demos |
| SocialGym 2.0 | social navigation | 4 | 4 | 1 | lidar, proprioceptive | ROS-based 2D (PettingZoo/SB3 integration) | unknwon | N/A (simulated training/eval) |


## HRI

- **Assistive Gym** (2019): Physics-based assistive robotics framework with human models and ADL tasks for safe robot assistance.
  
  *Resources*: [Paper](https://arxiv.org/abs/1910.04700) | [Code](https://github.com/Healthcare-Robotics/assistive-gym)

### Summary Comparison

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---:|---:|---:|---|---|---|---|
| Assistive Gym | - | 6 | 1 | 4 | proprioceptive, RGB | PyBullet | N/A | N/A |


## Safety

- **Safety Gym** (2019): Constrained-RL benchmark with hazard/constraint costs across goal, push, and button tasks and multiple robots.
  
  *Resources*: [Paper](https://cdn.openai.com/safexp-short.pdf) | [Website](https://openai.com/research/safety-gym) | [Code](https://github.com/openai/safety-gym)

- **safe-control-gym** (2021): Unified safe learning-based control suite with constraints/disturbances on cart-pole and quadrotor systems.
  
  *Resources*: [Paper](https://arxiv.org/abs/2109.06325) | [Website](https://utiasdsl.github.io/safe-control-gym/) | [Code](https://github.com/utiasDSL/safe-control-gym)

### Summary Comparison

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---:|---:|---:|---|---|---|---|
| Safety Gym | - | 18 | 3 | 3 | lidar, proprioceptive | MuJoCo | unknown | N/A (simulated training/eval) |
| safe-control-gym | - | 2 | 3 | 3 | proprioceptive | PyBullet | unknown | N/A (simulated training/eval) |


## Simulation

- **MuJoCo** (2012): A fast, accurate physics engine for rigid-body simulation in robotics and control.
  
  *Resources*: [Paper](https://arxiv.org/abs/2106.02653) | [Website](https://mujoco.org/) | [Code](https://github.com/google-deepmind/mujoco)

- **SAPIEN** (2020): Physics-rich robotics simulator with Vulkan renderer and PhysX 5, optimized for large-scale data generation.
  
  *Resources*: [Paper](https://openaccess.thecvf.com/content_CVPR_2020/papers/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.pdf) | [Website](https://sapien.ucsd.edu/) | [Code](https://github.com/haosulab/SAPIEN)

- **Genesis** (2024): GPU-accelerated universal simulator with photorealistic rendering; targets high-throughput robot learning.
  
  *Resources*: [Website](https://genesis-embodied-ai.github.io) | [Code](https://github.com/Genesis-Embodied-AI/Genesis)

- **Gazebo**: Modular, open-source robotics simulator with pluggable physics and rendering backends.
  
  *Resources*: [Website](https://gazebosim.org) | [Code](https://github.com/gazebosim/gz-sim)

- **Isaac Lab**: Open-source robot learning framework built on NVIDIA Isaac Sim (PhysX + RTX).
  
  *Resources*: [Website](https://developer.nvidia.com/isaac/lab) | [Code](https://github.com/isaac-sim/IsaacLab)

- **PyBullet**: Pythonic interface to Bullet physics; lightweight, widely used for robotics RL research.
  
  *Resources*: [Website](https://pybullet.org) | [Code](https://github.com/bulletphysics/bullet3)

### Summary Comparison

| Simulation | Physics Engine | Renderer | GPU Support | OS | License |
|---|---|---|---:|---:|---|
| MuJoCo | MuJoCo | OpenGL | ✓ | Linux, Windows, macOS | Apache-2.0 |
| SAPIEN | NVIDIA PhysX 5 (CPU/GPU) | Vulkan-based (SapienRenderer), ray tracing | ✓ | Linux | MIT |
| Genesis | Genesis (rigid/soft fluids) | Photorealistic rasterization + ray tracing | ✓ | Linux, Windows, macOS | Apache-2.0 |
| Gazebo | Plugins: DART (ref), Bullet, ODE, TPE; Chrono via plugin | gz-rendering (OGRE/OGRE2; OptiX experimental) | ✓ | Linux, Windows, macOS | Apache-2.0 |
| Isaac Lab | NVIDIA PhysX 5 (via Isaac Sim) | NVIDIA Omniverse RTX / path tracing | ✓ | Linux, Windows | BSD-3-Clause (Isaac Lab); Isaac Sim: Apache-2.0 repo + NVIDIA Omniverse EULA |
| PyBullet | Bullet (rigid/soft body) | OpenGL visualizer; TinyRenderer (CPU) | — | Linux, Windows, macOS | zlib |


## Generalist

- **ManiSkill** (2021): SAPIEN-based benchmark targeting generalizable skills with four articulated-object and mobile manipulation tasks and a large LfD dataset.
  
  *Resources*: [Paper](https://arxiv.org/abs/2107.14483) | [Website](https://maniskill.ai/) | [Code](https://github.com/haosulab/ManiSkill) | [Data](https://github.com/haosulab/ManiSkill#datasets)

- **EmbodiedBench** (2025): A comprehensive benchmark to evaluate vision-driven embodied agents (multi-modal LLM-based) across both high-level and low-level task. EmbodiedBench spans four simulated environments – EB-ALFRED and EB-Habitat (high-level household tasks), and EB-Navigation and EB-Manipulation (low-level navigation and robotic manipulation) – comprising 1,128 diverse test instances in total. It also defines six capability-oriented evaluation subsets to assess commonsense reasoning, complex instruction understanding, spatial awareness, visual perception, long-horizon planning, etc.
  
  *Resources*: [Paper](https://arxiv.org/abs/2502.09560 ) | [Website](https://embodiedbench.github.io ) | [Code](https://github.com/embodiedbench/EmbodiedBench ) | [Data](https://huggingface.co/embodiedbench (evaluation data))

- **EmbodiedMemory-Bench** (2026): Evaluates how agents build and update memory from observation and interaction history, then use it for later embodied actions. The benchmark contains 2,554 AI2-THOR episodes across visual recall, dynamic tracking, interaction outcomes, and experience generalization.
  
  *Resources*: [Paper](https://arxiv.org/abs/2609.28236) | [Website](https://zju-omniai.github.io/Embodied-Omni/EmbodiedMemoryBench/) | [Code](https://github.com/ZJU-OmniAI/Embodied-Omni/tree/main/embodied_memory) | [Data](https://huggingface.co/datasets/lzLiang/EmbodiedMemoryBench)

### Summary Comparison

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---:|---:|---:|---|---|---|---|
| ManiSkill | - | 50 | 1 | 39 | RGB, depth, pointcloud, proprioceptive | SAPIEN (PhysX) | motion_planner | ~36,000 successful trajectories (~1.5M frames) |
| EmbodiedBench | - | 1128 (testing tasks across 4 envs) | 2 (e.g., success rate and subgoal success) | 4 | RGB, language | Multiple – AI2-THOR (Unity) for EB-ALFRED, Habitat-Sim for EB-Habitat/Navigation, and a robotics simulator for EB-Manipulation | both (uses existing human-collected and synthetic tasks) | 1,128 evaluation scenarios (drawn from ALFRED, Habitat, etc.) |
| EmbodiedMemory-Bench | embodied-memory | 2554 (episodes across 4 task families) | 5 (SR, RAR, ERR, AES, MAE) | Not specified | RGB, language, interaction history | AI2-THOR (Unity); AI2-THOR and ProcTHOR scenes | synthetic (simulator-grounded construction) | 2,554 evaluation episodes |


## Other

- **CARLA** (2017): Open-source urban driving simulator and benchmark; standard CoRL’17 suite of goal-directed navigation tasks.
  
  *Resources*: [Paper](https://proceedings.mlr.press/v78/dosovitskiy17a/dosovitskiy17a.pdf) | [Website](https://carla.org/) | [Code](https://github.com/carla-simulator/carla)

- **D4RL** (2020): Offline RL benchmark with standardized environments and fixed datasets across multiple domains.
  
  *Resources*: [Paper](https://arxiv.org/abs/2004.07219) | [Website](https://sites.google.com/view/d4rl/home) | [Code](https://github.com/Farama-Foundation/D4RL) | [Data](https://github.com/Farama-Foundation/D4RL#datasets)

### Summary Comparison

| Benchmark | Subtype | Task Count | Metric Count | Robot Configs | Modality | SIM | Data Source | Data Size |
|---|---|---:|---:|---:|---|---|---|---|
| CARLA | automous-driving | N/A | N/A | N/A | RGB, depth, semantic, lidar, GPS_IMU | Unreal Engine (CARLA) | unknown | N/A (simulated scenarios) |
| D4RL | Offline-RL | 50 | 1 | 6 | proprioceptive, RGB, lidar | Multiple (MuJoCo, PyBullet, MiniGrid) | both | Multiple task-specific datasets |
