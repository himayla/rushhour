"""
This algorithm...
"""
from .breadth_first import Breadthfirst
from code.heuristics import advanced_block

class BeamSearch(Breadthfirst):

    def build_children(self, model):
        """
        Attaches new grids to the self.states and creates a dictionary to keep track of which graphs result in which child-graphs. 
        """
        empty_spaces = model.get_empty_spaces(model.board)

        for space in range(len(empty_spaces)):
            directions = model.get_relevant_rows(empty_spaces[space])

            # Find cars that can move to the empty spot
            possible_cars = model.get_possible_cars(directions)


            # For each car, move the car on the grid to create a child state.
            for car in possible_cars:
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
                
                #-------------------------------------- Beam search implementation ------------------------------------#
                scored_list = []

                # Score the current board based on the heuristic
                scored_child = advanced_block.BlockCar().run(new_model)
                
                # Add move to a list of scored grids
                scored_list.append(scored_child) 
    
                # Sort the list of dictionaries, higest first
                sorted_scores = sorted(scored_list, key=lambda k: list(k.values())[0], reverse=True)

                ranking = []

                # Pick the amount of children to select
                n = 3

                # To perform a beam search, only use the first n items in the list
                if len(sorted_scores) <= n:
                    for number in range(0, len(sorted_scores)):
                        ranking.append(sorted_scores[number])
                else:
                    for number in range(0, n):
                        ranking.append(sorted_scores[number])

                # Pick only the grid, not the score and loop through the list #MK: snap ik niet?
                for move in ranking:
                    for key, value in move.items():
                        # print(f"value: {value[1]}")
            #-------------------------------------- End beam search implementation ------------------------------------
                        # If the new graph is not yet in the list of states to visit, add it
                        if value[1] not in self.states and value[1] not in self.visited:
                            self.states.append(value[1])
                            self.visited.add(value[1])
