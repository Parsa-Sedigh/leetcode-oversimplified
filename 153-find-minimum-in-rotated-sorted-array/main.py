from typing import List


class Solution:
	def findMin(self, nums: List[int]) -> int:
		res = nums[0]  # You can pick any value in the input array
		l, r = 0, len(nums) - 1

		while l <= r:
			# If we get into a subarray that's already sorted, we can just compare left most element with current minimum
			if nums[l] < nums[r]:
				res = min(res, nums[l])
				break

			m = (l + r) // 2
			res = min(res, nums[m])

			# if this is true, m is part of the left sorted portion and therefore we wanna search the right sorted portion
			if nums[m] >= nums[l]:
				l = m + 1
			else:
				r = m - 1

		return res
