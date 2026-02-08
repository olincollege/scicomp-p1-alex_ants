""" Contains simulation step function for ant trial modeling: movement, pheromones, population updates. """

# imports
import ants as a
import grid as g

######## Global Variables ########
from constants import DIRECTION_VECTORS, EXPLORER, FOLLOWER, EVAP_RATE


######## Ant Movement ########
def move_ant(ant:a.Ant, grid:g.Grid, fidelity:int)->None:
    """
    Function moves the ant one lattice grid in the ant's chosen direction.

    Args:
        ant: Ant object representing ant that needs to be moved for one step of the simulation.
        grid: Grid object representing the grid on which the ant needs to move.
        fidelity: Int representing the probability of an ant to keep following a trail. From paper 3a: 255, 3b: 251, 3c: 247

    Returns:
        None.

    """
    if ant.is_on_grid():
        ant_x, ant_y = ant.get_location()  # gets current x/y location of ant

        # update direction
        ant.update_direction(grid, fidelity)
        ant_direction = (ant.get_direction())  # gets the updated 0-7 direction where ant is headed relative to 0 being 'up'.

        dx, dy = DIRECTION_VECTORS[ant_direction]

        new_x = ant_x + dx
        new_y = ant_y + dy

        # Check if ant moving across grid boundary:
        if not (0 <= new_x < grid.size and 0 <= new_y < grid.size):
            ant.set_on_grid(False)  # sets the ant as off the grid
            return

        ant.set_location(new_x, new_y)


######## Pheromone Functions ########
def deposit_pheromone(ant:a.Ant, grid:g.Grid, tau:int)->None:
    """
    Function that places a 'tau' amount of pheromone at the location of each ant. Meant to be run once per ant every timestep.

    Args:
        ant: Ant object representing ant that needs to be moved for one step of the simulation.
        grid: Grid object representing the grid on which the ant needs to move.
        tau: Int representing "units" of pheromone ants deposit to their location on the grid at each timestep.

    Returns:
        None.

    """
    if ant.is_on_grid() == True:
        x_deposit, y_deposit = ant.get_location()
        grid.set_pheromone_for_point(
            x_deposit,
            y_deposit,
            grid.get_pheromone_for_point(x_deposit, y_deposit) + tau,
        )

def evaporate_pheromone(grid:g.Grid)->None:
    """
    Function that performs global evaporation of pheromone at each grid point. Meant to be run once every timestep.

    Args:
        grid: Grid object representing the grid on which simulation is occuring.

    Returns:
        None.
    """
    grid.grid -= EVAP_RATE # global application evaporation rate per step
    grid.grid[grid.grid < 0] = 0 # setting negative values to 0


######## Ant Population ########
def add_ant(ants_on_grid:list[a.Ant], hill_loc:int)->None:
    """
    Function that adds an ant to the grid. Meant to be run once per timestep.

    Args:
        ants_on_grid: List of Ant objects on simulation_grid. Should contain only ants that are on the grid.
        hill_loc: Tuple with ant hill location, default (128, 128).
    
    Returns:
        ants_on_grid: ants_on_grid, but updated with another ant.

    """
    ants_on_grid.append(a.Ant(x=hill_loc, y=hill_loc))


######## Wrapper simulation function - all functions for one step ########
def simulation_step(ants_on_grid:list[a.Ant], simulation_grid:g.Grid, fidelity:int, tau:int)->None:
    """
    Performs one time step.

    Args:
        ants_on_grid: List of Ant objects on simulation_grid. Should contain only ants that are on the grid.
        simulation_grid: Grid object representing lattice ants are being simulated on.
        fidelity: Int representing the probability of an ant to keep following a trail. From paper 3a: 255, 3b: 251, 3c: 247
        tau: Int representing "units" of pheromone ants deposit to their location on the grid at each timestep.

    Returns:
        None.

    """
    # generate new ant per timestep
    add_ant(ants_on_grid, simulation_grid.get_hill_loc())
    active_ants = []

    # ant movement + ant deposition to new position
    for ant in ants_on_grid:
        # if ant not on grid, skips deposit pheromone and move ant
        if not ant.is_on_grid():
            continue
        # if an is on grid, deposit pheromone and move ant
        deposit_pheromone(ant, simulation_grid, tau)
        move_ant(ant, simulation_grid, fidelity)

        # if ant is on grid, add to "active_ants" list
        if ant.is_on_grid():
            active_ants.append(ant)

    # update ant list with off-grid ants
    ants_on_grid = active_ants

    # global grid evaporation
    evaporate_pheromone(simulation_grid)


######## Output Parameters ########
def total_L_value(ants_on_grid:list[a.Ant]):
    """
    Returns number of exploratory (lost) ants at time t across the whole grid.

    Args:
        ants_on_grid: List of Ant objects on simulation_grid. Should contain only ants that are on the grid.

    Returns:
        sum_L: Int representing the number of exploratory ants at time t.
    
    """
    sum_L = sum(1 for ant in ants_on_grid if ant.get_state() == EXPLORER)
    return sum_L

def total_F_value(ants_on_grid:list[a.Ant]):
    """
    Returns number of follower ants at time t across the whole grid.

    Args:
        ants_on_grid: List of Ant objects on simulation_grid. Should contain only ants that are on the grid.

    Returns:
        sum_F: Int representing the number of follower ants at time t.

    """
    sum_F = sum(1 for ant in ants_on_grid if ant.get_state() == FOLLOWER)
    return sum_F
