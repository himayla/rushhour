import copy
from code.algorithms import randomise as randomise

class DepthFirst:
    """
    A Depth First algorithm that builds a stack of graphs with a unique assignment of nodes for each instance.
    """
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)
        self.cars = cars

        self.states = [copy.deepcopy(self.grid)]

        self.best_solution = None
        self.best_value = float('inf')


    def get_next_state(self):
        """
        Method that gets the next state from the list of states.
        """
        return self.states.pop()

    def build_children(self, grid):
        """
        Creates all possible child-states and adds them to the list of states.

        Pseudo:
        grid  -> 
        list of empty spaces -> 
        for all spaces find all possible moves ->
        add to list of states.

        """
        # Retrieve randomise.py Randomise class for usefull funcitons
        Randomise = randomise.Randomise(grid)

        # Make a list of all empty spaces
        empty_spaces_list = Randomise.find_empty_spaces(self)

        # For all spaces find all possible moves
        for space in empty_spaces_list:

            # get the x and y axis of each empty spot
            relevant_rows = Randomise.get_relevant_rows(space)

            # find cars that can move to the empty spot
            possible_cars = Randomise.get_possible_cars(relevant_rows[3],relevant_rows[2], relevant_rows[4],relevant_rows[5])

            # for each car in possible cars, move the car and create a new grid (child)
            for car in possible_cars:

                grid = Randomise.move_car(space, car, relevant_rows[0], relevant_rows[1], relevant_rows[5], relevant_rows[4], relevant_rows[3], relevant_rows[2])

                # Add an instance of the graph to the stack, with each unique value assigned to the node.
                new_grid = copy.deepcopy(grid)
                self.states.append(new_grid)

    def check_solution(self, new_graph):
        """
        Checks and accepts better solutions than the current solution.

        Based on the amount of steps it took to reach a solution
        """

        new_value = new_graph.calculate_value()
        old_value = self.best_value

        # choose the list_of_moves with the fewest items, and save that board
        ##
        if new_value <= old_value:
            self.best_solution = new_graph
            print(f"New best solution: {self.best_value}")

    def run(self):
        """
        Runs the algorithm untill all possible states are visited.
        """
        while self.states:
            new_grid = self.get_next_state()

            # if the stack is not empty, build new children
            if new_grid is not None:
                self.build_children(new_grid)

            # save this solution if this is the best solution
            else:
                self.check_solution(new_grid)

        # Update the input graph with the best result found.
        self.grid = self.best_solution
        print(self.grid)