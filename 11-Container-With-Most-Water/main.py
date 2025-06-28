from typing import List


# 1. Brute Force
# T: O(n^2)
# M: O(1)
class Solution:
    # this will get "time limit exceeded"
    def maxAreaBruteForce(self, height: List[int]) -> int:
        # initialize it to 0, because we can't have a negative area(in this context)
        res = 0

        for l in range(len(height)):
            # the `r` pointer always needs to be at least one position a head if `l`
            for r in range(l + 1, len(height)):
                # width * height
                # Note: We don't want the water to spill out of the container, so for height, we need to find the smaller height
                area = (r - l) * min(height[l], height[r])
                res = max(res, area)

        return res


# 2. Two Pointers
# T: O(n)
# M: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1

        # if l and r are equal or pass together, that's not good
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1

            # The next two blocks can do the same:
            # elif height[l] >= height[r]:
            # 	r -= 1
            else:
                r -= 1

        return res
