# Contains code to set up grid

# imports
import numpy as np

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
        self.grid = np.zeros(size, size)
    
    def __repr__(self):
        return f"Grid(size={self.size}x{self.size}, hill_loc={self.hill_loc})"

    
    def get_size(self):
        """Gets grid size."""
        return self.size


# Simulation step functions
def move_ant(ant, grid):
    """
    Function moves the ant one lattice grid in the ant's chosen direction.

    Args:
        ant: Ant object representing ant that needs to be moved for one step of the simulation.
        grid: Grid object representing the grid on which the ant needs to move. 
    
    Returns:
        None.
    """
    ant_direction = ant.get_direction() # gets the 0-7 direction where ant is headed relative to 0 being 'up'.
    ant_x, ant_y = ant.get_location() # gets current x/y location of ant

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


# Visualization function
# needs to visualize both the C(x,t) values from the grid attribute of the Grid object and the ant location at the final timestep.

