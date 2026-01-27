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
    
    def update_location(self, x_new, y_new):
        """Updates x and y location of ant to new x and y location."""
        self.x = x_new
        self.y = y_new

    def set_ant_state(self, state_new):
        """Updates ant state to new state."""
        self.state = state_new