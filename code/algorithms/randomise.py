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
    empty_spaces_coor = []

    for x in range(len(grid.coordinates)):
        for y in range(len(grid.coordinates[x])):
            if grid.coordinates[y][x] == "0":
                empty_space = [x,y]
                empty_spaces_coor.append(empty_space)

    total_empty = len(empty_spaces_coor) - 1

    random_value = random.randint(0, total_empty)
    random_position = empty_spaces_coor[random_value]












    