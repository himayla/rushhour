import csv
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from .car import Car
import numpy as np


class Grid():
    def __init__(self, source_file):
        self.cars = self.load_cars(source_file)
        self.coordinates= self.load_coordinates(source_file)
        self.graph=self.load_grid()

    def load_grid(self):
        """
        Checks title of csv file to see how big the grid is and loads the grid.
        Requires source_file. 
        """
        plt.plot()
        # loops over the 2D array and checks the value at each place
        for x in range(len(self.coordinates)):
            for y in range(len(self.coordinates[x])):
                # If the value is 0, there is no car, the square is not filled
                if self.coordinates[y][x]=="0":
                    rect=mpatches.Rectangle((x,6-y),1,1, 
                                        fill = False,
                                        color = "purple",
                                        linewidth = 2)
                    plt.gca().add_patch(rect)
                    
                # If the value is not 0, there is a car, the square is filled
                else:
                    rect=mpatches.Rectangle((x,6-y),1,1, 
                                            fill = True,
                                            color = "purple",
                                            linewidth = 2)
                    plt.gca().add_patch(rect)
                    # Add the name of the car on the square where it's found
                    plt.text(x + 0.5, 6.5-y,self.coordinates[y][x],fontsize=16, color="red", weight="bold")

        plt.savefig('name.png') 
    
    
     
    def load_coordinates(self, source_file):
        # The size of the array is still hardcoded
        num_of_rows = 6
        num_of_cols = 6  
        # Make a 2D array filled with 0's 
        a = [["0" for x in range(num_of_rows)] for y in range(num_of_cols)] 
        with open(source_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            for row in reader:
                # Draw the car-name at the x and y coordinates at the starting point of the car
                a[int(row['row'])-1][int(row['col'])-1]=row['car']
                if row['orientation']=="H":
                    if row['length']=="2":
                        # If a horizontal car has length 2, draw the carname at x+1 as well
                        a[int(row['row'])-1][int(row['col'])]=row['car']
                    elif row['length']=="3":
                        # If a horizontal car has length 3, draw the carname at x+1 and x+2 as well
                        a[int(row['row'])-1][int(row['col'])]=row['car']
                        a[int(row['row'])-1][int(row['col'])+1]=row['car']
                elif row['orientation']=="V":
                    if row['length']=="2":
                        # If a vertical car has length 2, draw the carname at y+1 as well
                       a[int(row['row'])][int(row['col'])-1]=row['car']
                    elif row['length']=="3":
                        # If a vertical car has length 3, draw the carname at y+1 and y+2 as well
                        a[int(row['row'])+1][int(row['col'])-1]=row['car']
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
                cars[row['car']] = Car(row['car'],row['orientation'], row['col'], row['row'], row['length'])
                
        return cars

    def print(self):
        for car in self.cars.values():
            print(car)
        print()
        for coor in self.coordinates:
            print(coor)
        
   
    #def is_victory(self):
     #   """
     #   checks if the game is won.
     #   """
     #   pass
