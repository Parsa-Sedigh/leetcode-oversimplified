# 1. Sorting
# T: O(n * log(n) + m * log(m))
# M: O(1) or O(n + m) depending on the sorting algorithm.
# n: length of string s
# m: length of string t

# Convert each word to an array, sort the arrays, and then compare them.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)


# 2. Hash Map
# T: O(n + m)
# M: O(26) -> O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_chars_count = {}
        t_chars_count = {}

        for i in range(len(s)):
            s_chars_count[s[i]] = 1 + s_chars_count.get(s[i], 0)

        for i in range(len(t)):
            t_chars_count[t[i]] = 1 + t_chars_count.get(t[i], 0)

        return s_chars_count == t_chars_count


# 3-a. array
# T: O(n + m)
# M: O(26) -> O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars_count = [0] * 26
        t_chars_count = [0] * 26

        for i in range(len(s)):
            s_chars_count[ord(s[i]) - ord('a')] += 1

        for i in range(len(t)):
            t_chars_count[ord(t[i]) - ord('a')] += 1

        return s_chars_count == t_chars_count


# 3-b. array (optimized)
# T: O(max((m, n))
# M: O(1)

# Using one array to track both strings’ frequencies (by incrementing for s and decrementing for t) is a
# space-saving trick. If the strings are anagrams, `char_counts` should have all elements set to 0 at the end of the algo.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_counts = [0] * 26

        # At this point, the length of both s and t is the same. So it doesn't matter which string we iterate on.
        # We use both s[i] & t[i] in char_counts.
        for i in range(len(s)):
            s_char_idx = ord(s[i]) - ord('a')
            t_char_idx = ord(t[i]) - ord('a')

            char_counts[s_char_idx] += 1
            char_counts[t_char_idx] -= 1
