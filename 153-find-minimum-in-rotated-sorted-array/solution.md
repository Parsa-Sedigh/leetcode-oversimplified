Input array: [3, 4, 5, 1, 2]

One way to solve is to find the pivot or in other words, find the position where the elements are not in increasing order.
For example in input array we say from 3 to 4 they're in increasing order, from 4 to 5 they're in increasing order, but from
5 to 1 they're in decreasing order and therefore the pivot is [5, 1] and the minium is `1`.

---

Other approach: initialize l, r and middle pointers. The min is always the value pointer by the middle pointer. Now since the array is rotated and
not sorted in whole, we don't know where to find the minimum. Should we go to the left or right to find the minimum?

First let's consider this: Since we rotated the array, we have two portions of the array that are sorted. Left sorted portion and right sorted portion.

![](../img/153-1.png)

Now the question is: Is this middle pointer at the left sorted portion or right sorted portion(are we currently in left sorted portion or right
sorted portion)?

Now if we are in the left sorted portion of the array, **don't we want to search the right sorted portion? The reason being since we rotated the array,
the left portion is always going to have values that are greater than every value in the right sorted portion.** Because when we rotate,
we're taking the large values(which are at the right side because the array is sorted from the beginning) and putting them at left. Therefore the
values on the right are going to be smaller now.

If our middle pointer is currently in a value that's in the left sorted portion, then we want to search the right sorted portion because smaller
values are in the right sorted portion(we want to find the minimum value).

Q: How can we know if we're in the left sorted portion?

We know every value in the right sorted portion is gonna be smaller than every value in the left sorted portion, so one thing we can check is:
if the current middle value is greater than or equal to the value all the way at the left of the array: `nums[m] >= nums[l]`.
If this is true, that means the middle value is a part of the left sorted portion, in which case we want to search the right sorted portion.

(Why we used >= instead of > ? Because the middle pointer could be at the left most position as well which is one edge case(at index 0).)

Since we're gonna search right, that means we're never gonna search the values at the right sorted portion, so we can cross them out(we will never
look at them again). How we won't see them again? We will put `l = m + 1` .

If `nums[m] >= nums[l]` is false, then we want to search **to the left**. Because we wanna find even smaller values.

Note: The algorithm we're describing, only works on a **rotated sorted** array, if we ever got to the point where the current portion is entirely
sorted, we could not do this algo, in that case we just take the left most value and compare it to the current result(current minimum) and after that
we stop the entire binary search.

How do we know the current portion is entirely sorted?

If the value at `r` pointer is greater than(can include equal as well) the value at `l` pointer and then we can just take the left 
most value and compare it to the current smallest value and return the result.

`
if nums[m] >= nums[l]:
    search right
else
    search left
`