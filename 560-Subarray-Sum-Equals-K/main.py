# T: O(n)
# M: O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0

        # The empty subarr is one subarr that has the sum of 0
        prefixSums = {0: 1}

        for n in nums:
            curSum += n

            # if we can remove a prefix sum with the sum `diff`, then we can find a result. And we can have multiple prefix sums
            # that sum up to `diff`
            diff = curSum - k
            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

        return res
