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
    
    # print(f"horizontal:{x_values[empty_x]}")
    # print(f"vertical:{y_values[empty_y]}")
    # print(f"horizontal single:{empty_x}")
    # print(f"vertical single :{empty_y}")

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
        
    
    # print(f"(X) before :{before_x}")
    # print(f"(X) after :{after_x}")

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
    # print(f"(Y) before :{before_y}")
    # print(f"(Y) after :{after_y}")
    
    if before_y:
        last_place = len(before_y) -1
        before_car_y = before_y[last_place]
        # print(f" y before: {before_car_y}")
        count_by = 0
        for car in before_y:
            if car == before_car_y:
                count_by += 1
                
        if count_by > 1:
            possible_cars.append(before_car_y)

    if after_y:
        after_car_y = after_y[0]
        # print(f" y after: {after_car_y}")
        count_ay = 0
        for car in after_y:
            if car == after_car_y:
                count_ay += 1
                
        if count_ay > 1:
            possible_cars.append(after_car_y)

    if before_x:
        last_place = len(before_x) -1
        before_car_x = before_x[last_place]
        #print(f" y before: {before_car_x}")
        count_bx = 0
        for car in before_x:
            if car == before_car_x:
                count_bx += 1
                
        if count_bx > 1:
            possible_cars.append(before_car_x)

    if after_x:
        after_car_x = after_x[0]
        #print(f" y after: {after_car_x}")
        count_ax = 0
        for car in after_x:
            if car == after_car_x:
                count_ax += 1
                
        if count_ax > 1:
            possible_cars.append(after_car_x)

    print(f"possible cars: {possible_cars}")

    # If there is a possibility
    # if possible_cars:
    #     for car in possible_cars:
    #         if car in x_values:
    #             print("Before X", x_values) ## Remove later

    #             # Index the positions
    #             index1 = x_values.index(car)
    #             index2 = x_values.index(x_values[empty_y])
    #             print(f"index 1: {index1}")
    #             print(f"index 2: {index2}")

    #             # Swap the positions of elements
    #             x_values[index1], x_values[index2] = x_values[index2], x_values[index1]
       
    #             print("After X", x_values) ## Remove later

    #         elif car in y_values:
    #             print("Before Y", y_values) ## Remove later
    #             index1 = y_values.index(car)
    #             index2 = y_values.index(y_values[empty_y]) ## Remove later
           
    #             # Swap the positions
    #             y_values[index1], y_values[index2] = y_values[index2], y_values[index1]

    #             print("After Y", y_values)

    # Mila's attempt:
    count_lengthbx = 0
    count_lengthax = 0
    count_lengthby = 0
    count_lengthay = 0
    if possible_cars:
        for car in possible_cars:
            if car in before_x:
                for x_car in before_x:
                    if car == x_car:
                        count_lengthbx += 1
            if count_lengthbx == 2 or count_lengthbx == 3:
                grid.coordinates[empty_y][empty_x] = car
                grid.coordinates[empty_y][empty_x - count_lengthbx] = "0"

            if car in after_x:
                for x_car in after_x:
                    if car == x_car:
                        count_lengthax += 1
            if count_lengthax == 2 or count_lengthax == 3:
                grid.coordinates[empty_y][empty_x] = car
                grid.coordinates[empty_y][empty_x + count_lengthax] = "0"

            # if car in before_y:
            #     for y_car in before_y:
            #         if car == y_car:
            #             count_lengthby += 1
            # if count_lengthby == 2 or count_lengthby == 3:
            #     grid.coordinates[empty_y][empty_x] = car
            #     grid.coordinates[empty_y - count_lengthby][empty_x] = "0"

            # if car in after_y:
            #     for y_car in after_y:
            #         if car == y_car:
            #             count_lengthay += 1
            # if count_lengthax == 2 or count_lengthax == 3:
            #     grid.coordinates[empty_y][empty_x] = car
            #     grid.coordinates[empty_y + count_lengthay][empty_x ] = "0"
        
        for line in grid.coordinates:
            print(line)
    
    
    

