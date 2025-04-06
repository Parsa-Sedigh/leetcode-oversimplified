from typing import List

# T: O(n)
# M: O(1)
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        global_max, global_min = nums[0], nums[0]
        curr_max, curr_min = 0, 0
        total = 0

        for n in nums:
            # Instead of these two lines, we could say: curr_max = max(curr_max + n, n)
            curr_max = max(curr_max, 0)
            curr_max += n

            curr_min = min(curr_min, 0)
            curr_min += n

            total += n

            global_max = max(global_max, curr_max)
            global_min = min(global_min, curr_min)

        return max(global_max, total - global_min) if global_max > 0 else global_max