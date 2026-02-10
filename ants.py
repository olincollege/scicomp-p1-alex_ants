""" File containing ant class, move one grid space per turn. """

# imports
import numpy as np
import grid as g

######## Global Variables ########
from constants import DIRECTION_VECTORS, EXPLORER, FOLLOWER


######## Ant class ########
class Ant:
    """
    Represents an ant agent on the grid. 

    Attributes:
        x: Int representing x-location at current timestep. Default is 128.
        y: Int representing y-location at current timestep. Default is 128.
        direction: Int representing direction of the ant's movement from the
         previous timestep to current timestep; orients what direction is
         "forward".
        state: String representing state of ant: 'explorer' or 'follower'.
        B: Tuple representing the turning kernels (B1, B2, B3, B4). Default
          (0.360, 0.047, 0.008, 0.004) according to Fig 3 description.
        p_straight: Float between 0 and 1 representing the probability that an
          exploratory ant will go forward rather than turn. Default is 0.509;
            decimal percentage to get to 1 after summing all B kernels.
        on_grid
    """

    def __init__(self, x:int = 128, y:int = 128,
                 B:tuple[float, float, float, float] =
                 (0.360, 0.047, 0.008, 0.002))-> None:
        self.x = x
        self.y = y
        self.B = B
        self.p_straight = 1-sum(B) # default 0.581
        self.direction = np.random.randint(0, 8)
        self.state = EXPLORER
        self.on_grid = True

    def __repr__(self)->str:
        return f"ant | x-loc: {self.x}, y-loc: {self.y}, direction: {self.direction}, on grid: {self.on_grid}, state: {self.get_state()}, probability forward movement: {self.p_straight}, turning kernel (B): {self.B}"

    ######## 'Get' Functions ########
    def get_direction(self)->int:
        """Gets the ant's intended direction to move."""
        return self.direction

    def get_location(self)->tuple[int, int]:
        """Gets ant's x, y location on the grid."""
        return self.x, self.y

    def get_state(self)->str:
        """Gets ant's state: explorer or follower"""
        return self.state

    def is_on_grid(self)->bool:
        """Returns True is ant on grid, False if not."""
        return self.on_grid

    ######## 'Set' Functions ########
    def set_location(self, x_new:int, y_new:int)->None:
        """Set ant location."""
        if not isinstance(x_new, int) and isinstance(y_new, int):
            raise TypeError("Invalid data type; Ant location should be ints.")
        self.x = x_new
        self.y = y_new

    def set_ant_state(self, state_new:str)->None:
        """Set ant state."""
        if isinstance(state_new, str):
            if state_new in {EXPLORER, FOLLOWER}:
                self.state = state_new
            else:
                raise ValueError("Invalid state; Ant state should be either " \
                "EXPLORER or FOLLOWER.")
        else:
            raise TypeError("Invalid data type; Ant state should be a string.")

    def set_direction(self, direction_new:int)->None:
        """set ant direction to new angle."""
        self.direction = direction_new

    def set_on_grid(self, on_grid:bool)->None:
        """Sets ant as "off" when an ant crosses the grid boundary."""
        self.on_grid = bool(on_grid)


    ######## Explorer Movement Determination ########
    def _new_delta_turn(self)->int:
        """
        Function determines if ant will move straight or randomly turn.
        Used by explorer ants.

        Args:
            None.

        Returns:
            delta_turn: Int of value +/- 1, 2, 3, 4, 0 representing the number
              of 45 degree units to turn. If straight, the value is 0.

        """
        # deciding whether to go straight or turn; if random float between 0
        # and 1 is less than probability to go straight, ant will contine
        # straight. If not, the ant turns; the amount is randomized form
        # turning kernel B.
        if np.random.rand() < self.p_straight:
            delta_turn = 0
        else:
            delta_turn = angle_of_turn(self.B)
        return delta_turn

    def explorer_turn(self)->int:
        """
        Function determines if explorer ant will move straight or randomly
          turn.

        Args:
            None

        Returns:
            delta_turn: Int of value +/- 1, 2, 3, 4, 0 representing the number
              of 45 degree units to turn. If straight, the value is 0.

        """
        # determines turn only based onturning kernel and probability to go
        #  straight
        delta_turn = self._new_delta_turn()
        return delta_turn

    ######## Follower Movement Determination ########
    def _follower_pheromone_scan(self, direction_to_scan:int, grid:g.Grid,
                                  x:int, y:int)->int:
        """
        Returns pheromone value of step in direction to scan.

        Args:
            direction_to_scan: Int representing direction of grid space where
              ant may move on the next time step.
            grid: Grid representing grid used in simulation.
            x: ant's current x location on the grid.
            y: ant's current y location on the grid.

        Returns:
            pheromone: Int representing pheromone level at grid space ant is
              looking at in direction_to_scan.

        """
        dx, dy = DIRECTION_VECTORS[direction_to_scan]
        pheromone = grid.get_pheromone_for_point(x + dx, y + dy)
        return pheromone

    def follower_turn(self, grid:g.Grid)->int:
        """
        Function determines if follower ant will continue following path or
          switch to explorer.

        Args:
            grid: Grid representing grid used in simulation.

        Returns:
            delta_turn: Int of value +/- 1, 2, 3, 4, 0 representing the number
              of 45 degree units to turn. If straight, the value is 0.

        """
        x, y = self.get_location()

        forward = self.direction
        left = (forward - 1) % 8 # grid space 7
        right = (forward + 1) % 8 # grid space 1

        # check the values of 7 - 0 - 1, so grid values to left, forward, and
        #  right
        C_0 = self._follower_pheromone_scan(forward, grid, x, y)
        C_1 = self._follower_pheromone_scan(right, grid, x, y)
        C_7 = self._follower_pheromone_scan(left, grid, x, y)

        # path determination based on concentrations in the top left
        #  (-45degree), forward (0 degree), and right (45degree) grid spaces
        if C_0 > C_1 and C_0 > C_7: # if forward space has most pheromone, trail moves forward
            delta_turn = 0
        elif C_1 > C_7: # if C(1) > C(7): # if left concentration is greater than right concentration, move left
            delta_turn = 1
        elif C_1 < C_7: # if C(7) > C(1): # if right concentration is greater than the left concentration, move right
            delta_turn = -1
        else: # set state as explorer, run update_direction again
            self.set_ant_state(EXPLORER)
            delta_turn = self.explorer_turn()

        return delta_turn


    def update_direction(self, grid:g.Grid, fidelity:int)->None:
        """
        Function updates ant direction. Determines the new "forward" direction
          in terms of 45 degree turn units (0-7). Positive is clockwise.
        Imagine a 3x3 grid, with the ant occupying the central space:
        0: Forward
        1: Upper right (45 degrees)
        2: Right (90 degrees)
        3. Bottom right (135 degrees)
        4. Bottom/backward (180 degrees)
        5. Bottom left (225 degrees)
        6. Left (270 degrees)
        7. Upper left (315 degrees)
        
        Args:
            grid: Grid object used in simulation.
            fidelity: Int representing the user input fidelity value.
              Probability that the ant will stay on the path.
        
        Returns:
            None

        """
        # determine if new state is explorer or follower
        new_state = self.determine_state(fidelity)

        if new_state == EXPLORER:
            delta_turn = self.explorer_turn()
        else:
            delta_turn = self.follower_turn(grid)

        # self.direction (0-7, according to 3x3 grid around ant) + delta_turn
        #  (-4:+4) can be from -4 to 11.
        # the % allows the negative numbers to map to the left turn blocks
        #  (4-7), and the positive numbers to map to the right turn blocks
        #  (1-4)/
        new_direction = (self.direction + delta_turn) % 8

        self.set_direction(new_direction)


    def determine_state(self, fidelity:int)->str:
        """
        Determines whether ant is follower or explorer based on fidelity.

        Args:
            fidelity: Int representing the user input fidelity value.
              Probability that the ant will stay on the path.

        Returns:
            self.get_state(): String representing ant's state: explorer or
              follower
        
        """
        if np.random.randint(0, 257) < fidelity: # if the ant is staying a follower, not inclusive of 257, 0-256
            self.set_ant_state(FOLLOWER)
        else:
            self.set_ant_state(EXPLORER)

        return self.get_state()


######## Turning angle function ants ########

def angle_of_turn(B:tuple[float, float, float, float])->int:
    """
    Function generates a new turn angle with B kernel for an explorer ant's
      change in direction.

    Args:
        B: Tuple representing the turning kernels (B1, B2, B3, B4).
    Returns:
        angle_amount * turn_direction: Int of value +/- 1, 2, 3, 4 representing
          the number of 45 degree units to turn, and in which direction.

    """

    # use turning kernel B to randomize how many 45 degree directions the ant
    #  turns
    turn_angles = [1, 2, 3, 4] # each value represents turns in 45 degree increments; 0 is forward.

    # modifying B so that values add up to 1 but probabilities are still
    #  proportional:
    B_adjusted = tuple(np.array(B, dtype=float) / sum(B))

    angle_amount = np.random.choice(turn_angles, p = B_adjusted)

    # randomize left or right, 50% chance each way
    turn_direction = np.random.choice([-1, 1])

    return (angle_amount * turn_direction)
