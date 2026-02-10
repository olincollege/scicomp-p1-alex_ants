"""File contains visualization functions"""

# imports
import matplotlib.pyplot as mp
import ants as a
import grid as g

######## Global Variables ########
from constants import DIRECTION_TO_ANGLE


######## Static Visualization at a timestep ########
def visualize_grid(ants_on_grid:list[a.Ant], simulation_grid:g.Grid, figure:str)->None:
    """
    Function visualizes the grid and ants at one timestep. The grid shows
      pheromone concentrations (white - 0, grey - some, black - high), shows
      ant dots.

    Args:
        ants_on_grid: List of Ant objects on simulation_grid. Should contain
          only ants that are on the grid.
        simulation_grid: Grid object representing lattice ants are being
          simulated on.
        figure: str representing Figure name for figure titles.

    Returns:
        None.

    """

    mp.figure()
    _plot_grid(simulation_grid, vmax=84)
    _plot_ants(ants_on_grid)

    mp.title(f"Figure {figure}")

    mp.show()


######## Dynamic Visualization ########
def visualize_grid_live(ants_on_grid, simulation_grid, step, figure, pause=0.05):
    """
    Show live visualization of grid + ants.

    Args:
        ants_on_grid: List of Ant objects on simulation_grid. Should contain
          only ants that are on the grid.
        simulation_grid: Grid object representing lattice ants are being
          simulated on.
        step: Int representing the iteration number.
        figure: str representing Figure name for figure titles.
        pause: Number of seconds for the simulation to pause.

    Returns:
        None.
    """
    mp.clf()

    # showing grid pheromone concentration
    _plot_grid(simulation_grid, vmax=84)
    _plot_ants(ants_on_grid)

    mp.title(f"Figure {figure}, Step {step}")

    mp.pause(pause)


######## Helper Functions ########
def _plot_grid(grid:g.Grid, vmax:int)->None:
    """
    Function plots pheromone grid.

    Args:
        grid: Grid object representing lattice ants are being simulated on.
        vmax: Int representing max pheromone concentration value to show on
          plot.

    Returns:
        None.

    """
    mp.imshow(grid.grid, cmap="Greys", origin="upper", vmin=0, vmax=vmax)
    mp.colorbar(label="Pheromone Concentration (C(x,t))")
    mp.xlim(0, grid.get_size())
    mp.ylim(grid.get_size(), 0)


def _plot_ants(ants_on_grid:list[a.Ant])->None:
    """
    Function plot ants on grid.
    
    Args:
        ants_on_grid: List of Ant objects on simulation_grid. Should contain
          only ants that are on the grid.
    
    Returns:
        None

    """
    # showing ant
    for ant in ants_on_grid:
        if not ant.is_on_grid():
            continue
        x, y = ant.get_location()
        direction = ant.get_direction()

        angle = DIRECTION_TO_ANGLE[direction]

        mp.scatter(x, y, marker=(3, 0, angle), c="red", s=10)
