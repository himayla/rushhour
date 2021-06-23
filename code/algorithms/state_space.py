"""
Algorithm to print the state-space for a playing board by exploring all possible child states using a breadth first algorithm.
"""
from .breadth_first import Breadthfirst

class StateSpace(Breadthfirst):

    def run(self):
        """
        Runs the algorithm until all possible child boards are found.
        """
        while self.states:

            # Print out the number of children found
            print(len(self.visited))

            # If there is a board on the top of the stack, get it
            new_board = self.get_next_state()

            self.build_children(new_board)