class Model():
    def __init__(self, grid):
        self.grid = grid
        self.solution = [[]]


    def get_possibilities(self, options):
        available_options = set(options)

        return available_options


    def is_victory(self):
        # For each board size (=length of a random x axis), choose a different victory move where car x needs to be to win
        if len(self.board) == 6:
            victory_move = ['X', [5, 2]]

        elif len(self.board) == 9:
            victory_move = ['X', [8, 4]]

        elif len(self.board) == 12:
            victory_move = ['X', [11, 5]]

        if victory_move:
            return True
        else:
            return False


    def copy(self):
        print(self.grid)
        new = Model(self.grid)

        new.victory.update(self.victory)

        return new




