"""
The Best First algorithm is based on a breadth first algorithm. 
The difference between a Best First and a ...
"""

from .breadth_first import Breadthfirst
from code.heuristics import advanced_block_bf
import csv

class BestFirst(Breadthfirst):

    def run(self):
        """
        Runs the algorithm until a solution is found in a breadth first manner.????
        """
        # While there are still states to visit, stay in the loop
        while not self.pqueue.empty():
        
            new_model = self.get_next_state()
            board = new_model[1]

            if self.is_solution(board):
                path = self.find_solution_seq(new_model)
                
                new_model.print(self.moves==False, path)
                
                new_model.write_output(self.moves)

                return path
            else:
                self.build_children(new_model)


    def get_next_state(self):
        """
        Method that gets the next state from the list of states using a priority queue.
        """
        return self.pqueue.get()


    def build_children(self, model):
        """
        Attaches new boards to the self.states and creates a dictionary to keep track of which graphs result in which child-graphs. 
        """
        # Get a list of empty spaces where cars could move to
        empty_spaces = model.get_empty_spaces(model.board)

        for space in range(len(empty_spaces)):

            # Find the cars that are above, below and to the sides of the empty space
            directions = model.get_relevant_rows(empty_spaces[space])

            # Find cars that can move to the empty spot
            possible_cars = model.get_possible_cars(directions)

            # For each car, move the car on the board to create a child state
            for car in possible_cars:
                new_model = model.copy()

                # Move each car and save the result 
                new_move = new_model.move_car(empty_spaces[space], car, directions)
                
                # New board is in index 0
                new_board = new_move[0]
                # Relative movement and name of the moved car are in index 1
                rel_move = new_move[1]

                # Find the relative distance that the car has moved
                if rel_move[1] == "H":
                    rel_distance = empty_spaces[space][0] - rel_move[0]
                    car_move = [car, rel_distance]
                    
                elif rel_move[1] == "V":
                    rel_distance = empty_spaces[space][1] - rel_move[0]
                    car_move = [car, rel_distance]
                    
                # If the new board is not yet added to the dictionary of paths, add it
                if str(new_board) not in self.solution:
                    self.solution[str(new_board)] = [model, car_move]
                
                # If the new board is not yet in the list of states to visit, add it.
                if new_model not in self.tried:
                    self.states.append(new_model)
                    self.tried.add(new_model)

                print(type(new_board))

                #-------------------------------------- Best first implementation ------------------------------------#            
                scored_child = advanced_block_bf.BlockCar().run(new_board)

                # score grid based on a heuristic:
                scored_list = []

                # add move to a list of scored grids
                scored_list.append(scored_child) 
            
                # pick only the grid, not the score and loop through the list
                for item in scored_list:
                    # If the new graph is not yet in the list of states to visit, add it.
                    if item not in self.pqueue.queue:
                        if item[1] not in self.tried:
                            self.pqueue.put(item)
                    self.tried.append(item[1])

    #-------------------------------------- End Best first implementation ------------------------------------#
 