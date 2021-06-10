from code.classes import grid
from code.algorithms import randomise as rn
from code.algorithms import depth as dp


if __name__ == "__main__":
    
    # Input the filename 
    map_name = "6x6_1"

    # Create a grid from our data
    test_grid = grid.Grid(f"data/Rushhour{map_name}.csv")
    
    test_grid.print()

    #random_board = randomise.random_assignment(test_grid)

    test_random = rn.Randomise(test_grid.coordinates)
    test_random.run()

    # test_depth = dp.Depthfirst(test_grid.coordinates)
    # test_depth.run()
    # print(test_random)
