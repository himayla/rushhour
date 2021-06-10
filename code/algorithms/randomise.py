import random
import copy


class Randomise:
    """
    A random algorithm that moves random cars to random empty spaces until the red car reaches the end.
    """
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)
        self.x_values = []
        self.y_values = []
        self.left =[]
        self.right = []
        self.upper = []
        self.lower = []
        self.possible_cars = []
        self.random_car = ""
        self.list_of_moves = []
        self.random_position = []
        self.empty_spaces = []


    def find_empty_spaces(self):
        """
        Lists all empty spaces in the grid, by looping through the 2D-grid to find an empty space and append these to a list of empty spaces.
        """
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                if self.grid[y][x] == "0":
                    empty_space = [x,y]
                    self.empty_spaces.append(empty_space)
        return self.empty_spaces


    def get_random_space(self, empty_spaces):
        """
        Chooses a random empty space from a list of empty spaces.
        """
        # Amount of empty spaces -1 to account for indexing
        total_empty = len(empty_spaces) - 1

        # Get coordinates for random empty space on the grid
        random_value = random.randint(0, total_empty)
        self.random_position = empty_spaces[random_value]   
        return self.random_position 


    def get_relevant_rows(self, random_position):
        """
        Lists x and y axis connected to the selected empty space.
        """
        # Create lists to put the entire x and y axis that the chosen empty spaces resides on
        x_val = []
        y_val = []

        # Put x and y axis connected to the empty space in a list
        for x in self.grid[random_position[1]]:
            x_val.append(x)

        for y in range(len(self.grid)):
            y_val.append(self.grid[y][random_position[0]])

        # Add the x and y-axis values to the self
        self.x_values = x_val
        self.y_values = y_val

        # Create lists for values to the left and right of the chosen empty space
        left = []
        right = []
        counter_x = 0
        
        for value in self.x_values:

            # If the car is to the left of the empty space, and its value is not 0, add to list
            if counter_x < random_position[0]:
                if value != "0":
                    left.append(value)
                    
            # If the car is to the right of the empty space, and its value is not 0, add to other list
            else:
                if value != "0":
                    right.append(value)
            counter_x += 1 

        # Add the lists for left and right to self
        self.right = right
        self.left = left

        # Create counter and lists for upper and lower values to the empty space
        counter_y = 0
        upper = []
        lower = []

        for value in self.y_values:

            # If the car is lower than the empty space, and its value is not zero, add to list
            if counter_y < random_position[1]:
                if value != "0":
                    upper.append(value)
                    
            # If the car is higher than the empty space, and its value is not zero, add to other list
            else:
                if value != "0":
                    lower.append(value)
                    
            counter_y += 1

        # Add the lower and upper values of the empty space to the self
        self.lower = lower
        self.upper = upper
        return [self.x_values, self.y_values, self.lower, self.upper, self.right, self.left]


    def choose_random_car(self, upper, lower, right, left):
        
        """
        Lists all cars that could move to the empty spot, from the x and y axis of the empty spot, and chooses one at random.
        """
        possible = []

        # If there are cars above the empty space
        if self.upper:            
            last_place = len(self.upper) -1
            upper_car = self.upper[last_place]
            count_upper = 0
            for car in self.upper:
                if car == upper_car:
                   
                    count_upper += 1
                else:
                    count_upper = 0
                
                # Take the car to the right of the list, closest to the empty space and add to list if it's not put in yet
                if count_upper > 1 and upper_car not in possible:
                    possible.append(upper_car)
            

        # If there are any cars below the empty space: 
        if self.lower:
            car_left = self.lower[0]
            count_lower = 0
            for car in self.lower:
                if car == car_left:
                    count_lower += 1
                else:
                    count_lower = 0
                           
                #  Take the first car after the empty space and add it to the list if it's not in there yet
                if count_lower > 1 and car_left not in possible:
                    possible.append(car_left)

        # If there are cars to the left of the empty space
        if self.left:
            last_place = len(self.left) -1
            left_car = self.left[last_place]
            count_left = 0
            for car in self.left:
                if car == left_car:
                    count_left += 1
                else:
                    count_left = 0   
                
                # Take the carname to the left of the empty space and add to possible cars, if it's not in there yet
                if count_left > 1 and left_car not in possible:
                    possible.append(left_car)

        # If there are cars to the right of the empty space
        if self.right:
            right_car = self.right[0]
            count_right = 0
            for car in self.right:
                if car == right_car:
                    count_right += 1
                else:
                    count_right = 0
                
                # Add the first car to the right of the empty space to the list if it's not in there yet 
                if count_right > 1 and right_car not in possible:
                    possible.append(right_car)
        
        # Add the list of possible cars to the self
        self.possible_cars = possible
        
        # Choose random car from list of possible cars.
        if self.possible_cars:
            self.random_car = random.choice(self.possible_cars)

        else:
            self.random_car = ""

        return self.possible_cars


    def move_car(self):
        """
        Moves the selected car to the random empty spot by updating the current grid.
        """
        count_left = 0
        count_right = 0
        count_upper = 0
        count_lower = 0

        # If the car is to the left of the empty space
        if self.random_car in self.left:
            for x_car in self.left:
                if self.random_car == x_car:
                    index = self.x_values.index(x_car)
                    count_left += 1

            # If the car is in the correct orientation, change the old coordinates to 0 and the new coordinates to the name of the car
            if count_left > 1:
                for a in range(count_left):
                    self.grid[self.random_position[1]][index + a] = "0"
                for a in range(count_left):
                    self.grid[self.random_position[1]][self.random_position[0] - a] = self.random_car
                   
        #  If the car is to the right of the empty space
        elif self.random_car in self.right:
            for x_car in self.right:
                if self.random_car == x_car:
                    index = self.x_values.index(x_car)
                    count_right += 1
                    
            # Check the car’s orientation, then change the coordinates of the car to 0 and the empty space and relative coordinates to the name of the car
            if count_right > 1:
                for a in range(count_right):
                    self.grid[self.random_position[1]][index + a] = "0"
                for a in range(count_right):
                    self.grid[self.random_position[1]][self.random_position[0] + a] = self.random_car
                    
        # If the car is lower than the empty space
        elif self.random_car in self.lower:
            for y_car in self.lower:
                if self.random_car == y_car:
                    index = self.y_values.index(y_car)
                    count_lower += 1
                    
            # Check orientation, then move the length of the car first zero’s then car-names
            if count_lower > 1:
                for a in range(count_lower):
                    self.grid[index + a][self.random_position[0]] = "0"
                for a in range(count_lower):
                    self.grid[self.random_position[1] + a][self.random_position[0]] = self.random_car
                    
        # If the car is higher than the empty space
        elif self.random_car in self.upper:
            for y_car in self.upper:
                if self.random_car == y_car:
                    index = self.y_values.index(y_car)
                    count_upper += 1
            # Check orientation and then move the car
            if count_upper > 1:
                for a in range(count_upper):
                    self.grid[index + a][self.random_position[0]] = "0"
                for a in range(count_upper):
                    self.grid[self.random_position[1] - a][self.random_position[0]] = self.random_car          


    def run(self):
        """
        Run all the functions to find a empty space and move a car to that space.
        Stops when car x (red car) is in the winning position.
        """
        # For each board size (=length of a random x axis), choose a different victory move where car x needs to be to win
        victory_move = []

        while victory_move not in self.list_of_moves:
            
            # Find empty spaces in board
            empty_spaces = self.find_empty_spaces()
            
            # Choose a random space out of the empty spaces
            position = self.get_random_space(empty_spaces)

            # Create a list for all the X values and Y values connected to this empty space
            directions = self.get_relevant_rows(position)
            x_values = directions[0]
            y_values = directions[1]
            lower = directions[2]
            upper = directions[3]
            right = directions[4]
            left = directions[5]
            

            # For each board size (=length of a random x axis), choose a different victory move where car x needs to be to win
            if len(x_values) == 6:
                victory_move = ['X', [5, 2]]
            elif len(x_values) == 9:
                victory_move = ['X', [8, 4]]
            elif len(x_values) == 12:
                victory_move = ['X', [11, 5]]

            # Create a list with the cars left, up, right, down to the empty space and Choose random car from this list that can move to the empty space
            self.choose_random_car(upper, lower, right, left)   

            if self.random_car != "":
    
                # Add the new move to the list of moves
                new_move = [self.random_car, self.random_position]
                self.list_of_moves.append(new_move)
                
                # Move the car
                self.move_car()

                # Reset values
                self.random_car = ""
                self.random_position = []
                self.empty_spaces = []

        # Print final results
        print(f"Final board:")
        for line in self.grid:
            print(line)
        moves = len(self.list_of_moves)
        print(f"Amount of moves: {moves}")
