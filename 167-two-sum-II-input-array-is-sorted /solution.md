Note: The indices are 1-based, so the result values should be incremented by 1.

## intuition/brute force
Look at every single combination of two numbers.

If our current sum is larger than target, since the array is sorted, we shouldn't look at the **next** element and we can 
ignore it from now on for checking. Now move to the next first element and find a combination for it that adds up to the target(and if
a sum was greater than the target, ignore the next element after current second element from now on).

Worst case time complexity: O(n^2)

## Two pointer / optimal
We don't have to iterate through the entire array more than once(Left and right pointers are never gonna cross each other) -> O(n)

Time complexity: O(n)
Space complexity: O(1)
