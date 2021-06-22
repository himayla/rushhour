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

class HillClimber(Breadthfirst):
    def __init__(self, path):
        self.start_board = ""
        self.end_board = ""
        self.path_check = ""
        self.path = path
        self.stat_value = ""
        self.count = int(0)
        self.states = [self]
        self.visited_states = []
        self.solution = {}
        self.tried = set()
        self.moves = []

    def determine_path(self, path):
        length = len(path)
        self.path_check = random.randint(15, 25)
        self.start_value = random.randint(0, length - self.path_check)
        self.start_board = path[self.start_value]
        self.end_board = path[self.start_value + self.path_check - 1]

    def check_path(self, final_model):
        alt_path = self.find_solution_seq(final_model)
        
        if len(alt_path) < self.path_check:
            for board in range(self.start_value, self.start_value + self.path_check):
                self.path[board] = alt_path[board]
                if board > len(alt_path):
                    del self.path[board]
                    print(f"did something useful!")
            self.count = 0
            # self.run(iterations)
            return True
        else:
            self.count +=1
            # print(f"was not useful but still fun")
            # self.run(iterations)
            return False

    def check_solution(self, board):
        # print(f"board: {board.board}")
        # print(f"end board: {self.end_board.board}")
        if board == self.end_board:
            # print(f"found something!")
            # breakpoint()
            return True
        else:
            return False

    def run(self, iterations):
        for i in range(iterations):
            count = 0
            self.determine_path(self.path)
            while self.states:
                # for state in range(len(self.states*1000)):
                new_model = self.path[count]
                count +=1
                if self.check_solution(new_model):
                    self.check_path(new_model)
                    break
                else:
                    self.build_children(new_model)
        return self.path


        
