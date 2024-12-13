from typing import List

from cassandra.cluster import defaultdict


# m: number of strings
# n: length of the longest string

# 1. sorting
# T: O(m * nlog(n))
# M: O(m * n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)

        return list(res.values())


# T: O(m * n)
# M: O(m * 26) - because we have a hashmap with keys being a tuple of str and we have m strs, to a list of el with the length of 26.
# In other words: tuple (26 els) -> [ list of strs ]
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # mapping charCount to list of anagrams
        # (a, e, t) -> [[aet], [tae], ...]
        # So we would have M: O(26 * m * n)

        # Note: In order to make code simpler by avoiding to check if a key exists before using it, we use defaultdict() instead
        # of a simple {}.
        res = defaultdict(list)

        for s in strs:
            # one el for each char from a-z
            count = [0] * 26

            # count how many of each char is in s
            for c in s:
                # we wanna map char 'a' to index 0, z to index 25. One way to do this, is to take the ascii value of `c` and
                # then subtract the ascii value of 'a'. So for example: ord('a') - ord('a') is 0. ord('z') - ord('a') is 25.

                # Note: Let's say ord('a') is 80 and ord('b') is 81. Now if we wanna map it to 0, we can do: 80 - 80 which means doing:
                # ord('a') - ord('a').
                # If we wanna map 'b' to 1, we can do: ord('b') - ord('a')
                count[ord(c) - ord('a')] += 1

            # group the anagrams in the `count` group.
            # Note: In python lists can't be keys, so we convert the `count` list to a tuple.
            res[tuple(count)].append(s)

        # we don't want the keys, we only want the vals
        return list(res.values())
