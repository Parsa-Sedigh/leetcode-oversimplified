from typing import List

# T: O(n)
# M: O(1)
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 1

        # We're guaranteed that the input arr is non-empty and a single val does count as a turbulent subarr
        res, prev = 1, ""

        while r < len(arr):
            if arr[r - 1] > arr[r] and prev != ">":
                # r - l + 1 is the length of the current subarr
                res = max(res, r - l + 1)
                r += 1
                prev = ">"
            elif arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)
                r += 1
                prev = "<"

            # We have consecutive signs(we saw prev sign again) or we saw an = sign
            else:
                # We could set it to the real comparator or just an empty string because our code handles
                # empty str as well
                prev = ""

                # Note: when we have =, we wanna get rid of those two consecutive equal elements in our window. So move r forward
                # and l to where r previously was. By moving r forward, we would completely get rid of the equal elements.
                # But in case of a duplicate sign, we wanna get rid of the prev sign so that we don't have any duplicates.
                # And we know the last 3 els are causing the duplicate signs, so we wanna get rid of the first one. To do that,
                # we move l to be behind r and we won't move r.
                # Note: when there's a duplicate < or >, we don't want the l to jump all the way to r. We want l to stop
                # at r - 1 and we also don't want to move r forward.
                r = r + 1 if arr[r - 1] == arr[r] else r
                l = r - 1

        return res

