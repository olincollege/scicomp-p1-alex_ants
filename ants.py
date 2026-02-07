""" File containing ant class, move one grid space per turn. """

# imports
import numpy as np

# Global Variables - for follower ant
DIRECTION_VECTORS = [  # stores (dx, dy) lattice grid movement relative to current position for ant movement!!
    (0, -1),  # 0: Up
    (1, -1),  # 1: Up-Right
    (1, 0),  # 2: Right
    (1, 1),  # 3: Down-Right
    (0, 1),  # 4: Down
    (-1, 1),  # 5: Down-Left
    (-1, 0),  # 6: Left
    (-1, -1),  # 7: Up-Left
]


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

    def __init__(
        self, x=128, y=128, B=(0.360, 0.047, 0.008, 0.004), p_straight=0.581
    ):
        self.x = x
        self.y = y
        self.B = B
        self.p_straight = p_straight
        self.direction = np.random.randint(0, 8)
        self.state = "explorer"
        self.on_grid = True

    def __repr__(self):
        return (
            f"ant | x-loc: {self.x}, y-loc: {self.y}, direction:"
            f" {self.direction}, on grid: {self.on_grid}, state:"
            f" {self.get_state()}, probability forward movement:"
            f" {self.p_straight}, turning kernel (B): {self.B}"
        )

    # 'Get' functions
    def get_direction(self):
        """Gets the ant's intended direction to move."""
        return self.direction

    def get_location(self):
        """Gets ant's x, y location on the grid."""
        return self.x, self.y

    def get_state(self):
        """Gets ant's state: explorer or follower"""
        return self.state

    def is_on_grid(self):
        """Returns True is ant on grid, False if not."""
        return self.on_grid

    # 'Set' functions
    def set_location(self, x_new, y_new):
        """Updates x and y location of ant to new x and y location."""
        if isinstance(x_new, int) and isinstance(y_new, int):
            self.x = x_new
            self.y = y_new
        else:
            raise TypeError("Invalid data type; Ant location should be ints.")

    def set_ant_state(self, state_new):
        """Updates ant state to new state."""
        if isinstance(state_new, str):
            if state_new == "explorer" or state_new == "follower":
                self.state = state_new
            else:
                raise ValueError(
                    "Invalid state; Ant state should be either 'explorer' or"
                    " 'follower'."
                )
        else:
            raise TypeError("Invalid data type; Ant state should be a string.")

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

    def explorer_turn(self):
        """
        Function determines if explorer ant will move straight or randomly turn.

        Args:
            self: Ant object representing the ant.

        Returns:
            delta_turn: Int of value +/- 1, 2, 3, 4, 0 representing the number of 45 degree units to turn. If straight, the value is 0.
        """
        delta_turn = (
            self.new_random_delta_turn()
        )  # determines turn only based on turning kernel and probability to go straight
        return delta_turn

    ###### Follower Movement Determination ######
    def follower_turn(self, grid):
        """
        Function determines if follower ant will continue following path or switch to explorer.

        Args:
            self: Ant object representing the ant.
            grid: Grid representing grid used in simulation.

        Returns:
            delta_turn: Int of value +/- 1, 2, 3, 4, 0 representing the number of 45 degree units to turn. If straight, the value is 0.
        """
        ant_x, ant_y = self.get_location()
        # check the values of 7 - 0 - 1, so grid values to left, forward, and right
        forward_x, forward_y = DIRECTION_VECTORS[self.direction]  # grid space 0
        left_x, left_y = DIRECTION_VECTORS[
            (self.direction - 1) % 8
        ]  # grid space 7, represented as -1
        right_x, right_y = DIRECTION_VECTORS[
            (self.direction + 1) % 8
        ]  # grid space 1, represented as 1

        C_0 = grid.get_pheromone_for_point(ant_x + forward_x, ant_y + forward_y)
        C_1 = grid.get_pheromone_for_point(ant_x + right_x, ant_y + right_y)
        C_7 = grid.get_pheromone_for_point(ant_x + left_x, ant_y + left_y)
        if (
            C_0 > C_1 and C_0 > C_7
        ):  # if C(0) is > C(7) and C(1): # if trail moves forward
            delta_turn = 0
        elif (
            C_1 > C_7
        ):  # if C(1) > C(7): # if left concentration is greater than right C, move left
            delta_turn = 1
        elif (
            C_1 < C_7
        ):  # if C(7) > C(1): # if right C is greater than the left C, move right
            delta_turn = -1
        else:  # set state as explorer, run update_direction again
            self.set_ant_state("explorer")
            print("set state as explorer")
            delta_turn = self.explorer_turn()

        return delta_turn

    def update_direction(self, grid, fidelity):
        """
        Function updates ant direction. Determines the new "forward" direction in terms of 45 degree turn units (0-7). Positive is clockwise.
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
            grid: Grid object used in simulation.

        Returns:
            None
        """
        # determine if new state is explorer or follower
        new_state = self.determine_state(fidelity)

        if new_state == "explorer":
            delta_turn = self.explorer_turn()
        elif new_state == "follower":
            delta_turn = self.follower_turn(grid)

        new_direction = (
            self.direction + delta_turn
        ) % 8  # the remainder here turns the left "negative" delta_turns into 4, 5, 6, 7.

        self.set_direction(new_direction)

    # State determination function placeholder - will implement when multiple ants/second round of simulation
    def determine_state(self, fidelity):
        """
        Determines whether or not ant will be follower or explorer based on fidelity.

        Args:
            fidelity: Int representing the user input fidelity value. Probability that the ant will stay on the path.

        Returns:
            self.get_state(): String representing ant's state: explorer or follower"

        """
        if (
            np.random.randint(0, 257) < fidelity
        ):  # if the ant is staying a follower, not inclusive of 257, 0-256
            self.set_ant_state("follower")
            print("set state as follower")
        else:
            self.set_ant_state("explorer")
            print("set state as explorer")

        return self.get_state()


########### HELPER FUNCTIONS #########


def angle_of_turn(B):
    """
    Function generates a new turn angle with B kernel for an explorer ant's change in direction.

    Args:
        B: Tuple representing the turning kernels (B1, B2, B3, B4).
    Returns:
        angle_amount * turn_direction: Int of value +/- 1, 2, 3, 4 representing the number of 45 degree units to turn, and in which direction.
    """

    # use turning kernel B to randomize how many 45 degree directions the ant turns
    turn_angles = [
        1,
        2,
        3,
        4,
    ]  # each value represents turns in 45 degree increments; 0 is forward.

    # modifying 'B' so that values add up to 1 but probabilities are still the proportionally without:
    B_adjusted = tuple(np.array(B, dtype=float) / sum(B))

    angle_amount = np.random.choice(turn_angles, p=B_adjusted)

    # randomize left or right, 50% chance each way
    turn_direction = np.random.choice([-1, 1])

    return angle_amount * turn_direction
