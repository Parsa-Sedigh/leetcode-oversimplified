from typing import List


# Brute force
# T: O(n^2)
# M: O(1)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for L in range(len(nums)):
            # We have to start from L + 1 and not L, because as problem says, we shouldn't consider the same index twice.
            for R in range(L + 1, len(nums)):
                if nums[L] == nums[R] and R - L <= k:
                    return True

        return False


# Brute force but a bit more time efficient

# T: O(n * min(n, k)) - Why not n^2? Because we could be give a small k, like 2, so the inner loop gonna iterate at most 2 times.
# Therefore, we won't iterate n times per iteration of the outer loop. But if k > n, we would get O(n^2), because the inner loop
# is gonna iterate n times each time.

# M: O(1)
class Solution2:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for L in range(len(nums)):
            # Why L + k + 1?
            # Because the valid answer starting from L + 1 index, could be up to k indexes ahead(it needs to be in a valid window).
            # In other words, we should only search up to l + 1 + k index.
            # NOTE: If we're close to the end of the arr, L + 1 + k could go out of bounds. So we use min().
            for R in range(L + 1, min(len(nums), L + 1 + k)):
                if nums[L] == nums[R] and R - L <= k:
                    return True

        return False


# Hashmap
# T: O(n)
# M: O(n) - we're not removing the keys from map in case the window becomes larger. So in worst case, we've added all els to the mp.
class Solution3:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}  # val -> idx

        for i in range(len(nums)):
            if nums[i] in mp and i - mp[nums[i]] <= k:
                return True

            mp[nums[i]] = i

        return False


# Hashset
# T: O(n)
# M: O(min(n, k)) - because the number of els in the set at any given time could be up to k elements(if k < n).
# Now k could be larger than n (so: k > n), which in that case, M would be: O(n). So M is always min(n, k)
# In other words:
# - if k < n: M: O(k)
# - if k > n: M: O(n)

# n: size of the arr nums
# k: max distance between two equal numbers
class Solution4:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L = 0
        items = set()

        for R in range(len(nums)):
            # The indices are important not the length, so we shouldn't say: R - L + 1
            if R - L > k:
                items.remove(nums[L])
                L += 1

            if nums[R] in items:
                return True

            items.add(nums[R])

        return False
