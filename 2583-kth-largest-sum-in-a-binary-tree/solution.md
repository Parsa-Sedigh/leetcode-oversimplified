### Sorting solution

### max heap solution
Since we want kth **largest** sum, we use a max heap. We only have to pop k times.

- T: O(n + h + k * log(h)):
    - n because of traversing the whole tree using BFS
    - Then we turn the level sums into a heap which has time complexity of `h`
    - Popping from heap k times -> k * log(h)
- M: 

### min heap solution
We're gonna maintain a min-heap of size k. It's size always gonna be less than or equal to k. Because as we go through the
tree levels, we push the sum into the min-heap. Since we want the min-heap to be no larger than size k, we're gonna remove
the min el from the heap. 

In other words, the min-heap is always gonna store the kth largest sum. The minimum of els in the heap is the kth largest el.
It's at the top of the min-heap, we can get it in O(1).

- T: O(n + h * log(k))
    - traverse the tree -> O(n)
    - size of the heap is always up to size k. So pushing and popping from heap. We're gonna pop roughly h times and the size of the
    heap is k -> h * log(k)

- If tree is not balanced: h is n
- if it's balanced, h is log(n)

Also note that k could also be very big like equal to n. So in the worst case, both of the heap solutions would have the same
time.

---

### Time Complexity
The time complexity in this solution consists of traversal and heap ops.

- Traversal: The algorithm performs a level-order traversal, visiting each node in the tree exactly once. If the tree has n nodes, this takes O(n) time.
- Heap Operations: For each level, the algorithm:
  - Pushes the level sum into the min-heap, which takes `O(log k)` time since the heap size is at most k.
  - If the heap size exceeds `k`, pops the smallest element, also `O(log k)` time.

The total number of levels in the tree is h, where `h` is the height of the tree. In the worst case (e.g., a skewed tree),
`h` can be as large as n. In a balanced tree, `h` is `O(log n)`. For each of the h levels, the heap operations take `O(log k)` time,
so the total time for heap operations is `O(h log k)`.

Total Time: The overall time complexity is the sum of the traversal time and the heap operation time:

- Traversal: O(n)
- Heap operations: O(h log k)

So it's O(n + H * log(k)). Now in worst case, H is n not log(n). So now: O(n + nlog(k)) => O(nlog(k))

### Space complexity
Now, let's analyze the space complexity, considering only the extra space used by the algorithm (not the input tree itself):

- Queue: The queue stores nodes at a single level. In the worst case (e.g., a complete binary tree), the maximum number of
nodes at any level (the width) can be up to n/2, which is O(n). For example, in a tree with 
n = 7 nodes (root, 2 nodes at level 1, 4 at level 2), the last level has approximately n/2 nodes.
- Min-Heap: The min-heap stores at most k level sums, so its space complexity is O(k).
- Other Variables: Variables like level_sum use constant space, O(1).

Total Space: The total extra space is O(n) (queue) + O(k) (heap) = O(n + k). Since k is at most the number of levels h,
and h <= n, we have k <= n. Thus, O(n + k) simplifies to O(n).


Space Complexity: O(n)

This is due to the queue's potential size of O(n) and the heap's size of O(k), where k <= n.