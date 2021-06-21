#werkt nog niet

class DepthFirst:
    def __init__(self, model):
        self.model = model.copy()
        self.states = [self.model] ## states = stack. kind genereren en 1 aanpassing op doen.

        self.visited_states = [] 
        self.solution = {}
        self.moves = [["car", "move"]]

    def __repr__(self):
        return f'states:{self.states}'

    def __str__(self):
        return f'states:{self.states}'
        
    def get_next_state(self):
        return self.states.pop()

    def build_children(self, model):
        """
        Attaches new grids to the self.states and creates a dictionary to keep track of which graphs result in which child-graphs. 
        """
        board = model.board

        empty_spaces = model.get_empty_spaces(board)
        print(f'empty_spaces: {empty_spaces}')

        for space in range(len(empty_spaces)):
            directions = model.get_relevant_rows(empty_spaces[space], board)

            # Find cars that can move to the empty spot
            cars = model.get_possible_cars(directions)

            # For each car, move the car on the grid to create a child state.
            for car in cars:
                new_model = model.copy() 

                # Move each car and save the result of the movement in child variable
                new_model.move_car(empty_spaces[space], car, directions)
                # New_grid_car[car]

                # Child en rel move moeten worden gemuteerd in

                # child = move[0]
                # rel_move = move[1]
                # if rel_move[1] == "H":
                #     rel_distance = empty_spaces[space][0] - rel_move[0]
                #     car_move = [car, rel_distance]
                    
                # elif rel_move[1] == "V":
                #     rel_distance = empty_spaces[space][1] - rel_move[0]
                #     car_move = [car, rel_distance]

                # # If the new graph is not yet added to the dictionary of paths, add it. 
                # if str(child) not in self.solution:
                #     self.solution[str(child)] = [new_grid[car], car_move]

                # print(f' move: {car_move}')

                # If the new graph is not yet in the list of states to visit, add it.
                if new_model not in self.states: #and self.visited_states:
                    self.states.append(new_model)

                # ALS IK DIT UITCMOMENT KRIJG IK ERROR: LIST OBJECT HAS NO ATTRIBUTE TO BAORD
                # if str(child) not in self.visited_states:
                #     self.visited_states.append(str(child))

    def check_car_x(self, board):
        """
        Create victory coordinates based on the size of the graph.
        If the car X reaches the victory coordinates, return True 
        """
        if len(board[0]) == 6:
            victory_coor = [5, 2]
        elif len(board[0]) == 9:
            victory_coor = [8, 4]
        elif len(board[0]) == 12:
            victory_coor = [11, 5]
        if board[victory_coor[1]][victory_coor[0]] == 'X':
            return True
        else:
            return False

    def find_solution_seq(self, new_model):
        """
        Based on the final graph, trace back the previous graphs using the self.solution nested dictionary. 
        If the original graph is found, return the list of all graphs used to reach the final graph, in chronological order
        """
        pass
        # path = [new_model.grid]

        # if str(final_graph) not in str(board):
        #     previous_state = self.solution[str(final_graph)][0]
        #     path = self.find_solution_seq(previous_state) + path
        #     self.moves = self.moves + [self.solution[str(final_graph)][1]]
        #     return path

    def run(self):
        """
        Runs the algorithm until a solution is found.
        """
        counter = 0  # for testing

        print(f'start board')
        self.model.print()

        print(f'states: {self.states}') # NIET TE ZIEN

        while self.states: ##?
            # if counter == 10: # for testing
            #     break    # for testing

            #print(f'board 1 in model: {self.model.board}')
            new_model = self.get_next_state()
            #print(f'board 2 in model: {new_model.board}')

            # Check if the graph is an acceptable result, if so, print out the solution
            if self.check_car_x(new_model.board):
                path = self.find_solution_seq(new_model.board)

                count = 0
                for board in path:
                    count += 1
                print(f"moves: {self.moves}")
                print(count)
                
            else:
                print(f'ik maak kids')
                self.build_children(new_model)
        counter +=1
            
        self.model.print()
        print(f'{counter}')

           
