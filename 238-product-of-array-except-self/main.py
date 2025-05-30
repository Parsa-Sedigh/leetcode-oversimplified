from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))  # this does not count as extra memory in the context of this problem

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix # res[i] = res[i] * postfix
            postfix *= nums[i] # postfix = postfix * nums[i]

        return res
