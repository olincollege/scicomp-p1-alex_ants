# Run simulation from this file


import simulation_setup as ss
import ants as a
import grid as g

# Simulation 1
fidelity = 255 # according to Fig 3a from the paper
grid_size = 4
hill_loc = int(grid_size/2)
simulation_grid = g.Grid(size=grid_size, hill_loc=(hill_loc, hill_loc))
ants_on_grid = [] # will store all ant objects on the grid

# First ant
ant = a.Ant(x = hill_loc, y = hill_loc, p_straight=0.5)
ants_on_grid.append(ant)

### for sanity checking ###
print(ant)
print(simulation_grid)
# ss.visualize_grid(ants_on_grid, simulation_grid)

### run and print simulation ###
print ("####### DURING SIMULATION #######")
num_steps = 3
for i in range (0, num_steps):
    print(i)
    ss.simulation_step(ants_on_grid, simulation_grid, fidelity)

    # sanity checking for pheromone concentration where ant disappears off grid
    print(ant.is_on_grid)
    ant_loc_x, ant_loc_y = ant.get_location()
    print(simulation_grid.get_pheromone_for_point(ant_loc_x, ant_loc_y))
    print(ants_on_grid)
    ##### SANITY CHECK #####
    print(ant)
    ss.visualize_grid(ants_on_grid, simulation_grid)

### sanity checking simulation run ###
print ("####### POST SIMULATION #######")
print(ants_on_grid)
print(ant)
print(simulation_grid.grid)
ss.visualize_grid(ants_on_grid, simulation_grid)