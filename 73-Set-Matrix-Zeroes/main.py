from typing import List


class Solution:
	def setZeroes(self, matrix: List[List[int]]) -> None:
		"""
        Do not return anything, modify matrix in-place instead.
        """
		# O(1)

		# Get the number of rows and columns
		ROWS, COLS = len(matrix), len(matrix[0])

		# This variable is to tell us if the first row need to be set to zero or not
		rowZero = False

		# determine which rows and columns need to be zeroed
		# Iterate through the matrix
		for r in range(ROWS):
			for c in range(COLS):
				if matrix[r][c] == 0:
					# set the respected element in the first row to zero
					matrix[0][c] = 0

					# there's one catch: We can't set the respected element in the first column to zero, if we're still at the first row
					# In other words, we can not set the top left most position to 0, if we're still at the first row(meaning r == 0).
					# So check for r > 0. Remember that for row 0, we actually have a dedicated variable(rowZero)
					if r > 0:
						# we also want to set the respected element in the first column to zero
						matrix[r][0] = 0
					else:
						# If we're in the first row, for setting the element that is responsible for setting that row to 0,
						# we set this variable to True instead of the matrix[0][0] .
						rowZero = True

		# We have to skip the first row(range(1, ROWS)) and skip the first column(range(1, COLS)). Because we're gonna handle those
		# first row and first column, after. They have a special meaning, In other words, they're an indication of whetehte we should
		# zero out the respected row or column, so we need to treat them differently - we need to set them to 0, afterwards.
		for r in range(1, ROWS):
			for c in range(1, COLS):
				if matrix[0][c] == 0 or matrix[r][0] == 0:
					matrix[r][c] = 0

		# When we reach here, we have zeroed out the main part of the matrix. Now we can potentially zero out the first row and column if we need to

		# Remember the elements in the first row the matrix, tells us which COLUMNS we can zero out(for indexing columns, we use the second
		# Note: matrix[0][0] tells us if we can zero out the first column. Remember the green area is responsible for if we can set the
		# COLUMNS to zero.
		if matrix[0][0] == 0:
			# Zeroing out the first COLUMN of the matrix
			for r in range(ROWS):
				matrix[r][0] = 0

		# rowZero variable tells us if we can set the first row to zero or not.
		if rowZero:
			# Zeroing out the first ROW of the matrix. Go through every cell in the first row and zero it out
			for c in range(COLS):
				matrix[0][c] = 0