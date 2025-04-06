# Two pass
# T: O(2*n) => O(n)
# M: O(n)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.helper(s, t) and self.helper(t, s)

    def helper(self, s: str, t: str) -> bool:
        mp = {}

        for i in range(len(s)):
            if (s[i] in mp) and (mp[s[i]] != t[i]):
                return False

            mp[s[i]] = t[i]

        return True


# One pass
# T: O(n)
# M: O(2n)
class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}

        # both s and t have the same len according to problem desc
        # NOTE: Here, we could say: for c1, c2 in zip(s, t)
        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            if ((c1 in mapST and mapST[c1] != c2) or
                    (c2 in mapTS and mapTS[c2] != c1)):
                return False

            mapST[c1] = c2
            mapTS[c2] = c1

        return True
