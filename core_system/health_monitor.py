class HealthMonitor:
    def __init__(self):
        # Different components break at different depths/pressures
        self.crush_depths = {
            "hull": -300.0,
            "sonar_dome": -150.0,
            "camera_housing": -100.0
        }
        print("[HM&E Monitor] Online. Tracking machinery and pressure points.")

    def check_system_health(self, current_depth, tick):
        """
        Monitors machinery for failures and checks depth against crush ratings.
        Returns a dictionary of errors. Empty dictionary means healthy.
        """
        errors = {}

        # 1. Pressure Checks
        for component, limit in self.crush_depths.items():
            if current_depth <= limit:  # More negative is deeper
                errors[component] = f"CRITICAL PRESSURE: Exceeded crush depth ({limit}m)"

        # 2. Simulate a random machinery injury
        if tick == 3:
            errors["starboard_thruster"] = "HARDWARE FAULT: Motor stalled. Zero RPM detected."
            print("[HM&E Monitor] ALARM! Machinery failure detected!")

        return errors
