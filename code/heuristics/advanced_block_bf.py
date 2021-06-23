"""
This optimalisation heurisitic scores a board based on the cars that block the red car from driving to the exit.
This heuristic is specifically designed for the Best First algorithm, so the results can be put in to a priority queue.
Inherits from advanced_block_bs.
"""

from .advanced_block_bs import BlockCar

class BlockCarBF(BlockCar):
 
    def run(self, board):
        """
        Calls the methods for this heuristic.
        """
        scores = []

        right_red = self.check_red_car(board.board)
        rel_moves = self.relevant_moves(right_red, board.board)

        score = self.score_board(rel_moves[0], rel_moves[1])
        scores = (-score, board)

        return scores