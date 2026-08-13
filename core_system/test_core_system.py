import unittest
from c2_listener import C2Listener
from perception_map import PerceptionMap
from obstacle_bypass import ObstacleBypass
from weather_depth_controller import WeatherDepthController
from health_monitor import HealthMonitor
from emergency_manager import EmergencyManager
from comms_uplink import CommsUplink

class TestSubmarineCore(unittest.TestCase):

    def setUp(self):
        # Initialize modules before each test
        self.hq = C2Listener()
        self.perception = PerceptionMap()
        self.bypass = ObstacleBypass()
        self.weather = WeatherDepthController()
        self.health = HealthMonitor()
        self.emergency = EmergencyManager()
        self.network = CommsUplink()

    # 1. C2 Listener Tests
    def test_hq_target_update(self):
        # Default target
        target = self.hq.get_target_waypoint(tick=1)
        self.assertEqual(target['x'], 0.0)
        
        # HQ update at tick 2
        new_target = self.hq.get_target_waypoint(tick=2)
        self.assertEqual(new_target['x'], 500.0)

    # 2. Perception & APF Bypass Tests
    def test_obstacle_mapping(self):
        obs = self.perception.map_obstacles(None, tick=3)
        self.assertEqual(len(obs), 1)
        self.assertEqual(obs[0]['x'], 250.0)

    def test_apf_attractive_force(self):
        current_pos = {"x": 0.0, "y": 0.0, "z": -10.0}
        target = {"x": 100.0, "y": 0.0, "z": -10.0}
        obstacles = []
        
        vector = self.bypass.calculate_steering_vector(current_pos, target, obstacles)
        # Should pull strongly in positive X direction
        self.assertGreater(vector['x_vector'], 0.0)
        self.assertEqual(vector['y_vector'], 0.0)

    def test_apf_repulsive_force(self):
        current_pos = {"x": 90.0, "y": 0.0, "z": -10.0}
        target = {"x": 200.0, "y": 0.0, "z": -10.0}
        # Obstacle directly in front of sub
        obstacles = [{"x": 100.0, "y": 0.0, "size_radius": 10.0}]
        
        vector = self.bypass.calculate_steering_vector(current_pos, target, obstacles)
        # Repulsive force should push it backwards (negative X) to prevent collision
        self.assertLess(vector['x_vector'], 0.0)

    # 3. Weather Protocol Tests
    def test_storm_dive_protocol(self):
        # Calm sea
        depth_cmd = self.weather.calculate_safe_depth(-10.0, imu_heave_variance=0.1)
        self.assertEqual(depth_cmd, -10.0)
        
        # Thunderstorm (variance > 5.0)
        storm_cmd = self.weather.calculate_safe_depth(-10.0, imu_heave_variance=6.0)
        self.assertEqual(storm_cmd, -30.0)

    # 4. Health & Emergency Tests
    def test_crush_depth_warning(self):
        # Safe depth
        safe_errors = self.health.check_system_health(-50.0, 1)
        self.assertEqual(len(safe_errors), 0)
        
        # Too deep for camera (-100m limit)
        crush_errors = self.health.check_system_health(-101.0, 1)
        self.assertTrue("camera_housing" in crush_errors)

    def test_emergency_surfacing_override(self):
        health_errors = {"starboard_thruster": "Stalled"}
        is_emerg = self.emergency.evaluate_distress(health_errors)
        self.assertTrue(is_emerg)
        
        # Steering should halt XY progress and force 0.0m depth
        steering, safe_z = self.emergency.get_emergency_steering()
        self.assertEqual(steering['x_vector'], 0.0)
        self.assertEqual(safe_z, 0.0)

    # 5. Networking Tests
    def test_comms_stealth_mode(self):
        # Should stay in stealth when surfaced but no errors
        self.network.handle_comms(0.0, {})
        self.assertTrue(self.network.stealth_mode)
        
        # Should stay in stealth when errors exist but underwater
        self.network.handle_comms(-20.0, {"error": "test"})
        self.assertTrue(self.network.stealth_mode)
        
        # Should break stealth when surfaced AND errors exist
        self.network.handle_comms(0.0, {"error": "test"})
        self.assertFalse(self.network.stealth_mode)

if __name__ == '__main__':
    unittest.main()
