"""Main file - add user inputs and run simulation here"""

import simulation_run as sr


def run_figures():
    """
    Runs simulations for parameters of figure 3a, b, c from the paper. 
    """

    # figure names, fidelity - probability per iteration of an ant remaining
    #  on a trail with a local concentration C
    configs = [("3a", 255), ("3b", 251), ("3c", 247),]

    # constants across all figures
    tau = 8 # rate of pheromone deposition per ant per time step
    grid_size = 256
    num_steps = 1500
    verbose = False
    live_vis = False

    for figure, fidelity in configs:
        sr.run_simulation(grid_size, fidelity, tau, figure, num_steps, 
                          verbose, live_vis)


if __name__ == "__main__":
    run_figures()
