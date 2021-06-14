from code.classes import grid
from code.classes import visualisation as vs
from code.algorithms import randomise as rn
from code.algorithms import breadth_Mila as dp
from code.algorithms import breadth_first_Julius as BreadthFirst

if __name__ == "__main__":
    map_name = "6x6_1"

    # --------------------------- Random reassignment -------------------------- #
    
    new_grid = grid.Grid(f"data/Rushhour{map_name}.csv")
    #new_grid.print()

    # vs.Visualisation(new_grid.board).save_as("starting_board")

    # random_solver = rn.Randomise(new_grid.board).run()
    # vs.Visualisation(random_solver.grid).save_as("final_board")

    # --------------------------- Breadth first --------------------------------- #

    paths = dp.Depthfirst(new_grid.board).run()

    image_dir = "visualisation/boards"

    counter = 1

    # Visualise the different boards and save them in folder 
    for path in paths:
        vs.Visualisation(path).save_as(f"{image_dir}/{counter}")
        counter += 1

    # Create gif from images in the folder
    vs.Visualisation.create_gif(image_dir)
 
    # --------------------------- Depth first --------------------------------- #
    # depthfirst = BreadthFirst.DepthFirst(new_grid.board)
    # if depthfirst.run() == True:
    #     print("solution found")
    # else:
    #     print("not found")