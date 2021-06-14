import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np


class Visualisation():
    def __init__(self, board):
        self.board = self.draw_board(board)

    def draw_board(self, board):

        colors = ["yellow", "magenta", "purple"]

        size = len(board)

        # Initialise empty plot
        plt.plot()
        plt.xticks([])
        plt.yticks([])

        color_dict = {}
   

        car_ids = {}
        id = 0

        for x in range(size):
            for y in range(size):
                car = board[y][x] 
                if car not in car_ids:
                    car_ids[board[y][x]] = id
                    id += 1
        

        color_map = plt.cm.get_cmap("hsv", len(car_ids))

        # Loop over the 2D array and checks the value at each place
        for x in range(size):
            for y in range(size):
                    if board[y][x] != "0":
                        if board[y][x] == "X":

                            rect = patches.Rectangle((x, size-y), 1, 1, 
                                                    fill = True,
                                                    color = "red",
                                                    linewidth=0.4,
                                                    alpha=0.35,
                                                    capstyle ='round',
                                                    linestyle='solid')
                            plt.gca().add_patch(rect)
                        
                        else:

                        rect = patches.Rectangle((x, size-y), 1, 1, 
                                                fill = True,
                                                color = color_map(car_ids[board[y][x]]),
                                                linewidth=0.4,
                                                alpha=0.35,
                                                capstyle ='round',
                                                linestyle='solid')
                        plt.gca().add_patch(rect)
                        #plt.text(x + 0.3, size + 0.2-y,board[y][x], fontsize=10, color="gray")

                    else:
                        rect = patches.Rectangle((x, size-y), 1, 1, 
                                                fill = False, 
                                                color = "lightgrey",
                                                linewidth=0.4,
                                                alpha=0.55,
                                                capstyle='round')
                        plt.gca().add_patch(rect)

    def save_as(self, title):       
        # Save the plot as a file
        plt.savefig(f"{title}.png")
        plt.clf()

        # Or pop up
        #plt.show()
