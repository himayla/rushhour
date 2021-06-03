import csv
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from .car import Car
import numpy as np


class Grid():
    def __init__(self, source_file):
        self.cars = self.load_cars(source_file)
        self.coordinates= self.load_coordinates(source_file)
     
    def load_coordinates(self, source_file):
       

        # creating 2D array with nans
        num_of_rows = 6
        num_of_cols = 6
        a = np.zeros((num_of_rows, num_of_cols))   
        with open(source_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            for row in reader:
                a[int(row['col'])-1][int(row['row'])-1]=1
                 

        return a

    def load_cars(self, source_file):
        """
        load all cars into the grid.
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


    # def load_grid(self):
    #     """
    #     Checks title of csv file to see how big the grid is and loads the grid.
    #     Requires source_file. 
    #     """
    #     plt.plot()
    #     for x in range(6):
    #         for y in range(6):
    #             Checkforcar(x,y)
    #             if Checkforcar == True:
    #                 rect=mpatches.Rectangle((x,y),1,1, 
    #                                     fill = True,
    #                                     color = "purple",
    #                                     linewidth = 2)
    #                 plt.gca().add_patch(rect)
    #             else:
    #                 rect=mpatches.Rectangle((x,y),1,1, 
    #                                         fill = False,
    #                                         color = "purple",
    #                                         linewidth = 2)
    #                 plt.gca().add_patch(rect)

    #     plt.savefig('name.png') 
    
    # def Checkforcar(x,y):
    #     for 


   

    #def is_victory(self):
     #   """
     #   checks if the game is won.
     #   """
     #   pass
