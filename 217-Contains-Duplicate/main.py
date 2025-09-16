from typing import List


# T: O(n)
# M: O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True

            hashset.add(n)

        return False


# T: O(n)
# M: O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            hashset.add(n)

        return True if len(nums) > len(hashset) else False
