from typing import List

# Brute force solution
# T: O(m * n)
# M: O(1)
class Solution:
	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
		for row in matrix:
			for num in row:
				if num == target:
					return True

		return False

# T: O(log m + log n) where m and n are number of rows and cols.
# M: O(1)

# Note: that this algo is efficient because the given 2-d matrix is sorted
# in both rows and cols manner.
class Solution2:
	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
		# Get the dimensions of the matrix(we know matrix is always gonna be non empty)
		ROWS, COLS = len(matrix), len(matrix[0])

		# first binary search: look for the row that we need to find. top is top row and bot is bottom row
		top, bot = 0, len(matrix) - 1
		while top <= bot:
			row = (top + bot) // 2

			# is the target value greater than the largest value in this row?
			if target > matrix[row][-1]:  # or target > matrix[row][cols - 1]
				top = row + 1
			elif target < matrix[row][0]:
				bot = row - 1
			else:
				# target is not more than the last element of the row and also is not less than the first element of the row.
				# Therefore, it must be inside the row(could also be one of the first or last elements because the == case is not
				# covered)
				break

		# it's possible that if we did not break out of the loop, maybe we created an invalid condition where the condition got false. That
		# would tell us that we crossed out every single row and none of the rows contained the target, in that case we have to return False.
		if not (top <= bot):
			return False

		row = (top + bot) // 2
		l, r = 0, COLS - 1

		while l <= r:
			m = (l + r) // 2

			if target > matrix[row][m]:
				l = m + 1
			elif target < matrix[row][m]:
				r = m - 1
			else:
				return True

		return False
