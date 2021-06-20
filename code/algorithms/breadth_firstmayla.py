from .depth_first import DepthFirst


class Breadthfirst(DepthFirst):

    def get_next_state(self):
        """
        Method that gets the next state from the list of states.
        """
        return self.states.pop(0)