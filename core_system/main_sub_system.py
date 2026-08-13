from c2_listener import C2Listener
from perception_map import PerceptionMap
from obstacle_bypass import ObstacleBypass
from weather_depth_controller import WeatherDepthController
import time
import random

def main_loop():
    print("========================================")
    print("BOOTING SIMPLE ROBUST SUBMARINE SYSTEM")
    print("========================================\n")
    
    hq = C2Listener()
    hardware_map = PerceptionMap()
    bypass_engine = ObstacleBypass()
    weather_ctrl = WeatherDepthController()
    
    current_pos = {"x": 0.0, "y": 0.0, "z": -5.0} # Starting near surface
    
    for tick in range(1, 6):
        print(f"\n--- TIME: TICK {tick} ---")
        
        # 1. HQ gives us the target
        target = hq.get_target_waypoint(tick)
        print(f"[System] Current HQ Target: {target}")
        
        # 2. Hardware senses obstacles
        obstacles = hardware_map.map_obstacles(raw_sensor_data=None, tick=tick)
        
        # 3. Calculate XY steering to bypass obstacles and reach target
        steering = bypass_engine.calculate_steering_vector(current_pos, target, obstacles)
        
        # 4. Handle Weather and Depth (Simulate a thunderstorm hitting at tick 4)
        imu_turbulence = 0.1
        if tick == 4:
            imu_turbulence = 8.5 # Massive waves detected
            
        safe_z = weather_ctrl.calculate_safe_depth(target['z'], imu_turbulence)
        
        print(f"[Propulsion] Steer Vector (X, Y): ({steering['x_vector']}, {steering['y_vector']}) | Depth Command: {safe_z}m")
        
        # Update current pos mock
        current_pos['x'] += steering['x_vector'] * 10
        current_pos['y'] += steering['y_vector'] * 10
        current_pos['z'] = safe_z
        time.sleep(1)
        
if __name__ == "__main__":
    main_loop()
