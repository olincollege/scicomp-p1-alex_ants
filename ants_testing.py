"""Unit tests for ants.py"""

import pytest
import ants as a

def test_orb_sys_oneplanet_oneplanet():
    """
    Check that valid orbital system created with one central planet, one planet orbiting
    """
    central_object = Planet("Mars", 3390, 6.4191*10**23, 0, 0, 0, 1.5, "rocky")
    orbiting_object = Planet("Earth", 6371, 5.972e24, 0, 0, 0, 1.0, "rocky")
    system = OrbitalSystem("Test system", central_object)
    system.add_orbiting_object(orbiting_object)

    assert system.orbiting_objects_list() == "Orbiting Objects in Test system: Earth"



# set functions
def test_set_ant_state_explorer():
    """
    Check that set_ant_state function sets state as: 'explorer'
    """
    ant = a.Ant()

    # testing explorer
    ant.set_ant_state('explorer')
    assert ant.get_state() == 'explorer'

def test_set_ant_state_follower():
    """
    Check that set_ant_state function sets state as: 'follower'
    """
    ant = a.Ant()

    # testing follower
    ant.set_ant_state('follower')
    assert ant.get_state() == 'follower'

def test_set_ant_state_invalid():
    """
    Check that set_ant_state function cannot be set as something other than 'explorer' or 'follower'.
    """
    ant = a.Ant()

    # testing invalid state setting
    with pytest.raises(ValueError, match="Invalid state; Ant state should be either 'explorer' or 'follower'.")
        ant.set_ant_state('blah')

    with pytest.raises(TypeError, match="Invalid data type; Ant state should be a string.")

    