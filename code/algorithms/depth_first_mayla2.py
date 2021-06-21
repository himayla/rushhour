#werkt nog niet

class DepthFirst:
    def __init__(self, model):
        self.model = model.copy()
        self.states = [self.model] ## states = stack. kind genereren en 1 aanpassing op doen.

    def get_next_state(self):
        return self.states.pop(0)

    def build_children(self, model):
        """
        Attaches new grids to the self.states and creates a dictionary to keep track of which graphs result in which child-graphs. 
        """
        board = model.board

        empty_spaces = model.get_empty_spaces(board)

        for space in range(len(empty_spaces)-1):
            directions = model.get_relevant_rows(empty_spaces[space])
 
            # Find cars that can move to the empty spot
            cars = model.get_possible_cars(directions)

            # For each car, move the car on the grid to create a child state.
            for car in cars:
                new_model = model.copy()

                # Move each car and save the result of the movement in child variable
                new_model.move_car(empty_spaces[space], car, directions)

                self.states.append(new_model)

    def find_solution_seq(self, new_model):
        """
        Based on the final graph, trace back the previous graphs using the self.solution nested dictionary. 
        If the original graph is found, return the list of all graphs used to reach the final graph, in chronological order
        """
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
        counter = 0

        while self.states: 
            # if counter == 50:
            #     break
            
            new_model = self.get_next_state()
            if new_model.is_solution(new_model.board):
                print("victory")
                break
            else:
                self.build_children(new_model)

            #counter +=1
            #print(new_model)

        

        