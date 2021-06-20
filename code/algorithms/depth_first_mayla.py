from code.classes.model import Model

class DepthFirst:
    def __init__(self, model):
        self.model = model.copy()
        self.states = [model]

        self.solution = {} # or model.solution
        self.visited_states = [] # self.tried
        self.moves = [["car", "move"]]

    def get_next_state(self):
        """
        Method that gets the next state from the list of states.
        """
        return self.states.pop()

    def build_children(self, model):
        """
        Attaches new grids to the self.states and creates a dictionary to keep track of which graphs result in which child-graphs. 
        """
        # The board in the model
        board = model.grid.board

        # List all empty spaces
        empty_spaces = model.get_empty_spaces(board)

        # For all spaces find all possible moves
        for space in range(len(empty_spaces)):
            directions = model.get_relevant_rows(empty_spaces[space], board)

            # Find cars that can move to the empty spot
            cars = model.get_possible_cars(directions)

            new_grid = {} 

            # For each car, move the car on the grid to create a child state.
            for car in cars:
                new_grid[car] = board.copy()
            
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
                    self.solution[str(child)] = [board, car_move]
                
                # If the new graph is not yet in the list of states to visit, add it.
                if child not in self.states and self.visited_states:
                    self.states.append(child)
                self.visited_states.append(child)

    def check_car_x(self, board):
        """
        Check if the current state is a solution.
        """
        if len(board[0]) == 6:
            victory_coordinates = [5, 2]
        elif len(board[0]) == 9:
            victory_coordinates = [8, 4]
        elif len(board[0]) == 12:
            victory_coordinates = [11, 5]

        if board[victory_coordinates[1]][victory_coordinates[0]] == 'X':
            return True
        else:
            return False
            
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
            if counter == 5:
                break
            
            self.model.print() #

            # If there is a map on the top of the stack, get it
            new_model = self.get_next_state()

            board = self.model.grid.board

            # Check if this grid is a solution  
            if self.check_car_x(board):
                # Find the path for this solution
                path = self.find_solution_seq(board)

                count = 0
                for board in path:
                    count += 1
                print(f"moves: {self.moves}")
                print(count)
               
                self.model.write_output() # 
                #return path

            # Build new children
            else:
                self.build_children(self.model)

            counter +=1 
        self.model.print() #






