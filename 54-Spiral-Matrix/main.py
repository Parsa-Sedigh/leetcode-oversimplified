from typing import List


class Solution:
	def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
		res = []

		# r is basically gonna be the number of `columns + 1` which is exactly len(matrix[0]) is gonna give us.
		# Note: len(matrix[0]) gives the number of columns
		left, right = 0, len(matrix[0])

		# Note: len(matrix) gives us the number of rows.
		top, bottom = 0, len(matrix)

		while left < right and top < bottom:
			# go left to right and get every value in the top row
			# We initialize right to be out of bounds, because with range() in python, it's gonna
			for i in range(left, right):
				res.append(matrix[top][i])
			top += 1

			# get every i in the right column
			for i in range(top, bottom):
				# We subtract right by one because we know right is actually out of bounds. It would be out of bounds for each
				# rectangle that we iterate
				res.append(matrix[i][right - 1])
			right -= 1

			if not (left < right and top < bottom):
				break

			# get every i in the bottom row
			# Note: Since the second arg of range() is non-inclusive, so if we wanna go all the way to left, we have to subtract it by one
			for i in range(right - 1, left - 1, -1):
				res.append(matrix[bottom - 1][i])

			# Subtract bottom by one since we wanna shift it upwards
			bottom -= 1

			# get every i in the left column
			for i in range(bottom - 1, top - 1, -1):
				res.append(matrix[i][left])

			# We just completed the entire left column, so we need to move left to the right
			left += 1

		return res

