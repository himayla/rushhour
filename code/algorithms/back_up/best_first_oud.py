from .breadth_first import Breadthfirst
from code.heuristics import blocked_cars
from code.heuristics import advanced_block
from code.algorithms import randomise as rn
import csv
import copy



class BestFirst(Breadthfirst):
        def __init__(self, grid):

        # ---------- best first implementation -----# 
        self.pqueue = PriorityQueue()
        self.pqueue.put((1, copy.deepcopy(self.grid)))
        # ---------- best first implementation -----# 

    def get_next_state(self):
        """
        Method that gets the next state from the list of states.
        """
        return self.pqueue.get()

    def build_children(self, graph):
        """
        Attaches new grids to the self.states and creates a dictionary to keep track of which graphs result in which child-graphs.
        Sort each child on importance. Pick the n best children and only add them to the queue.
        """
        # Retrieve randomise.py Randomise class for useful functions
        rand_func = rn.Randomise(graph)

        # Creates a list with all empty spaces that exist on the graph
        empty_spaces = rand_func.find_empty_spaces(graph)
        scored_list = []

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
                move = rand_func.move_car(empty_spaces[space], car, x_values, y_values, left, right, upper, lower, new_graph[car])
                child = move[0]
                rel_move = move[1]
                if rel_move[1] == "H":
                    rel_distance = empty_spaces[space][0] - rel_move[0]
                    car_move = [car, rel_distance]
                    
                elif rel_move[1] == "V":
                    rel_distance = empty_spaces[space][1] - rel_move[0]
                    car_move = [car, rel_distance]
                    
                # If the new graph is not yet added to the dictionary of paths, add it. 
                if str(child) not in self.solution:
                    self.solution[str(child)] = [graph, car_move]

                
                # score grid based on a heuristic:

                #-------------------------------------- Block car heuristic ------------------------------------#
                # scored_child = blocked_cars.BlockCar().run(child)
                #-------------------------------------- Advanced block car heuristic ------------------------------------#
                scored_child = advanced_block.BlockCar().run(child)
  
                
                #-------------------------------------- Best first implementation ------------------------------------#
                # add move to a list of scored grids
                scored_list.append(scored_child) 
        
        # pick only the grid, not the score and loop through the list
        for item in scored_list:
            # If the new graph is not yet in the list of states to visit, add it.
            if item not in self.pqueue.queue:
                if item[1] not in self.tried:
                    self.pqueue.put(item)
            self.tried.append(item[1])

         #-------------------------------------- end Best first implementation ------------------------------------#



    def run(self):
        """
        Runs the algorithm untill a solution is found in a breadth first manner
        """
        # While there are still states to visit, stay in the loop
        while not self.pqueue.empty():

            # Pick a new graph
            new_graph_list = self.get_next_state()

            new_graph = new_graph_list[1]

            # Check if the graph is an acceptable result, if so, print out the solution
            if self.check_car_x(new_graph):
                path = self.find_solution_seq(new_graph)

                count = 0
                for board in path:
                    count += 1
                print(f"moves: {self.moves}")
                print(count)
                
                file = open('output.csv', 'w+', newline='')
                with file:
                    write = csv.writer(file)
                    write.writerows(self.moves)
                # with open("output.csv", 'w') as f:
                #     fc = csv.writer(f)
                # fc.writerows(self.moves)

                return path

            # If the graph is not an acceptable result, create possible "children" of the graph so more options can be visited
            else:
                self.build_children(new_graph)

