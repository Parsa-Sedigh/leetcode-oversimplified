from typing import List


class Solution:
	def solveNQueens(self, n: int) -> List[List[int]]:
		col = set()
		posDiag = set() # determined by r + c
		negDiag = set() # determined by r - c

		res = []
		board = [["."] * n for i in range(n)]

		def backtrack(r):
			# If this condition was true, that means we were able to find a valid n-queen solution
			if r == n:
				# Note: Since we're gonna be using the same board variable in subsequent function calls of this recursive function,
				# we need to make a copy of it.
				# Note: Also we need to change the formating of the board before adding it to the result, they want each row to be represented as
				# a string instead of an array
				copy = ["".join(row) for row in board]
				res.append(copy)

				return

			# Note: if we reached here, it means we didn't reach the base case, so we need to continue
			# Note: Try every single position in current row that we're at and see which positions are we allowed to place a queen inside?
			# Note: c represents a column number. Here, we're going through every column in the current row(r).
			for c in range(n):
				# 1- is the current column is already been used(we already have placed a queen in that column before)
				# 2- is there a queen already placed in current positive diagonal?
				# 3- is there a queen already placed in current negative diagonal?
				if (c in col or
				   (r + c) in posDiag or
				   (r - c) in negDiag):
					continue

				col.add(c)

				# r + c represents a diagonal in board, it means we can't put any other queen in any position that it's r + c adds up to the
				# one that we added to posDiag.
				# Note: Here we place a queen and update the related data structures. Now we go to the next row and go through all of it's
				# columns again to see at which column we can put the next queen.
				posDiag.add(r + c)
				negDiag.add(r - c)
				board[r][c] = "Q"

				backtrack(r + 1)

				# cleanup
				col.remove(c)
				posDiag.remove(r + c)
				negDiag.remove(r - c)
				board[r][c] = "."

		backtrack(0)

		return res