# 1. Brute Force
# T: O(n*m) - is actually O(n^2)
# M: O(m)
# m : total number of unique chars in str
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            char_set = set()

            for j in range(i, len(s)):
                if s[j] in char_set:
                    break

                char_set.add(s[j])

            res = max(res, len(char_set))

        return res


# 2. Sliding Window
# When we encounter a duplication char, we need to rem chars from the left until there's no duplicate char in the hashset.
# THEN, we can add the curr char(which was duplicate before), to the hashset.

# NOTE: Why we need to use `while(s[r] in charSet`?
# Because the duplicate char could be at the middle of the curr window. So now the correct window should start

# T: O(n)
# M: O(m)
# n: len of the str
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = 0

        # we're gonna do sliding window, so we need 2 pointers(l and r):
        l = 0

        for r in range(len(s)):
            # Before adding s[r] to charSet, first we need to make sure it wouldn't make our window invalid:
            # keep doing this while that duplicate remains in charSet
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            # At this point, our window is valid, so we can add s[r] to the set and calc the cur result.
            # after removing all duplicates, add rightmost character to set
            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res


# T: O(n)
# M: O(m)
# 3. Sliding Window (Optimal)
class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        res = 0
        l = 0

        for r in range(len(s)):
            if s[r] in mp:
                # This max() is very important. We can't just set: l = mp[s[r]] + 1.
                # This is because we're not deleting anything from mp in case there's a duplicate.
                # When there's a dup, there are 2 cases we need to deal:
                # 1. dup is behind l. Meaning it's already outside our window, so we just preserve l where it is
                # 2. dup is after l(between l and r). We need to move l after where the dup exists(mp[s[r]] + 1), since our window
                # becomes invalid.
                l = max(l, mp[s[r]] + 1)

            mp[s[r]] = r
            res = max(res, r - l + 1)

        return res
