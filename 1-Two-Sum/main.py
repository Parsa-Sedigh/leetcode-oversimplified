from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We call this prevMap because it has every element that comes before the current element(every previous element is gonna be stored
        # in this map)
        prevMap = {} # val: index

        for i, n in enumerate(nums):
            diff = target - n

            # we have put this check BEFORE inserting n into the hashmap. Because otherwise, if we insert into hashmap and THEN check,
            # we can get wrong answer. Why? Because we could potentially consider the current element twice! For example:
            # [3, 3] target = 6. At the first el, first we put into the hashmap and then see if current element and an element in the
            # hashmap can sum up to the target? Yes in this case we can. We are at 3 and we have a 3. But both are the same index!
            # So we HAVE to first check and THEN insert into the hashmap.
            if diff in prevMap:
                return [prevMap[diff], i]

            prevMap[n] = i

        # since we're guaranteed that a solution exists, we don't have to return anything out here