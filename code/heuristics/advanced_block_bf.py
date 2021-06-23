"""
This optimalisation heurisitic scores a board based on the cars that block the red car from driving to the exit.
This heuristic is specifically designed for the Best First algorithm, so the results can be put in to a priority queue.
"""

class BlockCar:
    def __init__(self):
        """
        Initializes lists and values to be used in the algorithm. 
        The right_red list is created to keep track of the cars that are to the right of the red car on the x-axis.
        The vertical_red is the value of the vertical row that the red car is on.
        The position_right_red is a dictionary of the position of the cars that are on the right of the red car on the x-axis:
        the names of the cars can be used as keys, the values are the horizontal values of where the cars are.  
        """
        self.right_red = [] 
        self.vertical_red = ""
        self.position_right_red = {}
        self.board_score = 1000


    def run(self, board):
        """
        Calls the methods for this heuristic.
        """
        scores = []

        right_red = self.check_red_car(board.board)
        rel_moves = self.relevant_moves(right_red, board.board)

        score = self.score_board(rel_moves[0], rel_moves[1])
        scores = (-score, board)

        return scores


    def check_red_car(self, board):
        """
        Checks every car to the right from the red car, saves the cars and returns the vertical value.
        """
        # Determine which row the red car is on by using the size of the board
        length = len(board[0])

        if length == 6: 
            self.vertical_red = 2
        elif length == 9:
            self.vertical_red = 4
        elif length == 12:
            self.vertical_red = 5

        # Determine the horizontal value of the red car
        horizontal_value = ""
        counter = 0
        for value in board[self.vertical_red]:
            
            if value == "X":
                horizontal_value = counter
            counter +=1

        counter = 0

        # Check if there is a car for each car to the right from the red car on the same horizontal row as the red car ###
        for value in range(horizontal_value + 1, len(board[self.vertical_red])):
            car_place = board[self.vertical_red][value], value

            # If there is a car append it to the list along with the horizontal value
            if board[self.vertical_red][value] != "0":
                self.right_red.append(car_place)

            # Only take the first three spaces into account when checking the empty spaces in front of the red car
            elif counter < 4:
                self.board_score = self.board_score + 10

            counter += 1

        # Update the score based on the to the end of the board
        self.board_score = self.board_score - (50 * counter)

        return self.right_red


    def relevant_moves(self, right_red, grid):
        """
        Checks the relative position for each car to see how far up or down the car needs to move to free up the space to the right of the red car.
        These relative moves are stored in the dictionaries: needs_up and needs_down where the key is the name of the car.
        """
        # For each car in the right_red list, use the car as a key in the dictionary that points to the row its on
        for value in right_red:
            car_row = []
            for car in range(0, len(grid[0])):
                car_row.append(grid[car][value[1]])
            self.position_right_red[value[0]] = car_row

        needs_up = {}
        needs_down = {}

        # Check how for each car in the dictionary needs to move up or down by counting how many cars are above and below the horizontal value of the red car
        for key, value in self.position_right_red.items():
            count_up = 1
            count_low = 1

            for letter in range(0, self.vertical_red):
                if key == value[letter]:
                    count_up +=1

            # Store the amount of moves the car needs to move down in the dictionary needs_down with the carname as a key
            needs_down[key] = count_up
            for letter in range(self.vertical_red + 1, len(grid[0])):
                if key == value[letter]:
                    count_low +=1

            # Store the amount of moves the car needs to move up in the dictionary needs_up with the carname as a key
            needs_up[key] = count_low

        return needs_up, needs_down
            
    def score_board(self, needs_up, needs_down):
        """
        Give one point for each way a car that blocks the red car to move up to free the x-axis. 
        Gives a half point for each way a car that blocks the red car to be able to move at all.
        Gives a tenth of a point for every empty spot that is in the car of a car that blocks the red car. 
        """
        for key, value in self.position_right_red.items():
                     
            count_empty_up = 0
            count_empty_low = 0
            count_vert = 0

            for letter in range(len(value)):
                if value[letter] == "0":
                    count_empty_up += 1

                    # If there is an empty space somewhere above the car that blocks the red car, attribute 0.1 points to the score
                    self.board_score += 0.1

                if value[letter] == key:
                    if needs_up[key] == count_empty_up:

                        # If there is enough space for the car to move upwards to free up a space on the red_car row, attribute 5 points
                        self.board_score += 5

                    if value[letter - 1]== "0":

                        # If there is a space directly above the car that blocks the red car, attribute 0.5 points
                        self.board_score += 0.5

                    continue

            for letter in range(self.vertical_red, len(value)):
                if value[letter] != key:
                    count_vert += 1

                    if value[letter] == "0":

                        # If there is an empty space somewhere below the car that blocks the red car, attribute 0.1 points to the score
                        self.board_score += 0.5
                        count_empty_low += 1

                        if count_vert == 1:

                            # If there is a space directly below the car that blocks the red car, attribute 0.5 points
                            self.board_score += 0.5
                    else:
                        continue

                if count_empty_low == needs_down[key]:

                    # If there is enough space for the car to move downwards to free up a space on the red_car row, attribute 5 points
                    self.board_score += 5

        return self.board_score