from code.classes.model import Model

class DepthFirst:
    def __init__(self, model):
        self.model = model.copy()
        self.states = [model]
        self.visited_states = []
        self.solution = {}

        self.moves = [["car", "move"]]

    def get_next_state(self):
        return self.states.pop()

    def build_children(self, model):
        # A list with all empty spaces that exist on the graph
        empty_spaces = model.get_empty_spaces(model.grid.board)

        # For all spaces find all possible moves
        for space in range(len(empty_spaces)):
            directions = model.get_relevant_rows(empty_spaces[space], model.grid.board)
            # Find cars that can move to the empty spot
            cars = model.get_possible_cars(directions)

            new_grid = {} 
            # For each car, move the car on the grid to create a child state.
            for car in cars:
                new_grid[car] = model.grid.board.copy()

                # Move each car and save the result of the movement in child variable
                move = model.move_car(new_grid[car], empty_spaces[space], car, directions)
                
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
                    self.solution[str(child)] = [model.grid.board, car_move]
      
                # If the new graph is not yet in the list of states to visit, add it.
                if child not in self.states and self.visited_states:
                    self.states.append(child)
                #self.visited_states.append(child)

    def find_solution_seq(self, final_graph):
        """
        Based on the final graph, trace back the previous graphs using the self.solution nested dictionary. 
        If the original graph is found, return the list of all graphs used to reach the final graph, in chronological order
        """
        path = [final_graph]
        board = self.model.grid.board

        if str(final_graph) not in str(board):
            previous_state = self.solution[str(final_graph)][0]
            path = self.find_solution_seq(previous_state) + path
            self.moves = self.moves + [self.solution[str(final_graph)][1]]
            return path

    def run(self):
        """
        Runs the algorithm untill a solution is found.
        """
        counter = 0
        while self.states:
            if counter == 15:    # for testing
                break
            new_model = self.get_next_state()


            if self.model.solution in self.states:
                path = self.find_solution_seq(new_model)

                count = 0
                for board in path:
                    count += 1
                print(f"moves: {self.moves}")
                print(count)

                return path
            else:
                    
                self.build_children(new_model)
                counter+=1

        self.model.print() # for testing
