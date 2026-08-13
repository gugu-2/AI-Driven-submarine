class PerceptionMap:
    def __init__(self):
        print("[Hardware Mapper] Initialized. Ready to ingest Sonar/LiDAR/Camera data.")

    def map_obstacles(self, raw_sensor_data, tick=0):
        """
        Takes generic hardware data and outputs a list of obstacle coordinates.
        It doesn't matter what the hardware is, it just gives us distance.
        """
        obstacles = []
        
        # Simulate an obstacle appearing on the sensors at tick 3
        if tick == 3:
            print("[Hardware Mapper] WARNING: Sensor hardware detects a massive object blocking the path!")
            obstacles.append({"x": 250.0, "y": 50.0, "size_radius": 20.0})
            
        return obstacles
