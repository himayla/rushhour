import csv
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from .car import Car
import numpy as np


class Grid():
    def __init__(self, source_file):
        self.cars = self.load_cars(source_file)
        self.coordinates= self.load_coordinates(source_file)
        self.graph=self.load_grid(source_file)

    def load_grid(self, source_file):
        """
        Checks title of csv file to see how big the grid is and loads the grid.
        Requires source_file. 
        """
        if "6" in source_file:
            size = 6
        elif "9" in source_file:
            size = 9   
        elif "12" in source_file:
            size = 12
        plt.plot()
        # loops over the 2D array and checks the value at each place
        for x in range(len(self.coordinates)):
            for y in range(len(self.coordinates[x])):
                # If the value is 0, there is no car, the square is not filled
                if self.coordinates[y][x]=="0":
                    rect=mpatches.Rectangle((x,size-y),1,1, 
                                        fill = False,
                                        color = "purple",
                                        linewidth = 2)
                    plt.gca().add_patch(rect)
                    
                # If the value is not 0, there is a car, the square is filled
                else:
                    rect=mpatches.Rectangle((x,size-y),1,1, 
                                            fill = True,
                                            color = "purple",
                                            linewidth = 2)
                    plt.gca().add_patch(rect)
                    # Add the name of the car on the square where it's found
                    plt.text(x + 0.25, size+0.25-y,self.coordinates[y][x],fontsize=10, color="red", weight="bold")

        plt.savefig('name.png') 
     
    def load_coordinates(self, source_file):
        if "6" in source_file:
            size = 6
        elif "9" in source_file:
            size = 9   
        elif "12" in source_file:
            size = 12   
        # Make a 2D array filled with 0's 
        a = [["0" for x in range(size)] for y in range(size)] 
        for car in self.cars.values():
            a[car.y-1][car.x-1]=car.name
            if car.orientation=="H":
                if car.length==2:
                    # If a horizontal car has length 2, draw the carname at x+1 as well
                    a[car.y-1][car.x]=car.name
                elif car.length==3:
                    # If a horizontal car has length 3, draw the carname at x+1 and x+2 as well
                    a[car.y-1][car.x]=car.name
                    a[car.y-1][car.x+1]=car.name
            elif car.orientation=="V":
                if car.length==2:
                    # If a vertical car has length 2, draw the carname at y+1 as well
                    a[car.y][car.x-1]=car.name
                elif car.length==3:
                    # If a vertical car has length 3, draw the carname at y+1 and y+2 as well
                    a[car.y][car.x-1]=car.name
                    a[car.y+1][car.x-1]=car.name
        return a

    def load_cars(self, source_file):
        """
        load all cars into the grid.
        No longer necessary
        """
        cars = {}
        with open(source_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                cars[row['car']] = Car(row['car'],row['orientation'], int(row['col']), int(row['row']), int(row['length']))
                
        return cars

    def print(self):      
        for coor in self.coordinates:
            print(coor)
        
   
    #def is_victory(self):
     #   """
     #   checks if the game is won.
     #   """
     #   pass
