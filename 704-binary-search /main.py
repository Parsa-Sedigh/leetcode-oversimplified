import bisect
from typing import List


# 1. Recursive Binary Search
# T: O(log(n))
# Why not O(n)?
# Well, the total number of nodes in the decision tree is n, but the time is not O(n) because the algo doesn't traverse both
# branches in each node of the decision tree, it only picks one branch at a time, meaning eliminating half of the nodes at each branch.
# Therefore, the time is O(log(n)). Also note that the time for visiting each node is O(1).

# M: O(log(n))
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recursive(l, r):
            if l > r:
                return -1

            m = (l + r) // 2

            if nums[m] < target:
                return recursive(m + 1, r)
            elif nums[m] > target:
                return recursive(l, m - 1)
            else:
                return m

        return recursive(0, len(nums) - 1)


# 2. Iterative Binary Search
# T: O(log(n))
# M: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # Why we used <= instead of <?
        # Because using <=, it ensures we check the case where there's only ONE SINGLE element is remaining.
        # For example, if we had [3], we have to use <= to check the 3. But if we used <, l and r would both be 0 and the
        # algo wouldn't run at all.
        while l <= r:
            m = l + ((r - l) // 2)

            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m

        return -1


# 5. Built-In Function
# T: O(log(n))
# M: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)

        return index if index < len(nums) and nums[index] == target else -1
