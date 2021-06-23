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
from .breadth_first import Breadthfirst
import random
import copy

class HillClimber(Breadthfirst):
    def __init__(self, path):
        self.start_board = ""
        self.end_board = ""
        self.path_check = ""
        self.path = path
        self.stat_value = ""
        self.states = [self.start_board]
        self.visited_states = []
        self.solution = {}
        self.visited = set()
        self.moves = []

    def determine_path(self, path):
        length = len(path)
        if length > 80:
            self.path_check = random.randint(60, 80)
        else:
            self.path_check = random.randint(5,20)
        self.start_value = random.randint(0, length - self.path_check)
        self.start_board = path[self.start_value]
        self.end_board = path[self.start_value + self.path_check - 1]

    def check_path(self, final_model):
        alt_path = self.find_solution_seq(final_model)
        
        if len(alt_path) < self.path_check:
            
            if self.start_value == 0:
                new_path = alt_path + self.path[self.start_value + self.path_check:]
            else:
                new_path = self.path[0:self.start_value -1] + alt_path + self.path[self.start_value + self.path_check:]   
            
            self.path = new_path        
            return True
        else:
            return False

    def check_solution(self, board):
        if board == self.end_board:
            return True
        else:
            return False

    def run(self, iterations):
        for i in range(iterations):
            self.determine_path(self.path)
            new_model = self.start_board
            while self.states: 
                if self.check_solution(new_model):
                    self.check_path(new_model)
                    break
                else:
                    self.build_children(new_model)
                if len(self.states) ==1:
                    break
                new_model = self.states.pop(1)
        return self.path


        
