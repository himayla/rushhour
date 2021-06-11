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


    def find_empty_spaces(self, grid):
        """
        Lists all empty spaces in the grid, by looping through the 2D-grid to find an empty space and append these to a list of empty spaces.
        """
        empty_spaces = []
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if self.grid[y][x] == "0":
                    empty_space = [x,y]
                    empty_spaces.append(empty_space)
        self.grid = grid
        self.empty_spaces = empty_spaces
        return empty_spaces
        


    def get_random_space(self, empty_spaces):
        """
        Chooses a random empty space from a list of empty spaces.
        """
        # Amount of empty spaces -1 to account for indexing
        total_empty = len(empty_spaces) - 1

        # Get coordinates for random empty space on the grid
        random_value = random.randint(0, total_empty)
        random_position = empty_spaces[random_value]   
        return random_position 


    def get_relevant_rows(self, random_position, grid):
        """
        Lists x and y axis connected to the selected empty space.
        """
        # Create lists to put the entire x and y axis that the chosen empty spaces resides on
        x_val = []
        y_val = []

        # Put x and y axis connected to the empty space in a list
        for x in grid[random_position[1]]:
            x_val.append(x)

        for y in range(len(grid)):
            y_val.append(grid[y][random_position[0]])

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
        self.grid = grid
        return [self.x_values, self.y_values, self.lower, self.upper, self.right, self.left]


    def get_possible_cars(self, upper, lower, right, left):
        
        """
        Lists all cars that could move to the empty spot, from the x and y axis of the empty spot, and chooses one at random.
        """
        possible = []

        # If there are cars above the empty space
        if upper:            
            last_place = len(upper) -1
            upper_car = upper[last_place]
            count_upper = 0
            for car in upper:
                if car == upper_car:
                   
                    count_upper += 1
                else:
                    count_upper = 0
                
                # Take the car to the right of the list, closest to the empty space and add to list if it's not put in yet
                if count_upper > 1 and upper_car not in possible:
                    possible.append(upper_car)
            

        # If there are any cars below the empty space: 
        if lower:
            car_left = lower[0]
            count_lower = 0
            for car in lower:
                if car == car_left:
                    count_lower += 1
                else:
                    count_lower = 0
                           
                #  Take the first car after the empty space and add it to the list if it's not in there yet
                if count_lower > 1 and car_left not in possible:
                    possible.append(car_left)

        # If there are cars to the left of the empty space
        if left:
            last_place = len(left) -1
            left_car = left[last_place]
            count_left = 0
            for car in left:
                if car == left_car:
                    count_left += 1
                else:
                    count_left = 0   
                
                # Take the carname to the left of the empty space and add to possible cars, if it's not in there yet
                if count_left > 1 and left_car not in possible:
                    possible.append(left_car)

        # If there are cars to the right of the empty space
        if right:
            right_car = right[0]
            count_right = 0
            for car in right:
                if car == right_car:
                    count_right += 1
                else:
                    count_right = 0
                
                # Add the first car to the right of the empty space to the list if it's not in there yet 
                if count_right > 1 and right_car not in possible:
                    possible.append(right_car)
        
        # Add the list of possible cars to the self
        self.possible_cars = possible
        return possible

    def choose_random_car(self, possible_cars):    
        # Choose random car from list of possible cars.
        if possible_cars:
            random_car = random.choice(possible_cars)

        else:
            random_car = ""
        return random_car

    def move_car(self, position, random_car, x_values, y_values, left, right, upper, lower, grid):
        """
        Moves the selected car to the random empty spot by updating the current grid.
        """
        count_left = 0
        count_right = 0
        count_upper = 0
        count_lower = 0

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
                for a in range(count_left):
                    grid[position[1]][position[0] - a] = random_car
                   
        #  If the car is to the right of the empty space
        elif random_car in right:
            for x_car in right:
                if random_car == x_car:
                    index = x_values.index(x_car)
                    count_right += 1
                    
            # Check the car’s orientation, then change the coordinates of the car to 0 and the empty space and relative coordinates to the name of the car
            if count_right > 1:
                for a in range(count_right):
                    grid[position[1]][index + a] = "0"
                for a in range(count_right):
                    grid[position[1]][position[0] + a] = random_car
                    
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
                for a in range(count_lower):
                    grid[position[1] + a][position[0]] = random_car
                    
        # If the car is higher than the empty space
        elif random_car in upper:
            for y_car in upper:
                if random_car == y_car:
                    index = y_values.index(y_car)
                    count_upper += 1
            # Check orientation and then move the car
            if count_upper > 1:
                for a in range(count_upper):
                    grid[index + a][position[0]] = "0"
                for a in range(count_upper):
<<<<<<< HEAD
                    self.grid[position[1] - a][position[0]] = random_car 

        return self.grid
=======
                    grid[position[1] - a][position[0]] = random_car
        self.grid = grid
        return grid
>>>>>>> 0f2cb2853e4be1d228d02258555594c06a204a85


    def run(self):
        """
        Run all the functions to find a empty space and move a car to that space.
        Stops when car x (red car) is in the winning position.
        """
        # For each board size (=length of a random x axis), choose a different victory move where car x needs to be to win
        victory_move = []

        while victory_move not in self.list_of_moves:
            
            # Find empty spaces in board
            empty_spaces = self.find_empty_spaces(self.grid)
            # print(f"empty spaces: {empty_spaces}")
            
            # Choose a random space out of the empty spaces
            position = self.get_random_space(empty_spaces)
            # print(f"position:{position}")
            # Create a list for all the X values and Y values connected to this empty space
            directions = self.get_relevant_rows(position)
            # print(f"directions: {directions}")
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
            possible_cars = self.get_possible_cars(upper, lower, right, left)
            # print(f"possible cars: {possible_cars}")
            random_car = self.choose_random_car(possible_cars)   
            # print(f"random_car: {random_car}")
            
            if random_car != "":
    
                # Add the new move to the list of moves
                new_move = [random_car, position]
                self.list_of_moves.append(new_move)
                
                # Move the car
                self.move_car(position, random_car, x_values, y_values, left, right, upper, lower, self.grid)
                
                # Reset values
                random_car = ""
                position = []
                self.empty_spaces = []
                for line in self.grid:
                    print(line)
                print("")

        # Print final results
        print(f"Final board:")
        for line in self.grid:
            print(line)
        moves = len(self.list_of_moves)
        print(f"Amount of moves: {moves}")
