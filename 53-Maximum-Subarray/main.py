from typing import List

# cubic solution. Gets time limit exceeded.
# T: O(n^3)
# M: O(1)
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]

        # i represents the starting point and j represents the ending point
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                curr_sum = 0

                for k in range(i, j + 1):
                    curr_sum += nums[k]
                    max_sum = max(max_sum, curr_sum)

        return max_sum

# Quadratic solution
# T: O(n^2)
# M: O(1)
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]

        for i in range(len(nums)):
            curr_sum = 0

            for j in range(i, len(nums)):
                curr_sum += nums[j]
                max_sum = max(max_sum, curr_sum)

        return max_sum

# Linear solution
# T: O(n)
# M: O(1)
class Solution3:
    def maxSubArray(self, nums: List[int]) -> int:
        # Note: We have to initialize max_sum to sth and we can't assign 0 to it, because the nums can be all negative.
        # Note: As stated in the description, the arr is non-empty so the zeroth element always exists.
        max_sum = nums[0]
        curr_sum = 0

        for n in nums:
            # If we have a negative prefix, we're gonna not consider that portion from the curr_sum.
            if curr_sum < 0:
                curr_sum = 0

            curr_sum += n
            max_sum = max(max_sum, curr_sum)

        return max_sum

# Linear solution
# T: O(n)
# M: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0

        for n in nums:
            # Instead of these two lines, we could say: curr_max = max(curr_max + n, n)
            curr_sum = max(curr_sum, 0)
            curr_sum += n

            max_sum = max(max_sum, curr_sum)

        return max_sum
