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
    
    # # Check for cars on x and y axis
    empty_x = random_position[0]
    empty_y = random_position[1]
    print(f"random position:{random_position}")

    # Attempy Mila en co
    for y in range(len(grid.coordinates)):
        if grid.coordinates[x][empty_y -1] != "0":
            print(f"value of coordinates {grid.coordinates[x][y]}")
            print(f"actual coordinates {x,y}")

    # Attempt Mayla
    for x in range(len(grid.coordinates)-1):
        for y in range(len(grid.coordinates[x])):

            # If coordinates are similar to the empty spot, print the row
            if grid.coordinates[y][x] == grid.coordinates[empty_x][empty_y]:
                print(grid.coordinates[x])