class BehaviorTreeSandbox:
    def __init__(self):
        print("[Behavior Tree Sandbox] Initializing Deterministic Reflex Logic...")

    def evaluate(self, llm_strategy, high_frequency_sensor_data):
        """
        The Behavior Tree acts as a 100Hz reflex safety layer.
        It evaluates the LLM's slow strategic intent against immediate raw sensor data.
        """
        obstacles = high_frequency_sensor_data.get('obstacles', [])
        
        # Node 1: Hard Reflex (Safety Override)
        # If the LLM commanded a waypoint but an obstacle just appeared, override the LLM immediately.
        if len(obstacles) > 0:
            print(f"[Behavior Tree Sandbox] CRITICAL: Obstacle detected at {obstacles[0]['distance']}m!")
            print("[Behavior Tree Sandbox] OVERRIDING LLM STRATEGY. Executing Evasive Reflex.")
            return {"action": "EVASIVE_MANEUVER", "priority": "HIGH", "safe_waypoint": [-10.0, 50.0, 0.0]}
            
        # Node 2: Pass-through (Nominal Operation)
        # If the environment is safe, allow the LLM's strategic waypoint to pass through to the thrusters.
        return {"action": "EXECUTE_STRATEGY", "priority": "LOW", "safe_waypoint": llm_strategy['target_waypoint']}
