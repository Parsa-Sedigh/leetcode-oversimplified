from typing import List


# T: O(n^2).
# Outer loop runs n times (i goes from 0 to n-1).
# Inner loop runs (n - i - 1) times for each i.
# The total number of iterations across all loops is:
# (n-1)+(n-2)+(n-3)+...(1)+(0) = ((n-1)*n)/2 = O(n^2)
# For example: n-1 means second loop gotta go through n - 1 elements, since it has to start from index = 1 and go through the end.

# M: O(1)

# This gets time limit exceeded err
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            largest = arr[i]

            if i + 1 < len(arr):
                largest = arr[i + 1]

            for j in range(i + 1, len(arr)):
                largest = max(largest, arr[j])

            arr[i] = largest

        arr[-1] = -1

        return arr


# T: O(n^2)
# Note:

# M: O(1) - we don't consider the result arr as extra memory
class Solution2:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) < 2:
            return [-1]

        cur_max = arr[-1]
        max_arr = []

        for i in range(len(arr) - 2, -1, -1):
            cur_max = max(cur_max, arr[i + 1])  # T: O(n)
            max_arr.insert(0, cur_max)

        max_arr.append(-1)

        return max_arr


class Solution3:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Note: We wouldn't have negative values in `arr`. So initial_max being -1 is correct.
        right_max = -1

        # start at the last el of the arr: (len(arr) - 1)
        # go backwards: -1
        # stop once we get to the beginning of the arr(exclusive): -1
        for i in range(len(arr) - 1, -1, -1):
            new_max = max(right_max, arr[i])
            arr[i] = right_max
            right_max = new_max

        return arr
