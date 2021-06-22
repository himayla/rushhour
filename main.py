from code.classes import grid, model
from code.classes import visualisation as vs
from code.algorithms import randomise as rn
from code.algorithms import breadth_first as dp
from code.algorithms import depth_first as DF
from code.algorithms import best_first as BF
from code.algorithms import beam_search as BS
from code.algorithms import concatenated_search as CS
from code.algorithms import hillclimber as hc

# Mayla's dingen:
from code.algorithms import randomise_mayla 
from code.algorithms import depth_first_mayla2 as df


if __name__ == "__main__":
    map_name = "6x6_1"
    new_grid = grid.Grid(f"data/Rushhour{map_name}.csv")

    # --------------------------- Randomise and Depth by Mayla ----------------------------------- #
    #random_model = randomise_mayla.random_solver(model.Model(new_grid))

    depth = df.DepthFirst(model.Model(new_grid))
    depth.run()
    
    # --------------------------- Hill Climber ---------------------------------
    # print("Setting up Hill Climber...")
    # climber = hc.HillClimber(random_model)

    # print("Running Hill Climber...")
    # climber.run(10, verbose=False)

    # print(f"Value of the configuration after Hill Climber: "
    #       f"{climber.model.calculate_value()}")

    # --------------------------- Breadth first ------------------------------- #
    # paths = dp.Breadthfirst(new_grid.board).run()
    # name = "breadth"
    
    # --------------------------- Depth first --------------------------------- #
    # paths = DF.DepthFirst(new_grid.board).run()

    # --------------------------- Randomise ----------------------------------- #
    #rn.Randomise(new_grid.board).run()

    # --------------------------- best first  --------------------------------- #
    # paths = BF.BestFirst(new_grid.board).run()

    # --------------------------- beam search  --------------------------------- #

    #paths = BS.BeamSearch(new_grid.board).run()

    # --------------------------- concatenated search  --------------------------------- #
    # paths = CS.BeamSearch(new_grid.board).run()
    # -------------------------- Visualisation (for depth and breadth)-------------------------------- #
    # car_ids = model.Model.get_car_ids(paths)
    # image_dir = f"visualisation/{name}"
    
    # # Visualise the different boards and save them in folder 
    # counter = 1.0
    # for path in paths:
    #     vs.Visualisation(path, car_ids).save_as(f"{image_dir}/{counter:.1f}")
    #     counter += 0.1

    # # Create gif from images in the folder
    # vs.Visualisation.create_gif(f"{image_dir}")
 

    