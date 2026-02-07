# Scientific Computing Project 1: Ants

This repository holds the code for the first project in ENGR3560: Scientific Computing. The goal is to replicate the cellular automata model used to simulate the formation of trails of foraging ants, as detailed in the paper 'Modelling the Formation of Trail Networks by Foraging Ants' (Watmough, Edelstein-Keshet), 1995. The specific deliverables are recreations of Figure 3 (a, b, c) from the paper.

This is implemented in Python. Individual agents (ants) move on a Numpy Array (grid) and deposit pheromone as they move. Other ants can react to the pheromone levels and change their movement behavior from exploratory to following (a trail). The grid (and the ants) are visualized using MatPlotLib.

## Requirements

The `requirements.txt` file contains the required package imports:
- matplotlib~=3.7.2
- numpy~=1.24.3
- pytest~=7.4.0

## How to Use
1. Clone the repository:
```
git clone https://github.com/olincollege/scicomp-p1-alex_ants.git
cd scicomp-p1-alex_ants/
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run the simulation:
```
python main.py
```

## File Structure
ants.py - Contains Ant class and all helper functions, including explorer/follower decision making.

grid.py - Contains Grid class.

simulation_setup.py - Contains functions relevant to each simulation step.

ants_testing.py - Tests relevant functions from ants.py.

main.py - Main python file from which to run the code.

## Author
The creator of this repository is Alex Mineeva (amineeva).


## Sources
James Watmough, Leah Edelstein-Keshet,
Modelling the Formation of Trail Networks by Foraging Ants,
Journal of Theoretical Biology,
Volume 176, Issue 3,
1995,
Pages 357-371,
ISSN 0022-5193,
https://doi.org/10.1006/jtbi.1995.0205.
(https://www.sciencedirect.com/science/article/pii/S0022519385702056)
Abstract: This paper studies the role of chemical communication in the formation of trail networks by foraging ants. A cellular automaton model for the motion of the ants is formulated, which assumes that individuals interact according to a simple behavioural algorithm. The ants communicate by depositing trail markers composed of volatile chemicals that serve as attractants for other ants. The ants interact with the network both by following the trails and by extending and reinforcing the trails they follow. By varying the parameters describing these interactions we determine how variations in the behaviour of the individual ants lead to changes in the patterns of trail networks formed by the population. The results indicate that the ability of the group to form trails is inversely related with individual fidelity to trails.


## Other
### Reminder for Alex!!!
Run vvv before submitting!! And make sure to update the requirements list above ^^^
```
pipreqs --mode compat --force
```