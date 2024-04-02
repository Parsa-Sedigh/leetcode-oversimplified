from collections import deque
from typing import List

# T: O(n * m)
# M: O(n * m)
class Solution:
	def orangesRotting(self, grid: List[List[int]]) -> int:
		ROWS = len(grid)
		COLS = len(grid[0])
		q = deque()
		time, fresh = 0, 0
		directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

		# Iterate over entire grid
		# Pre-work: We're gonna be doing 2 things at the same time:
		# 1. counting the number of fresh oranges
		# 2. identify all of the rotting oranges that exist at the beginning. Because we wanna have a multi-source BFS.
		for r in range(ROWS):
			for c in range(COLS):
				if grid[r][c] == 1:
					fresh += 1

				if grid[r][c] == 2:
					q.append([r, c])

		# if either of these become False, we wanna stop
		while q and fresh > 0:

			# Do not use a while loop here, because we would be adding to the q inside the loop but we don't want to work with
			# the newly updated data. We wanna take a snapshot and that's what range() does. If you wanted to use while,
			# you have to define a new variable called length outside of while and use that as the condition: `while len > 0:`

			# Note: Each iteration of this loop, is done in 1 unit of time. Because we're considering all of the rotten oranges that
			# we have before running the loop(we work with the snapshot)
			for i in range(len(q)):
				r, c = q.popleft()

				for dr, dc in directions:
					row, col = r + dr, c + dc

					# if in bounds and fresh, make it rotten
					if (row < 0 or row == ROWS or
						col < 0 or col == COLS or
						grid[row][col] != 1):
						continue

					grid[row][col] = 2
					q.append([row, col])
					fresh -= 1

			time += 1

		return time if fresh == 0 else -1
