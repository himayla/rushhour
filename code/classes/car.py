class Car():
    def __init__(self, name, orientation, x, y, length):
        self.name = name
        self.orientation = orientation
        self.x = x
        self.y = y
        self.length = length

    def __str__(self):
        return f"Car: {self.name}, {self.orientation}, {self.x}, {self.y}, {self.length}"
