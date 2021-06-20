"""
Depth first algorithm to find the first possible solution.
"""
import copy
from code.algorithms import randomise as randomise

class DepthFirst:
    """
    A Depth First algorithm that builds a stack of graphs with a unique assignment of nodes for each instance.
    """
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)
        self.states = [copy.deepcopy(self.grid)]
        self.visited_states = []
        self.generations = {}
        self.shortest_path= []

    def get_next_state(self):
        """
        Method that gets the next state from the list of states.
        """
        return self.states.pop()

    def build_children(self, grid):
        """
        Attaches new grids to the self.states and creates a dictionary to keep track of which graphs result in which child-graphs. 
        """
        # Retrieve randomise.py Randomise class for usefull funcitons
        rand_func = randomise.Randomise(grid)

        # Make a list of all empty spaces
        empty_spaces = rand_func.find_empty_spaces(grid)
        
        # For all spaces find all possible moves
        for space in range(len(empty_spaces)):

            # Get the x and y axis of each empty spot
            directions = rand_func.get_relevant_rows(empty_spaces[space], grid)
            x_values = directions[0]
            y_values = directions[1]
            lower = directions[2]
            upper = directions[3]
            right = directions[4]
            left = directions[5]
            
            # Find cars that can move to the empty spot
            cars = rand_func.get_possible_cars(upper, lower, right, left)
            children = []  
            new_grid = {} 

            # For each car, move the car on the grid to create a child state.
            for car in cars:

                new_grid[car] = copy.deepcopy(grid)
                move = rand_func.move_car(empty_spaces[space], car, x_values, y_values, left, right, upper, lower, new_grid[car])
                child = move[0]
                # The child cannot be already generated
                if child not in self.states and child not in self.visited_states:
                    self.states.append(child)

                # If we already came across the child, but this child has a shorter path, then pick this new path
                if child in self.visited_states:
                    path_child = self.find_solution_seq(child)
                    path_parent = self.find_solution_seq(grid)

                    child_path_count = 0
                    for board in path_child:
                        child_path_count += 1

                    parent_path_count = 0
                    for board in path_parent:
                        parent_path_count += 1

                    if parent_path_count + 1 < child_path_count:
                        self.generations[str(child)] = grid

                # If the child is not new, add it to the list of visited states and add it to the generations dictionary
                else:
                    self.generations[str(child)] = grid
                    self.visited_states.append(child)

        
    def check_is_visited(self, new_grid):
        """
        Checks if a child is already visited before.
        """
        if new_grid in self.visited_states:
            return True
        else:
            return False


    def find_solution_seq(self, final_graph):
        """
        Based on the final graph, trace back the previous graphs using the self.generations nested dictionary. 
        If the original graph is found, return the list of all graphs used to reach the final graph, in chronological order
        """
        path = [final_graph]
        if str(final_graph) not in str(self.grid):
            previous_state = self.generations[str(final_graph)]
            path = self.find_solution_seq(previous_state) + path   
                   
        return path


    def check_solution(self, new_grid):
        """
        Check if the current state is a solution.
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
        Runs the algorithm untill a solution is found.
        """
        while len(self.states) != 0:

            # If there is a map on the top of the stack, get it
            new_grid = self.get_next_state()

            # Check if this grid is a solution  
            if self.check_solution(new_grid) == True:

                # Find the path for this solution
                path = self.find_solution_seq(new_grid)

                count = 0
                for board in path:
                    count += 1
                print(count)

                return path


            # Build new children
            else:
                self.build_children(new_grid)