# Installation & Hardware Setup

## Software Prerequisites

The software stack relies on standard Python data science and reinforcement learning libraries.

1. **Python 3.8+**
2. **Core Dependencies**:
   ```bash
   pip install numpy opencv-python stable-baselines3
   ```
3. **Simulation (Optional)**:
   If you intend to run the Reinforcement Learning training loop, you must install HoloOcean (an Unreal Engine 4 based physics simulator).
   ```bash
   pip install holoocean
   ```

## Hardware Recommendations

If deploying to a physical Autonomous Underwater Vehicle (AUV), we strongly recommend the following architecture:

### Compute Layer (Edge AI)
- **NVIDIA Jetson AGX Orin**: Provides 275 TOPS at 15-60W. This is required if you intend to run the experimental Neuro-Symbolic (LLM) architecture locally.
- **Raspberry Pi 4 / 5**: Sufficient if you are exclusively running the math-based `/core_system/` (APF and Storm Dive).

### Sensor Suite
To fully utilize this codebase, the AUV requires:
1. **DVL (Doppler Velocity Log)**: e.g., Water Linked DVL A50. Critical for dead-reckoning navigation.
2. **IMU**: e.g., VectorNav. Required for the Storm Dive Protocol to detect surface turbulence.
3. **Forward-Looking Sonar (FLS)**: e.g., Blueprint Subsea Oculus. Required for 2D acoustic obstacle detection in murky water where optical cameras fail.
