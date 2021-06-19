"""
This file includes ...
"""

class Model():
    def __init__(self, grid):
        self.grid = grid
        self.solution = self.grid.solution
        self.states = []

    # ----------------------------- General ----------------------------------- # 
    def solution(self, grid):
        """
        The solution of the game depends on the size of the grid.
        """
        if len(grid) == 6:
            self.solution = ['X', [5, 2]]
        elif len(grid) == 9:
            self.solution = ['X', [8, 4]]
        elif len(grid) == 12:
            self.solution = ['X', [11, 5]]


    def is_solution(self):
        """
        The game is solved if the winning move is included in the states.
        """
        if self.solution not in self.states:
            return True
        return False


    def get_car_ids(paths):
        """
        Returns a dictionary with the cars and car ID's.
        """
        car_ids = {}
        id = 0
        for x in range(len(paths[0])):
            for y in range(len(paths[0])):
                car = paths[0][y][x] 
                if car not in car_ids:
                    car_ids[paths[0][y][x]] = id
                    id += 1

        return car_ids

    def copy(self):
        """
        Returns a copy of self.
        """
        new = Model(self.grid)

        return new

    def print(self):
        """
        Prints board.
        """
        print(f"Final board:")
        for line in self.grid.board:
            print(line)
        print(f"Amount of moves: {len(self.states)}")

    # --------------------------- Random ----------------------------------- #
    def get_empty_spaces(self, grid):
        """
        Returns a list of the coordinates of the empty spaces in the grid.
        """
        empty_spaces = []

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[y][x] == "0":
                    empty_space = [x,y]
                    empty_spaces.append(empty_space)

        return empty_spaces

    def get_relevant_rows(self, empty_space, grid):
        """
        Returns lists with the cars above, below and to the left and right from the empty space.
        """

        # Initialize lists for the cars below or above the empty space
        upper = []
        lower = []

        # The vertical row the empty space is in
        y_values = [grid[y][empty_space[0]] for y in range(len(grid))]

        # Get the cars in vertical row the empty space is in
        counter_y = 0
        for value in y_values:
            if value != "0":
                if counter_y < empty_space[1]:
                    upper.append(value)
                else:
                    lower.append(value)
            counter_y += 1
        
        x_values = grid[empty_space[1]]

        # Initialize lists for the cars to the left or right from the empty space
        left = []
        right = []

        # Get the cars in the horizontal row from the empty space
        counter_x = 0
        for value in x_values:
            if value != "0":
                if counter_x < empty_space[0]:
                    left.append(value) 
                else: 
                    right.append(value)
            counter_x += 1 

        return [upper, lower, left, right]

    def get_possible_cars(self, upper, lower, left, right):
        """
        Returns a list with cars that can move to the empty spot.
        """

        # List the directions
        directions = [upper, left, lower, right]

        # Initialize list for the different moves
        valid_moves = []

        count = 0
        for direction in directions:
            if direction:

                if count < 2:
                    last_place = len(direction) - 1
                    car_direction = direction[last_place]
                else:
                    car_direction = direction[0]

                count_car = 0
                for car in direction:
                    if car == car_direction:
                        count_car += 1
                    else:
                        count_car = 0
                    if count_car > 1 and car_direction not in valid_moves:
                        valid_moves.append(car_direction)
            count += 1
                
        return valid_moves

    def move_car(self, grid, position, random_car, upper, lower, left, right):
        """
        Moves the selected car to the random empty spot by updating the current grid.
        Returns the new grid.
        """

        # Check if the selected car is above or below the empty spot
        count_upper = 0
        count_lower = 0

        y_values = [grid[y][position[0]] for y in range(len(grid))]

        # If the car is higher than the empty space
        if random_car in upper:
            for y_car in upper:
                if random_car == y_car:
                    index = y_values.index(y_car)
                    count_upper += 1

            # Check orientation and then move the car
            if count_upper > 1:
                for a in range(count_upper):
                    grid[index + a][position[0]] = "0"
                    location = [index + 1, "V"]
                for a in range(count_upper):
                    grid[position[1] - a][position[0]] = random_car 

        # If the car is lower than the empty space
        elif random_car in lower:
            for y_car in lower:
                if random_car == y_car:
                    index = y_values.index(y_car)
                    count_lower += 1
                    
            # Check orientation, then move the length of the car first zero’s then car-names
            if count_lower > 1:
                for a in range(count_lower):
                    grid[index + a][position[0]] = "0"
                    location = [index, "V"]
                for a in range(count_lower):
                    grid[position[1] + a][position[0]] = random_car

        x_values = grid[position[1]]
    
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
                for a in range(count_left):
                    grid[position[1]][index + a] = "0"
                    location = [index + 1, "H"]
                for a in range(count_left):
                    grid[position[1]][position[0] - a] = random_car

        # If the car is to the right of the empty space
        elif random_car in right:
            for x_car in right:
                if random_car == x_car:
                    index = x_values.index(x_car)
                    count_right += 1
                    
            # Check the car’s orientation, then change the coordinates of the car to 0 and the empty space and relative coordinates to the name of the car
            if count_right > 1:
                for a in range(count_right):
                    grid[position[1]][index + a] = "0"
                    location = [index, "H"]
                for a in range(count_right):
                    grid[position[1]][position[0] + a] = random_car   

        return grid, location

    # ----------------------------------------------------------------- #