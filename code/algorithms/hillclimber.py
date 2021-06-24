"""
Hillclimber algorithm doesn't produce a solution in a certain amount of moves like the other algorithms. 
The hillclimber uses the path that resulted from the other algorithms such as depth first or randomise, then tries to improve that path. 
The algorithm does that by selecting a part of the path and running a breadth first on that part to see if it is possible to shorten it. 
It will do that for as many iterations as is specified in the main.py. Then the shortest path is returned to main.py
"""
from .breadth_first import Breadthfirst
import random

class HillClimber(Breadthfirst):
    def __init__(self, path):
        self.start_board = ""
        self.end_board = ""
        self.path_check = ""
        self.path = path
        self.states = [self.start_board]
        self.visited_states = []
        self.solution = {}
        self.visited = set()
        self.moves = []


    def run(self, iterations):
        """
        For the number of iterations specified in main.py, the hillclimber will choose a random subset of the path. 
        On this path the breadth first algorithm is run until the end board is found. 
        Then the new path to the end board will be checked to see if it is shorter, and if so, replaces the original subset of the path. 
        After all the iterations are completed, the shortest found path is returned to the user in main.py
        """
        for i in range(iterations):
            self.determine_path(self.path)
            new_model = self.start_board
            while self.states: 
                if self.check_solution(new_model):
                    self.check_path(new_model)
                    break
                else:
                    self.build_children(new_model)
                if len(self.states) == 1:
                    break
                new_model = self.states.pop(1)
        return self.path


    def determine_path(self, path):
        """
        Determines the path and decides on a random subset of the path to run the breadth first algorithm on. 
        """
        length = len(path)

        # This number can be changed by the user if they'd rather use bigger subsets of the path to run the breadth first on. 
        if length > 80:
            self.path_check = random.randint(60, 80)
        else:
            self.path_check = random.randint(5,20)

        # Determines where in the path the subset will start
        self.start_value = random.randint(0, length - self.path_check)
        self.start_board = path[self.start_value]
        self.end_board = path[self.start_value + self.path_check - 1]


    def check_path(self, final_model):
        """
        Checks whether the newly found path is shorter than the original path. 
        If it is shorter, the relevant section of the path is replaced by the shorter path, if not, it's not. 
        """
        alt_path = self.find_solution_seq(final_model)
        
        if len(alt_path) < self.path_check:

            # If the start_value is 0, the new path will start with the alternative path. 
            if self.start_value == 0:
                new_path = alt_path + self.path[self.start_value + self.path_check:]
            else:
                new_path = self.path[0:self.start_value -1] + alt_path + self.path[self.start_value + self.path_check:]   
            
            self.path = new_path        
            return True
        

    def check_solution(self, board):
        """
        Checks solution to see whether the breadth first algorithm has reached the chosen end board of the subset of the path.
        """
        if board == self.end_board:
            return True