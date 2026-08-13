class BehaviorTreePlanner:
    def __init__(self):
        print("Initializing Deterministic Behavior Tree...")

    def tick(self, environment_state):
        """
        A mock implementation of a Behavior Tree tick.
        In reality, we would use py_trees library to build a formal tree.
        This represents the logic:
        Fallback (Selector):
          1. Sequence: Check for obstacle -> Evasive Maneuver
          2. Sequence: Check if at waypoint -> Sample Data
          3. Action: Continue to Waypoint
        """
        obstacles = environment_state.get('obstacles', [])
        
        # Node 1: Obstacle Avoidance (Highest Priority)
        if len(obstacles) > 0:
            print(f"[Behavior Tree] Condition Met: Detected {len(obstacles)} obstacle(s)!")
            return {"action": "EVASIVE_MANEUVER", "priority": "HIGH"}
            
        # Node 2: Mission Waypoint Logic
        at_waypoint = environment_state.get('at_waypoint', False)
        if at_waypoint:
            print("[Behavior Tree] Condition Met: Arrived at Waypoint.")
            return {"action": "SAMPLE_DATA", "priority": "MEDIUM"}
            
        # Node 3: Default Action
        return {"action": "NAVIGATE_TO_TARGET", "priority": "LOW"}
