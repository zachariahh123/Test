import sys
from particle_system import ParticleSystem
from visualization import Visualizer

if __name__ == '__main__':
    particle_system = ParticleSystem()
    visualizer = Visualizer(particle_system)
    visualizer.run()