""" File containing Grid class, creates the grid for the simulation. """

# imports
import numpy as np


# Grid class
class Grid:
    """
    Object representing the square grid on which ants travel. Grid values
      represent pheromone concentration.

    Attributes:
        size: Int representing the number of points of grid, default 256 for a
          256x256 point grid.
        hill_loc: Tuple with ant hill location, default (128, 128).
        grid: Numpy 2D array of points.
    """

    def __init__(self, size:int=256)->None:
        if isinstance(size, int):
            if size % 2 == 0:
                self.size = size
                self.hill_loc = int(size/2)
                self.grid = np.zeros((size, size))
            else:
                raise ValueError("Invalid size input; size input must be even.")
        else:
            raise TypeError("Invalid input type; size input must be an int.")

    def __repr__(self)->str:
        return (
            f"Grid size = {self.size}x{self.size}, hill_loc ="
            f" {self.hill_loc}x{self.hill_loc})"
        )

    # 'Get' Functions
    def get_size(self)->int:
        """Gets grid size."""
        return self.size

    def get_hill_loc(self)->int:
        """Gets hill location."""
        return self.hill_loc

    def get_pheromone_for_point(self, x:int, y:int)->int:
        """Gets pheromone value for one point on the grid. Returns C = 0 if
          point off grid."""
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            return 0
        else:
            return self.grid[y, x]

    def set_pheromone_for_point(self, x:int, y:int, value:int)->None:
        """Sets new pheromone value for one point on the grid."""
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            return
        self.grid[y, x] = value
