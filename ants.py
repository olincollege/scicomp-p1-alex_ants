# File containing ant class, move one grid space per turn.


class Ant:
    """
    Represents an ant agent on the grid. 

    Attributes:
        x: Int representing x-location at current timestep.
        y: Int representing y-location at current timestep.
        direction: Int representing direction angle of last movement; movement to current timestep.
        state: String representing state of ant: 'explorer' or 'follower'.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"x-loc: {self.x}, y-loc: {self.y}"
    
    def set_location(self, x_new, y_new):
        """Updates x and y location of ant to new x and y location."""
        self.x = x_new
        self.y = y_new

    def set_ant_state(self, state_new):
        """Updates ant state to new state."""
        self.state = state_new

    def set_direction(self, direction_new):
        """Updates ant direction to new angle."""
        self.direction = direction_new


# Functions #

 # 50/50 chance for turning left or right
def determine_new_direction_angle(Ant):
 """
 Function determines new angle to rotate. 0 degrees is straight, 180 degrees

 Args:

 Returns:
 """

 def establish_simulation(system, orbiting_objects_dictionary, time):
    """
    Function used within run_simulation in order to create the initial system vectors. Defines intial position conditions. 

    Args:
        orbiting_objects_dictionary: Dictionary of objects, orbiting within system.
        time: Numpy array (vector) holding a timestep-ed time vector in years

    Returns:
        positions: Dictionary for x, y, z positions of each orbiting object
        velocities: Dictionary for x, y, z velocities of each orbiting object
        angular_velocities: Dictionary for angular velocity of each orbiting object
        orbit_radii: Dictionary for distances between system center and each orbiting object
        parent: Dictionary with parent of object - only applies to Orbital Systems within Orbital Systems
    """
    num_steps = len(time)
    