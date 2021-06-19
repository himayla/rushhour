"""
Visualisation of the game of Rush Hour
"""

import matplotlib.patches as patches
import matplotlib.pyplot as plt
import imageio
import os

class Visualisation():
    def __init__(self, board, car_ids):
        self.car_ids = car_ids
        self.board = self.draw_board(board)


    def draw_board(self, board):
        """
        Visualises the 2D array by creating a plot and filling this with different colors
        """
                
        # Get the amount of different colors based on the amount of cars. +2 removes red from the spectrum.
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
                        
                        # Make sure the car X is colored red
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


    def save_as(self, title):     
        """
        Saves the plot, based on input of the title.
        """
        plt.savefig(f"{title}.png")
        plt.clf()

    def create_gif(image_dir):
        """
        Creates a gif from the different paths in the solution. Source: https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python
        """
        images = []
        
        for file_name in os.listdir(image_dir):
            file_path = os.path.join(image_dir, file_name)
            images.append(imageio.imread(file_path))
            
        imageio.mimsave(f"{image_dir}/board.gif", images)