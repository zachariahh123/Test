if __name__ == '__main__':
    import sys
    from particle_life import ParticleLife

    # Initialize the simulation
    simulation = ParticleLife()
    
    # Run the simulation
    try:
        simulation.run()
    except Exception as e:
        print(f'An error occurred during the simulation: {e}')
