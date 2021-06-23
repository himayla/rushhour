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
        self.count = int(0)
        self.states = [self.start_board]
        self.visited_states = []
        self.solution = {}
        self.visited = set()
        self.moves = []

    def determine_path(self, path):
        length = len(path)
        # self.path_check = random.randint(100, 120)
        self.path_check = 194
        # self.start_value = random.randint(0, length - self.path_check)
        self.start_value = 0
        self.start_board = path[self.start_value]
        self.end_board = path[self.start_value + self.path_check - 1]

    def check_path(self, final_model):
        alt_path = self.find_solution_seq(final_model)
        
        if len(alt_path) < self.path_check:
            # print(f"start: {self.start_value}")
            print(f"check: {self.path_check}")
            print(f"lengte: {len(self.path)}")
            board_index = self.start_value + self.path_check -1
            # for board in range(self.start_value, self.start_value + self.path_check - 1):
                # print(f"board: {self.path[board]}")
                # if board >= len(alt_path):
                #     # GET RID OF THE REST
                #     self.path.remove(self.path[board_index])
                    
                #     board_index = board_index -1
                    
                # else:
                #     self.path[self.start_value + board] = alt_path[board]
                # if board < len(alt_path):
                #     self.path[self.start_value + board] = alt_path[board]
            for board in range(self.start_value, len(alt_path) - 1):
                self.path[self.start_value + board] = alt_path[board]
            for board2 in range(len(alt_path), self.path_check -1):
                self.path.remove(self.path[len(alt_path)])
                self.path_check = self.path_check -1
                
            print(f"lengte: {len(self.path)}")
                    
            self.count = 0
            # print(len(self.path))
            print(f"ben klaar")
            return True
        else:
            self.count +=1
            return False

    def check_solution(self, board):
        # print(f"board: {board.board}")
        # print(f"end: {self.end_board.board}")
        # print(f"start:{type(board)}")
        # print(f"eind: {type(self.end_board)}")
        if board == self.end_board:
            return True
        else:
            return False

    def run(self, iterations):
        for i in range(iterations):
            self.determine_path(self.path)
            new_model = self.start_board
            # print(f"new_model1: {new_model}")
            while self.states: 
                
                # print(f"new model: {new_model}")
                if self.check_solution(new_model):
                    # print(f"laatste board gevond")
                    self.check_path(new_model)
                    break
                else:
                    # print(f"new_model2: {new_model}")
                    self.build_children(new_model)
                    # print(f"self.states: {self.states}")
                new_model = self.states.pop(1)
        return self.path


        
