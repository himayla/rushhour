import random
import copy

"""
Pseudocode:
1. While [x, (5,2)] not in list_of_moves                                                run(new_grid) #als laatste
    2. Find empty spaces in board                                                       find_empty_spaces(new_grid), return empty_spaces
    3. Choose a random space out of the empty spaces                                    get_random_space(empty_spaces), return random_space
    4. Create a list for all the X values and Y values connected to this empty space    get_relevant_rows_cols(new_grid, random_space) return, list and cols
        5.  Create a list with the cars left, up, right, down to the empty space         
            Choose random car from this list that can move to the empty space           choose_random_car(new_grid) return random_car
            If list is empty, go back to step 3 and choose a new random place
        7. Move the car, add to list_of_moves and update the grid                        move_car(new_grid, random_car)
"""

# DEF class Randomise, daarin deepcopy. Run als laatste.

# Pseudocode: 
# Grid aan randomise geven.
# Zetten verzamelen:
# Welke vakjes zijn leeg?
# Kies random vakje van deze lege vakjes.
# Locatie van deze auto.
# Welke auto's zijn er in de buurt.
# Liggen zij in de orientatie dat ze bij dit vakje kunnen maken.
# Random keus daaruit maken.
# Check if auto X naar uitgang kan.
# Geef dit bord weer terug.

def random_assignment(grid):
    """
    Random
    """
    # List with coordinates of empty spaces
    empty_spaces_coor = []

    # Loop through the 2D grid to find an empty space, append to list of empty spaces
    for x in range(len(grid.coordinates)):
        for y in range(len(grid.coordinates[x])):
            if grid.coordinates[y][x] == "0":
                empty_space = [x,y]
                empty_spaces_coor.append(empty_space)

    # Amount of empty spaces -1 to account for indexing
    total_empty = len(empty_spaces_coor) - 1

    # Get coordinates for random empty space on the grid
    random_value = random.randint(0, total_empty)
    random_position = empty_spaces_coor[random_value]
    print(f"random position:{random_position}")
    
    # The coordinates of the empty spot
    empty_x = random_position[0]
    empty_y = random_position[1]

    # Lists for the possiblities based on coordinates
    x_values = []
    y_values = []

    for x in grid.coordinates[empty_y]:
        x_values.append(x)

    for y in range(len(grid.coordinates)):
        y_values.append(grid.coordinates[y][empty_x])
    

    counter_x = 0
    before_x = []
    after_x = []

    for value in x_values:

        # If the car is to the left of the empty space and it's value is not 0, add to list
        if counter_x < empty_x:
            if value != "0":
                before_x.append(value)

        # If the car is to the right of the empty space and it's value is not 0, add to other list
        else:
            if value != "0":
                after_x.append(value)
        counter_x += 1
        

    counter_y = 0
    before_y = []
    after_y = []

    for value in y_values:

        # If the car is lower than the empty space and it's value is not zero, add to list
        if counter_y < empty_y:
            if value != "0":
                before_y.append(value)

        # If the car is higher than the empty space and it's value is not zero, add to other list
        else:
            if value != "0":
                after_y.append(value)
        counter_y += 1

    possible_cars = []
    
    # If there are cars lower than the empty space: 
    if before_y:
        last_place = len(before_y) -1
        before_car_y = before_y[last_place]
        count_by = 0
        for car in before_y:
            if car == before_car_y:
                count_by += 1
        # Take the car to the right of the list, closest to the empty space and add to list
        if count_by > 1:
            possible_cars.append(before_car_y)

    # If there are any cars higher than the empty space: 
    if after_y:
        after_car_y = after_y[0]
        count_ay = 0
        for car in after_y:
            if car == after_car_y:
                count_ay += 1

        #  Take the first car after the empty space and add it to the list. 
        if count_ay > 1:
            possible_cars.append(after_car_y)

    # If there are cars to the left of the empty space
    if before_x:
        last_place = len(before_x) -1
        before_car_x = before_x[last_place]
        count_bx = 0
        for car in before_x:
            if car == before_car_x:
                count_bx += 1
        # Take the carname to the left of the empty space 
        if count_bx > 1:
            possible_cars.append(before_car_x)

    # If there are cars to the right of the empty space
    if after_x:
        after_car_x = after_x[0]
        count_ax = 0
        for car in after_x:
            if car == after_car_x:
                count_ax += 1

        # Add the first car to the right of the empty space to the list. 
        if count_ax > 1:
            possible_cars.append(after_car_x)

    print(f"possible cars: {possible_cars}")

    # move car to random empty space    
    
    count_lengthbx = 0
    count_lengthax = 0
    count_lengthby = 0
    count_lengthay = 0
    
    # Move every car in the list (change later to random car)
    for car in possible_cars:

        # If the car is to the left of the empty space in the grid
        if car in before_x:
            for x_car in before_x:
                index = x_values.index(x_car)
                if car == x_car:
                    count_lengthbx += 1

            # If the car is in the right orientation, change the old coordinates to 0 and the new coordinates to the name of the car
            if count_lengthbx > 1:
                for a in range(count_lengthbx):
                    grid.coordinates[empty_y][index - a + 1] = "0"
                    grid.coordinates[empty_y][empty_x - a + 1] = car

        #  If the car is to the right of the empty space
        if car in after_x:
            for x_car in after_x:
                index = x_values.index(x_car)
                if car == x_car:
                    count_lengthax += 1

            # check the  car's orientation, then change the coordinates of the car to 0 and the empty space and relative coordinates to the name of the car
            if count_lengthax > 1:
                for a in range(count_lengthax):
                    grid.coordinates[index][empty_x + a] = "0"
                    grid.coordinates[empty_y][empty_x + a] = car

        # If the car is lower than the empty space
        if car in before_y:
            for y_car in before_y:
                index = y_values.index(y_car)
                if car == y_car:
                    count_lengthby += 1

            # again, check orientation, then move the length of the car
            if count_lengthby > 1:
                for a in range(count_lengthby):
                    grid.coordinates[empty_y - index][empty_x] = "0"
                    grid.coordinates[empty_y - a + 1][empty_x] = car
                    
        #  If the car is to the right of the empty space: 
        if car in after_y:
            for y_car in after_y:
                index = y_values.index(y_car)
                if car == y_car:
                    count_lengthay += 1

            # Check orientation and then move the car 
            if count_lengthay > 1:
                for a in range(count_lengthay):
                    grid.coordinates[index + a][empty_x] = "0"
                    grid.coordinates[empty_y + a][empty_x] = car
                
        for line in grid.coordinates:
            print(line)
    
    
    
    
    

