import matplotlib.patches as patches
import matplotlib.pyplot as plt
import imageio
import os
#import numpy as np

class Visualisation():
    def __init__(self, board, car_ids):
        self.car_ids = car_ids
        self.board = self.draw_board(board)
        

    def draw_board(self, board):
        """
        Visualises the 2D array by creating a plot and filling this with different colors
        """
        # Create a dictionary for the cars and assign them ID's
        # car_ids = {}
        # id = 0
        # for x in range(len(board)):
        #     for y in range(len(board)):
        #         car = board[y][x] 
        #         if car not in car_ids:
        #             car_ids[board[y][x]] = id
        #             id += 1
        
        # Get the amount of different colors based on the amount of cars
        color_map = plt.cm.get_cmap("hsv", len(self.car_ids) + 2)

        # Initialise empty plot, without x  and y labels
        plt.plot()
        plt.xticks([])
        plt.yticks([])

        # Loop over the 2D array and checks the car at each place
        for x in range(len(board)):
            for y in range(len(board)):
                    
                    # Add color to the location of cars
                    if board[y][x] != "0":
                        if board[y][x] == "X":

                            rect = patches.Rectangle((x, len(board)-y), 1, 1, 
                                                    fill = True,
                                                    color = "red",
                                                    linewidth=0.4,
                                                    alpha=0.35,
                                                    capstyle ='round',
                                                    linestyle='solid')
                            plt.gca().add_patch(rect)
                        
                        else:

                        #plt.text(x + 0.3, len(board) + 0.2-y,board[y][x], fontsize=10, color="gray") # Optional
                            rect = patches.Rectangle((x, len(board)-y), 1, 1, 
                                                    fill = True,
                                                    color = color_map(self.car_ids[board[y][x]]),
                                                    linewidth=0.4,
                                                    alpha=0.35,
                                                    capstyle ='round',
                                                    linestyle='solid')
                            plt.gca().add_patch(rect)

                    else:
                        rect = patches.Rectangle((x, len(board)-y), 1, 1, 
                                                fill = False, 
                                                color = "lightgrey",
                                                linewidth=0.4,
                                                alpha=0.55,
                                                capstyle='round')
                    plt.gca().add_patch(rect)

        # Pop up
        #plt.show()


    def save_as(self, title):     
        """
        Saves the plot
        """  
        # Save the plot as a file
        plt.savefig(f"{title}.png")
        plt.clf()


    def create_gif(image_dir):
        """
        Creates a gif from the different paths in the solution. Source: https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python
        """
        # TO DO!!!!: not sorted correctly now. It sorts: 1,10,11,12 .. 2,20!!
        images = []
        
        for file_name in os.listdir(image_dir):
            file_path = os.path.join(image_dir, file_name)
            images.append(imageio.imread(file_path))

        imageio.mimsave(f"{image_dir}/board.gif", images)