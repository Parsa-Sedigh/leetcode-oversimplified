from typing import List


class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		result = []

		# base case
		# if there's only one value, then obviously it has only one permutation. Remember that the returned value should be a
		# list of lists.
		if len(nums) == 1:
			return [nums.copy()] # or: return nums[nums[:]]

		for i in range(len(nums)):
			n = nums.pop(0)
			print("hello 1: ", nums)

			perms = self.permute(nums)

			for perm in perms:
				perm.append(n)
			print("hello 2: ", result, perms)
			result.extend(perms)

			# undo the popped element back, but this time to the end of the list.
			nums.append(n)

		return result

	# Approach 2
	def permute2(self, nums: List[int]) -> List[List[int]]:
		res = []

		def backtrack(currI):
			if currI == len(nums):
				res.append(nums[:])

				return

			for i in range(currI, len(nums)):
				nums[i], nums[currI] = nums[currI], nums[i]
				backtrack(currI + 1)
				nums[currI], nums[i] = nums[i], nums[currI]

		backtrack(0)

		return res
