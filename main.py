from code.classes import grid, model

from code.algorithms import beam_search as bs
from code.algorithms import best_first as bf
# from code.algorithms import breadth_first as dp
from code.algorithms import concatenated_search as cs
from code.algorithms import depth_first as df
from code.algorithms import hillclimber as hc
from code.algorithms import randomise as rn
from code.classes import visualisation as vs


if __name__ == "__main__":
    map_name = "6x6_1"
    new_grid = grid.Grid(f"data/Rushhour{map_name}.csv")

    # --------------------------- Beam search  --------------------------------- #
    #paths = bs.BeamSearch(model.Model(new_grid)).run()  #TD: nog gelinkt aan Randomise
    
    # --------------------------- Best First  --------------------------------- #
    #paths = bf.BestFirst(model.Model(new_grid)).run() #TD: nog gelinkt aan Randomise

    # --------------------------- Breadth first ------------------------------- #
    # paths = bf.Breadthfirst(model.Model(new_grid)).run()  #TD: nieuwe PQ

    # -------------------------- Concatenated search  --------------------------------- #
    # paths = cs.BeamSearch(model.Model(new_grid)).run() #TD: nog gelinkt aan Randomise
    
    # --------------------------- Depth first --------------------------------- #
    # paths = df.DepthFirst(model.Model(new_grid)).run()

    # --------------------------- Randomise ----------------------------------- #
    # rn.Randomise(new_grid.board).run() #TD: paths returnen?

    # # --------------------------- Hill Climber ---------------------------------
    # print("Setting up Hill Climber...")      #TD: model meegeven?
    # climber = hc.HillClimber(paths).run(20)

    # print("Running Hill Climber...")

    # print(f"Value of the configuration after Hill Climber: "
    #       f"{climber.model.calculate_value()}")
    # --------------------------- Randomise ----------------------------------- #
    #rn.random_solver(model.Model(new_grid))

    # -------------------------- Visualisation (for depth and breadth) TO DO CHECKEN -------------------------------- #
    # car_ids = model.Model.get_car_ids(paths)
    # image_dir = f"visualisation/{name}"
    
    # # Visualise the different boards and save them in folder 
    # counter = 1.0
    # for path in paths:
    #     vs.Visualisation(path, car_ids).save_as(f"{image_dir}/{counter:.1f}")
    #     counter += 0.1

    # # Create gif from images in the folder
    # vs.Visualisation.create_gif(f"{image_dir}")
