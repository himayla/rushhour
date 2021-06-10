# Rush hour 

<i>Implementation by team: Unjamming my Jam</i>

Rush Hour is a logic game where the goal is to slide the cars in such a way that car (X) is free to drive to the exit. 
This code aims algorithimically solve this puzzle using the least amount of moves. To achieve this we have set ourselves the following sub-goals:

- [x] Read data from CSV-file
- [x] Visualise data in a grid
- [x] Algorithm which generates random solutions
- [ ] First algorithm 
- [ ] Second algorithm
- [ ] Find the quickest the solution

### Getting started
To run this code the package matplotlib is required, you can download this with this command:
```pip install matplotlib``` or or ```pip3 install matplotlib```.
After cloning the Git code you can run a board by running:
```python main.py``` or ```python3 main.py```.

A visualisation will be shown in the terminal as well as in a pop-up.

### Structure
The Git repository is structured as follows:
* **/code:**: all code of this project
    *  **/code/algorithms**: code for algorithms
        * Randomise.py: solves the board by finding empty spots and moves cars there until car X is at final destination.
    * **/code/classes**: contains a car and a grid class.
* **/data**: contains different starting positions from cars to fill a grid

### Authors
* Mila Sparreboom
* Julius Kemmer
* Mayla Kersten

Our group currently uses [this](https://drive.google.com/drive/folders/1weqj6__kEpObx-_6V2E9ijmGJZKb-iqt) folder to work in.
