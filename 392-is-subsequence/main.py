# Two pointers approach
# T: O(n)
# M: O(1)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        # keep going while both of the pointers are inbound.
        while i < len(s) and j < len(t):
            # As you can see, j is incremented in both cases, so we could say:
            # if s[i] == t[j]:
            # i += 1
            # j += 1

            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        # this means for every char in s, we were able to find a matching char in t
        if i == len(s):
            return True

        # if we reach here, it means s is not out of bounds and j went out of bounds of t, we searched the entire t but
        # we couldn't find a matching char for every char in s.
        return False


# T: O(n)
# M: O(1)
class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while i < len(s) and j < len(t):
            # As you can see, j is incremented in both cases, so we could say:
            if s[i] == t[j]:
                i += 1

            j += 1

        return True if i == len(s) else False
