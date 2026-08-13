class WeatherDepthController:
    def __init__(self):
        self.safe_storm_depth = -30.0 # 30 meters down is safe from surface storms
        print("[Weather Controller] Online. Monitoring IMU for surface turbulence.")

    def calculate_safe_depth(self, hq_target_depth, imu_heave_variance):
        """
        Overrides the HQ depth if surface weather is too violent (thunderstorm).
        """
        # If the submarine is bouncing up and down wildly (high heave variance)
        if imu_heave_variance > 5.0:
            print("[Weather Controller] THUNDERSTORM DETECTED! Surface is too turbulent.")
            print(f"[Weather Controller] Overriding HQ depth ({hq_target_depth}m) -> DOCKING STORM PROTOCOL: Diving to {self.safe_storm_depth}m.")
            return self.safe_storm_depth
            
        return hq_target_depth
