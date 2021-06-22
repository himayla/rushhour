import csv
import copy
from queue import PriorityQueue


class DepthFirst:
    def __init__(self, model):
        self.model = model.copy()
        self.states = [self.model] ## states = stack. kind genereren en 1 aanpassing op doen.
        self.start_board = ""
        self.tried = set()
        self.solution = {}
        self.moves = [["car", "move"]]

        # ---------- best first implementation -----# 
        self.pqueue = PriorityQueue()
        self.pqueue.put((1, model.copy()))
        # ---------- best first implementation -----# 


    def get_next_state(self):
        return self.states.pop()

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

    def is_solution(self, board):
        """
        The game is solved if the winning move is included in the states.
        """
        if len(board[0]) == 6:
            victory_coor = [5, 2]
        elif len(board[0]) == 9:
            victory_coor = [8, 4]
        elif len(board[0]) == 12:
            victory_coor = [11, 5]

        #print(board[victory_coor[1]][victory_coor[0]])

        if board[victory_coor[1]][victory_coor[0]] == 'X':
            return True
        else:
            return False

    def find_solution_seq(self, new_model):
        """
        Based on the final graph, trace back the previous graphs using the self.solution nested dictionary. 
        If the original graph is found, return the list of all graphs used to reach the final graph, in chronological order
        """
        #board = new_model.board
        path = [new_model]
        # start_board = self.start_board

        if new_model != self.start_board:
            previous_state = self.solution[str(new_model.board)][0]
            # breakpoint()
            path = self.find_solution_seq(previous_state) + path
            self.moves = self.moves + [self.solution[str(new_model.board)][1]]
        
        return path

    def run(self):
        """
        Runs the algorithm until a solution is found.
        """
        self.start_board = self.states[0]

        while self.states: 
      
            new_model = self.get_next_state()
            if self.is_solution(new_model.board):

                path = self.find_solution_seq(new_model)
                print(f"moves: {len(path)}")
            
                file = open('output.csv', 'w+', newline='')
                with file:
                    write = csv.writer(file)
                    write.writerows(self.moves)

                return path
            else:
                self.build_children(new_model)