# Contains code to set up grid

# imports
import numpy as np
import matplotlib.pyplot as mp

# Global Variables

DIRECTION_VECTORS = [ # stores (dx, dy) lattice grid movement relative to current position for ant movement!!
    (0, -1),  # 0: Up
    (1, -1),  # 1: Up-Right
    (1, 0),   # 2: Right
    (1, 1),   # 3: Down-Right
    (0, 1),   # 4: Down
    (-1, 1),  # 5: Down-Left
    (-1, 0),  # 6: Left
    (-1, -1), # 7: Up-Left
]
TAU = 8 # "units" of pheromone ants deposit to their location on the grid at each timestep.
direction_to_angle = { # for the visualization function, converting a direction to the angle for ant marker ONLY
    0: 90,
    1: 45,
    2: 0,
    3: -45,
    4: -90,
    5: -135,
    6: 180,
    7: 135,
}


# Grid class
class Grid:
    """
    Object representing the square grid on which ants travel. Grid values represent pheromone concentration.

    Attributes:
        size: Int representing the number of points of grid, default 256 for a 256x256 point grid.
        hill_loc: Tuple with ant hill location, default (128, 128).
        grid: Numpy 2D array of points.
    """

    def __init__(self, size=256, hill_loc=(128, 128)):
        self.size = size
        self.hill_loc = hill_loc
        self.grid = np.zeros((size, size))
    
    def __repr__(self):
        return f"Grid size = {self.size}x{self.size}, hill_loc = {self.hill_loc})"

    # 'Get' Functions
    def get_size(self):
        """Gets grid size."""
        return self.size
    
    def get_pheromone_for_point(self, x, y):
        """Gets pheromone value for one point on the grid."""
        return self.grid[y, x]
    
    def set_pheromone_for_point(self, x, y, value):
        """Sets new pheromone value for one point on the grid."""
        self.grid[y, x] = value


######## Simulation step functions ########
def move_ant(ant, grid):
    """
    Function moves the ant one lattice grid in the ant's chosen direction.

    Args:
        ant: Ant object representing ant that needs to be moved for one step of the simulation.
        grid: Grid object representing the grid on which the ant needs to move. 
    
    Returns:
        None.
    """
    if ant.is_on_grid():
        ant_x, ant_y = ant.get_location() # gets current x/y location of ant

        # update direction
        ant.update_direction()
        ant_direction = ant.get_direction() # gets the updated 0-7 direction where ant is headed relative to 0 being 'up'.

        dx, dy = DIRECTION_VECTORS[ant_direction]

        new_x = ant_x + dx
        new_y = ant_y + dy

        # If ant moving across grid boundary:
        if new_x > (grid.get_size()-1) or new_x < 0:
            ant.set_on_grid(False) # sets the ant as off the grid
            return
        if new_y > (grid.get_size()-1) or new_y < 0:
            ant.set_on_grid(False) # sets the ant as off the grid
            return

        ant.set_location(new_x, new_y)
    
def pheromone_deposition(ant, grid):
    """
    Function that places a 'tau' amount of pheromone at the location of each ant. Meant to be run once per ant every timestep. 
    
    Args:
        ant: Ant object representing ant that needs to be moved for one step of the simulation.
        grid: Grid object representing the grid on which the ant needs to move.
    
    Returns:
        None.
    """
    if ant.is_on_grid() == True:
        x_deposit, y_deposit = ant.get_location()
        grid.set_pheromone_for_point(x_deposit, y_deposit, grid.get_pheromone_for_point(x_deposit, y_deposit) + TAU)
        print(f"Pheromone deposited at: x = {x_deposit}, y = {y_deposit}")

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
            new_pheromone_value = grid.get_pheromone_for_point(point_x, point_y) - 1

            if new_pheromone_value <= 0: #If new proposed value is 0 or negative, set the pheromone concentration value to 0
                grid.set_pheromone_for_point(point_x, point_y, 0)
            else:
                grid.set_pheromone_for_point(point_x, point_y, new_pheromone_value)

#### WIP ####
# def add_ant():
#     """
#     Function that adds an ant to the grid. Meant to be run once per timestep.
#     """


######## Wrapper simulation function - all functions for one step ########
def simulation_step(ants_on_grid, simulation_grid):    # WIP!!! Right now only working with one ant!!!!! 
    """
    Wrapper function for all things that need to happen in a simulation step.
    """
    # generate new ant per timestep
    # add_ant() # WIP function (below)

    # ant movement + ant deposition to new position
    for ant in ants_on_grid:
        move_ant(ant, simulation_grid)
        if ant.is_on_grid() == True:
            pheromone_deposition(ant, simulation_grid)
    # global grid evaporation
    pheromone_evaporation(simulation_grid)

# Visualization function
# needs to visualize both the C(x,t) values from the grid attribute of the Grid object and the ant location at the final timestep.
def visualize_grid(ants_on_grid, simulation_grid):
    """
    Function visualizes the grid and ants at one timestep. The grid shows pheromone concentrations (white - 0, grey - some, black - high), shows ant dots.
    """

    # showing grid pheromone concentration
    grid = simulation_grid.grid
    mp.figure()
    mp.imshow(grid, cmap = "Greys", origin = "upper")
    mp.colorbar(label = "Pheromone Concentration (C(x,t))")

    # showing ant 
    for ant in ants_on_grid:
        if ant.is_on_grid():
            x, y = ant.get_location()
            direction = ant.get_direction()

            angle = direction_to_angle[direction]
            mp.scatter(x, y, marker = (3, 0, angle), c="red", s=100)

    mp.show()

