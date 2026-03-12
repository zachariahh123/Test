class Particle:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = position
        self.velocity = velocity

    def update_position(self, time_delta):
        """Update the position of the particle based on its velocity and the time delta."""
        self.position += self.velocity * time_delta

    def collide(self, other_particle):
        """Handle collision with another particle."""
        # Simple elastic collision response
        if self.position == other_particle.position:
            total_mass = self.mass + other_particle.mass
            new_velocity_self = ((self.mass - other_particle.mass) / total_mass) * self.velocity + ((2 * other_particle.mass) / total_mass) * other_particle.velocity
            new_velocity_other = ((2 * self.mass) / total_mass) * self.velocity + ((other_particle.mass - self.mass) / total_mass) * other_particle.velocity
            self.velocity = new_velocity_self
            other_particle.velocity = new_velocity_other

