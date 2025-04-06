from typing import List

# T: O(2^n)
# M: O(n)
# This gets: Time Limit Exceeded
class Solution:
	def rob(self, nums: List[int]) -> int:
		max_money = 0

		def dfs(i, res):
			nonlocal max_money

			if i == len(nums) - 1 or i == len(nums) - 2:
				max_money = max(max_money, res + nums[i])

				return

			if i > len(nums) - 2:
				return

			res += nums[i]

			# We need to choose the next houses that we can rob from. Since we can't rob the adjacent houses, we can either
			# rob the i + 2 or i + 3.
			dfs(i + 2, res)
			dfs(i + 3, res)

		dfs(0, 0)
		dfs(1, 0)

		return max_money

# Neetcode
# T: O(n)
# M: O(1)
class Solution2:
	def rob(self, nums: List[int]) -> int:
		# We only need to maintain the last two maxes that we can rob from. Initialize them to 0, because if we get an empty
		# subarr, we wanna return 0
		# pattern is: [rob1, rob2, m, n, o, ...] : If we wanna rob m, we have to rob rob1 as well, we can't use rob2.
		# But if we don't wanna rob m, we have to include rob2.
		rob1, rob2 = 0, 0

		for n in nums:
			# compute the maximum that we can rob up until this value `n`
			# Note: n + rob1 means we decide to rob the current house. So we can't rob include the prev house, so we use rob1
			# Note: using rob2 means we include the prev house, so we can't include the current house, hence don't add it to `n`
			temp = max(n + rob1, rob2)

			# As we move forward, we update rob1 and rob2(move them forward as well)
			rob1 = rob2
			rob2 = temp

		# rob2 because by the time we get to the end, rob2 will be the max we can rob from the entire houses. Note that rob2 is always
		# greater than or equal to rob1.
		return rob2