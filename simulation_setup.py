""" Contains code to set up grid """

# imports
import numpy as np
import matplotlib.pyplot as mp
import ants as a

######## Global Variables ########
DIRECTION_VECTORS = [  # stores (dx, dy) lattice grid movement relative to current position for ant movement!!
    (0, -1),  # 0: Up
    (1, -1),  # 1: Up-Right
    (1, 0),  # 2: Right
    (1, 1),  # 3: Down-Right
    (0, 1),  # 4: Down
    (-1, 1),  # 5: Down-Left
    (-1, 0),  # 6: Left
    (-1, -1),  # 7: Up-Left
]

######## Simulation step functions ########
def move_ant(ant, grid, fidelity):
    """
    Function moves the ant one lattice grid in the ant's chosen direction.

    Args:
        ant: Ant object representing ant that needs to be moved for one step of the simulation.
        grid: Grid object representing the grid on which the ant needs to move.

    Returns:
        None.

    """
    if ant.is_on_grid():
        ant_x, ant_y = ant.get_location()  # gets current x/y location of ant

        # update direction
        ant.update_direction(grid, fidelity)
        ant_direction = (
            ant.get_direction()
        )  # gets the updated 0-7 direction where ant is headed relative to 0 being 'up'.

        dx, dy = DIRECTION_VECTORS[ant_direction]

        new_x = ant_x + dx
        new_y = ant_y + dy

        # If ant moving across grid boundary:
        if new_x > (grid.get_size() - 1) or new_x < 0:
            ant.set_on_grid(False)  # sets the ant as off the grid
            return
        if new_y > (grid.get_size() - 1) or new_y < 0:
            ant.set_on_grid(False)  # sets the ant as off the grid
            return

        ant.set_location(new_x, new_y)


def pheromone_deposition(ant, grid, tau):
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


def pheromone_evaporation(grid):
    """
    Function that performs global evaporation of pheromone at each grid point. Meant to be run once every timestep.

    Args:
        grid: Grid object representing the grid on which simulation is occuring.

    Returns:
        None.
    """
    for point_x in range(grid.size):
        for point_y in range(grid.size):
            new_pheromone_value = (
                grid.get_pheromone_for_point(point_x, point_y) - 1
            )

            if (
                new_pheromone_value <= 0
            ):  # If new proposed value is 0 or negative, set the pheromone concentration value to 0
                grid.set_pheromone_for_point(point_x, point_y, 0)
            else:
                grid.set_pheromone_for_point(
                    point_x, point_y, new_pheromone_value
                )


def add_ant(ants_on_grid, hill_loc):
    """
    Function that adds an ant to the grid. Meant to be run once per timestep.

    Args:
        ants_on_grid: List of Ant objects on simulation_grid. Should contain only ants that are on the grid.
        hill_loc: Tuple with ant hill location, default (128, 128).
    
    Returns:
        ants_on_grid: ants_on_grid, but updated with another ant.

    """
    ants_on_grid.append(a.Ant(x=hill_loc, y=hill_loc))
    return ants_on_grid


######## Wrapper simulation function - all functions for one step ########
def simulation_step(ants_on_grid, simulation_grid, fidelity, tau):
    """
    Wrapper function for all things that need to happen in a simulation step.

    Args:
        ants_on_grid: List of Ant objects on simulation_grid. Should contain only ants that are on the grid.
        simulation_grid: Grid object representing lattice ants are being simulated on.
        fidelity: Int representing the probability of an ant to keep following a trail. From paper 3a: 255, 3b: 251, 3c: 247

    Returns:
        None.

    """
    # generate new ant per timestep
    ants_on_grid = add_ant(ants_on_grid, simulation_grid.get_hill_loc())

    # ant movement + ant deposition to new position
    for ant in ants_on_grid:
        if ant.is_on_grid() == True:
            pheromone_deposition(ant, simulation_grid, tau)
            move_ant(ant, simulation_grid, fidelity)
            if ant.is_on_grid() == False:  # if ant moves off grid, remove ant
                ants_on_grid.remove(ant)
        else:  # if ant somehow off grid but still in ants_on_grid, remove ant
            ants_on_grid.remove(ant)
    # global grid evaporation
    pheromone_evaporation(simulation_grid)


######## Output Parameters ########
def total_L_value(ants_on_grid):
    """
    Returns number of exploratory (lost) ants at time t across the whole grid.

    Args:
        ants_on_grid: List of Ant objects on simulation_grid. Should contain only ants that are on the grid.

    Returns:
        sum_L: Int representing the number of exploratory ants at time t.
    
    """
    sum_L = 0
    for ant in ants_on_grid:
        if ant.get_state() == "explorer":
            sum_L += 1
    return sum_L


def total_F_value(ants_on_grid):
    """
    Returns number of follower ants at time t across the whole grid.

    Args:
        ants_on_grid: List of Ant objects on simulation_grid. Should contain only ants that are on the grid.

    Returns:
        sum_F: Int representing the number of follower ants at time t.

    """
    sum_F = 0
    for ant in ants_on_grid:
        if ant.get_state() == "follower":
            sum_F += 1
    return sum_F
