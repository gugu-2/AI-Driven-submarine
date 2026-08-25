# AI-Driven Submarine (AUV) Architecture---

Welcome to the open-source repository for the Fully Autonomous Submarine. This repository contains the core logic for a robust, GPS-denied autonomous underwater vehicle capable of complex navigation, obstacle avoidance, and weather-aware depth management.

## 🚀 Features

*   **Command & Control (C2) Navigation:** Listens for HQ coordinates and navigates dynamically.
*   **Reactive Obstacle Bypass (APF):** Uses Artificial Potential Fields (APF) to naturally flow around obstacles detected by *any* sensor (Sonar, LiDAR, Camera) without requiring complex neural networks.
*   **Storm Dive Protocol:** A weather-aware controller that monitors IMU turbulence. If surface waves are too extreme (thunderstorms), the sub automatically dives to a calm, safe depth (e.g., -30m).
*   **Neuro-Symbolic Sandbox (Experimental):** Contains an advanced architecture that safely bounds Large Language Models (LLMs) inside deterministic Behavior Trees for high-level tactical reasoning.
*   **Reinforcement Learning (SAC):** Scripts for training a Soft Actor-Critic model in HoloOcean to fight ocean currents continuously.

## 📁 Repository Structure

*   `/core_system/`: The robust, production-ready reactive architecture (APF, Storm Dive, HQ Listener).
*   `/cognition/`: Experimental Neuro-Symbolic AI logic (LLM Strategist, Behavior Tree Sandbox).
*   `/perception/`: Scripts for processing raw 2D acoustic sonar data using OpenCV.
*   `/control/`: The Reinforcement Learning (SAC) inference agent.
*   `/simulation/`: Configuration files for the HoloOcean physics engine.
*   `/docs/`: Detailed guides for Architecture, Installation, and Simulation.

---
## 🏁 Quick Start

To see the core reactive system in action:

```bash
cd core_system
python main_sub_system.py
```
This will run a 5-second simulation demonstrating HQ target tracking, a massive obstacle bypass, and an emergency Storm Dive response.

## 📚 Documentation

For an in-depth understanding, please refer to the `docs/` folder:
*   [Architecture Guide](docs/ARCHITECTURE.md)
*   [Installation & Setup](docs/INSTALLATION.md)
*   [Simulation & Training](docs/SIMULATION.md)
