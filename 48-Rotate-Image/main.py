from typing import List


class Solution:
	def rotate(self, matrix: List[List[int]]) -> None:
		"""
		Do not return anything, modify matrix in-place instead.
		"""
		# Left and right boundaries. r is the <number of columns - 1>. So len(matrix[0]) - 1, but we know that the number of columns
		# and rows are the same(n * n matrix). So we can just say: len(matrix) - 1
		l, r = 0, len(matrix) - 1

		while l < r:
			# Iterate through the entire row except the last element. So: range(l, r) . Or range(r - l). Let's say l is 0 and r is 3,
			# so we would do 3 - 0 which is gonna be 3 iterations even though we have 4 columns.
			for i in range(r - l):
				# top is the same as l and bottom the same as r. Because we do have a square matrix not a rectangle, it's a rectangle(n * n matrix).
				top, bottom = l, r

				# save the top left value
				topLeft = matrix[top][l + i]

				# move bottom left to top left
				# Note: By doing bottom - i(subtracting), we would go upwards vertically which is what we want as we move to inner matrixes
				# Note: We don't need to increment or decrement the column to get to the bottom left of inner matrixes, because l is gonna
				# get incremented automatically in the next iteration of while loop.
				matrix[top][l + i] = matrix[bottom - i][l]

				# move bottom right to bottom left
				matrix[bottom - i][l] = matrix[bottom][r - i]

				# move top right to bottom right
				# Note: As we go to inner matrixes, we're gonna move down in this column, so `top + i`
				matrix[bottom][r - i] = matrix[top + i][r]

				# move top left into top right
				matrix[top + i][r] = topLeft

			l += 1
			r -= 1