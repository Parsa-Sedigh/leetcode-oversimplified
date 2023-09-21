from typing import List


class Solution:
	def trap(self, height: List[int]) -> int:
		# edge case - if the input array is empty. This if block is needed for this problem
		if not height: return 0

		l, r = 0, len(height) - 1
		leftMax, rightMax = height[l], height[r]
		res = 0

		while l < r:
			if leftMax < rightMax:
				l += 1
				leftMax = max(leftMax, height[l])

				# Notice we're not checking if the leftMax - height[l] is negative. Because technically this is never going to be negative.
				# Because we're updating the leftMax in the line before by getting the max of leftMax and height[l].
				# Note: If you were swapped the order of previous and next line, you had to check if the result of leftMax - height[l] is negative
				# and if it was, don't add it to res.
				res += leftMax - height[l]
			else:
				r -= 1
				rightMax = max(rightMax, height[r])
				res += rightMax - height[r]

		return res