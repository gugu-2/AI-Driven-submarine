# Simulation and Training

This repository uses **HoloOcean**, an open-source Unreal Engine based simulator, to train the Reinforcement Learning (RL) agents for continuous thruster control.

## Why Simulate? (Sim-to-Real Transfer)
Training a neural network to balance 6-DOF (Degree of Freedom) thrusters in turbulent ocean currents takes millions of trial-and-error steps. Doing this in the real world is impossible. By using a physics engine with Domain Randomization (randomizing current speeds and water density), the AI learns to fight stochastic currents virtually and translates that skill to the real ocean.

## Training the Soft Actor-Critic (SAC) Agent

1. Ensure the `simulation/holo_ocean_config.json` is set. It configures a Hovering AUV with a massive 1.5 m/s stochastic cross-current.
2. Run the training script:
   ```bash
   python train_sac.py
   ```
3. The script uses Stable Baselines3. It initializes a PyTorch Multi-Layer Perceptron (MLP) policy and will simulate a 1,000,000 step loop.
4. The final model is saved to `models/sac_auv_final.zip`.

## Using the Trained Model
Once trained, the `rl_agent.py` script automatically loads the `.zip` model for inference, translating APF coordinates into physical thruster force outputs (Surge, Sway, Heave).
