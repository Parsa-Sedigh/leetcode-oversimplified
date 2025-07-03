from typing import List


# 1. Two pointer
# T: O(n^2)
# M: O(1)
class Solution:
    def triangleNumber(self, heights: List[int]):
        # Python's sort() method uses Timsort, which has a time complexity of O(n * log(n))
        count = 0

        heights.sort()

        # second arg of range is exclusive, so here 1 means until third element of the list(index 2)
        # NOTE: 'i' represents the largest side of the triangle
        for i in range(len(heights) - 1, 1, -1):
            l, r = 0, i - 1
            while l < r:
                if heights[l] + heights[r] > heights[i]:
                    # Since the list is sorted, all elements from l to r-1 can pair with r to form a triangle with i.

                    # NOTE: Hey, cur l can satisfy the triangle. Sine the arr is sorted, larger `l`s would satisfy it as well.
                    # There's no need to test them all. So add all these els and try a smaller `r`.

                    # NOTE: We shouldn't increase l here, because that would make the sum bigger which is already big enough.
                    # Instead, make `r` smaller(we can't make l smaller! It's already the lowest idx!).
                    count += r - l
                    r -= 1
                else:
                    # Sum was too small, we need to increase it. So move the left pointer right to increase the sum
                    l += 1

        return count
