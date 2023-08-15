from typing import List


class Solution:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		res = []

		# i: we want to maintain which of the candidates we're still to choose. For this we use the `i` arg.
		# total: current total of cur
		def dfs(i, cur, total):
			# first base case
			if total == target:
				res.append(cur.copy())

				return

			# second base case -> if we end up being impossible to find a valid combination
			if i>= len(candidates) or total > target:
				return

			# we have two decisions to make. We can decide whether or not add candidates[i] to the cur.

			# first decision: include it:
			cur.append(candidates[i])

			# Note: why we still pass i? We included candidates[i] to cur, but we can continue to include candidates[i] again. By doing this,
			# it means we're not restricting which candidates we're allowed to choose from just yet.
			# Note: total should change because cur changed, so pass the updated value of it
			dfs(i, cur, total + candidates[i])

			# second decision:
			cur.pop()

			# by passing i + 1, we're indicating that we can't include any occurrences of candidates[i] which is what we want
			# Note: we didn't add any candidates to cur, so total is gonna stay the same(look at each right subtree, nothing is being added)
			dfs(i + 1, cur, total)

		dfs(0, [], res)

		return res




