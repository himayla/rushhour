"""
NIET AF!
Pseudocode:
    While True:
        1. Kies een random (geldige) staat:
        2. Herhaal x iteraties
            2.1 Kopieer de staat
            2.2 Muteer de kopie
            2.3 Check of staat is verbeterd. [len(moves to exit?) < len(moves)]
                2.4 Indien beter vervang oude staat door nieuwe
"""
import copy
import random

from code.algorithms import randomise_mayla as rn

class HillClimber:
    
    def __init__(self, model):
        self.model = model.copy()

    def check_solution(self, new_model):
        """
        Checks and accepts better solutions than the current solution.
        """
        new_value = new_model.calculate_value()
        old_value = self.value

        # We are looking for maps that cost less!
        if new_value <= old_value:
            self.model = new_model
            self.value = new_value

    def run(self, iterations, verbose=False):
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        """
        self.iterations = iterations

        for iteration in range(iterations):
            # Nice trick to only print if variable is set to True
            print(f'Iteration {iteration}/{iterations}, current value: {self.value}') if verbose else None

            # Create a copy of the model to simulate the change
            new_model = self.model.copy()

            self.mutate(new_model)

            # Accept it if it is better
            self.check_solution(new_model)