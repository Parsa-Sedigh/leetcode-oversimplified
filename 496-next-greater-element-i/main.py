from typing import List


# 1. Brute Force
# T: O(n * m)
# M: O(1) if we don't count the output as extra memory, otherwise, O(n)
# n: number of els in nums1, m: number of els in nums2
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for num in nums1:
            next_greater = -1

            for i in range(len(nums2) - 1, -1, -1):
                if nums2[i] > num:
                    next_greater = nums2[i]
                elif nums2[i] == num:
                    break

            res.append(next_greater)

        return res


# 2. Hash Map
# T: O(n * m)
# M: O(n) - because of nums1ToIdx which is the size of nums1
class Solution2:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1ToIdx = {n: i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            # curr value is not in nums1(not in nums1ToIdx, meaning not in nums1). So we skip it
            if nums2[i] not in nums1ToIdx:
                continue

            # we only wanna look at vals that come after curr el, so start from `i+1`
            for j in range(i + 1, len(nums2)):
                # if there is a greater el than curr val(nums2[i]), look at the index of curr val in nums1 which we
                # can get by saying: nums1ToIdx[nums2[i]] and then we put this larger el(nums2[j]) in the idx position of res
                # Then break out of inner loop, because we found the next greater el of curr el.
                # NOTE: If we never find the next greater el, the default is -1 which is what we set in res initially.
                if nums2[j] > nums2[i]:
                    idx = nums1ToIdx[nums2[i]]
                    res[idx] = nums2[j]

                    break

        return res


# 3. Stack - uses monotonic stack technique
# T: O(n + m)
# M: O(m) - because of the hashmap which is the size of nums1 and also the stack that is the size of nums1 because we're only adding
# els that are in nums1, to stack
class Solution3:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1ToIdx = {n: i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)

        # This stack holds the next greater val of els in nums1 which are also in nums1ToIdx
        stack = []

        for i in range(len(nums2)):
            cur = nums2[i]

            # is `cur` the next greater el for any prev values that could be on stack?
            while stack and cur > stack[-1]:
                # cur is next greater el of stack[-1]. So we can pop the val from stack(because we've found it's next greater el)
                # and then we need to find it's index in nums1 which is: nums1ToIdx[stack[-1]] and put this next greater el at res.
                val = stack.pop()
                idx = nums1ToIdx[val]
                res[idx] = cur

            if cur in nums1ToIdx:
                stack.append(cur)

        return res
