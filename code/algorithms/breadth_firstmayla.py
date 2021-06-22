"""
Algorithm that uses the breadth first approach to find the shortest possible path to the answer.
"""
#MK: ^ een betere uitleg van 'breadth first approach', iets in trant van: zoekt de oplossingen door elke generatie horizontaal te bekijken?

from .depth_first_mayla2 import DepthFirst


class Breadthfirst(DepthFirst):

    def get_next_state(self):
        """
        Method that gets the next state from the list of states.
        """
        return self.states.pop(0)