from typing import List


class Solution:
	def partition(self, s: str) -> List[List[str]]:
		res = []

		# current partition
		part = []

		def dfs(i):
			# Since this is a recursive function, first thing we do is to check the base case
			if i >= len(s):
				# When we get to here, we know that we have a valid partition and we have no more characters to add, so let's add
				# it to the res
				res.append(part.copy())
				print("hello: ", part)

				return

			# with this loop, we're generating every single possible substring from i to j and if it's a palindrome, we add it to `part`.
			# If it's not a palindrome, we skip it using the if block
			for j in range(i, len(s)):
				# is `s` starting from i and ending in j, a palindrome?
				if self.isPali(s, i, j):
					# Note: We wanna include j as well, because sub-listing in python is exclusive, we need to add 1 to j
					part.append(s[i:j+1])
					print("ok: ", i, j , s[i:j+1])

					dfs(j + 1)

					# after doing the recursive calls, we have to clean up:
					part.pop()

		dfs(0)

		return res

	def isPali(self, s, l, r):
		while l < r:
			if s[l] != s[r]:
				return False

			l, r = l + 1, r - 1

		return True
