import copy
from code.algorithms import randomise as randomise

class DepthFirst:
    """
    A Depth First algorithm that builds a stack of graphs with a unique assignment of nodes for each instance.
    """
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)
        self.states = [copy.deepcopy(self.grid)]

        # self.best_solution = None
        # self.best_value = float('inf')

        self.all_moves = []
        self.visited_states = []

        self.solution = []


    def get_next_state(self):
        """
        Method that gets the next state from the list of states.
        """
        return self.states.pop(0)

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
        empty_spaces_list = Randomise.find_empty_spaces(grid)

        # For all spaces find all possible moves
        for space in empty_spaces_list:

            # get the x and y axis of each empty spot
            relevant_rows = Randomise.get_relevant_rows(space, grid)

            # find cars that can move to the empty spot
            possible_cars = Randomise.get_possible_cars(relevant_rows[3],relevant_rows[2], relevant_rows[4],relevant_rows[5])

            # for each car in possible cars, move the car and create a new grid (child)
            for car in possible_cars:

                grid = Randomise.move_car(space, car, relevant_rows[0], relevant_rows[1], relevant_rows[5], relevant_rows[4], relevant_rows[3], relevant_rows[2], grid)

                # add the move to a list of all moves
                self.all_moves.append(space)

                # Add an instance of the graph to the stack, with each unique value assigned to the node.
                new_grid = copy.deepcopy(grid)
                self.states.append(new_grid)

                # add grid to visited states
                self.visited_states.append(grid)


    def check_is_visited(self, new_grid):
        """
        Checks if a child is already visited before.
        """
        if new_grid in self.visited_states:
            return True
        else:
            return False



    def check_solution(self, new_grid):
        """
        Check if the current state is a solution

        Checks and accepts better solutions than the current solution.

        Based on the amount of steps it took to reach a solution, save the best solution.
        keep track of the amount of steps it takes to go there
        """
        if len(self.grid[0]) == 6:
            victory_coordinates = [5, 2]
        elif len(self.grid[0]) == 9:
            victory_coordinates = [8, 4]
        elif len(self.grid[0]) == 12:
            victory_coordinates = [11, 5]

        if new_grid[victory_coordinates[1]][victory_coordinates[0]] == 'X':
            return True
        else:
            return False


    def run(self):
        """
        Runs the algorithm untill all possible states are visited.
        """
        # counter = 0

        while self.states:
            # counter += 1
            new_grid = self.get_next_state()

            for line in new_grid:
                print(line)
            print("")

            # if the grid is not already visited before, check for a solution and build new children
            # if self.check_is_visited(new_grid) == False:
                    

            if self.check_solution(new_grid) == True:

                return True

            self.build_children(new_grid)

        return False

                # else:
                #     self.solution = new_grid
                #     for line in self.solution:
                #         print(line)
                #     print("")

        # print("------------self.states-----------")
        # for state in self.states:
        #     for line in state:
        #         print(line)
        #     print("")
        
        
    

        # Update the input graph with the best result found.
        #self.grid = self.best_solution
        #print(self.grid)