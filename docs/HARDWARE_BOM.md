# Hardware, "The Brain", and Redundancy

A truly autonomous submarine requires a split-brain architecture: a high-level cognitive engine (The Cerebrum) for making decisions, and a low-level real-time controller (The Cerebellum) for spinning motors instantly.

## The Brain Architecture

### 1. The Cerebrum (High-Level AI)
**Hardware:** NVIDIA Jetson AGX Orin (or equivalent Edge AI computer).
*   **Purpose:** Runs the heavy Python code (APF navigation, Object Detection, YOLO, System Health Monitoring).
*   **Connectivity:** Connects to all high-bandwidth sensors (Cameras, Sonar, DVL) via Gigabit Ethernet. 

### 2. The Cerebellum (Low-Level Control)
**Hardware:** Pixhawk 6C (or equivalent Real-Time Microcontroller).
*   **Purpose:** Runs C++ firmware (like ArduSub or PX4) to instantly translate the Jetson's commands into PWM signals that spin the Electronic Speed Controllers (ESCs) for the thrusters.
*   **Connectivity:** Connects to the Jetson via UART (Serial over USB).

## Essential Equipment (BOM)

To build a fully autonomous sub, you need:
1.  **Forward-Looking Sonar (FLS):** (e.g., Blueprint Subsea Oculus). For detecting obstacles in pitch-black water.
2.  **DVL (Doppler Velocity Log):** (e.g., Water Linked DVL A50). Bounces sound off the sea floor to tell you exactly how fast you are moving. Critical because GPS does not work underwater.
3.  **IMU (Inertial Measurement Unit):** (e.g., VectorNav). Tells you your tilt, pitch, and heave (critical for the Storm Dive Protocol).
4.  **Pressure/Depth Sensor:** (e.g., BlueRobotics Bar30). Tells you how deep you are.
5.  **Thrusters:** Minimum of 6 thrusters for full 6-DOF (Degree of Freedom) control (Surge, Sway, Heave, Pitch, Roll, Yaw).

## Hardware Redundancy (Failover Protocols)

In the ocean, single equipment failure is inevitable. The AI handles this gracefully:
*   **Sonar Fails $\rightarrow$ Camera Fallback:** If the Sonar stops returning data, the AI instantly switches to the optical cameras (with lights) for obstacle detection. Range is severely limited, but the mission survives.
*   **DVL Fails $\rightarrow$ IMU Integration:** If the DVL loses bottom-lock, the AI switches to double-integrating the IMU accelerometers to guess its velocity. (This introduces "drift", so the sub will eventually need to surface for a GPS fix).
*   **Thruster Fails $\rightarrow$ Asymmetric Allocation:** If Thruster 1 (Front Left) dies, the AI shifts more power to Thruster 3 (Rear Left) and limits speed to maintain a straight line without spinning out of control. This is managed by the `emergency_manager.py`.
