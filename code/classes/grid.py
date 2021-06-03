import csv

from .car import Car


class Grid():
    def __init__(self, source_file):
        self.nodes = self.load_nodes(source_file)
     

    def load_cars(self, source_file):
        """
        load all cars into the grid.
        """
        cars = {}
        with open(source_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                cars[row['car']] = Car(row['orientation'], row['col'], row['row'], row['length'])

                # rooms[room_number] = Room(room_number, room_name, long_description)

        return cars

    def load_grid(self):
        """
        Checks title of csv file to see how big the grid is and loads the grid.
        """
        pass

     def is_victory(self):
         """
         checks if the game is won.
         """
         pass