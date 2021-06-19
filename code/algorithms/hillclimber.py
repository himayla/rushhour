"""
Pseudocode:
    While True:
        1. Kies een random (geldige) staat:
        2. Herhaal x iteraties
            2.1 Kopieer de staat
            2.2 Muteer de kopie
            2.3 Check of staat is verbeterd. [len(moves to exit?) < len(moves)]
                2.4 Indien beter vervang oude staat door nieuwe
"""

import copy
import random

from code.algorithms import randomise as rn

class HillClimber:

    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)
        self.states = [copy.deepcopy(self.grid)]
        self.visited_states = []
        self.generations = {}
        self.shortest_path= []



    def build_children(self, grid):
        # Retrieve randomise.py Randomise class for usefull funcitons
        rand_func = rn.Randomise(grid)

        # Make a list of all empty spaces
        empty_spaces = rand_func.find_empty_spaces(grid)
        
        # For all spaces find all possible moves
        for space in range(len(empty_spaces)):

            # Get the x and y axis of each empty spot
            directions = rand_func.get_relevant_rows(empty_spaces[space], grid)
            x_values = directions[0]
            y_values = directions[1]
            lower = directions[2]
            upper = directions[3]
            right = directions[4]
            left = directions[5]
            
            # Find cars that can move to the empty spot
            cars = rand_func.get_possible_cars(upper, lower, right, left)
            children = []  
            new_grid = {} 

            # For each car, move the car on the grid to create a child state.
            for car in cars:

                new_grid[car] = copy.deepcopy(grid)
                child = rand_func.move_car(empty_spaces[space], car, x_values, y_values, left, right, upper, lower, new_grid[car])
                
                # The child cannot be already generated
                if child not in self.states and child not in self.visited_states:
                    self.states.append(child)

                # If we already came across the child, but this child has a shorter path, then pick this new path
                if child in self.visited_states:
                    path_child = self.find_solution_seq(child)
                    path_parent = self.find_solution_seq(grid)

                    child_path_count = 0
                    for board in path_child:
                        child_path_count += 1

                    parent_path_count = 0
                    for board in path_parent:
                        parent_path_count += 1

                    if parent_path_count + 1 < child_path_count:
                        self.generations[str(child)] = grid

                # If the child is not new, add it to the list of visited states and add it to the generations dictionary
                else:
                    self.generations[str(child)] = grid
                    self.visited_states.append(child)


    def run(self, iterations, verbose=False):
        """
        Runs the algorithm untill a solution is found.
        """
        self.iterations = iterations

        for iteration in range(iterations):
            # Nice trick to only print if variable is set to True
            print(f'Iteration {iteration}/{iterations}, current value: {self.value}') if verbose else None

            # Create a copy of the model to simulate the change
            new_model = self.model.copy()


            # new_grid = self.get_next_state()

            # if self.check_solution(new_grid) == True:

            #     path = self.find_solution_seq(new_grid)

            #     count = 0
            #     for board in path:
            #         count += 1
            #     print(count)

            #     return path
            # else:
            #     self.build_children(new_grid)
    




