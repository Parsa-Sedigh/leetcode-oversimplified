from typing import List

from cassandra.cluster import defaultdict


# 1. Brute Force
# T: O(n^2)
# M: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        # T: O(n)
        # In Python, the set() constructor iterates through each element in the input iterable (e.g., nums) and inserts it into the set.
        els = set(nums)

        # T: O(n)
        for n in nums:
            streak, cur = 0, n

            # T: O(n)
            while cur in els:
                streak += 1
                cur += 1

                res = max(res, streak)

        return res


# 2. Sorting
# T: O(n * log(n))
# M: O(1) or O(n) depending on the sorting algo impl
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        res = 1
        streak = 1  # Current streak length

        for i in range(len(nums)):
            if nums[i] == nums[i - 1]:  # Skip duplicates
                continue
            elif nums[i] == nums[i - 1] + 1:  # Consecutive number
                streak += 1
                res = max(res, streak)
            else:  # Sequence breaks
                streak = 1

        return res


# 3-a. Hash Set
# T: O(n)
# M: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set from the initial array nums
        # T: O(n)
        num_set = set(nums)

        # keep track of what the longest consecutive sequence is
        longest = 0

        # Q: Why we should iterate over the set instead of the input array?
        # A: Otherwise, we would get time limit exceeded. That's because nums arr may contain duplicates. So you're checking
        # a number multiple times to see if it's a start of a sequence or not, which is redundant work.
        # For example: If a sequence like [1, 2, 3, 4] appears multiple times in nums (e.g., nums = [1, 1, 1, 2, 2, 3, 4]),
        # you'll traverse the sequence [1, 2, 3, 4] three times (once for each 1).
        for n in num_set:
            # check if it's the start of a sequence.
            # If current number doesn't have a left neighbour, that means it's start of a sequence
            # Only start the inner loop IF `n` is start of a sequence. Otherwise, we would skip n.
            if (n - 1) not in num_set:
                length = 0

                # keep getting next consecutive number and check if it exists in our num_set, if it does, keep adding to `length`.
                # Note: Initially length is 0, so we're checking if the current number exist in the num_set. As length grows, we'll check
                # next consecutive numbers that if they exist in the num_set
                while (n + length) in num_set:
                    length += 1

                # at this point, we could've potentially found the longest sequence, so we wanna potentially update our `longest`
                longest = max(length, longest)

        return longest


# 3-b. Hash Map
# T: O(n)
# M: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        longest = 0

        for n in nums:
            mp[n] = True

        for n in mp:
            if n - 1 not in mp:
                cur_longest = 1
                
                while n + 1 in mp:
                    n += 1
                    cur_longest += 1

                longest = max(longest, cur_longest)

        return longest
