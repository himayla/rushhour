import csv
from .car import Car

class Grid():
    def __init__(self, source_file):
        self.cars = self.load_cars(source_file)
        self.board = self.load_grid(source_file)
        self.solution

    def load_cars(self, source_file):
        """
        Returns a dictionary filled with car objects based on the data from source_file.
        """
        cars = {}

        with open(source_file, 'r') as file:
            csv_file = csv.DictReader(file)

            for row in csv_file:
                cars[row['car']] = Car(row['car'],row['orientation'], int(row['col']), int(row['row']), int(row['length']))

        return cars


    def load_grid(self, source_file):
        """
        Returns a 2D grid array with the starting positions of the car objects.
        """
        if "6x6" in source_file:
            size = 6
            self.solution = ['X', [5, 2]]
        elif "9x9" in source_file:
            size = 9 
            self.solution = ['X', [8, 4]]
        elif "12x12" in source_file:
            size = 12
            self.solution = ['X', [11, 5]]
        else:
            print("Invalid size of board")
    
        # Initialise a 2D array filled with 0's based on the size
        array = [["0" for x in range(size)] for y in range(size)]

        # Loop through the car objects
        for car in self.cars.values():
            array[car.y-1][car.x-1] = car.name

            # Check if the car is positioned vertical or horizontal
            if car.orientation == "H":
                
                # If a horizontal car has length 2 display the car at x+1
                if car.length == 2:
                    array[car.y-1][car.x] = car.name

                # If a horizontal car has length 3, draw the name of the car at x+1 and x+2 as well
                elif car.length == 3:
                    array[car.y-1][car.x] = car.name
                    array[car.y-1][car.x+1] = car.name

            # If car is positioned vertical
            elif car.orientation == "V" :

                # If a vertical car has length 2, draw the name of the car at y+1
                if car.length == 2:
                    array[car.y][car.x-1] = car.name

                # If a vertical car has length 3, draw the carname at y+1 and y+2 as well
                elif car.length == 3:
                    array[car.y][car.x-1] = car.name
                    array[car.y+1][car.x-1] = car.name

        return array

    def print(self):      
        for car in self.board:
            print(car)