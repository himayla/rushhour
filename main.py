"""
Instructions: 
    - Uncomment any algorithm to run diffenrent algoritms. 
    - You can combine Hillclimber with any algorithm, and you can combine the visualisation with any algorithm(s).
    - Change the playing board by changing the map_name to 6x6_1/2/3, 9x9_4/5/6 or 12x12_7.
"""
import sys

from code.classes import grid, model
from code.algorithms import beam_search as bs
from code.algorithms import best_first as bf
from code.algorithms import breadth_first as dp
from code.algorithms import depth_first as df
from code.algorithms import hillclimber as hc
from code.algorithms import randomise as rn
from code.classes import visualisation as vs
from code.algorithms import state_space as ss

# Modifies Pythons recursion limit for longer paths
sys.setrecursionlimit(5000)

if __name__ == "__main__":

    # Change board here:
    map_name = "6x6_1"

    # Create a new object based on the data
    new_grid = grid.Grid(f"data/Rushhour{map_name}.csv")

    # ------- Algoritm implementations. Uncomment to run the algorithm!----------- #

    # --------------------------- Beam search  ----------------------------------- #
    # paths = bs.BeamSearch(model.Model(new_grid)).run()

    # --------------------------- Best First  ------------------------------------ #
    # paths = bf.BestFirst(model.Model(new_grid)).run()

    # --------------------------- Breadth first ---------------------------------- #
    # paths = bf.Breadthfirst(model.Model(new_grid)).run()

    # --------------------------- Depth first ------------------------------------ #
    # paths = df.DepthFirst(model.Model(new_grid)).run()

    # ---------------------------- Randomise ------------------------------------- #
    # paths = rn.random_solver(model.Model(new_grid))

    # --------------------------- Hill Climber ----------------------------------- #
    # print("Setting up Hill Climber...")
    # print(f"length path before: {len(paths)}")
    # model_path = []
    # for path in paths:
    #     model_path.append(model.Model(path))      
    
    # path = hc.HillClimber(model_path).run(100)
    # print(f"length path after: {len(path)}")
    # ---------------------------- Visualisation ---------------------------------- #
    # car_ids = model.Model.get_car_ids(new_grid)    
    # image_dir = f"visualisation/boards"
    
    # # Visualise the different boards and save them in folder 
    # counter = 1.0
    # for path in paths:
    #     vs.Visualisation(path, car_ids).save_plot(f"{image_dir}/{counter:.1f}")
    #     counter += 0.1

    # # Create gif from images in the folder
    # vs.Visualisation.create_gif(f"{image_dir}")