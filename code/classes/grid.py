import csv
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from .car import Car


class Grid():
    def __init__(self, source_file):
        self.cars = self.load_cars(source_file)
     

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


    def load_grid(self):
        """
        Checks title of csv file to see how big the grid is and loads the grid.
        Requires source_file. 
        """
        plt.plot()
        for x in range(6):
            for y in range(6):
                Checkforcar(x,y)
                if Checkforcar == True:
                    rect=mpatches.Rectangle((x,y),1,1, 
                                        fill = True,
                                        color = "purple",
                                        linewidth = 2)
                    plt.gca().add_patch(rect)
                else:
                    rect=mpatches.Rectangle((x,y),1,1, 
                                            fill = False,
                                            color = "purple",
                                            linewidth = 2)
                    plt.gca().add_patch(rect)

        plt.savefig('name.png') 
    
    def Checkforcar(x,y):
        for 


   

    #def is_victory(self):
     #   """
     #   checks if the game is won.
     #   """
     #   pass
