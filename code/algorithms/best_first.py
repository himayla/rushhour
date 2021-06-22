from .breadth_first import Breadthfirst
from code.heuristics import blocked_cars
from code.heuristics import advanced_block
import csv
import copy

class BestFirst(Breadthfirst):

    def get_next_state(self):
        """
        Method that gets the next state from the list of states.
        """
        return self.pqueue.get()


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
                if new_model not in self.tried:
                    self.states.append(new_model)
                    self.tried.add(new_model)

                print(type(new_board))

                #-------------------------------------- Block car heuristic ------------------------------------#
                scored_child = blocked_cars.BlockCar().run(new_board)

                #-------------------------------------- Advanced block car heuristic ------------------------------------#
                #scored_child = advanced_block.BlockCar().run(new_board)
  
                #-------------------------------------- Best first implementation ------------------------------------#            
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

    #-------------------------------------- end Best first implementation ------------------------------------#
    def run(self):
        """
        Runs the algorithm untill a solution is found in a breadth first manner
        """
        # While there are still states to visit, stay in the loop
        while not self.pqueue.empty():
      
            new_model = self.get_next_state()
            board = new_model[1]

            if self.is_solution(board):

                path = self.find_solution_seq(new_model)
                print(f"moves: {len(path)}")
            
                file = open('output.csv', 'w+', newline='')
                with file:
                    write = csv.writer(file)
                    write.writerows(self.moves)

                return path
            else:
                self.build_children(new_model)