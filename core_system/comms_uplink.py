class CommsUplink:
    def __init__(self):
        self.stealth_mode = True
        print("[Networking] Online. Defaulting to silent underwater acoustics.")

    def handle_comms(self, current_depth, health_errors):
        """
        Manages the network connection to the Head Office.
        """
        # If we are safely on the surface (0.0m) and we have errors, blast the SOS!
        if current_depth >= 0.0 and len(health_errors) > 0:
            if self.stealth_mode:
                self.stealth_mode = False
                print("\n[Networking] Submarine has broken the surface.")
                print("[Networking] Switching to RF/Satellite Mode. Deploying Antenna.")
            
            print("==================================================")
            print(">> SATELLITE UPLINK TO HEAD OFFICE ESTABLISHED <<")
            print(">> TRANSMITTING DISTRESS BEACON & ERROR LOGS   <<")
            for component, error_msg in health_errors.items():
                print(f"     ERROR: [{component}] -> {error_msg}")
            print(">> AWAITING RECOVERY TEAM...                   <<")
            print("==================================================\n")
            
        elif current_depth < 0.0:
            # Underwater: We stay totally silent. Radar doesn't work, and we don't want 
            # to make acoustic noise that could be detected.
            pass
