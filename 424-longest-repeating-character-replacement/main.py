from collections import defaultdict


# 1. Brute Force
# T: O(n^2)
# M: O(n)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0

        for i in range(len(s)):
            count = defaultdict(int)
            max_f = 0

            for j in range(i, len(s)):
                count[s[j]] += 1
                max_f = max(max_f, count[s[j]])

                # (j - i + 1) is the size of the current window.
                # (j - i + 1) - max_f is the number of els that are not the same as majority char.
                # So if number of non-majority chars(which is (j - i + 1) - max_f) is < = k, it means, the window is valid,
                # so we can consider it.
                if (j - i + 1) - max_f <= k:
                    res = max(res, j - i + 1)

        return res


# T: Assuming s only contains English chars(according to problem's description): O(26 * n), otherwise: O(n^2). Why?
# Because we have a loop over whole input and also this: max(count.values()) which if we only have english chars, in worst case
# would be O(26) otherwise can be O(n). Therefore: O(n^2).
# M: Assuming s only contains English chars: O(26) => O(1). Otherwise: M: O(n)
class Solution2:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            # is the current window valid? We find out by subtracting the length of the window and the count of the most frequent
            # character which is max(count.values()). The max(count.values() is going through the hashmap which could be of size 26,
            # so this operation would be O(26)
            # Note: The number of replacements we have to do for current window is (r - l + 1) - max(count.values()) .
            # Note: If (r - l + 1) - max(count.values()) > k, it means we can't make all chars of the curr window to be the same.
            # Therefore, curr window is invalid, we need to make it smaller by moving l forward.
            # Note: Here, instead of while, you can use an if block as well
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            # the computation of `res` should be after changing the `l`. So this line should be after the while loop
            res = max(res, r - l + 1)

        return res


# T: If `s` only contains english chars: O(n), if it contains non-english chars, it would still be O(n), because we're not
# going through the `count` hashmap in this optimized solution.
# M: O(26) => O(1)
class Solution3:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0

        # with this, we don't need to do max(count.values() which is getting the max value of entire hashmap, anymore.
        # Note: count.values() at worst case is O(26).
        maxF = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            # maybe the new count of s[r] is now the maximum in entire hashmap. Maybe s[r] became the most frequent character now.
            # The max() function is constant time operation(O(1))
            maxF = max(maxF, count[s[r]])

            while (r - l + 1) - maxF > k:
                # Notice that even though we're shifting l pointer, which means we're removing characters from our window and therefore
                # potentially decreasing the value of current maximum number of occurrences in hashmap, we're STILL NOT decrementing maxF(which
                # we can't because we don't know the character that was removed was actually the maximum occurrence char). Because
                # we actually don't need to, it won't end up affecting the result if we don't decrementing it(which could also give us a
                # wrong result). That's why we only needed to store an int for maxF not which character actually has the most occurrences.
                # So this was an optimization which is hard to see why we're allowed to do that.
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
