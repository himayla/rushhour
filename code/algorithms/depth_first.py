"""
The Depth First algorithm finds the first solution by building a stack of children boards and traverses in a vertical manner through the tree of children boards. 
"""
from queue import PriorityQueue


class DepthFirst:

    def __init__(self, model):
        """
        Initializes the Depth First class.
        Self.model calls the copy method in model.py.
        Self.states includes a list with models.
        Self.visited is unique collections of states.
        Self.moves is initialized to store moves and index them.
        Self.pqueue is only required attribute for the algorithms.
        """
        self.model = model.copy()
        self.states = [self.model]
        self.start_board = ""
        self.visited = set()
        self.solution = {}
        self.moves = [["car", "move"]]

        # Allows for priority queue so the algorithm can be expanded upon with a best first approach. 
        self.pqueue = PriorityQueue()
        self.pqueue.put((1, model.copy()))


    def run(self):
        """
        Runs the algorithm until a solution is found or it ran through all children boards.
        """
        self.start_board = self.states[0]

        while self.states: 
            new_model = self.get_next_state()
        
            # If a solution is found, return the path to reach that solution
            if self.is_solution(new_model.board):
                path = self.find_solution_seq(new_model)

                new_model.print(self.moves==False, path)

                new_model.write_output(self.moves)

                return path

            # If not, build new children
            else:
                self.build_children(new_model)


    def get_next_state(self):
        """
        Get the next board from the stack.
        """
        return self.states.pop()


    def build_children(self, model):
        """
        Attaches new boards to the self.visited and creates a dictionary to keep track of which boards result in which child-boards. 
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

                # Board is in index 0
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
                
                # If the new board is not yet in the list of states to visit, add it to that list and to a list of visited states
                if new_model not in self.visited:
                    self.states.append(new_model)
                    self.visited.add(new_model)


    def is_solution(self, board):
        """
        Checks if the game is solved, it is solved if the winning move is included in board.
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
        Traces back the previous boards using the self.solution nested dictionary. If the original graph is found, returns the path of all boards used to reach the final board.
        """
        path = [new_model]

        if new_model != self.start_board:
            previous_state = self.solution[str(new_model.board)][0]
            path = self.find_solution_seq(previous_state) + path
            self.moves = self.moves + [self.solution[str(new_model.board)][1]]
        
        return path