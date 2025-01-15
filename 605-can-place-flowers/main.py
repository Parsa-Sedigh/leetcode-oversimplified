from typing import List


# T: O(n)
# M: O(n)
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Assume there are empty spots at the beginning and the end of the flowerbed.
        # since we're modifying the input arr, it's counted as extra space. If we didn't modify it, memory complexity would be: O(1).
        f = [0] + flowerbed + [0]

        # skip the first index and last ones, since we added them for making the code simpler.
        for i in range(1, len(f) - 1):
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                # We have to modify the arr, since this position becomes the prev position in the next iteration of the loop.
                f[i] = 1

                # we could use a separate variable as well, if we wanted to have a better code!
                n -= 1

        # if n <= 0 is True, it means we successfully planted all or even more flowers than we needed to. Why we could plant more flowers
        # than the given n?
        # Because we could have a lot more 0s than n.
        return n <= 0


# T: O(n)
# M: O(1)
class Solution2:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # empty shows consecutive empty plots
        empty = 0 if flowerbed[0] else 1

        for f in flowerbed:
            if f:
                # NOTE: int division - round toward zero. You could instead use // without casting to int

                # NOTE: If empty was 0, will have -1/2, which would result: -0.5 and this is not what we want. We want to round it to 0.
                # In most languages it will round towards 0., but not in py. By casting the result with int(), it will round it towards 0.

                # NOTE: Why (empty - 1) and not empty?
                # Because before the current plot(which has a flower in it since we're executing this `if` block), requires the prev plot to
                # not have a flower in it. So one of the plots MUST remain empty. So we decrease one from empty -> `empty - 1`

                # NOTE: Why dividing by 2?
                # Because after accounting for one empty plot for spacing, the remaining empty plots are divided into groups of 2.
                # Each group of 2 plots can hold one flower.
                n -= int((empty - 1) / 2)
                empty = 0
            else:
                empty += 1

        # Note: when the loop ends, yes the empty var correctly represents the number of empty slots from the last flower plot but
        # we didn't calculate the n variable. It could be the case that we have only zeroes after the last 1 and therefore the if block of
        # for loop didn't execute and `n` is not updated. So we update it here too.

        # NOTE: Now why empty / 2 and not empty - 1 / 2. Because we're in the last group of 0s and there won't be any 1s at the end unlike the
        # preceding groups. So there won't be decrement by 1 in this formula again. Don't worry about the preceding 1. It doesn't interfere with
        # the formula.
        n -= int(empty / 2)

        return n <= 0
