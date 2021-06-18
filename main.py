from code.classes import grid
from code.classes import visualisation as vs
from code.algorithms import randomise as rn
from code.algorithms import breadth_first as dp
from code.algorithms import depth_first as DF
from code.algorithms import best_first as BF
from code.algorithms import beam_search as BS

if __name__ == "__main__":
    map_name = "6x6_1"
    new_grid = grid.Grid(f"data/Rushhour{map_name}.csv")

    def get_car_ids(paths):
        """
        Returns a dictionary with the cars and car ID's
        """
        car_ids = {}
        id = 0
        for x in range(len(paths[0])):
            for y in range(len(paths[0])):
                car = paths[0][y][x] 
                if car not in car_ids:
                    car_ids[paths[0][y][x]] = id
                    id += 1

        return car_ids

    # --------------------------- Breadth first ------------------------------- #
    # paths = dp.Breadthfirst(new_grid.board).run()
    
    # # --------------------------- Depth first --------------------------------- #
    # paths = DF.DepthFirst(new_grid.board).run()

    # --------------------------- Randomise ----------------------------------- #
    # rn.Randomise(new_grid.board).run()

    # --------------------------- best first  --------------------------------- #
    # paths = BF.BestFirst(new_grid.board).run()
    # --------------------------- beam search  --------------------------------- #
    paths = BS.BeamSearch(new_grid.board).run()
    
    # -------------------------- Visualisation (for depth and breadth)-------------------------------- #
    # car_ids = get_car_ids(paths)
    
    # image_dir = "visualisation/boards"

    # # Visualise the different boards and save them in folder 
    # counter = 1.0
    # for path in paths:
    #     vs.Visualisation(path, car_ids).save_as(f"{image_dir}/{counter}")
    #     counter += 0.1

    # # Create gif from images in the folder
    # vs.Visualisation.create_gif(image_dir)
 

    