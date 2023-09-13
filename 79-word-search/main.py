from typing import List


class Solution:
	def exist(self, board: List[List[str]], word: str) -> bool:
		ROWS, COLS = len(board), len(board[0])
		path = set()

		def dfs(r, c, i):
			# Did we find the word?
			# We reached the word(i == len(word)) and we've found all the letters.
			if i == len(word):
				return True

			if (r < 0 or c < 0 or
				r >= ROWS or c >= COLS or
				word[i] != board[r][c] or
				(r, c) in path):
				return False

			# at this point, we found the character that we're looking for, so we can add the current position to the `path`
			path.add((r, c))

			# run dfs for all 4 adjacent positions.
			# Note: We're adding one to i because we found the character, now we wanna look for the next character
			# Note: If any of these recursive calls return True, then the res is gonna be true. Because we only need to find our
			# target word one single time.
			res = (dfs(r + 1, c, i + 1) or
				   dfs(r - 1, c, i + 1) or
				   dfs(r, c + 1, i + 1) or
				   dfs(r, c - 1, i + 1))

			# clean up - remove the position we just added to the `path`
			# Note: This is because we no longer visiting that position
			path.remove((r, c))

			return res

		# brute-force go through every single position in our grid and run the dfs function on it
		for r in range(ROWS):
			for c in range(COLS):
				print("loop", r, c)
				# if ever the dfs function returns True, we can immediately return True from this loop and exit the function
				if dfs(r, c, 0): return True

		return False
