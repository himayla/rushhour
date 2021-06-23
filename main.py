from code.classes import grid, model

from code.algorithms import beam_search as bs
from code.algorithms import best_first as bf
from code.algorithms import breadth_first as dp
from code.algorithms import depth_first as df
from code.algorithms import hillclimber as hc
from code.algorithms import randomise as rn
from code.algorithms import state_space as ss

from code.classes import visualisation as vs


if __name__ == "__main__":
    map_name = "6x6_1"
    new_grid = grid.Grid(f"data/Rushhour{map_name}.csv")

    # --------------------------- Beam search  -------------------------------- #
    # paths = bs.BeamSearch(model.Model(new_grid)).run() # duurt heel lang met 6x6_3, dus weet niet of hij het doet
   
    # --------------------------- Best First  --------------------------------- #
    #paths = bf.BestFirst(model.Model(new_grid)).run() #!!!

    # --------------------------- Breadth first -------------------------------- #
    #paths = bf.Breadthfirst(model.Model(new_grid)).run()  # doet het wel met 6x6_3

    # -------------------------- Concatenated search  -------------------------- #
    #paths = cs.ConcatenatedSearch(model.Model(new_grid)).run() #!!!
    
    # --------------------------- Depth first --------------------------------- #
    paths = df.DepthFirst(model.Model(new_grid)).run() # recursie error

    # # # --------------------------- Hill Climber --------------------------------- #
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
    #paths = rn.random_solver(model.Model(new_grid)) # doet het wel met 6x6_3
    #print(paths[0])
    # for line in paths[0]:
    #     print(line)
    # length = len(paths)
    # print(f"other side:")
    # for line in paths[length - 1]:
    #     print(line)

    #  --------------------------- State Space ------------------------------------ #
    # paths = ss.StateSpace(model.Model(new_grid)).run()
    
    # --------------------------- Visualisation ----------------------------------- #
    car_ids = model.Model.get_car_ids(new_grid)    
    image_dir = f"doc/visualisation"
    
    # Visualise the different boards and save them in folder 
    counter = 1.0
    for path in paths:
        vs.Visualisation(path, car_ids).save_plot(f"{image_dir}/{counter:.1f}")
        counter += 0.1

    #Create gif from images in the folder
    vs.Visualisation.create_gif(f"{image_dir}")
