'''

'''
import copy
from code.algorithms import randomise as rn
from collections import deque

class Depthfirst:
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)
        self.states = [copy.deepcopy(self.grid)]
        self.solution = {}
        self.tried = []
        
    def get_next_state(self):
        """
        Method that gets the next state from the list of states.
        """
        return self.states.pop(0)

    def build_children(self, graph):
        """
        Attaches new grids to the self.states
        pseudocode:
        1. Check which empty spaces exist
        2. if cars can move there:
            3. move each one and store the new grid
        4. if not:
            5. check next empty space
        """

        rand_func = rn.Randomise(graph)
        empty_spaces = rand_func.find_empty_spaces(graph)
        
        for space in range(len(empty_spaces)):
            directions = rand_func.get_relevant_rows(empty_spaces[space], graph)
            x_values = directions[0]
            y_values = directions[1]
            lower = directions[2]
            upper = directions[3]
            right = directions[4]
            left = directions[5]
            
            cars = rand_func.get_possible_cars(upper, lower, right, left)
            children = []  
            new_graph = {}       
            for car in cars:
                
                new_graph[car] = copy.deepcopy(graph)
                
                child = rand_func.move_car(empty_spaces[space], car, x_values, y_values, left, right, upper, lower, new_graph[car])
                if child not in self.states:
                    self.states.append(child)
                    children.append(child)   
                # self.tried.append(child)          
                
                # print("grid")
                # for line in child:
                #     print(line)
                
                self.solution[str(new_graph[car])] = children

        
          
                
    def check_car_x(self, new_graph):
        if len(self.grid[0]) == 6:
            victory_coor = [5, 2]
        elif len(self.grid[0]) == 9:
            victory_coor = [8, 4]
        elif len(self.grid[0]) == 12:
            victory_coor = [11, 5]
        # print(f"vic_coor: {new_graph[victory_coor[1]][victory_coor[0]]}")
        if new_graph[victory_coor[1]][victory_coor[0]] == 'X':
            return True
        else:
            return False

    def find_solution_seq(self, final_graph):
        counter = 0
        for generation in self.solution:
            counter +=1
            if str(final_graph) in generation:
                print(f"moves: {counter}")  

    def run(self):
        """
        Runs the algorithm untill all possible states are visited.
        """
        
        childcounter = 0
        while self.states:
            new_graph = self.get_next_state()
            # print("grids:")
            # for line in new_graph:
            #     print(line)
            
            if self.check_car_x(new_graph):
                print(f"final board")
                for line in new_graph:
                    print(line)
                self.find_solution_seq(new_graph)
                
                # print(f"amount of moves: {layers}")
                break
            else:
                self.build_children(new_graph)
            # if childcounter < 10:
            #     print("new generation:")
            #     for line in self.solution:
            #         print(line) 
            childcounter +=1

            # if childcounter % 1000 == 0: 
            #     print(f"new grid: {childcounter}")
            #     for line in new_graph:
            #         print(line)
                
            
                
        
        
