"""Contains global variables for all files in ants simulation."""

# ant states
EXPLORER = "explorer"
FOLLOWER = "follower"

# direction vectors
DIRECTION_VECTORS = [ # stores (dx, dy) lattice grid movement relative to current position for ant movement!!
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