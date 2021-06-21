# Rush hour 

<i>Implementation by team: Unjam my Jam</i>

Rush Hour is a logic game where the goal is to slide the cars in such a way that the car (X) is able to drive to the exit. 
This project aims to algorithimically solve this puzzle using the least amount of moves. To achieve this we have set ourselves the following sub-goals:

- [x] Read data from CSV-file
- [x] Visualise data in a grid
- [x] Algorithm which generates random solutions
- [x] First algorithm 
- [x] Second algorithm
- [?] Find the quickest the solution

### Getting started
After cloning the Git code you can run a board by running:
```python main.py``` or ```python3 main.py```.
To run this code the package matplotlib is required, you can download this with this command:
```pip install matplotlib``` or ```pip3 install matplotlib```.
In order to create GIFs of the solutions, another package is required called imageio. Which can be downloaded with this command: 
```pip install imageio``` or ```pip3 install imageio```.

A visualisation will of the board will be available in **visualisation/boards**

### Structure
The Git repository is structured as follows:
* **/code:**: all code of this project
    *  **/code/algorithms**: code for algorithms
        * Best_first.py: solve the board by sorting the children based on their score.
        * Beam_search.py: solve the board by removing children based on their score.
        * Breadth_first.py: solves the board by checking each generation from left to right (horizontally).
        * Depth_first.py: solves the board by checking the generations vertically. It selects the first possible next state of the original board and then the next state of that board until a solution is reached or there are no more states to check. 
        * Concatenated_search.py: solves the board by adapting to the situation it's presented with.
        * Randomise.py: solves the board by finding empty spots and moves cars there until car X is at final destination.
    * **/code/classes**: contains a car, grid and visualisation class.
    * **/code/heuristics**: heuristics for algorithms
* **/data**: contains different starting positions from cars to fill a grid

### Authors
* Mila Sparreboom
* Julius Kemmer
* Mayla Kersten