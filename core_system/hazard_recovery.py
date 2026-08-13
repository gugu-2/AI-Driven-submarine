class HazardRecovery:
    def __init__(self):
        self.under_ice = False
        print("[Hazard System] Online. Monitoring for physical entanglements and ice canopies.")

    def detect_and_clear_tangle(self, thruster_id, commanded_power, actual_rpm):
        """
        If a whale shark, kelp, or rope gets tangled in the propeller/fan, 
        commanded power will be high, but actual RPM will be 0.
        """
        if commanded_power > 50.0 and actual_rpm == 0:
            print(f"[Hazard System] WARNING: Thruster {thruster_id} is JAMMED! Possible animal/kelp tangle.")
            print("[Hazard System] INITIATING CLEARING PULSE: Violently reversing motors...")
            # Simulate the clearing pulse (Full reverse, full forward, full reverse)
            pulse_commands = [-100.0, 100.0, -100.0]
            for p in pulse_commands:
                print(f"   > Pulsing Thruster {thruster_id} at {p}% power")
            
            # Assume 80% chance the pulse clears the tangle
            cleared = True 
            if cleared:
                print(f"[Hazard System] Tangle cleared! Thruster {thruster_id} nominal.")
                return True
            else:
                print(f"[Hazard System] TANGLE FATAL. Thruster {thruster_id} destroyed. Switching to backup.")
                return False
        return True

    def check_glacier_protocol(self, upward_sonar_distance):
        """
        If we are under a glacier, we cannot just ascend to 0.0m or we crash into ice.
        """
        if upward_sonar_distance < 10.0:  # Ice is right above us!
            self.under_ice = True
            print("[Hazard System] ICE CANOPY DETECTED! We are under a glacier.")
            print("[Hazard System] Engaging Polynya Search Mode (looking for a hole in the ice).")
            return True
        else:
            self.under_ice = False
            return False
