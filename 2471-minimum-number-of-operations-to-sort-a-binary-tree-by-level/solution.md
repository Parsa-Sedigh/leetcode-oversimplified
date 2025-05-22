As we see **level** of the tree, we think about doing BFS.

Q: How do we minimize the number of ops?

A: We take a greedy approach. First we sort the arr. Then we go through every el in the given arr.
If the vals at the same idx don't match, it means the val at the given arr is not in the right place(it should get sorted).

Now where should that el go?

Let's say the arr and it's sorted version is: arr=[1, 4, 5, 3] and sorted_arr=[1, 3, 4, 5].

In this ex, 4 is not in the right place. We know for sure that in idx=1, 3 should live not 4. But we don't know where 3 lives
in the arr, unless we go through the arr and find 3 to do the swap which is inefficient.

Instead, we can do some preprocessing and build a hashmap of `val -> idx` out of `arr` and keep it updated when we do any swap.