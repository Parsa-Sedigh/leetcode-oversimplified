# T: O(n)
# M: O(1)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word_len = 0
        inside_word = False

        for i in range(len(s) - 1, -1, -1):
            if s[i] == " " and inside_word:
                break

            if s[i] != " ":
                inside_word = True
                last_word_len += 1

        return last_word_len


# neetcode
# T: O(n) - we might iterate through the entire string if we have a single word at the beginning and there's a lot of spaces
# at the end.
# M: O(1)
class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) - 1, 0

        # first phase: eliminate the leading whitespaces(starting from the end)
        while s[i] == " ":
            i -= 1

        # second phase
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length
