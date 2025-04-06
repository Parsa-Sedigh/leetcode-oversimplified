from typing import List


class Solution:
    # if we can allocate extra memory
    # neetcode
    # T: O(n), S: O(n)
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []

        for i in range(n):
            res.append(nums[i])
            res.append([nums[i+n]])

        return res

    # neetcode
    # T: O(n), S: O(1)
    def shuffle2(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
            # shift the x value stored in nums[i] to the left by 10 bits and store that in it's original spot in the arr. Because
            # we're just making space for the y value.
            nums[i] = nums[i] << 10

            # take the y value which initially is at nums[i + n] and logic OR it with(bit-wise OR it with) nums[i] and store y in nums[i]
            # So this line will store x and y values together in a single spot(nums[i]) in binary(make a pair of x and y in each spot in the
            # first half of the arr)
            nums[i] = nums[i] | nums[i + n]

        # j is the last index in the arr
        j = 2 * n - 1

        # iterate through the first half of the arr in reverse order.
        # We wanna iterate through the pairs that we just stored, but we wanna do it in reverse order because we don't want to
        # override values that we're gonna end up to use later on.
        # Note: Start at the middle point of the arr, keep going backwards until the zeroth index(-1 index exclusive)
        for i in range(n - 1, -1, -1):
            y = nums[i] & (2**10 - 1)

            # shift x to the right by 10 bits
            x = nums[i] >> 10

            nums[j] = y
            nums[j - 1] = x

            # we just stored 2 values, so shift j backwards by 2 spots
            j -= 2

        return nums