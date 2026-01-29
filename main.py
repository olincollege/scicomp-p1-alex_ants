# Run simulation from this file


import simulation_setup as ss
import ants as a

# Simulation 1
grid_size = 16
hill_loc = int(grid_size/2)
simulation_grid = ss.Grid(size=grid_size, hill_loc=(hill_loc, hill_loc))
ants_on_grid = [] # will store all ant objects on the grid

# First ant
ant = a.Ant(x = hill_loc, y = hill_loc, p_straight=0.5)
ants_on_grid.append(ant)

### for sanity checking ###
print(ant)
print(simulation_grid)

### run and print simulation ###
print ("####### DURING SIMULATION #######")
num_steps = 10
for i in range (0, num_steps):
    ss.simulation_step(ants_on_grid, simulation_grid)
    ##### SANITY CHECK #####
    print(ant)

### sanity checking simulation run ###
print ("####### POST SIMULATION #######")
print(ants_on_grid)
print(ant)
print(simulation_grid.grid)
ss.visualize_grid(ants_on_grid, simulation_grid)