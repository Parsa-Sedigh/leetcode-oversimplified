approach 1: max heap
- worst case time: O(n + k * log(n)). k could be really big or small. Since k is typically much smaller than n in practice,
we can often consider the time complexity to be approximately O(n). But if k is large(like equal to n), The time is: `O(k * log(n))`.
Also we could use a k-sized min heap so that we get `O(n * log(k))`.
The worst case is better than worst case of quickselect which is O(n^2).
But the average case time is not as good as the quickselect average time which is O(n) .

We want a max heap.

Popping from a heap of size n is gonna be O(log (n)) . We have to do it k times, so O(k * log(n))