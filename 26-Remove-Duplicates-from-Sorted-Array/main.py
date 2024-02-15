from collections import defaultdict
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        els = defaultdict(int)
        counter = 0

        for num in nums:
            els[num] += 1

            if els[num] == 1:
                nums[counter] = num
                counter += 1

        return len(els)

    # neetcode
    # T: O(n), M: (1)
    def removeDuplicates2(self, nums: List[int]) -> int:
        # What if the nums is an empty arr? Shouldn't we return 0? Well you're right but for some reason, leetcode accepts this code as it is!
        l = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1

        return l