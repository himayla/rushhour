import random #td
import copy

def randomise(grid): # Main function
    new_grid = copy.deepcopy(grid)

    for line in new_grid:
        print(line)

    empty_spaces(new_grid)

    place = [0,1] ## Temporary. (Randomise later)

    options(new_grid, place)


def empty_spaces(grid):
    # List for the coordinates of empty spaces in grid
    empty_spots = []

    # Loop through the 2D grid to find an empty space and add to list of empty spaces
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[y][x] == "0":
                empty_spots.append([x,y])

    return empty_spots


def options(new_grid, place): 
    
    # Rows X and Y based on coordinates of empty spot
    x_values = []
    y_values = []

    for x in new_grid[place[1]]:
        x_values.append(x)

    for y in range(len(new_grid) - 1):
        y_values.append(new_grid[y][place[0]])

    # Get cars before and after empty spot

    counter_x = 0
    before_x = []
    after_x = []

    for x in new_grid[place[1]]:
        if counter_x < place[0]:
            if x != "0":
                before_x.append(x)
        else:
            if x != "0":
                after_x.append(x) 
        counter_x += 1

    counter_y = 0
    before_y = []
    after_y = []

    for y in y_values:
        if counter_y < place[1]:
            if y != "0":
                before_y.append(y)
        else:
            if y != "0":
                after_y.append(y)
        counter_y += 1

    # print(f'befx:{before_x}')
    # print(f'afterx:{after_x}')
    # print(f'befy:{before_y}')
    # print(f'aftery:{after_y}')

    closest_car(before_x, after_x) # For testing I only use X


def closest_car(before, after): # Only X values for now.
    possible_cars = []
    
   # If there are cars to the left of the empty space
    if before:
        last_place = len(before) - 1
        before_car_x = before[last_place]

        count_bx = 0
        for car in before:
            if car == before_car_x:
                count_bx += 1

        # Take the carname to the left of the empty space 
        if count_bx > 1:
            possible_cars.append(before_car_x)

    # If there are cars to the right of the empty space
    if after:
        after_car_x = after[0]
        count_ax = 0
        for car in after:
            if car == after_car_x:
                count_ax += 1

        # Add the first car to the right of the empty space to the list. 
        if count_ax > 1:
            possible_cars.append(after_car_x)

    print(f"possible cars: {possible_cars}")

    return possible_cars