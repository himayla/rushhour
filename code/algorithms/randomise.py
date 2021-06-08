import random
import copy

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
    
    #
    empty_x = random_position[0]
    empty_y = random_position[1]
    print(f"random position:{random_position}")


    x_values = []
    y_values = []

    for x in grid.coordinates[empty_y]:
        #print(f"x value: {x}")
        x_values.append(x)

    for y in range(len(grid.coordinates)):
        #print(f"y value: {grid.coordinates[y][empty_x]}")
        y_values.append(grid.coordinates[y][empty_x])
    
    print(f"horizontal:{x_values[empty_x]}")
    print(f"vertical:{y_values[empty_y]}")
    print(f"horizontal single:{empty_x}")
    print(f"vertical single :{empty_y}")

    counter_x = 0
    before_x = []
    after_x = []

    for value in x_values:
        if counter_x < empty_x:
            if value != "0":
                before_x.append(value)
        else:
            if value != "0":
                after_x.append(value)
        counter_x += 1
        
    
    print(f"(X) before :{before_x}")
    print(f"(X) after :{after_x}")

    counter_y = 0
    before_y = []
    after_y = []

    for value in y_values:
        if counter_y < empty_y:
            if value != "0":
                before_y.append(value)
        else:
            if value != "0":
                after_y.append(value)
        counter_y += 1

    possible_cars = []
    print(f"(Y) before :{before_y}")
    print(f"(Y) after :{after_y}")

    if before_y:
        last_place = len(before_y) -1
        before_car_y = before_y[last_place]
        print(f" y before: {before_car_y}")
        count_by = 0
        for car in before_y:
            if car == before_car_y:
                count_by += 1
                
        if count_by > 1:
            possible_cars.append(before_car_y)

    if after_y:
        after_car_y = after_y[0]
        print(f" y after: {after_car_y}")
        count_ay = 0
        for car in after_y:
            if car == after_car_y:
                count_ay += 1
                
        if count_ay > 1:
            possible_cars.append(after_car_y)

    if before_x:
        last_place = len(before_x) -1
        before_car_x = before_x[last_place]
        print(f" y before: {before_car_x}")
        count_bx = 0
        for car in before_x:
            if car == before_car_x:
                count_bx += 1
                
        if count_bx > 1:
            possible_cars.append(before_car_x)

    if after_x:
        after_car_x = after_x[0]
        print(f" y after: {after_car_x}")
        count_ax = 0
        for car in after_x:
            if car == after_car_x:
                count_ax += 1
                
        if count_ax > 1:
            possible_cars.append(after_car_x)

    print(f"possible cars: {possible_cars}")
        

    
    
    
    