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