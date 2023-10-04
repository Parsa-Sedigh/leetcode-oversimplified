Q: How are we gonna get the two heaviest stones?

A: We could sort the array. But even if we did sort the array, we need to introduce a new stone possibly after smashing those. So we'll
be introducing a new one and we need to maintain the sorted property of our list which might be a bit annoying.
Another solution is to use a **max heap**. Because we're gonna be taking the max stones each iteration.

In order to take this input array and transform it into a max heap, is an `O(n)` operation with the heapify function. But everytime we want to
get the maximum, that's gonna be a `log n` (we're actually doing a pop, so `O(log n)`) operation and how many times potentially are 
we gonna need to get the maximum? n times. So `O(n log n)` is overall time complexity.

Note: We said getting the maximum is O(log n). Here, we're **not** actually **getting** the maximum, neetcode explained it misleading, we're
actually **popping** from the heap, hence O(log n).

The only tricky part is Python doesn't have max heaps, so we're gonna use a min heap to simulate a max heap and you can do that by
negating all the values in the heap. So we would have -8 at the root of the min heap, but it's actually 8 in the max heap. Later in the logic,
we would convert it back to 8.

`Time: O(n log n)`

Edge case: What if stones at the end of the algo was empty. What if we didn't have any stones left in max heap?
One way is to say: `stones.append(0)` before returning. In that case, if there was already a stone in the max heap, we will end up
returning that stone because it'll be at zeroth index(since it would be greater than 0 which we just appended).
If there was not any stones, we appended that 0 stone and we will end up returning that as the result of the algo.