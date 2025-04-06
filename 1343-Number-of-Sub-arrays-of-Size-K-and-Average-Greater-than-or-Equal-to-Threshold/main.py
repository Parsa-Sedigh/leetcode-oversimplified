from typing import List


# 1- Brute force
# Initially, `l` is at 0, `r` is at k - 1. At the end of each iteration, move l by one, to maintain the fixed size window.

# T: O(n * k)
# The outer loop runs n times and for each iteration of it, the inner loop runs k times.

# M: O(1)

# Where n is size the arr and k is the size of the sub-arr
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        l = 0

        for r in range(k - 1, len(arr)):
            sum_ = 0

            for i in range(l, r + 1):
                sum_ += arr[i]

            if sum_ / k >= threshold:
                res += 1

            l += 1

        return res


# 2-prefix sum
# T: O(n)
# M: O(n)
class Solution2:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        prefix_sum = [0] * (len(arr) + 1)

        for i in range(len(arr)):
            prefix_sum[i + 1] = prefix_sum[i] + arr[i]

        res = 0

        for i in range(k - 1, len(prefix_sum)):
            sum_ = prefix_sum[i + 1] - prefix_sum[i - k]

            if sum_ / k >= threshold:
                res += 1

        return res


# 3. Sliding Window - I
# T: O(n)
# M: O(1)
class Solution3:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0

        # We have calculated the sum until the index k - 2 (since [:k-1]) is exclusive. So there's one more el remaining to
        # calc the FIRST k els. And it's done at the first iteration of the loop below. We
        cur_sum = sum(arr[:k - 1])

        for L in range(len(arr) - k + 1):
            # L + (k - 1) is where R points.
            cur_sum += arr[L + (k - 1)]

            if cur_sum / k >= threshold:
                res += 1

            cur_sum -= arr[L]

        return res


# 3. Sliding Window - I - First we sum() the initial k-el window. But since in the loop we add to the cur_sum, we also have to
# remove the 0th index from cur_sum before starting the loop. Since the 0th index is no longer in the window, the loop has to
# start from the 1st index.
# NOTE: As you can see, if we sum() the whole initial k-size window, we have to deal with a couple of edge cases. This is why in the
# prev solution, we sum() the first k-1 els, so that when the loop starts, the kth el(k-1 index), is added to the cur_sum.
# If we don't do this, the kth el is added to the cur_sum TWICE.

# T: O(n)
# M: O(1)
class Solution4:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0

        # we have calculated the sum for first k elements, so in the loop body, FIRST we have to put the if block for checking if
        # we reached the threshold. And THEN add to the curr_sum.
        cur_sum = sum(arr[:k])

        if cur_sum / k >= threshold:
            res += 1

        cur_sum -= arr[0]

        for L in range(1, len(arr) - k + 1):
            cur_sum += arr[L + (k - 1)]

            if cur_sum / k >= threshold:
                res += 1

            cur_sum -= arr[L]

        return res


# 4. Sliding Window - II
# T: O(n)
# M: O(1)
class Solution5:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = cur_sum = 0

        for R in range(len(arr)):
            cur_sum += arr[R]

            # since R starts at 0, at the beginning, it could be that our window is smaller than size k. But the moment our
            # window gets bigger than size k, we need to rem the val at L every time that R moves. So this if block should be
            # executed everytime, after the window becomes of size k. So the condition should be: `R >= k - 1`. Since R is always incrementing,
            # this if block executes everytime after a certain point(the point where window becomes of size k).
            if R >= k - 1:
                # if curr_sum / k is >= threshold, it means we found a sub-arr, so inc `res`
                res += cur_sum / k >= threshold
                cur_sum -= arr[R - k + 1]

        return res
