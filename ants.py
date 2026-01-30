# File containing ant class, move one grid space per turn.

# imports
import numpy as np


class Ant:
    """
    Represents an ant agent on the grid. 

    Attributes:
        x: Int representing x-location at current timestep. Default is 128.
        y: Int representing y-location at current timestep. Default is 128.
        direction: Int representing direction of the ant's movement from the previous timestep to current timestep; orients what direction is "forward".
        state: String representing state of ant: 'explorer' or 'follower'.
        B: Tuple representing the turning kernels (B1, B2, B3, B4). Default (0.360, 0.047, 0.008, 0.004) according to Fig 3 description.
        p_straight: Float between 0 and 1 representing the probability that an exploratory ant will go forward rather than turn. Default is 0.509; decimal percentage to get to 1 after summing all B kernels.
        on_grid
    """

    def __init__(self, x = 128, y = 128, B = (0.360, 0.047, 0.008, 0.004), p_straight = 0.509):
        self.x = x
        self.y = y
        self.B = B
        self.p_straight = p_straight
        self.direction = np.random.randint(0, 8)
        self.state = 'explorer' # self.determine_state() - WIP!! function is being implemented later, this is a placeholder FOR NOW
        self.on_grid = True

    def __repr__(self):
        return f"ant | x-loc: {self.x}, y-loc: {self.y}, direction: {self.direction}, on grid: {self.on_grid}, probability forward movement: {self.p_straight}, turning kernel (B): {self.B}"
    
    # 'Get' functions
    def get_direction(self):
        """Gets the ant's intended direction to move."""
        return self.direction
    
    def get_location(self):
        """Gets ant's x, y location on the grid."""
        return self.x, self.y
    
    def is_on_grid(self):
        """Returns True is ant on grid, False if not."""
        return self.on_grid
    
    # 'Set' functions
    def set_location(self, x_new, y_new):
        """Updates x and y location of ant to new x and y location."""
        self.x = x_new
        self.y = y_new

    def set_ant_state(self, state_new):
        """Updates ant state to new state."""
        self.state = state_new

    def set_direction(self, direction_new):
        """set ant direction to new angle."""
        self.direction = direction_new

    def set_on_grid(self, on_grid):
        """Sets ant as "off" grid; for when an ant crosses the grid boundary."""
        self.on_grid = on_grid


    ###### Exploratory Movement Determination ######
    def new_random_delta_turn(self):
        """
        Function determines if ant will move straight or randomly turn.

        Args:
            self: Ant object representing the ant.

        Returns:
            delta_turn: Int of value +/- 1, 2, 3, 4, 0 representing the number of 45 degree units to turn. If straight, the value is 0.
        """

        if np.random.rand() < self.p_straight:
            delta_turn = 0
        else:
            delta_turn = angle_of_turn(self.B)
        return delta_turn
    
    def update_direction(self):
        """
        Function updates ant direction with new delta_turn. Determines the new "forward" direction in terms of 45 degree turn units (0-7). Positive is clockwise.
        0: Forward
        1: Upper right (45 degrees)
        2: Right (90 degrees)
        3. Bottom right (135 degrees)
        4. Bottom/backward (180 degrees)
        5. Bottom left (225 degrees)
        6. Left (270 degrees)
        7. Upper left (315 degrees)
        
        Args:
            self: Ant object representing the ant.
        
        Returns:
            None
        """
        delta_turn = self.new_random_delta_turn()

        new_direction = (self.direction + delta_turn) % 8 # the remainder here turns the left "negative" delta_turns into 4, 5, 6, 7. 
        
        self.set_direction(new_direction)



    # State determination function placeholder - will implement when multiple ants/second round of simulation
    def determine_state(self):
        """WIP - Will return string representing ant's 'follower' or 'explorer' state."""



########### HELPER FUNCTIONS #########

def angle_of_turn(B):
    """
    Function generates a new random turn angle for an explorer ant's change in direction.

    Args:
        B: Tuple representing the turning kernels (B1, B2, B3, B4). Default (0.25, 0.25, 0.25, 0.25).
    Returns:
        angle_amount * turn_direction: Int of value +/- 1, 2, 3, 4 representing the number of 45 degree units to turn, and in which direction.
    """

    # use turning kernel B to randomize how many 45 degree directions the ant turns
    turn_angles = [1, 2, 3, 4] # each value represents turns in 45 degree increments; 0 is forward.
    angle_amount = np.random.choice(turn_angles, p = B)

    # randomize left or right, 50% chance each way
    turn_direction = np.random.choice([-1, 1])

    return (angle_amount * turn_direction)
