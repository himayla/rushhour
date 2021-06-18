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
        elke auto rechts van de rode auto, sla de naam vd auto op en op welke verticale waarde ie staat
        """
        length = len(grid[0])
        
        if length == 6: 
            self.row_x = 2
        elif length == 9:
            self.row_x = 4
        elif length == 12:
            self.row_x = 5

        
        hort_value = ""
        counter =0
        for value in grid[self.row_x]:
            
            if value == "X":
                hort_value = counter
            counter +=1
        
        for value in range(hort_value + 1, len(grid[self.row_x])):
            car_place = grid[self.row_x][value], value
            if grid[self.row_x][value] != "0":
                self.right_x.append(car_place)
            else:
                self.board_score = self.board_score + 10
        return self.right_x
        

    def relevant_moves(self, right_x, grid):
        """
        for each car, checks the relative position to see how far up or down it needs to move 
        to free up the space to the right of the red car
        Each relative move is stored in the dictionaries needs_up and needs_down where the key is the name of the car
        """
        
        for value in right_x:
            car_row = []
            for car in range(0, len(grid[0])):
                car_row.append(grid[car][value[1]])
            self.pos_car_row_x[value[0]] = car_row
        needs_up = {}
        needs_down = {}
        for key, value in self.pos_car_row_x.items():
            countu = 1
            countl = 1
            for letter in range(0, self.row_x):
                if key == value[letter]:
                    countu +=1
            needs_down[key] = countu
            for letter in range(self.row_x + 1, len(grid[0])):
                if key == value[letter]:
                    countl +=1
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
                    self.board_score += 0.1
                if value[letter] == key:
                    if needs_up[key] == count_empty_up:
                        self.board_score += 5
                    if value[letter -1]== "0":
                        self.board_score += 0.5
                    continue
            for letter in range(self.row_x, len(value)):
                if value[letter] != key:
                    count_vert += 1
                    if value[letter] == 0:
                        self.board_score += 0.5
                        count_empty_low += 1
                        if count_vert == 1:
                            self.board_score += 0.5
                    else:
                        continue
                if count_empty_low == needs_down[key]:
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
