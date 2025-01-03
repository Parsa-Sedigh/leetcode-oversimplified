from typing import List


# 1. Brute Force
# T: O(n)
# M: O(n)
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        tmp = []

        for num in nums:
            if num != val:
                tmp.append(num)

        for i in range(len(tmp)):
            nums[i] = tmp[i]

        return len(tmp)


# two pointers I
# T: O(n)
# M: O(1)
class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            # if el is not eq to val, put it at where k stands and move k forward. So if we encounter a val, we just ignore it.
            # NOTE: Here, an el could be replaced with itself. Because it's not eq to val and k points to this el index. It's ok!
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


# Two pointer II
# T: O(n)
# M: O(1)
class Solution3:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]

                r -= 1
            else:
                l += 1

        return l
