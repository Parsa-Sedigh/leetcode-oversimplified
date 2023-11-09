from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We call this prevMap because it has every element that comes before the current element(every previous element is gonna be stored
        # in this map)
        prevMap = {} # val: index

        for i, n in enumerate(nums):
            diff = target - n

            if diff in prevMap:
                return [prevMap[diff], i]

            prevMap[n] = i

        # since we're guaranteed that a solution exists, we don't have to return anything out here