"""
Algorithm that uses the breadth first approach to find the shortest possible path to the answer
"""
import copy
from code.algorithms import randomise as rn

class Breadthfirst:
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)
        self.states = [copy.deepcopy(self.grid)]
        self.solution = {}
        self.tried = []
        self.board_til_final = []
        
    def get_next_state(self):
        """
        Method that gets the next state from the list of states.
        """
        return self.states.pop(0)

    def build_children(self, graph):
        """
        Attaches new grids to the self.states and creates a dictionary to keep track of which graphs result in which child-graphs. 
        """
        # Retrieve randomise.py Randomise class for useful functions
        rand_func = rn.Randomise(graph)

        # Creates a list with all empty spaces that exist on the graph
        empty_spaces = rand_func.find_empty_spaces(graph)

        # For each empty space that exists in the list of empty spaces
        for space in range(len(empty_spaces)):
            directions = rand_func.get_relevant_rows(empty_spaces[space], graph)
            x_values = directions[0]
            y_values = directions[1]
            lower = directions[2]
            upper = directions[3]
            right = directions[4]
            left = directions[5]

            # Creates a list of all cars that can move to that empty space
            cars = rand_func.get_possible_cars(upper, lower, right, left)
            new_graph = {}     

            # For each car that can move to that same empty space:   
            for car in cars:
                new_graph[car] = copy.deepcopy(graph)

                # Move each car and save the result of the movement in child variable
                child = rand_func.move_car(empty_spaces[space], car, x_values, y_values, left, right, upper, lower, new_graph[car])
                
                # If the new graph is not yet added to the dictionary of paths, add it. 
                if str(child) not in self.solution:
                    self.solution[str(child)] = graph
                
                # If the new graph is not yet in the list of states to visit, add it.
                if child not in self.states and self.tried:
                    self.states.append(child)
                self.tried.append(child)


    def check_car_x(self, new_graph):
        """
        Create victory coordinates based on the size of the graph.
        If the car X reaches the victory coordinates, return True 
        """
        if len(self.grid[0]) == 6:
            victory_coor = [5, 2]
        elif len(self.grid[0]) == 9:
            victory_coor = [8, 4]
        elif len(self.grid[0]) == 12:
            victory_coor = [11, 5]
      
        if new_graph[victory_coor[1]][victory_coor[0]] == 'X':
            return True
        else:
            return False

    def find_solution_seq(self, final_graph):
        """
        Based on the final graph, trace back the previous graphs using the self.solution nested dictionary. 
        If the original graph is found, return the list of all graphs used to reach the final graph, in chronological order
        """
        path = [final_graph]
        if str(final_graph) not in str(self.grid):
            previous_state = self.solution[str(final_graph)]
            path = self.find_solution_seq(previous_state) + path   
                   
        return path

    def run(self):
        """
        Runs the algorithm untill a solution is found in a breadth first manner
        """
        # While there are still states to visit, stay in the loop
        while self.states:

            # Pick a new graph
            new_graph = self.get_next_state()

            # Check if the graph is an acceptable result, if so, print out the solution
            if self.check_car_x(new_graph):
                path = self.find_solution_seq(new_graph)

                count = 0
                for board in path:
                    count += 1
                print(count)

                return path

            # If the graph is not an acceptable result, create possible "children" of the graph so more options can be visited
            else:
                self.build_children(new_graph)