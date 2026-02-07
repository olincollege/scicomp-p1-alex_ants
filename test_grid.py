"""Unit tests for grid.py"""

# imports
import pytest
import numpy as np
import grid as g

######## initialize ########

def test_default_initialization():
    """Check default initialization values."""
    grid = g.Grid()

    assert grid.size == 256
    assert grid.hill_loc == 128
    assert grid.grid.shape == (256, 256)
    assert np.all(grid.grid == 0)


def test_custom_size_initialization():
    """Check grid initialization with custom size."""
    grid = g.Grid(size=100)

    assert grid.size == 100
    assert grid.hill_loc == 50
    assert grid.grid.shape == (100, 100)

def test_custom_size_initialization_odd():
    """Check grid initialization with custom size that is not an even number."""

    with pytest.raises(ValueError, match="Invalid size input; size input must"\
    " be even."):
        g.Grid(size=101)


def test_custom_size_initialization_invalid_type():
    """Check grid initialization with wrong type input for size."""
    with pytest.raises(TypeError, match="Invalid input type; size input must"\
    " be an int."):
        g.Grid(size=101)

######## get function tests ########

def test_get_size():
    """Check function get_size()."""
    grid = g.Grid(100)

    assert grid.get_size() == 100

def test_get_hill_loc():
    """Check function get_hill_loc()."""
    grid = g.Grid(80)

    assert grid.get_hill_loc() == 40

######## get_pheromone_inside_grid tests ########

def test_get_pheromone_inside_grid():
    """Check get_pheromone_inside_grid(), valid value."""
    grid = g.Grid(10)

    grid.grid[3, 4] = 5

    value = grid.get_pheromone_for_point(4, 3)

    assert value == 5

def test_get_pheromone_out_of_bounds_negative():
    """Check get_pheromone_inside_grid(), negative value."""
    grid = g.Grid(10)

    assert grid.get_pheromone_for_point(-1, 5) == 0

    assert grid.get_pheromone_for_point(5, -1) == 0

def test_get_pheromone_out_of_bounds_large():
    """Check get_pheromone_inside_grid(), outisde grid bounds."""
    grid = g.Grid(10)

    assert grid.get_pheromone_for_point(10, 5) == 0

    assert grid.get_pheromone_for_point(5, 10) == 0

######## set_pheromone_for_point tests ########

def test_set_pheromone_for_point():
    """Checks that set_pheromone_for_point function sets the right pheromone at
     the correct spot."""
    grid = g.Grid(size = 30)

    grid.set_pheromone_for_point(2, 3, 47)

    assert grid.grid[3, 2] == 47

def test_set_pheromone_out_of_bounds_negative():
    """Check set_pheromone_for_point if input bound is negative."""
    grid = g.Grid(10)

    grid.set_pheromone_for_point(-1, 2, 5)

    # Grid should remain unchanged
    assert np.all(grid.grid == 0)

def test_set_pheromone_out_of_bounds_large():
    """Check set_pheromone_for_point if input bound larger than grid size."""
    grid = g.Grid(10)

    grid.set_pheromone_for_point(15, 2, 5)

    assert np.all(grid.grid == 0)

######## test and set combination test ########

def test_set_then_get():
    """Check that the set and get pheronomone functions work."""
    grid = g.Grid(20)

    grid.set_pheromone_for_point(5, 6, 8)

    value = grid.get_pheromone_for_point(5, 6)

    assert value == 8
