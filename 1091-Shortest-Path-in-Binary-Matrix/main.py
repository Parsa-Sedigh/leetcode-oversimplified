from collections import deque
from typing import List

# Neetcode solution. I tweaked it a bit, because didn't understand it.
class Solution:
	def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
		N = len(grid) # in this question, the grid is n * n, so ROWS = COLS = N

		# Note: We can have a separate variable for length, but that would complicate the while loop.
		q = deque([(0, 0, 1)]) # (r, c, length)

		# Should we add the node to the visit hashset at the time we ADD a cell to the queue, or at the time we POP it from
		# the queue. We prefer to do it as we ADD to the queue. You could do it the other way. It would be slightly less efficient,
		# not in terms of big o time complexity, big o would be the same because the number of cells we visit would be the same.
		visit = set((0, 0))
		directions = [[0, 1], [1, 0], [0, -1], [-1, 0],
					  [1, 1], [-1, -1], [1, -1], [-1, 1]]

		# This is an important edge case.
		if grid[0][0] == 1:
			return -1

		while q:
			r, c, length = q.popleft()

			# did we reach the destination
			if r == N - 1 and c == N - 1:
				return length

			# go through all the neighbors. We could write an arr with 8 elements,
			for dr, dc in directions:
				newR = r + dr
				newC = c + dc

			# Note: We're not checking `(r, c) in visit` condition here. Look at the solution.md for this.
				if (min(newR, newC) < 0 or
					newR == N or newC == N or # since it's a square matrix, we could say: max(r, c) == N
					(newR, newC) in visit or
					grid[newR][newC] == 1):
					continue

				# If we don't have this guard here, it means we're appending every single neighbor. It's ok if we append
				# some neighbors that are out of bounds, because we have a check for them in the first if block of the while loop,
				# it's also ok if we append a position that is an obstacle(is 1), because we're checking for that in that if block
				# as well, but what's not ok is visiting a node more than once. So we check it here and we don't check it in the
				# first if block of while.
				q.append((newR, newC, length + 1))
				visit.add((newR, newC))

		return -1

# Cracking FAANG
# T: O(R * C)
# M: O(R * C)
class Solution2:
	def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
		if grid[0][0] or grid[-1][-1]:
			return -1

		ROWS = len(grid)
		COLS = len(grid[0])

		queue = deque([ (0, 0, 1) ]) # r, c, length
		directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
					  (1, 1), (1, -1), (-1, 1), (-1, -1)]

		grid[0][0] = 1

		while queue:
			x, y, path_len = queue.popleft()

			# have we reached the target
			if (x, y) == (ROWS - 1, COLS - 1):
				return path_len

			# go 8-directionally
			for dx, dy in directions:
				new_x = x + dx
				new_y = y + dy

				if ((0 <= new_x < ROWS) and (0 <= new_y < COLS) and
					grid[new_x][new_y] == 0):
					# overwrite the position, so we won't visit that cell again.
					# Note: We're assuming we CAN modify the input. If we don't want to modify the grid, then we can use a set.
					grid[new_x][new_y] = 1
					queue.append((new_x, new_y, path_len + 1))

		return -1