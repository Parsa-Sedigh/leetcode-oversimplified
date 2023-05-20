from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # This array is gonna be the same size as input array. The index is gonna be the frequency(count) of the element and the value
        # is gonna be the list of values that occur that particular many number of times.
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        res = []

        # We iterate the frequency array(freq) in descending order, because we wanna start with the numbers that occur
        # most frequently. So we use `-1` as decrementer.
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)

                # This if block guaranteed to execute at some point, so we don't need to put a return statement outside
                # of the loop(in top-level of function), because the question told us
                if len(res) == k:
                    return res