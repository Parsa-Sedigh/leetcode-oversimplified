from typing import List


# Brute force
# Gets time limit exceeded

# T: O(n^2)
# M: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices)):
            buy = prices[i]

            for j in range(i + 1, len(prices)):
                sell = prices[j]
                max_profit = max(max_profit, sell - buy)

        return max_profit


# Two pointer
# T: O(n)
# M: O(1)
class Solution2:
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
                # NOTE: We know all vals between l and r are greater than l. But curr r is even less than l. So it's
                # definitely less than those vals between as well. So move l to r.
                l = r

            r += 1

        return maxP


# Dynamic Programming
# T: O(n)
# M: O(1)
class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = 0

        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)

        return max_profit
