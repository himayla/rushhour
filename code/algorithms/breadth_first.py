"""
Algorithm that searches hoirzontally through the tree of children boards and finds the shortest possible path to the answer.
"""

from .depth_first import DepthFirst

class Breadthfirst(DepthFirst):
    
    def get_next_state(self):
        """
        Get the next board from the queue.
        """
        return self.states.pop(0)
