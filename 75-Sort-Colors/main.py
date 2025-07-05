from typing import List


# 1. Counting Sort
# Time: O(n)
# Space: O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # The idx represents the actual color(val)
        # The val represents the frequency of that color
        # For example [2, 3, 2] means:
        # - there are 2 instances of of color 0
        # - 3 instances of color 1
        # - 2 instances of color 2
        counts = [0] * 3

        for num in nums:
            counts[num] += 1

        # Initialize position where the next color will be written
        write_pos = 0

        # since we're getting indexes, it means we're getting the color values
        for color_val in range(len(counts)):
            while counts[color_val]:
                nums[write_pos] = color_val

                counts[color_val] -= 1
                write_pos += 1


# 2. Three Pointers - I
# Time: O(n)
# Space: O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # l: where next 0 goes, r: where next 2 goes
        l, r = 0, len(nums) - 1

        # i: current element being checked
        i = 0

        def swap(i: int, j: int):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        # Continue until i PASSES r (all elements processed)
        while i <= r:
            if nums[i] == 0:
                swap(l, i)

                # The el at l is in it's right place, so move l to point to the place where the next 0 goes.
                l += 1

                # Move i forward since swapped element is now in correct place.
                i += 1
            elif nums[i] == 2:
                # Found a 2: swap it to the right boundary (r) and move r left
                swap(i, r)

                # NOTE: We shouldn't incr `i`, because we grabbed an el from the right side of the list(pointer by r) and
                # swapped it with an el on left side(i). We don't know where the el that was on the right should live ultimately.
                # So we can't increment i, because we need to find where the el that we brought to i, should live. It's not decided yet.

                # NOTE: This is different than when we encounter a 0. Because in that case we swap it with an el on the LEFT side of
                # the list and we know everything on the left(up until l) is sorted. So the el at `i` is actually in it's right place.
                r -= 1
            else:
                # Found a 1: it's in the right "middle" section, just move i forward
                i += 1

# 4. Three Pointers - II
# TODO neet

# 5. Three Pointers - III
# TODO neet
