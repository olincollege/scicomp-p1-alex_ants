"""Unit tests for grid.py"""

# imports
import pytest
import grid as g
import numpy as np

######## initialize ########

def test_default_initialization():
    """
    Check default initialization values.
    """
    grid = g.Grid()

    assert grid.size == 256
    assert grid.hill_loc == 128
    assert grid.grid.shape == (256, 256)
    assert np.all(grid.grid == 0)


def test_custom_size_initialization():
    """
    Check grid initialization with custom size.
    """
    grid = g.Grid(size=100)

    assert grid.size == 100
    assert grid.hill_loc == 50
    assert grid.grid.shape == (100, 100)

def test_custom_size_initialization_odd():
    """
    Check grid initialization with custom size that is not an even number.
    """

    with pytest.raises(ValueError, match="Invalid size input; size input must be even."):
        grid = g.Grid(size=101)

def test_custom_size_initialization_invalid_type():
    """
    Check grid initialization with wrong type input for size.
    """
    with pytest.raises(TypeError, match="Invalid input type; size input must be an int."):
        grid = g.Grid(size=101)



######## get function tests ########

def test_get_size():
    """Check function get_size()."""
    grid = g.Grid(100)

    assert grid.get_size() == 100


def test_get_hill_loc():
    """Check function get_hill_loc()."""
    grid = g.Grid(80)

    assert grid.get_hill_loc() == 40


# ---------- __repr__ Test ----------

def test_repr():
    grid = Grid(50)

    rep = repr(grid)

    assert "Grid size = 50x50" in rep
    assert "25x25" in rep


# ---------- get_pheromone_for_point Tests ----------
def test_get_pheromone_inside_grid():
    grid = Grid(10)

    grid.grid[3, 4] = 2.5

    value = grid.get_pheromone_for_point(4, 3)

    assert value == 2.5


def test_get_pheromone_out_of_bounds_negative():
    grid = Grid(10)

    assert grid.get_pheromone_for_point(-1, 5) == 0
    assert grid.get_pheromone_for_point(5, -1) == 0

def test_get_pheromone_out_of_bounds_large():
    grid = Grid(10)

    assert grid.get_pheromone_for_point(10, 5) == 0
    assert grid.get_pheromone_for_point(5, 10) == 0


# ---------- set_pheromone_for_point Tests ----------



def test_set_pheromone_for_point():
    """
    Checks that set_pheromone_for_point function sets the right pheromone at the correct spot.
    """
    grid = g.Grid(size = 30)

    grid.set_pheromone_for_point(2, 3, 47)

    assert grid.grid[3, 2] == 47


def test_set_pheromone_out_of_bounds_negative():
    grid = Grid(10)

    grid.set_pheromone_for_point(-1, 2, 5)

    # Grid should remain unchanged
    assert np.all(grid.grid == 0)


def test_set_pheromone_out_of_bounds_large():
    grid = Grid(10)

    grid.set_pheromone_for_point(10, 2, 5)

    assert np.all(grid.grid == 0)


# ---------- Integration Test ----------

def test_set_then_get():
    grid = Grid(20)

    grid.set_pheromone_for_point(5, 6, 3.14)

    value = grid.get_pheromone_for_point(5, 6)

    assert value == 3.14

