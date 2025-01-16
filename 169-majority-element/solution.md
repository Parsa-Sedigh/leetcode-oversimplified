According to the problem, the majority element is the el that appears in more than half of the arr.

**To count the number of occurrences of vals, use hashmap. We could use an arr but if the input vals are arbitrary and not in a specific range,
we can't do that.**

In the hashmap for num of occurrences, key is gonna be the input el and val is num of occurrences of that input val: <el>: <count>

### Boyer-Moore Voting Algorithm
Maintain the count of most occurred el and the val itself in `count` and `res`.
Whenever encountering the same val, inc the count, otherwise dec count. When count is 0(before decrementing), swap the res with curr el.

When count becomes 0 for a res, we don't know if cur res is gonna be the majority el anymore because it's count is 0. That means,
before curr el, it was majority, but now it's not anymore.

Note: Before assuming this algo doesn't work, first verify the input arr is valid and has a majority el that appears more than half the size
the arr.