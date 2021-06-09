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
        # print("start empty spaces")
        """
        Lists all empty spaces in the grid.
        """
        # Loop through the 2D grid to find an empty space, append to the list of empty spaces
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                if self.grid[y][x] == "0":
                    empty_space = [x,y]
                    self.empty_spaces.append(empty_space)


    def get_random_space(self):
        """
        Chooses a random empty space from a list of empty spaces.
        """
        
        
        # Amount of empty spaces -1 to account for indexing
        total_empty = len(self.empty_spaces) - 1

        # Get coordinates for random empty space on the grid
        random_value = random.randint(0, total_empty)
        self.random_position = self.empty_spaces[random_value]
        
        # print(f"random position:{self.random_position}")
    

    def get_relevant_rows(self):
        """
        Lists x and y axis connected to the selected empty space.
        """
        # print("start get relevant rows")
        x_val = []
        y_val = []
        # Lists for the possiblities based on coordinates
        for x in self.grid[self.random_position[1]]:
            x_val.append(x)

        for y in range(len(self.grid)):
            y_val.append(self.grid[y][self.random_position[0]])

        self.x_values = x_val
        self.y_values = y_val

        left = []
        right = []
        counter_x = 0
        for value in self.x_values:

            # If the car is to the left of the empty space and it's value is not 0, add to list
            if counter_x < self.random_position[0]:
                if value != "0":
                    left.append(value)

            # If the car is to the right of the empty space and it's value is not 0, add to other list
            else:
                if value != "0":
                    right.append(value)
            counter_x += 1 

        counter_y = 0
        self.right = right
        self.left = left

        upper = []
        lower = []
        for value in self.y_values:

            # If the car is lower than the empty space and it's value is not zero, add to list
            if counter_y < self.random_position[1]:
                if value != "0":
                    upper.append(value)
                    

            # If the car is higher than the empty space and it's value is not zero, add to other list
            else:
                if value != "0":
                    lower.append(value)
                    
            counter_y += 1
        self.lower = lower
        self.upper = upper
        

    def choose_random_car(self):
        """
        Lists all possible cars from the x and y axis of the empty spot, and chooses one at random.
        """
        

        # 5.  Create a list with the cars left, up, right, down to the empty space         
        # Choose random car from this list that can move to the empty space           choose_random_car(new_grid) return random_car
        possible = []
        # If there are cars lower than the empty space: 
        
        if self.upper:            
            last_place = len(self.upper) -1
            before_car_y = self.upper[last_place]
            count_by = 0
            for car in self.upper:
                if car == before_car_y:
                   
                    count_by += 1
                else:
                    count_by = 0
                
            # Take the car to the right of the list, closest to the empty space and add to list
                if count_by > 1:
                    possible.append(before_car_y)
            

        # If there are any cars higher than the empty space: 
        if self.lower:
            after_car_y = self.lower[0]
            count_ay = 0
            for car in self.lower:
                if car == after_car_y:
                    
                    count_ay += 1
                else:
                    count_ay = 0
                           
                #  Take the first car after the empty space and add it to the list. 
                if count_ay > 1:
                    possible.append(after_car_y)

        # If there are cars to the left of the empty space
        if self.left:
            last_place = len(self.left) -1
            before_car_x = self.left[last_place]
            count_bx = 0
            for car in self.left:
                if car == before_car_x:
                    count_bx += 1
                else:
                    count_bx = 0   
                
                # Take the carname to the left of the empty space 
                if count_bx > 1:
                    possible.append(before_car_x)

        # If there are cars to the right of the empty space
        if self.right:
            after_car_x = self.right[0]
            count_ax = 0
            for car in self.right:
                if car == after_car_x:
                    count_ax += 1
                else:
                    count_ax = 0
                

                # Add the first car to the right of the empty space to the list. 
                if count_ax > 1:
                    possible.append(after_car_x)
        count_by = 0
        count_ay = 0
        count_bx = 0
        count_ax = 0

        self.possible_cars = possible
        # print(f"possible cars: {self.possible_cars}")

        # choose random car from list of possible cars.
        if self.possible_cars:
            self.random_car = random.choice(self.possible_cars)
            # print(f"auto op 152: {self.random_car}")

        else:
            self.random_car = ""
        


    def move_car(self):
        """
        Moves the selected car to the random empty spot by updating the current grid.
        """
        
        count_left = 0
        count_right = 0
        count_upper = 0
        count_lower = 0
        if self.random_car in self.left:
            
            for x_car in self.left:
                if self.random_car == x_car:
                    index = self.x_values.index(x_car)
                    count_left += 1
            # If the car is in the right orientation, change the old coordinates to 0 and the new coordinates to the name of the car
            if count_left > 1:
                
                for a in range(count_left):
                    self.grid[self.random_position[1]][index + a] = "0"
                    
                for a in range(count_left):
                    self.grid[self.random_position[1]][self.random_position[0] - a] = self.random_car
                   
            count_left = 0
        #  If the car is to the right of the empty space
        elif self.random_car in self.right:
            for x_car in self.right:
                if self.random_car == x_car:
                    index = self.x_values.index(x_car)
                    count_right += 1
            # check the  car’s orientation, then change the coordinates of the car to 0 and the empty space and relative coordinates to the name of the car
            if count_right > 1:
                
                for a in range(count_right):
                    self.grid[self.random_position[1]][index + a] = "0"
                    
                for a in range(count_right):
                    self.grid[self.random_position[1]][self.random_position[0] + a] = self.random_car
                    
            count_right = 0
        # If the car is lower than the empty space
        elif self.random_car in self.lower:
            for y_car in self.lower:
                if self.random_car == y_car:
                    index = self.y_values.index(y_car)
                    count_lower += 1
            # again, check orientation, then move the length of the car first zero’s then car-names
            if count_lower > 1:
                
                for a in range(count_lower):
                    self.grid[index + a][self.random_position[0]] = "0"
                    
                for a in range(count_lower):
                    self.grid[self.random_position[1] + a][self.random_position[0]] = self.random_car
                    
            count_lower = 0
        #  If the car is to the right of the empty space:
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
                    
            count_upper = 0
        


    def run(self):
        """
        Run all the funcitons to find a empty space and move a car to that space.
        Stops when car x (red car) is in the winning position.
        """
        

        while "[x, (5,2)]" not in self.list_of_moves:

            # Find empty spaces in board
            self.find_empty_spaces()
            
            # Choose a random space out of the empty spaces
            self.get_random_space()

            # Create a list for all the X values and Y values connected to this empty space
            self.get_relevant_rows()

            # Create a list with the cars left, up, right, down to the empty space and Choose random car from this list that can move to the empty space
            self.choose_random_car()   

            if self.random_car != "":
    
                # add the new move to the list of moves.
                new_move = [self.random_car, self.random_position]
                self.list_of_moves.append(new_move)
                
                # move the car
                self.move_car()
                self.x_values = []
                self.y_values = []
                self.left =[]
                self.right = []
                self.upper = []
                self.lower = []
                self.possible_cars = []
                self.random_car = ""
                self.random_position = []
                self.empty_spaces = []
        print(f"final board")
        for line in self.grid:
            print(line)
        print(f"solution: {self.set.list_of_moves}")
