from typing import List


class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		l, r = 0, 1  # left is the day we buy and right is the day we sell
		maxP = 0

		while r < len(prices):
			# is it profitable?
			if prices[l] < prices[r]:
				profit = prices[r] - prices[l]
				maxP = max(maxP, profit)
			else:
				# we don't just want to shift the l pointer by 1, we want to shift it all the way to the r, because we found
				# a really low price, we found the lowest price until now. We want our `l` to be at the minimum. So put it where `r` is at the moment.
				# Note: When we encounter this block, it means all the values after `l` and before `r`, are less than value of `l`, because we crossed
				# them and moved to the next price(if it wasn't the case, we already have encountered this block at that moment!). Thefore,
				# instead of just moving `l` by one price, put it where `r` is.
				l = r

			r += 1

		return maxP
