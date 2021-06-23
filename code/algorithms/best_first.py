"""
The Best First algorithm is based on a breadth first algorithm. 
The difference between a Best First and a breadth first algorithm is that a best first uses a heuristic to score boards. 
These scores are based on the advanced block heuristic in the heuristic directory. 
The Best First then uses those scores to give priority to the boards that score highly. 
Then, based on priority, these boards are popped from the list of states. 
This ensures the boards with the highest likelihood of reaching a solution, will be investigated first. 
"""
from .breadth_first import Breadthfirst
from code.heuristics import advanced_block_bf
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
        scored_list = []

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

                #-------------------------------------- Advanced block car heuristic ------------------------------------#
                # score grid based on a heuristic:
                scored_child = advanced_block_bf.BlockCar().run(new_model)
  
                #-------------------------------------- Best first implementation ------------------------------------#            
                
                # add the scored child if its not already in the queue
                if scored_child not in self.pqueue.queue:
                    if scored_child[1] not in self.visited:
                        self.pqueue.put(scored_child)
                self.visited.add(scored_child[1])

        #-------------------------------------- end Best first implementation ------------------------------------#
    
    def find_solution_seq(self, new_model):
        """
        Based on the final graph, trace back the previous graphs using the self.solution nested dictionary. 
        If the original graph is found, return the list of all graphs used to reach the final graph, in chronological order
        """
        path = [new_model]

        if new_model != self.start_board:
            previous_state = self.solution[str(new_model.board)][0]
            path = self.find_solution_seq(previous_state) + path
            self.moves = self.moves + [self.solution[str(new_model.board)][1]]
        
        return path
    
    
    def run(self):
        """
        Runs the algorithm untill a solution is found in a breadth first manner
        """
        self.start_board = self.pqueue.queue[0][1]
        
        # While there are still states to visit, stay in the loop
        while not self.pqueue.empty():
      
            new_model = self.get_next_state()

            board = new_model[1]

            if self.is_solution(board.board):

                path = self.find_solution_seq(board)
                board.print()
                print(f"moves: {len(path)}")
            
                file = open('output.csv', 'w+', newline='')
                with file:
                    write = csv.writer(file)
                    write.writerows(self.moves)

                return path
            else:
                self.build_children(board)