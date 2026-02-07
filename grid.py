""" File containing Grid class, creates the grid for the simulation. """

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

    def __init__(self, size=256, hill_loc=128):
        self.size = size
        self.hill_loc = hill_loc
        self.grid = np.zeros((size, size))
    
    def __repr__(self):
        return f"Grid size = {self.size}x{self.size}, hill_loc = {self.hill_loc}x{self.hill_loc})"

    # 'Get' Functions
    def get_size(self):
        """Gets grid size."""
        return self.size
    
    def get_hill_loc(self):
        """Gets hill location."""
        return self.hill_loc
    
    def get_pheromone_for_point(self, x, y):
        """Gets pheromone value for one point on the grid. Returns C = 0 if point off grid.
        """
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            return 0
        else:
            return self.grid[y, x]
    
    def set_pheromone_for_point(self, x, y, value):
        """Sets new pheromone value for one point on the grid."""
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            return
        self.grid[y, x] = value

