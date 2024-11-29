from typing import List


# T: O(n)
# M: O(1)
# if you count the result as needing additional memory, memory would be O(n), but if you don't consider it, it's O(1)
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)

        for i in range(length):
            nums.append(nums[i])  # O(1)

        return nums


class Solution2:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        # do it 2 times
        for i in range(2):
            for n in nums:
                ans.append(n)  # O(1)

        return ans
