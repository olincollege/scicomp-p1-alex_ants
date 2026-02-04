# Run simulation from this file


import simulation_setup as ss
import ants as a
import grid as g
import matplotlib.pyplot as mp


# Simulation 1
fidelity = 255 # according to Fig 3a from the paper
grid_size = 256
hill_loc = int(grid_size/2)
simulation_grid = g.Grid(grid_size, hill_loc)
ants_on_grid = [] # will store all ant objects on the grid

# First ant
p_straight = 0.5 # needed for simulation steps!
ant = a.Ant(x = hill_loc, y = hill_loc, p_straight = p_straight)
ants_on_grid.append(ant)

### for sanity checking ###
print(ants_on_grid)
print(simulation_grid)
# ss.visualize_grid(ants_on_grid, simulation_grid)

### run and print simulation ###
print ("####### DURING SIMULATION #######")
mp.figure()
num_steps = 1500
for i in range (num_steps):
    print(i)
    ss.simulation_step(ants_on_grid, simulation_grid, p_straight, fidelity)

    # sanity checking for pheromone concentration where ant disappears off grid
    # print(ant.is_on_grid)
    # ant_loc_x, ant_loc_y = ant.get_location()
    # print(simulation_grid.get_pheromone_for_point(ant_loc_x, ant_loc_y))
    # print(ants_on_grid)
    ##### SANITY CHECK #####
    # print(ant)
    # ss.visualize_grid(ants_on_grid, simulation_grid)
    ss.visualize_grid(
    ants_on_grid,
    simulation_grid,
    i,
    pause=0.01
    )
mp.show()

### sanity checking simulation run ###
print ("####### POST SIMULATION #######")
print(ants_on_grid)
print(ant)
print(simulation_grid.grid)
# ss.visualize_grid(ants_on_grid, simulation_grid)