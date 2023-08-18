from typing import List


class Solution:
	def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
		res = []

		nums.sort()

		def backtrack(i, subset):
			if i == len(nums):
				# we use copy() because when we do a future backtrack call(), we won't mutate the subset that we have added to `res`. Because
				# we're appending a reference to subset to res. We want to create a copy of that subset.
				res.append(subset[::])

				return

			# we have two decisions to make:
			# 1. all subsets that include nums[i]
			subset.append(nums[i]) # include nums[i] to the current subset
			backtrack(i + 1, subset) # this is gonna take care of all subsets that include nums[i]

			# remove from subset the value that we just added
			subset.pop()


			# 2. all subsets that do not include nums[i]
			# since we sorted the input array(nums), the duplicates are gonna be next to each other
			# Why we're doing this? Let's say nums is [1, 2, 2, 3] and we're at index = 1 and we're choosing to skip this index, then
			# we should skip the second 2 as well. Because we don't want duplicates.
			while i + 1 < len(nums) and nums[i] == nums[i + 1]:
				i += 1

			# after the while loop does terminate, we still want to run our backtrack. Because even if skipped the entire array by incrementing `i`
			# in the while loop, the current case is gonna be the case that ends up adding the empty array to the `res`. So we don't want
			# to skip calling `backtrack` regardless what the while loop ends up doing.
			backtrack(i + 1, subset)

		backtrack(0, [])

		return res