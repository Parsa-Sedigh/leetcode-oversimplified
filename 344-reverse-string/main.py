class Solution:
    # approach 1
    def reverseString1(self, s: List[str]) -> None:
        # Time: O(n) Space: O(1)

        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1

    # approach 2
    def reverseString2(self, s: List[str]) -> None:
        # Time: O(n) Space: O(n)

        stack = []
        for c in s:
            stack.append(c)
        i = 0
        while stack:
            s[i] = stack.pop()
            i += 1

    # approach 3
    def reverseString3(self, s: List[str]) -> None:
        # Time: O(n) Space: O(n)

        def reverse(l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                reverse(l + 1, r - 1)

        reverse(0, len(s) - 1)
