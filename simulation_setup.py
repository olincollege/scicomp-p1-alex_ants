# Contains code to set up grid

# imports
import numpy as np

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
        return f"set size: {self.size}x{self.size}, hill_loc: {hill_loc}, grid: {np.zeros}"


# Visualization function
# needs to visualize both the C(x,t) values from the grid attribute of the Grid object and the ant location at the final timestep. 