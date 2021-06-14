from code.classes import grid
from code.algorithms import randomise as rn
from code.algorithms import breadth_Mila as dp
from code.algorithms import breadth_first_Julius as BreadthFirst


if __name__ == "__main__":
    
    # Input the filename 
    map_name = "6x6_1"

    # Create a grid from our data
    new_grid = grid.Grid(f"data/Rushhour{map_name}.csv")
    print("---------startbord--------")
    new_grid.print()
    print("---------startbord--------")

    # random_solver = rn.Randomise(new_grid.board)
    # random_solver.run()

    test_depth = dp.Depthfirst(new_grid.board)
    test_depth.run()

    # depthfirst = BreadthFirst.DepthFirst(new_grid.board)
    # if depthfirst.run() == True:
    #     print("solution found")
    # else:
    #     print("not found")
