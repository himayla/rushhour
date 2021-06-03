from code.classes import grid

if __name__ == "__main__":
    map_name = "6x6_1"

    # Create a grid from our data
    test_grid = grid.Grid(f"data/Rushhour{map_name}.csv")
    
    test_grid.print()
