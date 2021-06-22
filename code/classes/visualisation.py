"""
Visualisation of the game of Rush Hour
"""
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import imageio
import os

class Visualisation():
    def __init__(self, path, car_ids):
        #self.car_ids = get_car_ids(model.board)
        self.board = self.draw_board(path.board, car_ids)
        #self.car_ids

    def draw_board(self, board, car_ids):
        """
        Visualises the 2D array by creating a plot and filling this with different colors
        """
        # Initialise an empty plot
        plt.plot()

        # Remove the x and y labels
        plt.xticks([])
        plt.yticks([])

        # Loop over the 2D array for the different cars
        for x in range(len(board)):
            for y in range(len(board)):

                # Car X will be colored red
                if board[y][x] == "X":
                    rect = patches.Rectangle((x, len(board)-y), 1, 1, 
                                            fill = True,
                                            color = "red",
                                            linewidth=0.4,
                                            alpha=0.35,
                                            capstyle ='round',
                                            linestyle='solid')
                    plt.gca().add_patch(rect)

                # The other cars will be a color from the color_map
                if board[y][x] != "0":

                    # Get the amount of different colors based on the amount of cars, + 2 removes red from the spectrum
                    color_map = plt.cm.get_cmap("hsv", len(car_ids) + 2)
                    rect = patches.Rectangle((x, len(board)-y), 1, 1, 
                                            fill = True,
                                            color = color_map(car_ids[board[y][x]]),
                                            linewidth=0.4,
                                            alpha=0.35,
                                            capstyle ='round',
                                            linestyle='solid')
                    plt.gca().add_patch(rect)

                # The empty spaces not have any color
                rect = patches.Rectangle((x, len(board)-y), 1, 1, 
                    fill = False, 
                    color = "lightgrey",
                    linewidth=0.4,
                    alpha=0.55,
                    capstyle='round')
                plt.gca().add_patch(rect)


    def save_plot(self, title):     
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