"""
pseudocode: 
1. get list of children from algorithms
2. Check for each child if the red car is blocked
    2a. if not: move red car and return final board / tell to move red car
3. For each car that blocks the red car: 
    4. Check if that car is blocked
        5. If so, check what blocks that
"""
class BlockCar:
    def __init__(self):
        self.right_x = []
        self.row_x = ""
        self.pos_car_row_x = {}
        self.board_score = 0


    def check_red_car(self, grid):
        """
        for every car that's to the right to the red car, save the name of the car and the vertical value it's on
        """
        length = len(grid[0])
        # Determine the row the red car is on vertically by using the size of the grid
        if length == 6: 
            self.row_x = 2
        elif length == 9:
            self.row_x = 4
        elif length == 12:
            self.row_x = 5

        # Determine the horizontal value of the red car
        hort_value = ""
        counter =0
        for value in grid[self.row_x]:
            
            if value == "X":
                hort_value = counter
            counter +=1
        # For each car to the right of the red car on the same horizontal row as the red car, check if there is a car
        for value in range(hort_value + 1, len(grid[self.row_x])):
            car_place = grid[self.row_x][value], value
            # If there is a car append it to the list along with the horizontal value
            if grid[self.row_x][value] != "0":
                self.right_x.append(car_place)
            # If there isn't a car, add 10 points to the board score
            else:
                self.board_score = self.board_score + 10
        return self.right_x
        

    def relevant_moves(self, right_x, grid):
        """
        for each car, checks the relative position to see how far up or down it needs to move 
        to free up the space to the right of the red car
        Each relative move is stored in the dictionaries needs_up and needs_down where the key is the name of the car
        """
        # for each car in the right_x list, use the car as a key in the dictionary that points to the row it's on
        for value in right_x:
            car_row = []
            for car in range(0, len(grid[0])):
                car_row.append(grid[car][value[1]])
            self.pos_car_row_x[value[0]] = car_row
        needs_up = {}
        needs_down = {}
        # Check how for each car in the dictionary needs to move up or down by counting how many cars are above and below the horizontal value of the red car
        for key, value in self.pos_car_row_x.items():
            countu = 1
            countl = 1
            for letter in range(0, self.row_x):
                if key == value[letter]:
                    countu +=1
            # Store the amount of moves the car needs to move down in the dictionary needs_down with the carname as a key
            needs_down[key] = countu
            for letter in range(self.row_x + 1, len(grid[0])):
                if key == value[letter]:
                    countl +=1
            # Store the amount of moves the car needs to move up in the dictionary needs_up with the carname as a key
            needs_up[key] = countl
        return needs_up, needs_down
            
    def check_moves(self, needs_up, needs_down):
        """
        Give one point for each way a car that blocks the red car to move up to free the x-axis. 
        Gives a half point for each way a car that blocks the red car to be able to move at all.
        Gives a tenth of a point for every empty spot that is in the car of a car that blocks the red car. 
        """
        for key, value in self.pos_car_row_x.items():
                     
            count_empty_up = 0
            count_empty_low = 0
            count_vert = 0
            for letter in range(len(value)):
                if value[letter] == "0":
                    count_empty_up += 1
                    # If there is an empty space somewhere above the car that blocks the red car, attribute 0.1 points to the score
                    self.board_score += 0.1
                if value[letter] == key:
                    if needs_up[key] == count_empty_up:
                        # If there is enough space for the car to move upwards to free up a space on the red_car row, attribute 5 points
                        self.board_score += 5
                    if value[letter -1]== "0":
                        # If there is a space directly above the car that blocks the red car, attribute 0.5 points
                        self.board_score += 0.5
                    continue
            for letter in range(self.row_x, len(value)):
                if value[letter] != key:
                    count_vert += 1
                    if value[letter] == "0":
                         # If there is an empty space somewhere below the car that blocks the red car, attribute 0.1 points to the score
                        self.board_score += 0.1
                        count_empty_low += 1
                        if count_vert == 1:
                            # If there is a space directly below the car that blocks the red car, attribute 0.5 points
                            self.board_score += 0.5
                    else:
                        continue
                if count_empty_low == needs_down[key]:
                    # If there is enough space for the car to move downwards to free up a space on the red_car row, attribute 5 points
                    self.board_score += 5
        return self.board_score

    def reset(self):
        self.right_x = []
        self.row_x = ""
        self.pos_car_row_x = {}
        self.board_score = 0

    def run(self, grid):
        scores = {}   
        right_x = self.check_red_car(grid)
        rel_moves = self.relevant_moves(right_x, grid)
        score = self.check_moves(rel_moves[0], rel_moves[1])
        self.reset()
        scores[str(grid)] = [score, grid]
        return scores
            
# """
# Future ideas: 
# - check the third row
# - Each row has a different amount of points awarded for it, decreasing each degree. 
# - The red-car row has a different amount of points awarded to it, decreasing to the right. 
# """