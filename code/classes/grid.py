import csv

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


    # def load_grid(self):
    #     """
    #     Checks title of csv file to see how big the grid is and loads the grid.
    #     """
    #     pass

    #def is_victory(self):
     #   """
     #   checks if the game is won.
     #   """
     #   pass
