"""Unit tests for ants.py"""

import pytest
import ants as a


######## set_ant_state ########
def test_set_ant_state_explorer():
    """Check that set_ant_state function sets state as: 'explorer'"""
    ant = a.Ant()

    # testing explorer
    ant.set_ant_state("explorer")
    assert ant.get_state() == "explorer"

def test_set_ant_state_follower():
    """Check that set_ant_state function sets state as: 'follower'"""
    ant = a.Ant()

    # testing follower
    ant.set_ant_state("follower")
    assert ant.get_state() == "follower"

def test_set_ant_state_invalid():
    """Check that set_ant_state function cannot be set as something other than 
    'explorer' or 'follower'."""
    ant = a.Ant()

    # testing invalid state setting
    with pytest.raises(
        ValueError,
        match=(
            "Invalid state; Ant state should be either 'explorer' or"
            " 'follower'."
        ),
    ):
        ant.set_ant_state("blah")

    with pytest.raises(
        TypeError, match="Invalid data type; Ant state should be a string."
    ):
        ant.set_ant_state(30)


######## set_location ########
def test_set_location_valid():
    """Check that set_location function only sets x and y integer positions. 
    Valid (int) x and y locations."""
    ant = a.Ant()

    # testing valid location
    ant.set_location(10, 10)
    assert ant.get_location() == (10, 10)

def test_set_location_both_invalid():
    """Check that set_location functions only sets x and y integer positions."""
    ant = a.Ant()

    # both x and y invalid
    with pytest.raises(
        TypeError, match="Invalid data type; Ant location should be ints."
    ):
        ant.set_location(1.0, "hello")

def test_set_location_x_invalid():
    """Check that set_location functions only sets x and y integer positions.
      X invalid."""
    ant = a.Ant()

    # both x and y invalid
    with pytest.raises(
        TypeError, match="Invalid data type; Ant location should be ints."
    ):
        ant.set_location(3.5, 10)

def test_set_location_y_invalid():
    """Check that set_location functions only sets x and y integer positions. 
    Y invalid."""
    ant = a.Ant()

    # both x and y invalid
    with pytest.raises(
        TypeError, match="Invalid data type; Ant location should be ints."
    ):
        ant.set_location(10, "woah")
