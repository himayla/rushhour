from .depth_first import DepthFirst


class StateSpace(DepthFirst):
    """
    Loop breadth first through all the children, until no more children can be made
    """

    def get_next_state(self):
        """
        Method that gets the next state from the list of states.
        """
        return self.states.pop(0)

    
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