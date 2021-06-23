"""
This class contains the car object. 
The car object has a name, orientation of the car, their x and y coordinates along with the length of the car.
"""

class Car():
    def __init__(self, name, orientation, x, y, length):
        self.name = name
        self.orientation = orientation
        self.x = x
        self.y = y
        self.length = length