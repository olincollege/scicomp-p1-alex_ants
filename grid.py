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
        hill_loc: Int of ant hill location, default 128. Calculated from size.
        grid: Numpy 2D array of points.
    """

    def __init__(self, size:int=256)->None:
        if isinstance(size, int): # checking grid input type
            if size % 2 == 0: # checking if grid size even
                if size > 0: # checking if grid size above 0
                    self.size = size
                    self.hill_loc = int(size/2)
                    self.grid = np.zeros((size, size))
                else:
                    raise ValueError("Invalid size input, size input must be larger than 0.")
            else:
                raise ValueError("Invalid size input; size input must be even.")
        else:
            raise TypeError("Invalid input type; size input must be an int.")

    def __repr__(self)->str:
        return (
            f"Grid size = {self.size}x{self.size}, hill_loc ="
            f" {self.hill_loc}x{self.hill_loc})"
        )

    ######## 'Get' Functions ########
    def get_size(self)->int:
        """Gets grid size."""
        return self.size

    def get_hill_loc(self)->int:
        """Gets hill location."""
        return self.hill_loc

    def get_pheromone_for_point(self, x:int, y:int)->int:
        """Gets pheromone value for one point on the grid. Returns C = 0 if
          point off grid."""
        if not self._in_bounds(x, y):
            return 0
        else:
            return self.grid[y, x]

    ######## 'Set' Functions ########
    def set_pheromone_for_point(self, x:int, y:int, value:int)->None:
        """Sets new pheromone value for one point on the grid."""
        if not self._in_bounds(x, y):
            return
        self.grid[y, x] = value

    ######## Helper Function ########
    def _in_bounds(self, x:int, y:int)->int:
        """Checks if (x, y) is inside grid."""
        in_bounds = 0 <= x < self.size -1 and 0 <= y < self.size -1
        return in_bounds
