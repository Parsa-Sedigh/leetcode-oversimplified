import collections
from typing import List


# T: O(1) - we're always iterating on a 9x9 board.
# M: O(1)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)  # Tracks digits in each column
        rows = collections.defaultdict(set)

        # Tracks digits in each 3x3 square. The key is gonna be a pair of values, so: (row / 3, column / 3).
        # For example: Cell (4, 5) belongs to the square at (4//3, 5//3) = (1, 1) (second row, second column of 3x3 squares).
        squares = collections.defaultdict(set)

        # according to the question desc, we're always given a 9x9 matrix.
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                # Have we found duplicates?
                if (board[r][c] in rows[r] or
                        board[r][c] in cols[c] or
                        board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
