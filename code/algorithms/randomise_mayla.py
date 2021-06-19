import random

def get_empty_spaces(grid):
    """
    Returns the coordinates a random empty space in the grid, from a list with of empty spaces in board.
    """
    empty_spaces = []

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[y][x] == "0":
                empty_space = [x,y]
                empty_spaces.append(empty_space)

    return empty_spaces

def get_relevant_rows(random_position, grid):
    """
    Returns a list with cars horizontally and vertical from empty space.
    """    
    upper = []
    lower = []

    # The vertical row from empty space
    y_values = [grid[y][random_position[0]] for y in range(len(grid))]

    counter_y = 0
    for value in y_values:
        if value != "0":
            if counter_y < random_position[1]:
                upper.append(value)                
            else:
                lower.append(value)  
        counter_y += 1
    
    x_values = grid[random_position[1]]

    left = []
    right = []

    # The cars in the horizontal row from empty space
    counter_x = 0
    for value in x_values:
        if value != "0":
            if counter_x < random_position[0]:
                left.append(value) 
            else: 
                right.append(value)
            counter_x += 1 

    return [upper, lower, left, right]
    
def get_possible_cars(upper, lower, left, right):
    """
    Returns a random car from a all cars that could move to the empty spot.
    """
    
    directions = [upper, left, lower, right]
    possible = []
    count = 0
    for direction in directions:
        if direction: 
            if count < 2:
                last_place = len(direction) -1
                car_direction = direction[last_place]
            else:
                car_direction = direction[0] 
            count_car = 0
            for car in direction:
                if car == car_direction:
                    count_car += 1
                else:
                    count_car = 0
                if count_car > 1 and car_direction not in possible:
                    possible.append(car_direction)
        count += 1
            
    return possible

def choose_random(possibilities):  
    """
    Returns a random car from the list of possible cars. 
    """  
    if possibilities:
        possibility = random.choice(possibilities)
    else:
        possibility = ""

    return possibility

def move_car(grid, position, random_car, upper, lower, left, right):
    """
    Moves the selected car to the random empty spot by updating the current grid.
    Returns the new grid.
    """
    y_values = [grid[y][position[0]] for y in range(len(grid))]

    count_upper = 0
    count_lower = 0
    location = []

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
                x_values[index + a] = "0"
                location = [index + 1, "H"]
            for a in range(count_left):
                x_values[position[0] - a] = random_car
                
                
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
                location = [index, "H"]
            for a in range(count_right):
                grid[position[1]][position[0] + a] = random_car   

    return grid, location

def rearrange_board(grid):
    """
    Rearranges the board by finding an empty space and the different directions
    """
    # Choose a random space out of the empty spaces
    # for line in grid.board: 
    #     print(line)
    empty_spaces = get_empty_spaces(grid.board)
    position = choose_random(empty_spaces)
    # print(f"empty space: {position}")
    # Create a list for all the X values and Y values connected to this empty space
    directions = get_relevant_rows(position, grid.board)
    
    upper = directions[0]
    lower = directions[1]
    left = directions[2]
    right = directions[3]

    # Create a list with the cars left, up, right, down to the empty space and Choose random car from this list that can move to the empty space
    possible_cars = get_possible_cars(upper, lower, left, right)
    random_car = choose_random(possible_cars)
    # print(f"car: {random_car}")
    if random_car != "":

        # Add the new move to the list of moves
        new_move = [random_car, position]
        grid.list_of_moves.append(new_move)
        
        # Move the car
        move_car(grid.board, position, random_car, upper, lower, left, right)

def random_solver(grid):
    """
    Solve the game by looking for empty spots, until car X (red car) is in the winning position.
    """
    count = 0    
    while grid.solution not in grid.list_of_moves:
        rearrange_board(grid)
        count += 1
        # if count == 40:
        #     break

    # Print final results
    print(f"Final board:")
    for line in grid.board:
        print(line)
    moves = len(grid.list_of_moves)
    print(f"Amount of moves: {moves}")
