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

    def __str__(self):
        return f"{self.coordinates}"


    def load_grid(self, source_file):
        """
        Plots the gameboard as a grid based on the dimensions in name of input file and fills the grid with beginning positions.
        Requires source_file. 
        """
        if "6" in source_file:
            size = 6
        elif "9" in source_file:
            size = 9   
        elif "12" in source_file:
            size = 12
        
        # An empty plot, to fill 
        plt.plot()

        # Loops over the 2D array and checks the value at each place
        for x in range(len(self.coordinates)):
            for y in range(len(self.coordinates[x])):

                # Only fill squares if the coordinates aren't null, source https://datavizpyr.com/how-to-draw-a-rectangle-on-a-plot-in-matplotlib/
                if self.coordinates[y][x] != "0":
                    rect=mpatches.Rectangle((x,size-y),1,1, 
                                            fill = True,
                                            color = "purple",
                                            linewidth = 2)
                    plt.gca().add_patch(rect)

                    # Add the name of the car on the square where it's found
                    plt.text(x + 0.25, size+0.25-y,self.coordinates[y][x],fontsize=10, color="red", weight="bold")

        # Save the plot as a file
        plt.savefig('name.png')

        # # Pop up
        # plt.show()
     
    def load_coordinates(self, source_file):
        """
        For every car the X and Y coordinates are inserted into a 2D grid array.
        """
        if "6" in source_file:
            size = 6
        elif "9" in source_file:
            size = 9   
        elif "12" in source_file:
            size = 12
    
        # Draw a 2D array filled with 0's, based on the size
        a = [["0" for x in range(size)] for y in range(size)]

        for car in self.cars.values():
            a[car.y-1][car.x-1] = car.name

            # Check if the car is positioned vertical or horizontal
            if car.orientation == "H" :
                
                # If a horizontal car has length 2, draw the name of the car at x+1
                if car.length == 2:
                    a[car.y-1][car.x] = car.name
                
                # If a horizontal car has length 3, draw the name of the car at x+1 and x+2 as well
                elif car.length == 3:
                    a[car.y-1][car.x] = car.name
                    a[car.y-1][car.x+1] = car.name

            # If car is positioned vertical
            elif car.orientation == "V" :

                # If a vertical car has length 2, draw the name of the car at y+1
                if car.length == 2:
                    a[car.y][car.x-1] = car.name

                # If a vertical car has length 3, draw the carname at y+1 and y+2 as well
                elif car.length == 3:
                    a[car.y][car.x-1] = car.name
                    a[car.y+1][car.x-1] = car.name
        return a


    def load_cars(self, source_file):
        """
        Create car objects from the information in the CSV file
        """

        # Empty dictionary to store the cars in
        cars = {}

        with open(source_file, 'r') as in_file:

            # Read the car information from file
            reader = csv.DictReader(in_file)

            for row in reader:

                # Create the car objects
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
