"""
Algorithm that uses the breadth first approach to find the shortest possible path to the answer
"""
from code.algorithms import randomise as rn

class Breadthfirst:
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)
        self.states = [copy.deepcopy(self.grid)]
        self.solution = {}
        self.tried = []
        self.moves = [["car", "move"]]

        # ---------- best first implementation -----# 
        self.pqueue = PriorityQueue()
        self.pqueue.put((1, copy.deepcopy(self.grid)))
        # ---------- best first implementation -----# 