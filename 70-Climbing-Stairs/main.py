# T: O(n)
# M: O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        # This is bottom-up DP. We're starting at step = n. Now how many ways we can reach the last step from current
        # step? One. So we initialize two as 1. Also from the previous step(n - 1), we can reach the last step in one
        # way. So one is also initialized as 1. At the end, we return one, because that's the previous step and as we
        # move backwards form the bottom to top, we wanna return this one.
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one