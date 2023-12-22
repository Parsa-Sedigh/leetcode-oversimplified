If k = 1, it means we want the largest element(right most element in the sorted arr).

Approach 1: sort the array

Sort the array and then return the index you want. If k = 2, you want the second largest, so the index would be: `len(arr) - k`.

Time: O(n * log(n))

Can we do better than n * log(n) ? Yes

---

approach 2: Max heap
- Time: O(n + k * log(n))

Using a heap will be slightly better because we won't have to sort the entire input arr. Heapify would be O(n) . After we've already
done an O(n) operation to turn this array into a heap, then we're gonna have to pop from that heap k times, so we can get the kth largest element.
Everytime you pop from a heap, it takes a O(log n) operation where n is the size of the heap and we do this k times.

It's slightly better than O(n * log(n)) depending on whatever ke happens to be. So in some cases, it will be better than the sorting approach. If k
is relatively small.

The time complexity that we reached in this approach is as good as you can do in terms of worst case time complexity. But there's a solution that's
better in terms of average case time complexity.

---

approach 3: quickselect algo
- worst time: O(n^2)
- average time: O(n)

Similar to quicksort. We know the main part of quicksort is the partition. We take the arr and partition it into two halfs. Every value in the
left half is less than or equal to every value in the right half. That's how we partition the arr.

How can we make sure that it's always gonna be half? Well we can't. That's why the worst case time complexity is O(n^2) and the average time
is O(n). Because we're gonna randomly pick up a pivot, like the right most element of the arr(which is not sorted) each time,

All of this is gonna be in-place.

pivot decides what element goes to the left half and what goes to the right half.

Note: Partitions are not necessarily gonna be sorted in themselves. But every value in left partition is less than or equal to every value
in the right partition.

Now we know the kth largest is at `len(arr) - k`. Now based on the partition, we arrive at a index which belongs to the left half or
right half and we know the index we want. But that half is not sorted yet. So we can't just return that value in that index yet.

But if ever the target index is the same as the `l(fill)` index(index where two partitions are split based on), then we've actually found our result
and the algo is over. Why? It's because we know for sure that the element pointed by `l(fill)`(or whatever pointer name) is the kth largest element.
Because we know for sure that everything in the left half is less than or equal to this element and we know for sure that the elements to the
right of it, are greater than this element. In other words, the position of this element is the same no matter halfs or sorted or not.
Now if the k was not the same as the `l(fill)` pointer, for example bigger, we partition the right half and ... .

With quicksort, when you do the partition, then you have to recursively run quicksort on left and right partitions which ends up
giving an average time of `O(n * log(n))`. But in this case, the average time is O(n) because we're not gonna be looking at both halfs of the
partitions, we're only gonna be looking at at most one half wherever we know that the target happens to be.
And assuming in the average case, everytime we choose a pivot, that pivot is gonna be somewhere in the middle of the arr where half of the
elements less than or equal and half of elements are greater than it, that's gonna give us O(n) because we have to iterate through the entire
arr once. Then we have to iterate through half of the arr which is gonna be n/2 operation, then we have to iterate through half of that,
which is gonna be n/4 and ... . This is an infinite series: n + n/2 + n/4 + ... which evaluates to `2n`, which is O(n). So the average case
time is `O(n)`.

That's the average time.

But we know that in some cases, we could have a pivot that is the greatest element of the arr. Then if we didn't find the result,
then we would have to look through pretty much the entire arr except the pivot and the arr could be organized in such a way that every time
we choose a pivot, that pivot is always the greatest value, so each time we iterate through the entire arr, we eliminate one value(pivot) and
again iterate through the entire arr, eliminate one value and ... . That's O(n^2) which is the worst case.