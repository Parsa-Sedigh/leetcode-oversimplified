In this problem, unlike the subsets I, the input array that we're given can contain some duplicate values.

Since we do have duplicate values, it's gonna be tricky for us to not have any duplicate subsets in our result.

Note: In subsets, the order of elements(related to input array) is preserved.

Dynamic programming is possible but by looking at this problem, we can't do DP. Because we're not really counting subsets or anything
like that, we're actually **creating** the subsets. So even if we found some kind of shortcut, it wouldn't really make this anymore efficient
because we still have to **create all of the** subsets.

Q: How many possible subsets could we have?

A: To generate a subset, for each value we can either choose to include this value or not. So for each value we have 2 choices.
We have n values so `2^n`.

Note: In this problem it's not actually `2^n`. Because we're eliminating duplicate subsets. But we're calculating the worst case, so it's 2^n.

How long each subset is gonna be?

At most it can be length n. So time complexity is `maximum length * number of subsets`

Overall time complexity: n * 2^n - we figured this out even without solving the problem. This is a hint to how solve the problem, we need
to do brute force, so we're gonna be using backtracking.

Note: We're not guaranteed that the input array is sorted. So we have to sort it ourself to solve this problem. The sorting is gonna be `O(nlogn)`.
But this is not a problem because we already know the time complexity of this solution is gonna be O(n * 2^n). So sorting time complexity is insignificant.

In order to prevent having duplicate subsets, we need to skip some of the numbers in the input array when we're iterating them with `i`. So for example
we shit i two times or three times to prevent having duplicate subsets.

The base case is when we hit the last element of `nums` for each decision subtree. Look at the leaf nodes, we're making a decision on whether add
3 or not at each decision subtree. Leaf nodes are the base cases.

![](../img/90-1.png)