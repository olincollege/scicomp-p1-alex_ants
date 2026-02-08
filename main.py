# Run simulation from this file

import simulation_run as sr


# Simulation 1
fidelity = 255  # according to Fig 3a from the paper
tau = 12 # according to Fig 3a from the paper
grid_size = 256 # according to paper
num_steps = 100 # according to Fig 3a description from paper
verbose = False
live_vis = False

# Run simulation
sr.run_simulation(grid_size, fidelity, tau, num_steps, verbose, live_vis)
