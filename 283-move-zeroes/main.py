from typing import List


# 1. Extra Space
# T: O(n)
# M: O(n)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zeroes = []

        # First loop: Collect all non-zero elements in their original order
        # This helps us grab only the numbers we want to keep at the front
        for num in nums:
            if num != 0:
                non_zeroes.append(num)

        # Second loop rebuilds nums: non-zeros first, then zeros
        for i in range(len(nums)):
            if i < len(nums):
                nums[i] = non_zeroes[i]
            else:
                nums[i] = 0


# 2. Two Pointers (Two Pass)
# T: O(n)
# M: O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l] = nums[r]
                l += 1

        while l < len(nums):
            nums[l] = 0
            l += 1


# 3. Two Pointers (One Pass)
# NOTE: This problem is hard to solve using swaps. Just use index assignments.
# T: O(n)
# M: O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # points to the position where the next non-zero element should be placed
        l = 0

        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
