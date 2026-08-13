from c2_listener import C2Listener
from perception_map import PerceptionMap
from obstacle_bypass import ObstacleBypass
from weather_depth_controller import WeatherDepthController
from health_monitor import HealthMonitor
from emergency_manager import EmergencyManager
from comms_uplink import CommsUplink
import time

def main_loop():
    print("========================================")
    print("BOOTING SUBMARINE SYSTEM (WITH HM&E)")
    print("========================================\n")
    
    hq = C2Listener()
    hardware_map = PerceptionMap()
    bypass_engine = ObstacleBypass()
    weather_ctrl = WeatherDepthController()
    
    # New HM&E Subsystems
    monitor = HealthMonitor()
    emergency = EmergencyManager()
    network = CommsUplink()
    
    current_pos = {"x": 0.0, "y": 0.0, "z": -20.0}
    health_errors = {}
    
    for tick in range(1, 6):
        print(f"\n--- TIME: TICK {tick} ---")
        
        # 1. Health Monitoring (Check machinery & pressure)
        new_errors = monitor.check_system_health(current_pos['z'], tick)
        health_errors.update(new_errors)
        
        # 2. Check for Emergency Surfacing
        if emergency.evaluate_distress(health_errors):
            steering, safe_z = emergency.get_emergency_steering()
            print("[Propulsion] OVERRIDE: Forcing Sub to Surface!")
        else:
            # Standard Operations (APF & Weather)
            target = hq.get_target_waypoint(tick)
            obstacles = hardware_map.map_obstacles(raw_sensor_data=None, tick=tick)
            steering = bypass_engine.calculate_steering_vector(current_pos, target, obstacles)
            
            # Weather check
            imu_turbulence = 0.1
            safe_z = weather_ctrl.calculate_safe_depth(target['z'], imu_turbulence)

        print(f"[Propulsion] Steer Vector (X, Y): ({steering['x_vector']}, {steering['y_vector']}) | Depth Command: {safe_z}m")
        
        # Apply physics/movement mock
        current_pos['x'] += steering['x_vector'] * 10
        current_pos['y'] += steering['y_vector'] * 10
        # Slowly ascend if ordered to 0.0, else snap to safe_z (mock logic)
        if safe_z == 0.0 and current_pos['z'] < 0.0:
            current_pos['z'] += 10.0 # Ascend 10 meters per tick
        else:
            current_pos['z'] = safe_z
            
        print(f"[System] Current Depth: {current_pos['z']}m")
        
        # 3. Handle Communications to Head Office
        network.handle_comms(current_pos['z'], health_errors)
        
        time.sleep(1)
        
if __name__ == "__main__":
    main_loop()
