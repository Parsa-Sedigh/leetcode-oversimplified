Easiest way to solve this, is through brute-force.

At any point, we have two choices, right or down.

The cache can be either a hashmap or a 2-dimensional grid like the original grid(same size).
Using cache, the time complexity will decrease from O(2^(m+n)) to O(m * n). And with caching, the space would be: O(m * n).
To reduce the space complexity as well, we need to use true DP approach which is bottom up to make the space O(n).

---

real DP:

The values in the cache, are filled until the [0, 0] el in the cache(which is a grid) is filled which is the final result. We can
compute these values bottom-up instead of trying to compute the first el at the beginning, which depends on right and down els
which themselves depend on right and bottom and ... (sub-problems). So instead of trying to going deeper in the sub-problems,
we START with the last sub-problem at the beginning and compute them from bottom to top(top is the ultimate solution).

We know from the bottom right cell, we can reach the target(itself) in **1** way.

We don't need a m*n grid to store the cache. We only need to store the prev row

![](63-1.png)

ChatGPT:

