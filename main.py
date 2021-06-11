from code.classes import grid
from code.algorithms import randomise as rn
from code.algorithms import depth as dp


if __name__ == "__main__":
    
    # Input the filename 
    map_name = "12x12_7"

    # Create a grid from our data
    new_grid = grid.Grid(f"data/Rushhour{map_name}.csv")
    new_grid.print()

    # random_solver = rn.Randomise(test_grid.coordinates)
    # random_solver.run()

    test_depth = dp.Depthfirst(new_grid.board)
    test_depth.run()
