"""
This algorithm...
"""

from .depth_first import Depthfirst
from code.heuristics import blocked_cars

class BeamSearch(Breadthfirst):

    def build_children(self, model):
        """
        Attaches new grids to the self.states and creates a dictionary to keep track of which graphs result in which child-graphs.
        Sort each child on importance. Pick the n best children and only add them to the queue.
        """

        #   COPY PASTE FROM DEPTH_FIRST [insert here]

        # Initialize scores for the children
        scored_list = []

        scored_child = blocked_cars.BlockCar().run(child)
        
        # Add move to a list of scored grids
        scored_list.append(scored_child) 

        # Sort the list of dictionaries, higest first
        sorted_scores = sorted(scored_list, key=lambda k: list(k.values())[0], reverse=True)

        ranking = []

        # Pick the amount of children to select
        n = 100

        # To perform a beam search, only use the first n items in the list
        if len(sorted_scores) <= n:
            for number in range(0, len(sorted_scores)):
                ranking.append(sorted_scores[number])
        else:
            for number in range(0, n):
                ranking.append(sorted_scores[number])
                
        # Pick only the grid, not the score and loop through the list #MK: snap ik niet?
        for move in ranking:
            for key, value in move.items():
    #-------------------------------------- end beam search implementation ------------------------------------#
            # If the new graph is not yet in the list of states to visit, add it
                if value[1] not in self.states and self.tried:
                    self.states.append(value[1])
                self.tried.append(value[1])