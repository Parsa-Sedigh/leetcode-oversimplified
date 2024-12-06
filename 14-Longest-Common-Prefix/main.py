from typing import List


# iteration
# T: O(n * m) - where n is the length of the shortest string(not the first string) and m is the number of strings.
# M: O(1) - we don't consider the resulting str as memory complexity. Otherwise, in worst case, it's the length of the shortest string.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Let's say we didn't even have a common prefix among any of the strings, they all started with a different character,
        # like [a, b, c], so then we return an empty string
        res = ""

        # Explanation: For every single char in first str, go through all `strs`(in), if at any point,
        # we went out of bounds(i == len(s)) or current char in str is not equal to the current char in strs[0], return the result.
        # Otherwise, after going through all strs, since everything was good, add the current char at strs[0] to the res.
        # Note: We could add the ith char in any str to the res, since they're all equal at that point.

        # Note: Why we didn't first loop through the strs and then the char loop?(Basically why the for loops can't be reversed)?
        # Because we wanna go char by char in every str, so the char loop should be the first and then the loop through the strs.
        for i in range(len(strs[0])):
            for s in strs:
                # If we went out of bounds of s, or if cur char in s is not the same as cur char in strs[0], the algo is done.
                # NOTE: THE FIRST CHECK HAVE TO BE IF WE WENT OUT OF BOUNDS. If you put it as the second condition, we could go
                # out of bounds and accessing s[i] would throw runtime error.

                # Note: We don't need to check for strs[0] going out of bounds, since we're using for loop over it's chars.

                # i == len(s): It could be the case where the strs[0] is a long string and other strings are very short, in that case we would be
                # comparing a char of strs[0] with nothing(out of bound) of other shorter strings. So we need to check for this.
                # We can figure this out with `i == len(s)` and if this was true, we would immediately return `res` and end the algo.
                if s[i] != strs[0][i] or i == len(s):
                    return res

            # If we reach here, it means current char (strs[0][i]) is the same among all strs(since we didn't return yet),
            # so add cur char to res.

            # Note: We could add ith char of any str to the res, they're all equal. Like strs[1][i] or ... .
            res += strs[0][i]

        return res


# iteration II - Doesn't need to build a `res` string
# T: O(n * m)
# M: O(1)
class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    # s[:i] meaning: `i` should be exclusive, because ith char was the char were the char where the chars didn't match,
                    # or we went ouf of bounds, so it shouldn't be counted in the resulting string.
                    return s[:i]

        # doesn't matter to return which string in the strs arr. Because since we reached this line, they're all the same.
        return strs[0]


# Sorting

# T: O(n * mlog(m))
# M: O(1)
# n: length of the longest string and
# m: number of strings.
class Solution3:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        # Sorting the strings helps reduce the comparison to only the first and last strings in the sorted list,
        # as they will have the smallest and largest prefix differences. In other words, the common prefix between all strings,
        # is gonna be between the first one and last one.
        # Note: The strings are sorted lexicographically (alphabetical order).

        # T: O(n * mlog(m)) - because we're sorting m elements but each element is a string of n chars(worst case), so n is multiplied by m * log(m).
        # Note: Sorting of m integers would be m * log(m), but here we have STRINGS which have multiple chars and all of them need to get sorted.
        strs = sorted(strs)

        # Note: The sorted() func just sorts the string in alphabetical order, not by length. So smallest string could appear in any position.
        # We wanna iterate equal to the length of smaller string between the first and last one, so we have to say
        for i in range(min(len(strs[0]), len(strs[-1]))):
            # strs[0][i] != strs[-1][i] means: If a mismatch is found, it means the longest common prefix ends just before this position,
            # and the prefix up to index i is returned(strs[0][:i]): get the min length of strs[0] and [-1]
            if strs[0][i] != strs[-1][i]:
                return strs[0][:i]

        return strs[0]


class TrieNode:
    def __init__(self):
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()

            cur = cur.children[char]

        cur.word = True

    def search(self, word: str) -> bool:
        cur = self.root

        for char in word:
            if char not in cur.children:
                return False

            cur = cur.children[char]

        return cur.word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for char in prefix:
            if char not in cur.children:
                return False

            cur = cur.children[char]

        return True

    # Finds how many characters of `word` match with the Trie. The word param can match with trie up to common_prefix_len number of characters.
    # Note: The only path in the trie is the path for chars of shortest string in the strs arr.
    def lcp(self, word: str, common_prefix_len: int) -> int:
        cur = self.root

        for i in range(common_prefix_len):
            # if cur char at word, is not in children of the cur node in trie, the common prefix is valid until prev char of current char in word.
            # So the length would be equal to i(since length = index + 1)
            # Note: Return the i as the new common_prefix_len
            if word[i] not in cur.children:
                return i

            cur = cur.children[word[i]]

        # word matches with all the chars in trie, so common_prefix_len doesn't change, return it.
        return common_prefix_len


# 4. Trie
# T: O(n * m)
# M: O(n) - because we only insert the shortest string at the trie

# n: length of the shortest string
# m: number of strings
class Solution4:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        # Find the shortest str.

        # Note: For this, first assume the first str is the shortest one. Then start from str at index 1 and go through the whole strs
        # and compare the len of each with the current shortest, if it was shorter, it becomes the new `mini`.

        # Note: mini is the index of shortest string in strs arr. At the beginning, we assume the first string is the shortest one,
        # until we find another shorter one.
        mini = 0
        for i in range(1, len(strs)):
            if len(strs[mini]) > len(strs[i]):
                # the el at index i is shorter. Assign i to mini
                mini = i

        trie = Trie()

        # Insert the shortest str in trie. At the end, we know the result(longest common prefix) should be this word or a prefix of it.
        trie.insert(strs[mini])
        lcpLen = len(strs[mini])

        # go through every string in strs arr to compare it with the inserted word at trie.
        for i in range(len(strs)):
            lcpLen = trie.lcp(strs[i], lcpLen)

        return strs[0][:lcpLen]
