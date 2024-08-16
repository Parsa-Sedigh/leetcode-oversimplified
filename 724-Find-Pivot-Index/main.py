# T: O(n)
# M: O(1)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums) # T: O(n)
        leftSum = 0

        # T: O(n)
        for i in range(len(nums)):
            rightSum = total - leftSum - nums[i]

            if leftSum == rightSum:
                return i

            # in the next iteration, curr el is added to the leftSum:
            leftSum += nums[i]

        return -1