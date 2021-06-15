from code.classes import grid
from code.classes import visualisation as vs
from code.algorithms import randomise as rn
from code.algorithms import breadth_Mila as dp
from code.algorithms import depth_first as DF

if __name__ == "__main__":
    map_name = "6x6_1"

    # --------------------------- Random Reassignment -------------------------- #
    
    new_grid = grid.Grid(f"data/Rushhour{map_name}.csv")
    #new_grid.print()

    # vs.Visualisation(new_grid.board).save_as("starting_board")

    # random_solver = rn.Randomise(new_grid.board).run()
    # vs.Visualisation(random_solver.grid).save_as("final_board")

    # --------------------------- Breadth first --------------------------------- #

    # paths = dp.Breadthfirst(new_grid.board).run()

    # image_dir = "visualisation/boards"

    # counter = 1.0

    # # Create a dictionary of colors for the cars:
    # car_ids = {}
    # id = 0
    # for x in range(len(paths[0])):
    #     for y in range(len(paths[0])):
    #         car = paths[0][y][x] 
    #         if car not in car_ids:
    #             car_ids[paths[0][y][x]] = id
    #             id += 1
    # # Visualise the different boards and save them in folder 
    # for path in paths:
    #     vs.Visualisation(path, car_ids).save_as(f"{image_dir}/{counter}")
    #     counter += 0.1

    # Create gif from images in the folder
    # vs.Visualisation.create_gif(image_dir)
 
    # --------------------------- Depth first --------------------------------- #
    depthfirst = DF.DepthFirst(new_grid.board)
    depthfirst.run()
    