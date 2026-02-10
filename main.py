"""Main file - add user inputs and run simulation here"""

import simulation_run as sr


######## Fig 3a ########
fidelity = 255  # according to Fig 3a from the paper
tau = 12 # according to Fig 3a from the paper
grid_size = 256 # according to paper
num_steps = 1500 # according to Fig 3a description from paper
verbose = False
live_vis = False

# Run simulation
if __name__ == "__main__":
    sr.run_simulation(grid_size, fidelity, tau, num_steps, verbose, live_vis)