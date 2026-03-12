class ParticleSystem:
    def __init__(self):
        self.particles = []

    def add_particle(self, particle):
        self.particles.append(particle)

    def update(self):
        for particle in self.particles:
            particle.update()  # Assume particle has an update method

    def draw(self):
        for particle in self.particles:
            particle.draw()  # Assume particle has a draw method
