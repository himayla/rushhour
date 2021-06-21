"""
pseudo van mila
input is path
count = 0
1. Get a random board from the path that's at least 25 moves away from the final board. 
2. Choose another board between 15 and 25 further down the path. 
3. Do a breath first algorithms on the first chosen board and save the steps in a dictionary. 
4. When the final board is found:
5. If the path to the final board is smaller than the path that was given originally to the algorithm. 
    6. Put the moves of the breadth first algorithm into the place of the original path
    count += 1
7. Else:
    8. Repeat with another combination of boards. 
    count = 0
9. if count = 100 / 1000 / 100000:
    return path
"""

import copy
import random

from code.algorithms import randomise_mayla as rn

class HillClimber:
    
    def __init__(self, model):
        self.model = model.copy()
        self.solution = {}

    def get_random_solution(self, new_model):
        pass
        #1. Get a random board from the path 

        # 1. One that's at least 25 moves away from the final board.

        # 2. Another board between 15 and 25 further down the path

    def check_solution(self, new_model):
        pass
        # Breadth search the first chosen board and save the steps in a dictionary. 

        # dict[board] = steps

        # when the final board is found:
            #return

    def compare_solutions(self, solution):
        pass
        #If the path to the final board is smaller than the path that was given originally to the algorithm. 
        # 6. Put the moves of the breadth first algorithm into the place of the original path
        #count += 1

        #Else:
        #8. Repeat with another combination of boards. 
        #count = 0

        #9. if count = 100 / 1000 / 100000:
        #return path
        

    def run(self, iterations, paths):
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        """
        self.iterations = iterations

        for iteration in range(iterations):

            # Create a copy of the model to simulate the change
            new_model = self.model.copy()

            #1. Get 2 random boards
            solution = self.get_random_board(new_model)

            #3. Breadth search these boards
            solution_1 = self.check_solution(solution)

            # Compare solutions
            self.compare_solutions(solution_1)