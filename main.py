from code.classes import grid, model

from code.algorithms import beam_search as bs
from code.algorithms import best_first as bf
from code.algorithms import breadth_first as dp
from code.algorithms import concatenated_search as cs
from code.algorithms import depth_first as df
from code.algorithms import hillclimber as hc
from code.algorithms import randomise as rn
from code.classes import visualisation as vs


if __name__ == "__main__":
    map_name = "6x6_1"
    new_grid = grid.Grid(f"data/Rushhour{map_name}.csv")

    # --------------------------- Beam search  -------------------------------- #
    #paths = bs.BeamSearch(model.Model(new_grid)).run() 
   
    # --------------------------- Best First  --------------------------------- #
    #paths = bf.BestFirst(model.Model(new_grid)).run() #!!!

    # --------------------------- Breadth first -------------------------------- #
    #paths = bf.Breadthfirst(model.Model(new_grid)).run() 

    # -------------------------- Concatenated search  -------------------------- #
    #paths = cs.ConcatenatedSearch(model.Model(new_grid)).run() #!!
    
    # --------------------------- Depth first --------------------------------- #
    paths = df.DepthFirst(model.Model(new_grid)).run()

    # # --------------------------- Hill Climber --------------------------------- #
    # print("Setting up Hill Climber...")
    # model_path = []
    # for path in paths:
    #     model_path.append(model.Model(path))      
    # climber = hc.HillClimber(model_path).run(100)
    # if len(climber) < len(paths):
    #     print(f"faster path: {len(climber)}")
    # else:
    #     print(f"that's plenty efficient!")

    #  --------------------------- Randomise ----------------------------------- #
    #rn.random_solver(model.Model(new_grid))
    
     # --------------------------- Visualisation ----------------------------------- #

    # car_ids = model.Model.get_car_ids(new_grid)    
    # image_dir = f"visualisation/boards"
    
    # # Visualise the different boards and save them in folder 
    # counter = 1.0
    # for path in paths:
    #     vs.Visualisation(path, car_ids).save_plot(f"{image_dir}/{counter:.1f}")
    #     counter += 0.1

    # #Create gif from images in the folder
    # vs.Visualisation.create_gif(f"{image_dir}")
