"""
This file includes the model that is used in all algorithms. 
By making the grid into a model it is easier and faster to run algorithms. 
The actions that can be performed within this model are divided into general abilities and algorithm abilities.
 
The general abilities include:
- Getting car id's from a board.
- Printing a specific board from a grid.
- Creating a csv file to show the car that moves and the relative move that it makes.

The algorithms abilities include: 
- Getting a list of all the empty spaces that exist on the board of the grid.
- Showing the cars in four directions (upper, lower, left, right) relative to a specific empty space. 
- Showing a list of cars that can move to a specific empty space.
- Moving a chosen car to a chosen empty space.
- Showing which location the red car needs to be in to qualify the algorithm as "done".
"""
import csv
import copy

class Model():
    def __init__(self, grid):
        """ 
        Initializes a model class based on the Grid class. Self.grid is used to access the board and the victory move from the Grid class.
        The list_of_moves is initialized to save the moves cars make and paths contains the different ways for a solution. 
        """ 
        self.grid = grid
        self.board = copy.deepcopy(grid.board)
        self.victory_move = grid.victory_move
        self.list_of_moves = [["car", "move"]]
        self.paths = []


    def __hash__(self):
        """ 
        Hashes the board to ensure no duplicates are created.
        """ 
        return hash(str(self.board))


    def __eq__(self, other):
        """
        Substitutes the original Python equal method to ensure only boards are compared, not models.
        """
        return str(self.board) == str(other.board)


    def __ne__(self, other):
        """
        Substitutes the original Python not equal method to ensure only boards are compared, not models.
        """
        return str(self.board) != str(other.board)


    def __lt__(self, other):
        """
        When models are compared, the other board (not self) will be the one greater than the self (one is chosen arbitrarily over the other).
        """
        return False

    # ----------------------------- General ----------------------------------- # 
    def get_car_ids(self):
        """
        Returns a dictionary with the cars and car ID's.
        """
        car_ids = {}

        car_id = 0
        for x in range(len(self.board)):
            for y in range(len(self.board)):
                car = self.board[y][x] 
                if car not in car_ids:
                    car_ids[self.board[y][x]] = car_id
                    car_id += 1

        return car_ids


    def copy(self):
        """
        Returns a copy of self.
        """
        new = Model(self.grid)

        # Update the board after copy
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                new.board[row][col] = self.board[row][col]

        return new


    def print(self, moves=False, path=False):
        """
        Prints board. 
        Optional arguments: 
            moves, prints the board and the amount of moves.
            path, prints the board and the length of path.
        """
        print(f"Board:")
        for line in self.board:
            print(line)

        if moves:
            print(f"Amount of moves: {len(self.list_of_moves)}")
        if path:
            print(f"Amount of moves in path: {len(path)}")


    def write_output(self, moves):
        """
        Writes the relative distance from the moves of cars in a CSV file.
        """
        file = open('output.csv', 'w+', newline='')
        with file:
            write = csv.writer(file)
            write.writerows(moves)
    
    # ---------------------------- Algorithms ----------------------------------- #
    def get_empty_spaces(self, board):
        """
        Returns a list of coordinates for the empty spaces in the board.
        """
        empty_spaces = []

        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[y][x] == "0":
                    empty_space = [x,y]
                    empty_spaces.append(empty_space)

        return empty_spaces


    def get_relevant_rows(self, empty_space):
        """
        Returns a list with the cars above, below, to the left and right from the empty space.
        """

        # Initialize lists for the cars below or above the empty space
        upper = []
        lower = []

        # The vertical row the empty space is in
        y_values = [self.board[y][empty_space[0]] for y in range(len(self.board))]

        # Get the cars in vertical row the empty space is in
        counter_y = 0
        for value in y_values:
            if value != "0":

                # Check if the car is either upper or below the empty space
                if counter_y < empty_space[1]:
                    upper.append(value)
                else:
                    lower.append(value)
            counter_y += 1
        
        x_values = self.board[empty_space[1]]

        # Initialize lists for the cars to the left or right from the empty space
        left = []
        right = []

        # Find the cars in the horizontal row from the empty space
        counter_x = 0
        for value in x_values:
            if value != "0":

                # Check if the car is either left or right from the empty space
                if counter_x < empty_space[0]:
                    left.append(value) 
                else: 
                    right.append(value)
            counter_x += 1 

        return [upper, lower, left, right]


    def get_possible_cars(self, directions):
        """
        Returns a list with cars that can move to the empty spot.
        """
        valid_cars = []

        # if a car is above the empty spot      
        upper = directions[0]
        if upper:            
            last_place = len(upper) - 1
            upper_car = upper[last_place]
            count_upper = 0
            for car in upper:
                if car == upper_car:
                    count_upper += 1
                else:
                    count_upper = 0

                if count_upper > 1 and upper_car not in valid_cars:
                    valid_cars.append(upper_car)
        
        # if a car is below the empty spot
        lower = directions[1]
        if lower:
            car_lower = lower[0]
            count_lower = 0
            for car in lower:
                if car == car_lower:
                    count_lower += 1
                else:
                    count_lower = 0

                if count_lower > 1 and car_lower not in valid_cars:
                    valid_cars.append(car_lower)

        # if a car is to the left of the empty spot
        left = directions[2]
        if left:
            last_place = len(left) - 1
            left_car = left[last_place]
            count_left = 0
            for car in left:
                if car == left_car:
                    count_left += 1
                else:
                    count_left = 0   

                if count_left > 1 and left_car not in valid_cars:
                    valid_cars.append(left_car)

        # if a car is to the right of the empty spot
        right = directions[3]
        if right:
            right_car = right[0]
            count_right = 0
            for car in right:
                if car == right_car:
                    count_right += 1
                else:
                    count_right = 0

                if count_right > 1 and right_car not in valid_cars:
                    valid_cars.append(right_car)

        return valid_cars


    def move_car(self, position, random_car, directions):
        """
        Moves the selected car to the random empty spot by updating the current grid.
        Returns the new board and the move.
        """
        upper = directions[0]
        lower = directions[1]

        # Check if the selected car is above or below the empty spot
        count_upper = 0
        count_lower = 0

        y_values = [self.board[y][position[0]] for y in range(len(self.board))]

        # If the car is higher than the empty space
        if random_car in upper:
            for y_car in upper:
                if random_car == y_car:
                    index = y_values.index(y_car)
                    count_upper += 1

            # Check orientation and then move the car
            if count_upper > 1:
                for car in range(count_upper):
                    self.board[index + car][position[0]] = "0"
                location = [index - count_upper + 1, "V"]
                for car in range(count_upper):
                    self.board[position[1] - car][position[0]] = random_car 

        # If the car is lower than the empty space
        elif random_car in lower:
            for y_car in lower:
                if random_car == y_car:
                    index = y_values.index(y_car)
                    count_lower += 1
                    
            # Check orientation, then move the length of the car first zero’s then car-names
            if count_lower > 1:
                for car in range(count_lower):
                    self.board[index + car][position[0]] = "0"
                    location = [index, "V"]
                for car in range(count_lower):
                    self.board[position[1] + car][position[0]] = random_car

        x_values = self.board[position[1]]

        left = directions[2]
        right = directions[3]
    
        # If the selected car is to the left or right from the empty spot
        count_left = 0
        count_right = 0

        # If the car is to the left of the empty space
        if random_car in left:
            for x_car in left:
                if random_car == x_car:
                    index = x_values.index(x_car)
                    count_left += 1

            # If the car is in the correct orientation, change the old coordinates to 0 and the new coordinates to the name of the car
            if count_left > 1:
                for car in range(count_left):
                    self.board[position[1]][index + car] = "0"
                location = [index - count_left + 1, "H"]
                for car in range(count_left):
                    self.board[position[1]][position[0] - car] = random_car

        # If the car is to the right of the empty space
        elif random_car in right:
            for x_car in right:
                if random_car == x_car:
                    index = x_values.index(x_car)
                    count_right += 1
                    
            # Check the car’s orientation, then change the coordinates of the car to 0 and the empty space and relative coordinates to the name of the car
            if count_right > 1:
                for car in range(count_right):
                    self.board[position[1]][index + car] = "0"
                    location = [index, "H"]
                for car in range(count_right):
                    self.board[position[1]][position[0] + car] = random_car
        
        return self.board, location


    def get_victory_coor(self):
        """
        Gets the victory coordinates for each size playing board.
        """
        if len(self.board) == 6:
            victory_coor = [5, 2]
        elif len(self.board) == 9:
            victory_coor = [8, 4]
        elif len(self.board) == 12:
            victory_coor = [11, 5]
        
        return victory_coor