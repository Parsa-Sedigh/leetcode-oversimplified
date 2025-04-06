## Brute force
Why brute force approach is O(n^2)? Because we have n^2 different subarrays inside of arr.

## Sliding window(two pointers)
This approach is not possible. Because by looking at the constraints of the problem,
the values in nums could be negative, so just by adding a val to curr subarr, doesn't 
guarantee we're increasing the sum and removing a val doesn't guarantee we're decreasing the sum, since some of the values
could be negative.

## prefix sum
Why we're using count as the value of hashmap?

A: since we could have possibly negative values in the nums, there could be multiple prefixes that have a specific sum.
Note that we wanna get all the possible results. So we want the count, not just yeah there exists one subarr.

Note: We can't just compute every single prefix **before** we actually start building our result. We have to do it **simultaneously**.
Why? Because we wanna have the prefixes for the **current** subarray not the entire arr.
