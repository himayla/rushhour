from .breadth_first import Breadthfirst
from code.heuristics import blocked_cars
from code.algorithms import randomise as rn
import csv
import copy


class BestFirst(Breadthfirst):

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
                
                #-------------------------------------- Best first implementation ------------------------------------#
                # score grid based on a heuristic

                scored_child = blocked_cars.BlockCar().run(move[0])
                
                # add move to a list of scored grids

                scored_list.append(scored_child) 

        

        # TODO: check of er een standaard afwijking zit in de scores, als zo is, sorteer dan en selecteer de beste

        # sort the list of dictionaries, higest first
        
        sorted_scores = sorted(scored_list, key=lambda k: list(k.values())[0], reverse=True)
        
        # pick only the grid, not the score and loop through the list
        for move in sorted_scores:
            
            for key in move:

        #-------------------------------------- end Best first implementation ------------------------------------#
                
                child = key[0]
                rel_move = key[1]
                if rel_move[1] == "H":
                    rel_distance = empty_spaces[space][0] - rel_move[0]
                    car_move = [car, rel_distance]
                    
                elif rel_move[1] == "V":
                    rel_distance = empty_spaces[space][1] - rel_move[0]
                    car_move = [car, rel_distance]
                    
                # If the new graph is not yet added to the dictionary of paths, add it. 
                if str(child) not in self.solution:
                    self.solution[str(child)] = [graph, car_move]
                
                # If the new graph is not yet in the list of states to visit, add it.
                if child not in self.states and self.tried:
                    self.states.append(child)
                self.tried.append(child)