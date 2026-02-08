# Run simulation from this file


import simulation_setup as ss
import ants as a
import grid as g
import matplotlib.pyplot as mp


# Simulation 1
fidelity = 255  # according to Fig 3a from the paper
tau = 12 # according to Fig 3a from the paper
grid_size = 256
simulation_grid = g.Grid(grid_size)
ants_on_grid = []  # will store all ant objects on the grid

### for sanity checking ###
print(ants_on_grid)
print(simulation_grid)
print(simulation_grid.get_hill_loc())

### run and print simulation ###
print("####### DURING SIMULATION #######")
mp.figure()
num_steps = 1500
for i in range(num_steps):
    print(f"Step: {i}, num ants on grid: {len(ants_on_grid)}")
    # print(i)
    ss.simulation_step(ants_on_grid, simulation_grid, fidelity, tau)

    # sanity checking for pheromone concentration where ant disappears off grid
    # print(ant.is_on_grid)
    # ant_loc_x, ant_loc_y = ant.get_location()
    # print(simulation_grid.get_pheromone_for_point(ant_loc_x, ant_loc_y))
    # print(ants_on_grid)
    ##### SANITY CHECK #####
    # print(ant)
    # ss.visualize_grid(ants_on_grid, simulation_grid)
    ss.visualize_grid_live(ants_on_grid, simulation_grid, i, pause=0.01)
mp.show()

### sanity checking simulation run ###
print("####### POST SIMULATION #######")
print(ants_on_grid)
print(ant)
print(simulation_grid.grid)
print(
    f"Follower ants: {ss.total_F_value(ants_on_grid)}, Explorer ants:"
    f" {ss.total_L_value(ants_on_grid)}"
)
ss.visualize_grid(ants_on_grid, simulation_grid)
