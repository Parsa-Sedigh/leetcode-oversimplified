import random
from collections import defaultdict
from typing import List


# 1. Brute force

# Go through the arr and for each el, count it's num of appearances. The el with the count strictly larger than half of the size of arr,
# is definitely the majority el(according to the problem).

# T: O(n^2)
# M: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for num in nums:
            count = 0

            for i in range(len(nums)):
                if nums[i] == num:
                    count += 1

            if count > len(nums) // 2:
                return num


# 2. Hash Map
# T: O(n)
# M: O(n)
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)

        # we need to store both the number that is the majority element(in `res`) and the actual number of occurrences of that number, which is
        # stored in `max_count`.
        res = max_count = 0

        for n in nums:
            count[n] += 1
            if count[n] > max_count:
                max_count = count[n]
                res = n

        return res


# 3. Sorting
# T: O(n*log(n))
# M: O(1) or O(n) depending on the sorting algorithm.
class Solution3:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        return nums[len(nums) // 2]


# 4. Bit Manipulation
# T: O(n * 32)
# M: O(32)
# NOTE: 32 represents the number of bits as the given numbers are integers.
class Solution4:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        bit = [0] * 32

        for num in nums:
            for i in range(32):
                bit[i] += ((num >> i) & 1)

        res = 0
        
        for i in range(32):
            if bit[i] > (n // 2):
                if i == 31:
                    res -= (1 << i)
                else:
                    res |= (1 << i)

        return res


# 5. Boyer-Moore Voting Algorithm
# T: O(n)
# M: O(1)
class Solution5:
    def majorityElement(self, nums: List[int]) -> int:
        # we don't call it max_count, because it's gonna go up and down.
        res = count = 0

        for num in nums:
            if count == 0:
                res = num

            # inc count if cur el is the same as `res`, otherwise, dec it
            count += (1 if num == res else -1)

        return res


# 6. Randomization
# The probability of randomly choosing the majority element is greater than 50% so the expected number of iterations in the
# outer while loop is constant.

# T: O(n)
# M: O(1)
class Solution6:
    def majorityElement(self, nums: List[int]) -> int:
        # O(x) where x is constant
        while True:
            candidate = random.choice(nums)

            # nums.count() is T: O(n)
            if nums.count(candidate) > len(nums) // 2:
                return candidate
