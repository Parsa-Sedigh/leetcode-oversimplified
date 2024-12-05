from typing import List


# Brute force
# T: O(n ^ 2)
# M: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        # we shouldn't hit this lint, but we've put it anyway
        return []


# Sorting
# T: O(n * log(n))
# M: O(1)
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []

        for i, num in enumerate(nums):
            # Why we append both [num, i] instead of just num?
            # Because in the result we wanna return, we have to return the original index of num in nums. So we have to keep that
            # original index somewhere, both for having the correct answer and being faster.
            # About 1: Because let's say we find a num. We might not be able to
            # find that number in nums because we could have multiple values of that num, we don't know which index is correct.

            # About 2: Another reason for storing original index is: we don't have to go through the nums arr to find the index which
            # is slow and also again(which also cloud yield the wrong result).
            A.append([num, i])

        A.sort()

        print(A)

        # binary search - since we have a sorted arr
        i, j = 0, len(nums) - 1

        # we can't have <=. Since we can't use the same el twice.
        while i < j:
            cur_sum = A[i][0] + A[j][0]

            if cur_sum == target:
                # we could return the indexes in any order, so both are ok:
                # return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
                return [A[i][1], A[j][1]]
            elif cur_sum < target:
                i += 1
            else:
                j -= 1

            return []


# 3. Hash Map (Two Pass)
# T: O(n)
# M: O(n)
class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}  # val -> index

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n

            # Since we've already constructed the hashmap, because currently, we've encountered an el and that el is also present in
            # the hashmap, we shouldn't consider the same element twice. So check for it's indexes in both places to NOT be equal.
            if diff in indices and i != indices[diff]:
                return [i, indices[diff]]


# 4. Hash Map (One Pass)
# T: O(n)
# M: O(n)
class Solution4:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We call this prevMap because it has every element that comes before the current element(every previous element is gonna be stored
        # in this map)
        prevMap = {}  # val: index

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
