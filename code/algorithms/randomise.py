"""
The random algorithm reconfigures the board by randomly looking for empty spots and cars that can move to this spot and moves these until the red car can reach the exit.
"""
import random
import copy

def random_solver(model):
    """
    Rearrange the board by looking for empty spots until a solution is found.
    """
    while model.victory_move not in model.list_of_moves:
        rearrange_board(model)
    

        #print(model.moves)
       
    # Print out the final board and amount of moves in the terminal
    model.print(moves=True)
    # breakpoint()
    # print(model.moves[0])
    # for line in model.moves[0]:
    #     print(line)
    return model.moves
    
    
def rearrange_board(model):
    """
    Chooses an empty space and a car that can move to this place and swaps these.
    """
 
    # List all the empty spaces on the board
    empty_spaces = model.get_empty_spaces(model.board)

    # Choose a random spaces from the empty spaces
    random_empty_space = choose_random(empty_spaces)

    # Find the cars that are above, below and to the sides of the empty space
    directions = model.get_relevant_rows(random_empty_space)

    # Create a list for the cars that can move to the empty space
    possible_cars =  model.get_possible_cars(directions)

    # Choose a car that to move to the empty space
    random_car = choose_random(possible_cars)

    # Make sure the chosen place contains a car  
    if random_car != "":
        
        # Initialise the move
        new_move = [random_car, random_empty_space]

        # Add the new move to the list of moves
        model.list_of_moves.append(new_move)
        
        # Swap the car with an empty spot
        model.move_car(random_empty_space, random_car, directions)

        if model.board not in model.moves:
            temp_board = copy.deepcopy(model.board)
            model.moves.append(temp_board)
        

def choose_random(possible_cars):  
    """
    Returns "" or a random car from a list of possible cars. 
    """  
    if possible_cars:
        random_car = random.choice(possible_cars)
    else:
        random_car = ""

    return random_car