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

        self.solution = {}
        self.generations = {}
        self.generation_counter = 0

        self.end_of_branch = False
        


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
        rand_func = randomise.Randomise(grid)

        # Make a list of all empty spaces
        empty_spaces = rand_func.find_empty_spaces(grid)
        
        # For all spaces find all possible moves
        for space in range(len(empty_spaces)):

            # get the x and y axis of each empty spot
            directions = rand_func.get_relevant_rows(empty_spaces[space], grid)
            x_values = directions[0]
            y_values = directions[1]
            lower = directions[2]
            upper = directions[3]
            right = directions[4]
            left = directions[5]
            
            # find cars that can move to the empty spot
            cars = rand_func.get_possible_cars(upper, lower, right, left)
            children = []  
            new_grid = {} 

            self.generation_counter += 1

            # variable used to check if any child states are added, otherwise its an end of branch
            end_of_branch = copy.deepcopy(self.states)

            for car in cars:
                
                new_grid[car] = copy.deepcopy(grid)
                
                child = rand_func.move_car(empty_spaces[space], car, x_values, y_values, left, right, upper, lower, new_grid[car])

                # child cannot be an already existing state, or the previous move
                if child not in self.states and child not in self.visited_states:
                    self.visited_states.append(child)
                    self.states.append(child)
                    children.append(child)   

            # if there are no child states added, it is the end of the branch
            if len(end_of_branch) == len(self.states):
                self.end_of_branch = True
                print("end of branch")

            # if there are children, add them to the generations dictionary
            else:
                parent = grid       
                self.generations[str(parent)] = children
        
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
        counter = 0
        while self.states:
            counter = counter + 1
            new_grid = self.get_next_state()

            for line in new_grid:
                print(line)
            print("")

            # if the grid is not already visited before, check for a solution and build new children
            if self.check_solution(new_grid) == True:
                print(counter)
                
                
                # for generation, children in self.generations.items():
                #     if str(new_grid) in children:
                #         print(generation)

                
                
                return True

            self.build_children(new_grid)

        else:
            return False

        # for state in self.states:
        #     for line in state:
        #         print(line)
        #     print("")

        

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