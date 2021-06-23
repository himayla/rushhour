"""
The Beam Search algorithm chooses the best children in the queue by giving a score to each child using the Block Car heuristic. Only the best n children will be put in the queue.
The user can decide for a value n (69). This decision is a tradeoff, a lower n value will produce a quicker but a higher n value will produce a shorter solution. 
For example, the 6x6_1 board can be solved by using n >= 4 quickly, but not with the quickest solution. 
"""
from .breadth_first import Breadthfirst
from code.heuristics import advanced_block_bs

class BeamSearch(Breadthfirst):

    def build_children(self, model):
        """
        Attaches new (scored) board models to the self.visited and creates a dictionary to keep track of which grids are created from which grids. 
        """

        # Get a list of empty spaces where cars could move to
        empty_spaces = model.get_empty_spaces(model.board)

        # Initialize list for later use
        scored_list = []

        for space in range(len(empty_spaces)):

            # Find the cars that are above, below and to the sides of the empty space
            directions = model.get_relevant_rows(empty_spaces[space])

            # Find cars that can move to the empty spot
            possible_cars = model.get_possible_cars(directions)

            # For each car, move the car on the board to create a child board
            for car in possible_cars:
                new_model = model.copy()

                # Move each car and save the result
                new_move = new_model.move_car(empty_spaces[space], car, directions)

                # New board is in index 0
                new_board = new_move[0]

                # Relative movement and name of the moved car are in index 1
                rel_move = new_move[1]

                # Find the relative distance that the car has moved and save it into car_move
                if rel_move[1] == "H":
                    rel_distance = empty_spaces[space][0] - rel_move[0]
                    car_move = [car, rel_distance]
                elif rel_move[1] == "V":
                    rel_distance = empty_spaces[space][1] - rel_move[0]
                    car_move = [car, rel_distance]
                                    
                # If the new board is not yet added to the dictionary of paths, add it
                if str(new_board) not in self.solution:
                    self.solution[str(new_board)] = [model, car_move]
                
                #-------------------------------------- Beam search implementation ------------------------------------#
                
                # Score the current board based on the heuristic
                scored_child = advanced_block_bs.BlockCar().run(new_model)
                
                # Add move to a list of scored boards
                scored_list.append(scored_child)
    
        # Sort the list of dictionaries, higest first, source:https://code-maven.com/slides/python/sort-dictionary-by-value
        sorted_scores = sorted(scored_list, key=lambda k: list(k.values())[0], reverse=True)

        # Initialize list for the ranked children
        ranking = []

        # Pick the amount of children to select from a parent board
        n = 7

        # Pick the first n children
        ranking = sorted_scores[:n]
        
        for board in ranking:
            for value in board.values():

                # If the new board is not yet in the list of states to visit, add it
                if value[1] not in self.visited:
                    self.states.append(value[1])
                    self.visited.add(value[1])
        #-------------------------------------- End beam search implementation -------------------------------------#
