from typing import List


class Solution:
    # T: O(n). n is total number of chars in list of words
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    # T: O(n)
    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str: str) -> List[str]:
        res, i = [], 0

        # read the whole encoded str char by char
        # Each iteration of this loop is gonna read one entire word
        while i < len(str):
            # when we first start off, the first char that we see is gonna be an int. So we wanna find the delimiter which
            # specifies the end of int, like: 426#... . Here, the len of next word is 426.
            j = i

            # while this condition is true, it means we're still reading the int. We're guaranteed to find a # char. So keep
            # moving the j pointer forward until reaching the # char. By the end of this loop, the j points to #.
            while str[j] != "#":
                j += 1

            # once we get to #, we know the len of following str is gonna be:
            length = int(str[i:j])  # not including index j, because index j points to the # char.

            # the length var tells us how many following chars we have to read after j in order to get every char of the word
            # Note: Why we started at j + 1? Because j is at the # char, so j + 1 is the first char of the word.
            res.append(str[j + 1:j + 1 + length])

            # update i to point the NEXT char
            i = j + 1 + length

        return res
