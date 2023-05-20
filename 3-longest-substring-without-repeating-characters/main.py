class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = 0

        # we're gonna do sliding window, so we need 2 pointers(l and r):
        l = 0

        for r in range(len(s)):

            # keep doing this while that duplicate remains in charSet
            while (s[r]) in charSet:
                charSet.remove(s[l])
                print(charSet, s[r], r)
                l += 1

            # after removing all duplicates, add rightmost character to set
            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res
