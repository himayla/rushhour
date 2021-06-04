from code.classes import grid

if __name__ == "__main__":
    # Input the filename 
    map_name = "12x12_7"

    # Create a grid from our data
    test_grid = grid.Grid(f"data/Rushhour{map_name}.csv")
    
    test_grid.print()
