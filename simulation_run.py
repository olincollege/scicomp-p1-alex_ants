"""Contains simulation function. To be run in main.py."""

# imports
import matplotlib.pyplot as mp
import simulation_setup as ss
import grid as g
import visualize as v


def run_simulation(grid_size:int, fidelity:int, tau:int, num_steps:int=1500, figure:str,
                   verbose:bool = False, live_vis:bool = False):
    """
    Function contains loop of simulation steps. Shows final plot of ant trails.

    Args:
        grid_size: Int representing the number of points of grid, default 256
         for a 256x256 point grid.
        fidelity: Int representing the probability of an ant to keep following
          a trail. From paper 3a: 255, 3b: 251, 3c: 247
        tau: Int representing "units" of pheromone ants deposit to their
          location on the grid at each timestep.
        num_steps: Int representing number of steps to simulate. Default 1500,
          according to Fig 3 description.
        figure: str representing Figure name for figure titles.
        verbose: Boolean to show extra print statements, good for debugging.
          Default False; off.
        live_vis: Boolean to show live visualization, nice to see steps
          dynamically but takes a lot fo time. Default False; off.

    Returns:
        None

    """
    ######## Pre-simulation ########
    # initializing grid and list to store ant population
    ants_on_grid = []  # will store all ant objects on the grid
    simulation_grid = g.Grid(grid_size)


    # optional debugging output, live figure
    if verbose:
        print(ants_on_grid)
        print(simulation_grid)
        print(simulation_grid.get_hill_loc())
    if live_vis:
        mp.figure()


    ######## During simulation ########
    # Main simulation loop
    print("####### DURING SIMULATION #######")
    for i in range(num_steps):
        ss.simulation_step(ants_on_grid, simulation_grid, fidelity, tau)

        # optional debugging output, live figure
        if verbose:
            print(f"Step: {i}, num ants on grid: {len(ants_on_grid)}")
        if live_vis:
            v.visualize_grid_live(ants_on_grid, simulation_grid, i, figure, pause=0.05)


    ######## Post-simulation ########
    # final statistics and visualize results
    print("####### POST SIMULATION #######")

    # final follower and explorer ant counts
    print(
        f"Follower ants: {ss.total_F_value(ants_on_grid)}, Explorer ants:"
        f" {ss.total_L_value(ants_on_grid)}"
    )

    # Visualize matplotlib of grid at final timestep
    v.visualize_grid(ants_on_grid, simulation_grid)

    # optional debugging output, live figure
    if live_vis:
        mp.show()

    if verbose:
        print(ants_on_grid)
        print(simulation_grid.grid)
