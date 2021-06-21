
"""
pseudocode: 
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
from code.classes.model import Model
from .breadth_firstmayla import Breadthfirst
import random

class Hillclimber(Breadthfirst):
    def __init__(self):
        self.start_grid = ""
        self.end_grid = "" 
        self.path_check = ""

    def determine_path(self, path):
        length = len(path)
        self.path_check = random.randint(15, 25)
        start_value = random.randint(0, length - path_check)
        self.start_grid = path[start_value]
        self.end_grid = path[start_value + path_check]

    def check_path(self, grid):
        alt_path = self.find_solution_seq(grid)
        if len(alt_path) < self.path_check:
            self.alt_path = alt_path
            return True
        else:
            return False

    def check_solution(self, grid):
        if grid == self.end_grid:
            return True
        else:
            return False

    def go (self, path):
        self.determine_path(path)
        while self.tried < self.check_path:
            self.run()
            if self.check_solution(grid):
                self.check_path(grid)

