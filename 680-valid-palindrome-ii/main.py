# Brute force
# T: O(n^2)
# M: O(n) - O(n) + O(n)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # M: O(n)
        s_list = list(s)

        # T: O(n)
        for i in range(len(s_list)):

            # M: O(n) - since only one list copy exists at a time, it does not multiply across iterations.
            # remove one char
            modified_list = s_list[:i][i + 1:]

            l, r = 0, len(modified_list) - 1
            is_palindrome = True

            # T: O(n)
            while l < r:
                if modified_list[l] != modified_list[r]:
                    is_palindrome = False

                    break

                l += 1
                r -= 1

            if is_palindrome:
                return True

        return False


# T: O(n)
# M: O(n)
class Solution2:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                # skip_l: remove the left char and consider the chars after it until r(inclusive)
                # M: O(n) - since we're building two sub-arrs
                # NOTE: We could avoid having skip_l and skip_r vars and do the comparison with s directly. That would make M: O(1)
                # The could would be:
                # return (s[l + 1:r + 1] == s[l + 1:r + 1:-1] or
                #        s[l:r] == s[l:r:-1])
                skip_l, skip_r = s[l + 1:r + 1], s[l:r]

                return (skip_l == skip_l[::-1] or
                        skip_r == skip_r[::-1])

            l, r = l + 1, r - 1

        return True


# T: O(n)
# M: O(1)
class Solution3:
    def validPalindrome(self, s: str) -> bool:
        s = list(s)

        return self.is_palindrome(s, True)

    def is_palindrome(self, s: list, can_rem: bool) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                if not can_rem:
                    return False

                return (self.is_palindrome(s[l + 1:r + 1], False) or
                        self.is_palindrome(s[l:r], False))

            l, r = l + 1, r - 1

        return True
