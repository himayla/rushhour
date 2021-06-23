"""
The Best First algorithm is based on a Breadth First algorithm. The difference is that Best First uses a heuristic to score boards. 
These scores are based on the advanced block heuristic in the heuristic directory. The Best First then uses those scores to give priority,
to the boards that score highly. Based on priority, these boards are popped from the list of states. 
This ensures the boards with the highest likelihood of reaching a solution, will be investigated first. 
"""
from .breadth_first import Breadthfirst
from code.heuristics import advanced_block_bf

class BestFirst(Breadthfirst):

    def run(self):
        """
        Runs the algorithm until a solution is found in a breadth first manner.
        """
        # Initialize starting board
        self.start_board = self.pqueue.queue[0][1]
        
        # Continue solving the game until the queue is empty
        while not self.pqueue.empty():
            new_model = self.get_next_state()

            # The priority queue returns a tuple where the second element is a model
            new_model = new_model[1]
            
            # If a solution is found, return the path to reach that solution
            if self.is_solution(new_model.board):

                path = self.find_solution_seq(new_model)

                # Print solution and write output in CSV
                new_model.print(self.moves==False, path)
                new_model.write_output(self.moves)

                return path

            # If no solutions found, build children
            self.build_children(new_model)

    def get_next_state(self):
        """
        Method that gets the next state from the priority queue.
        """
        return self.pqueue.get()


    def build_children(self, model):
        """
        Attaches new grids to the self.states and creates a dictionary to keep track of which graphs result in which child-graphs. 
        """
        # Get a list of empty spaces where cars could move to
        empty_spaces = model.get_empty_spaces(model.board)

        for space in range(len(empty_spaces)):

            # Find the cars that are above, below and to the sides of the empty space
            directions = model.get_relevant_rows(empty_spaces[space])

            # Find cars that can move to the empty spot
            cars = model.get_possible_cars(directions)

            # For each car, move the car on the board to create a child state
            for car in cars:
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

                #-------------------------------------- Advanced Block Car heuristic ------------------------------------#
                # Score the board based on a heuristic:
                scored_model = advanced_block_bf.BlockCarBF().run(new_model)
  
                #-------------------------------------- Best First implementation ------------------------------------#            
                # Add the scored board if its not already in the queue
                if scored_model not in self.pqueue.queue:
                    if scored_model[1] not in self.visited:
                        self.pqueue.put(scored_model)
                self.visited.add(scored_model[1])
