import csv
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from .car import Car
import numpy as np

class Grid():
    def __init__(self, source_file):
        self.cars = self.load_cars(source_file)
        self.board = self.load_grid(source_file)
        #self.draw_board()

    def load_cars(self, source_file):
        """
        Returns a dictionary with car objects based on data from source_file.
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
        elif "9x9" in source_file:
            size = 9   
        elif "12x12" in source_file:
            size = 12
        else:
            print("Invalid size of board")
    
        # Initialise a 2D array filled with 0's based on the size
        array = [["0" for x in range(size)] for y in range(size)]

        colors_H = ["cyan", "magenta", "purple"]
        colors_V = ["blue", "orange", "pink", "brown"]

        # Loop through the car objects
        for car in self.cars.values():
            array[car.y-1][car.x-1] = car.name

            # Check if the car is positioned vertical or horizontal
            if car.orientation == "H":
                
                # If a horizontal car has length 2 display the car at x+1
                if car.length == 2:
                    array[car.y-1][car.x] = car.name

                    if car.name == "X":
                        car.color = "red"
                    else:
                        car.color = np.random.choice(colors_H)

                # If a horizontal car has length 3, draw the name of the car at x+1 and x+2 as well
                elif car.length == 3:
                    array[car.y-1][car.x] = car.name
                    array[car.y-1][car.x+1] = car.name
                    car.color = "green"

            # If car is positioned vertical
            elif car.orientation == "V" :

                # If a vertical car has length 2, draw the name of the car at y+1
                if car.length == 2:
                    array[car.y][car.x-1] = car.name
                    car.color = np.random.choice(colors_V)


                # If a vertical car has length 3, draw the carname at y+1 and y+2 as well
                elif car.length == 3:
                    array[car.y][car.x-1] = car.name
                    array[car.y+1][car.x-1] = car.name
                    car.color = "yellow"

        return array

    def print(self):      
        for car in self.board:
            print(car)