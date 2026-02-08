"""File contains visualization functions"""

# imports
import matplotlib.pyplot as mp

######## Global Variables ########
from constants import DIRECTION_TO_ANGLE


######## Functions ########
def visualize_grid(ants_on_grid, simulation_grid):
    """
    Function visualizes the grid and ants at one timestep. The grid shows pheromone concentrations (white - 0, grey - some, black - high), shows ant dots.

    Args:
        ants_on_grid: List of Ant objects on simulation_grid. Should contain only ants that are on the grid.
        simulation_grid: Grid object representing lattice ants are being simulated on.

    Returns:
        None.

    """

    # showing grid pheromone concentration
    grid = simulation_grid.grid
    mp.figure()
    mp.imshow(grid, cmap="Greys", origin="upper", vmin=0, vmax=60)

    mp.colorbar(label="Pheromone Concentration (C(x,t))")
    mp.xlim(0, simulation_grid.get_size())
    mp.ylim(simulation_grid.get_size(), 0)

    # showing ant
    for ant in ants_on_grid:
        if ant.is_on_grid():
            x, y = ant.get_location()
            direction = ant.get_direction()

            angle = DIRECTION_TO_ANGLE[direction]
            mp.scatter(x, y, marker=(3, 0, angle), c="red", s=20)

    mp.show()


def visualize_grid_live(ants_on_grid, simulation_grid, step, pause=0.05):
    """
    Show live visualization of grid + ants.

    Args:
        ants_on_grid: List of Ant objects on simulation_grid. Should contain only ants that are on the grid.
        simulation_grid: Grid object representing lattice ants are being simulated on.
        step: Int representing the iteration number.
        pause: Number of seconds for the simulation to pause.

    Returns:
        None.
    """
    mp.clf()

    # showing grid pheromone concentration
    grid = simulation_grid.grid

    mp.imshow(grid, cmap="Greys", origin="upper", vmin=0, vmax=84)
    mp.colorbar(label="Pheromone Concentration (C(x,t))")
    mp.xlim(0, simulation_grid.get_size())
    mp.ylim(simulation_grid.get_size(), 0)
    mp.title(f"Step {step}")

    # showing ant
    for ant in ants_on_grid:
        if ant.is_on_grid():
            x, y = ant.get_location()
            direction = ant.get_direction()

            angle = DIRECTION_TO_ANGLE[direction]
            mp.scatter(x, y, marker=(3, 0, angle), c="red", s=20)

    mp.pause(pause)

