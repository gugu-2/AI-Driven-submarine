class C2Listener:
    def __init__(self):
        # Default starting target
        self.current_target = {"x": 0.0, "y": 0.0, "z": -10.0}
        print("[HQ Listener] Online. Waiting for commands from Headquarters.")

    def get_target_waypoint(self, tick=0):
        """
        Simulates receiving a coordinate update from HQ.
        In reality, this would read from an acoustic modem or satellite uplink.
        """
        # Simulate HQ changing the mission target mid-way
        if tick == 2:
            print("[HQ Listener] BEEP! New orders received from HQ. Updating target.")
            self.current_target = {"x": 500.0, "y": 100.0, "z": -10.0}
            
        return self.current_target
