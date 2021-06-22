"""
Simple state space algorithm to calculate the state space for a playing board. 
Loops in a breadth first manner through all possible child states.
"""
from .breadth_firstmayla import Breadthfirst


# veranderen naar breadth first
class StateSpace(Breadthfirst):

    def run(self):
        """
        Runs the algorithm untill a solution is found.
        """
        while self.states:

            print(len(self.visited_states))

            # If there is a map on the top of the stack, get it
            new_grid = self.get_next_state()

            # build children
            self.build_children(new_grid)