# T: O(n)
# M: O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # These must always start at 0, because we know 0 is not a part of the cycle, that's for sure.
        slow, fast = 0, 0

        # keep going until they intersect. Note: they already intersect at the beginning, so first move the pointers and THEN
        # check. If you do the checking first, we would get wrong result.
        while True:
            # advance slow pointer by one. Why this is actually "advancing"? Because the vals of els are actually the indexes
            # that they're pointing to. So when we get to an el, it's val is the index, so we can say: nums[val] and this advances
            # us to another el. Think of this as a LL.
            slow = nums[slow]

            # we're advancing fast twice
            # Note: fast and slow are always gonna in bounds, they never gonna point out of bounds because the vals which are the
            # indexes that they point to, are in the [1, n] inclusive.
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                break

        # we can return slow2 as well
        return slow

        # or we could write the last while loop like:
        # while True:
        #     slow = nums[slow]
        #     slow2 = nums[slow2]
        #
        #     if slow == slow2:
        #         return slow