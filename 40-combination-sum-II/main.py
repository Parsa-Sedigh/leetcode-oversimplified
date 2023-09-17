from typing import List


class Solution:
	def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
		# by sorting the input array, it's gonna make it easy for us to eliminate the duplicates
		candidates.sort()

		res = []

		# cur: is current combination
		# target: is the current target that we're trying to sum up to. Because every time we add a candidate, we're basically decreasing
		# the target that we're trying to sum up to
		def backtrack(cur, pos, target):
			if target == 0:
				# we we need to pass a copy of cur because after appending it to res, in future recursions, we're still gonna be
				# updating the cur variable and therefore when we append it to `res`, we want to append a copy of it. We don't want to
				# append the original cur itself because that's a reference.
				res.append(cur.copy())

			if target <= 0:
				return

			# none of the candidates are gonna be -1 so the if statement in the for loop that we have for checking if the prev candidate is
			# the same as current one, will never get exected in the first iteration(because in first iteration we haven't seen anything yet,
			# right?!)
			# Note: Using this prev, we can eliminate the duplicates
			prev = -1

			for i in range(pos, len(candidates)):
				if candidates[i] == prev:
					continue

				cur.append(candidates[i])

				# with i + 1, we're saying in the next call of backtrack, we can choose any of the next candidates
				backtrack(cur, i + 1, target - candidates[i])

				# cleanup
				cur.pop()

				# prev is the prev candidate that we chose
				prev = candidates[i]

		backtrack([], 0, target)

		return res
