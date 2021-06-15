from code.classes import grid
from code.classes import visualisation
from code.algorithms import randomise as rn
from code.algorithms import breadth_Mila as dp
from code.algorithms import breadth_first_Julius as BreadthFirst


if __name__ == "__main__":
    
    # Input the filename 
    map_name = "6x6_1"

    # **************** Randomise **************** #
    # Create a grid from our data
    new_grid = grid.Grid(f"data/Rushhour{map_name}.csv")
    new_grid.print()

    # visualisation.Visualisation(new_grid.board).save_as("stating board")

    # random_solver = rn.Randomise(new_grid.board)
    # random_solver.run()
    # visualisation.Visualisation(random_solver.grid).save_as("final board")

    # ********************************************* #

    # test_depth = dp.Depthfirst(new_grid.board)
    # test_depth.run()

    depthfirst = BreadthFirst.DepthFirst(new_grid.board)
    depthfirst.run()
    
