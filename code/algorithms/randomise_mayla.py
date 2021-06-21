"""
Algorithm that reconfigures the grid by randomly finding empty spots and cars that can move to this spot, until car X reaches the exit.
"""
import random

def random_solver(model):
    """
    Rearrange the board by looking for empty spots until solution is found.
    """
    while model.victory_move not in model.list_of_moves:
        rearrange_board(model, model.grid)
    
    # Print out the final board and amount of moves in the terminal
    model.print(moves=True)


def rearrange_board(model, grid):
    """
    Chooses an empty space and a car that can move to this place and swaps these.
    """
    board = grid.board

    # List all the empty spaces on the board
    empty_spaces = model.get_empty_spaces(board)

    # Choose a random spaces from the empty spaces
    position = choose_random_car(empty_spaces)

    # List all horizontal and vertical cars connected to the empty space
    directions = model.get_relevant_rows(position, board)

    # Create a list for the cars that can move to the empty space
    possible_cars =  model.get_possible_cars(directions)

    # Choose a car that to move to the empty space
    random_car = choose_random_car(possible_cars)

    # Make sure the chosen place contains a car  
    if random_car != "":
        
        # Initialise the move
        new_move = [random_car, position]

        # Add the new move to the list of moves
        model.list_of_moves.append(new_move)
        
        # Swap the car with an empty spot
        model.move_car(board, position, random_car, directions)


def choose_random_car(possible_cars):  
    """
    Returns "" or a random car from a list of possible cars. 
    """  
    if possible_cars:
        random_car = random.choice(possible_cars)
    else:
        random_car = ""

    return random_car