import math

class ObstacleBypass:
    def __init__(self):
        # Constants for Artificial Potential Fields (APF)
        self.attract_strength = 1.0
        self.repel_strength = 1000.0

    def calculate_steering_vector(self, current_pos, target_pos, obstacles):
        """
        Uses Artificial Potential Fields to naturally bypass obstacles.
        Target pulls the sub forward. Obstacles push it away.
        Returns the (x, y) vector the sub should steer toward.
        """
        # 1. Attractive force (Pull toward target)
        dx_target = target_pos['x'] - current_pos['x']
        dy_target = target_pos['y'] - current_pos['y']
        
        # Normalize target pull
        dist_target = math.sqrt(dx_target**2 + dy_target**2) + 0.001
        force_x = (dx_target / dist_target) * self.attract_strength
        force_y = (dy_target / dist_target) * self.attract_strength

        # 2. Repulsive force (Push away from obstacles)
        for obs in obstacles:
            dx_obs = current_pos['x'] - obs['x']
            dy_obs = current_pos['y'] - obs['y']
            dist_obs = math.sqrt(dx_obs**2 + dy_obs**2) + 0.001
            
            # If obstacle is dangerously close, push back hard!
            if dist_obs < obs['size_radius'] * 3:
                repel_mag = self.repel_strength / (dist_obs**2)
                force_x += (dx_obs / dist_obs) * repel_mag
                force_y += (dy_obs / dist_obs) * repel_mag
                print(f"[Obstacle Bypass] Math Engine overriding steering! Pushing away from obstacle.")

        # Return the final steering vector
        return {"x_vector": round(force_x, 2), "y_vector": round(force_y, 2)}
