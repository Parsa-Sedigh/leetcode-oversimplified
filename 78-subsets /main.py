from typing import List

class Solution:
	def subsets(self, nums: List[int]) -> List[List[int]]:
		res = []

		subset = []

		# we wrote this function inside of the outer function so that we don't have to pass in res or nums into it.
		# `i` is the index of the value that we're making a decision on. For example the input is [1, 2, 3], i is the index of
		# the value that we're gonna decide whether add that value to the decision tree or not.
		def dfs(i):
			# the base case is when `i` is out of bounds
			if i >= len(nums):
				# we only add the leaf nodes to the result. So when we passed the leaf node, we can add the current `subset` to the `res`.
				res.append(subset.copy())

				return

			# we have 2 decisions:
			# - decision to include nums[i](the left position at each node that we have based on our decision tree)
			############# Left branch at each step(node) of the decision tree #############
			# We have to append() before calling the dfs() recursively. Because at each node, the elements are added according to the
			# decision tree. So call append() before calling dfs(i + 1) in preorder manner.
			subset.append(nums[i])
			dfs(i + 1)

			# - decision NOT to include nums[i](skipping nums[i]). How do we skip? By popping the last element of the current subset
			############# Right branch #############
			# When we arrive here, it means we've gone through current path completely. Now we wanna try other paths. For this,
			# we need to backtrack. So remove the last element from subset and instead try the next element in nums arr by using `i + 1`.

			## Backtracking phase
			subset.pop()
			dfs(i + 1)

		dfs(0)

		return res