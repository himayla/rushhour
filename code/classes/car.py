class Car():
    def __init__(self, name, orientation, x, y, length):
        self.name = name
        self.orientation = orientation
        self.x = x
        self.y = y
        self.length = length

    def __str__(self):
        return f"Car: {self.name}, {self.orientation}, {self.x}, {self.y}, {self.length}"


    def is_move_valid(self):
        """
        runs is_on_grid, is_correct_orientation and is_not_blocked to check if the move is valid.
        if move is valid, car can move
        """
        pass


    def is_on_grid(self):
        """
        Gets new direction to move in (x, y).
        checks if the position the user wants to move to is not off the grid.
        """
        pass

    def is_correct_orientation(self):
        """
        Gets car orientation.
        checks if  the move the user wants to make aligned is with the orientation of the car. 
        i.e. car is horizontal, car can only move left and right.
        """
        pass

    def is_not_blocked(self):
        """
        Gets new direction to move in (x, y).
        checks the position the user wants to move to is not blocked by other cars.
        """
        pass
      


        