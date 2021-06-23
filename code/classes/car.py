"""
This class contains the Car object its attributes contain: a name, orientation (vertical or horizontal), x and y coordinates and the length of the car.
"""
class Car():
    def __init__(self, name, orientation, x, y, length):
        self.name = name
        self.orientation = orientation
        self.x = x
        self.y = y
        self.length = length