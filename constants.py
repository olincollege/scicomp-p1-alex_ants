"""Contains global variables for all files in ants simulation."""

# ant states
EXPLORER = "explorer"
FOLLOWER = "follower"

# direction vectors
# stores (dx, dy) lattice grid movement relative to current position for ant
#  movement!!
DIRECTION_VECTORS = [
    (0, -1),  # 0: Up
    (1, -1),  # 1: Up-Right
    (1, 0),   # 2: Right
    (1, 1),   # 3: Down-Right
    (0, 1),   # 4: Down
    (-1, 1),  # 5: Down-Left
    (-1, 0),  # 6: Left
    (-1, -1), # 7: Up-Left
]

# global pheromone evaporation rate (per step):
EVAP_RATE = 1

# ant heading direcitons for matplotlib visualization
DIRECTION_TO_ANGLE = {
    0:   0,     # Up
    1:  -45,    # Up-right
    2:  -90,    # Right
    3: -135,    # Down-right
    4:  180,    # Down
    5:  135,    # Down-left
    6:   90,    # Left
    7:   45,    # Up-left
}
