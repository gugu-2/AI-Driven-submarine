class EmergencyManager:
    def __init__(self):
        self.is_emergency = False
        print("[Emergency System] Online. Standing by for distress signals.")

    def evaluate_distress(self, health_errors):
        """
        If there are any errors, trigger the Emergency Blow protocol.
        """
        if len(health_errors) > 0 and not self.is_emergency:
            self.is_emergency = True
            print("[Emergency System] CRITICAL INJURY VERIFIED. Aborting mission.")
            print("[Emergency System] INITIATING EMERGENCY BLOW: Ballast emptying. Surfacing immediately.")
            
        return self.is_emergency

    def get_emergency_steering(self):
        """
        Overrides the APF. Forces the sub straight up to the surface (Depth 0.0m).
        Halts forward momentum (X, Y = 0) to prevent further damage.
        """
        return {"x_vector": 0.0, "y_vector": 0.0}, 0.0
