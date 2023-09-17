from typing import List


class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		res = []

		nums.sort()

		# We want to use each number in the input array as a possible first value, so we iterate through every element in the input array:
		for i, a in enumerate(nums):
			# i > 0 means this isn't the first value in the input array.
			# Note: We don't want the same value as before as our possible first element of the result(a), so continue
			# Note: If we don't put i > 0, we would get an out of range error
			# Note: We shouldn't put this if block inside the while loop. Because in that case we could end up in an infinite loop inside
			# the while loop, because by executing the `continue` statement, the `index` won't change and we will end up going into that
			# if statement infinitely. Why index won't change? Because we're inside the while loop and we're doing the continue which won't
			# affect index at all so the index won't change and we end up going into if statement infinitely!
			if i > 0 and a == nums[i - 1]: continue

			l, r = i + 1, len(nums) - 1

			# l and r can't be equal(to avoid duplicates in res), so `l < r`
			while l < r:
				threeSum = a + nums[l] + nums[r]

				if threeSum > 0:
					r -= 1
				elif threeSum < 0:
					l += 1
				else:
					res.append([a, nums[l], nums[r]])
					l += 1

					# Let's say the nums is: [-2, -2, 0, 2, 2]. Let's say l is at 0 and r is at the end(let's imagine we're solving
					# two sum without having duplicates)After adding the first combination to res, our l gets to index 1.
					# But our l gets to -2 again. So we want to shift l again. Now our sum is gonna be too big, because we're gonna
					# be at 0 + 2. So then our while loop is gonna execute going into threeSum > 0: block and we're gonna shift
					# r pointer to left. Notice how that r pointer is at 2 again as previously was, but we don't need to write
					# a for loop for r pointer to make it non duplicate again! Notice how each value is only gonna have corresponding
					# value that it can sum equal to target which is 0. So we ONLY have to update one pointer(for example l) and then
					# our first two conditions that check threeSum value will update the other pointer if necessary, by itself. We don't even
					# have to worry about it.
					# So in this case, we only gonna shift the l pointer if necessary:
					# Note: We don't want the l pointer to ever pass the r pointer, so we need l < r condition as well
					while nums[l] == nums[l - 1] and l < r:
						l += 1

		return res