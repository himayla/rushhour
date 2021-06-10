'''

'''
import copy
from code.algorithms import randomise as rn

class Depthfirst:
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)
        self.states = [copy.deepcopy(self.grid)]
        self.solution = []
        

    def build_children(self):
        """
        Attaches new grids to the self.states
        pseudocode:
        1. Check which empty spaces exist
        2. if cars can move there:
            3. move each one and store the new grid
        4. if not:
            5. check next empty space
        
        """
        rand_func = rn.Randomise(self.grid)
        empty_spaces = rand_func.find_empty_spaces()
        print(f"empty space: {empty_spaces}")
        for space in range(len(empty_spaces)):

            rows = rand_func.get_relevant_rows(empty_spaces[space])
            print(f"space: {empty_spaces[space]}")
            print(f"rows: {rows}")

            cars = rand_func.choose_random_car(rows[0], rows[1], rows[2], rows[3])
            print(f"cars: {cars}")

    def run(self):
        """
        Runs the algorithm untill all possible states are visited.
        """
        self.build_children()
        # while self.states:
        #     new_graph = self.get_next_state()

        #     # Retrieve the next empty node.
        #     node = new_graph.get_empty_node()

        #     if node is not None:
        #         self.build_children(new_graph, node)
        #     else:
        #         # Stop if we find a solution
        #         # break

        #         # or ontinue looking for better graph
        #         self.check_solution(new_graph)

        # # Update the input graph with the best result found.
        # self.graph = self.best_solution