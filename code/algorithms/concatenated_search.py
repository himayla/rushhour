from .breadth_first import Breadthfirst
from code.heuristics import blocked_cars
from code.heuristics import advanced_block
from code.algorithms import randomise as rn
import numpy as np

class ConcatenatedSearch(Breadthfirst):

    def build_children(self, model):
        """
        Attaches new grids to the self.states and creates a dictionary to keep track of which graphs result in which child-graphs. 
        """
        empty_spaces = model.get_empty_spaces(model.board)

        for space in range(len(empty_spaces)):
            directions = model.get_relevant_rows(empty_spaces[space])
 
            # Find cars that can move to the empty spot
            cars = model.get_possible_cars(directions)

            # For each car, move the car on the grid to create a child state.
            for car in cars:
                new_model = model.copy()

                # Move each car and save the result 
                new_move = new_model.move_car(empty_spaces[space], car, directions)

                new_board = new_move[0]
                rel_move = new_move[1]
                if rel_move[1] == "H":
                    rel_distance = empty_spaces[space][0] - rel_move[0]
                    car_move = [car, rel_distance]
                    
                elif rel_move[1] == "V":
                    rel_distance = empty_spaces[space][1] - rel_move[0]
                    car_move = [car, rel_distance]
                    
                # If the new graph is not yet added to the dictionary of paths, add it. 
                if str(new_board) not in self.solution:
                    self.solution[str(new_board)] = [model, car_move]
                
                # If the new graph is not yet in the list of states to visit, add it.
                if new_model not in self.visited_states:
                    self.states.append(new_model)
                    self.visited_states.add(new_model)
                
                scored_list = []

                # score grid based on a heuristic
                #-------------------------------------- blocked car heuristic ------------------------------------#
                # scored_child = blocked_cars.BlockCar().run(child)
                #-------------------------------------- Advanced block heuristic ------------------------------------#
                scored_child = advanced_block.BlockCar().run(new_board)
                # add move to a list of scored grids

                scored_list.append(scored_child)

                # TODO: check of er een standaard afwijking zit in de scores, als zo is, sorteer dan en selecteer de beste

                # sort the list of dictionaries, higest first
                #-------------------------------------- Sort the scores ------------------------------------#
                sorted_scores = sorted(scored_list, key=lambda k: list(k.values())[0], reverse=True)
                numbers = []
                # Make a list of scores and determine their standard deviation
                for item in sorted_scores:
                    for value in item.items():
                        numbers.append(value[1][0])

                standard_dev = np.std(numbers)
                # CALIBRATE THIS SHIT
                if standard_dev > 4:

                    ranking = []
                    # pick amount of children you want to select
                    n = 4
                    # for beam search, pick only the first n items in the list
                    for number in range(0, len(sorted_scores)):
                        if number <= n:
                            ranking.append(sorted_scores[number])
                        # pick only the grid, not the score and loop through the list
                    for move in ranking:
                        for key, value in move.items():
        
                        # If the new graph is not yet in the list of states to visit, add it.
                            if value[1] not in self.states and self.tried:
                                self.states.append(value[1])
                            self.tried.append(value[1])
                #-------------------------------------- end beam search implementation ------------------------------------#
                else:
                    for move in sorted_scores:
                        for key, value in move.items():
        
                            # If the new graph is not yet in the list of states to visit, add it.
                            if value[1] not in self.states and self.tried:
                                self.states.append(value[1])
                            self.tried.append(value[1])
                #-------------------------------------- end best first implementation ------------------------------------#