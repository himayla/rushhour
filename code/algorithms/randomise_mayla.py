import random

def rearrange_board(model, grid):
    """
    Rearranges the board by finding an empty space and the different directions
    """
    # Choose a random space out of the empty spaces
    empty_spaces = model.get_empty_spaces(grid.board)
    position = choose_random(empty_spaces)

    # Create a list for all the X values and Y values connected to this empty space
    directions = model.get_relevant_rows(position, grid.board)
    
    upper = directions[0]
    lower = directions[1]
    left = directions[2]
    right = directions[3]

    # Create a list with the cars left, up, right, down to the empty space and Choose random car from this list that can move to the empty space
    possible_cars =  model.get_possible_cars(upper, lower, left, right)
    random_car = choose_random(possible_cars)

    if random_car != "":

        # Add the new move to the list of moves
        new_move = [random_car, position]
        model.states.append(new_move)
        
        # Move the car
        model.move_car(grid.board, position, random_car, upper, lower, left, right)


def choose_random(possibilities):  
    """
    Returns a random car from the list of possible cars. 
    """  
    if possibilities:
        possibility = random.choice(possibilities)
    else:
        possibility = ""

    return possibility


def random_solver(model):
    """
    Solve the game by looking for empty spots, until car X (red car) is in the winning position.
    """
    while model.solution not in model.states:
        rearrange_board(model, model.grid)
       
    # Print final results
    print(f"Final board:")
    for line in model.grid.board:
        print(line)
    moves = len(model.states)
    print(f"Amount of moves: {moves}")