from code.classes.model import Model

#werkt nog niet

class DepthFirst:
    def __init__(self, model):
        self.model = model.copy() ##??

        self.states = [model] ###?

        self.visited_states = [] 
        self.solution = {}

    def get_next_state(self):
        return self.states.pop()

    def build_children(self, model):
        """
        Attaches new grids to the self.states and creates a dictionary to keep track of which graphs result in which child-graphs. 
        """
        # List all empty spaces
        empty_spaces = model.get_empty_spaces(model)

        # For all spaces find all possible moves
        for space in range(len(empty_spaces)):
            directions = model.get_relevant_rows(empty_spaces[space], model)

            # Find cars that can move to the empty spot
            cars = model.get_possible_cars(directions)

            new_grid = {} 

            # For each car, move the car on the grid to create a child state.
            for car in cars:
                new_grid[car] = model.copy()

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
                if str(child) not in self.generations:
                    self.generations[str(child)] = [model, car_move]

                # If the new graph is not yet in the list of states to visit, add it.
                if child not in self.states and self.visited_states:
                    self.states.append(child)
                self.visited_states.append(child)

    def check_car_x(self, new_graph):
        """
        Create victory coordinates based on the size of the graph.
        If the car X reaches the victory coordinates, return True 
        """
        if len(self.model[0]) == 6:
            victory_coor = [5, 2]
        elif len(self.model[0]) == 9:
            victory_coor = [8, 4]
        elif len(self.model[0]) == 12:
            victory_coor = [11, 5]
        if new_graph[victory_coor[1]][victory_coor[0]] == 'X':
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
        counter = 0  # for testing

        while self.states:

            if counter == 5: # for testing
                break    # for testing
            
            # Pick a new graph
            new_graph = self.get_next_state()

            # Check if the graph is an acceptable result, if so, print out the solution
            if self.model.solution == self.solution:
                path = self.find_solution_seq(new_graph)

                count = 0
                for board in path:
                    count += 1
                print(f"moves: {self.moves}")
                print(count)
                
                file = open('output.csv', 'w+', newline='')
                with file:
                    write = csv.writer(file)
                    write.writerows(self.moves)
                # with open("output.csv", 'w') as f:
                #     fc = csv.writer(f)
                # fc.writerows(self.moves)

                return path

            # If the graph is not an acceptable result, create possible "children" of the graph so more options can be visited
            else:
                self.build_children(new_graph)

            counter+=1