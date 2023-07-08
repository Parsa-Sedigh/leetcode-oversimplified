By rotating they mean that they took a certain index of the array and they cut the array in half in that index and then swap the portions.
So right hand portion of the index, being swapped to the left.

The most straightforward way to approach this is to literally check evey single value: is this our target, is this our target? ... and then
we return it's index.

Time complexity: `O(n)`

---

Anytime you're looking for a solution that is O(logn) or better than linear(O(n)), almost everytime you're gonna be looking for a binary search
type solution.

This array was originally rotated, can we use that to our advantage to potentially find a binary search type solution?

After rotating, there are two portions of the array(before and after the pivot or left and right of pivot):
- left portion
- right portion

Both **independently** are sorted, so it's like we have two halfs that are sorted.

**Note:** Binary search usually have 3 pointers: left, middle and right pointers and left is always less than or equal to the right.

First ex: nums = [4, 5, 6, 7, 0, 1, 2], target = 0

**Note:** We solve this problem by looking at the discreet cases.

### If we're on the left portion of the array

Q: Let's say our middle value was 6 at some point. This means that we're int the left sorted portion of the array. Can we use this to our advantage?

A: Let's say our target was greater than 6, in that case, we know for sure since we're in the left sorted portion of the array, none of the values at
the left side of 6(middle) are greater than 6. So we can eliminate them by moving `l` to `m + 1` and now let's continue binary search on the
remaining portion(the range between l and r). 

**So if know that we're in the left sorted portion and our target is greater than the middle, we can do: l = m + 1**

Q: What if our target is less than the middle value(we're in the left sorted portion BTW)? For example our `target` was less than 6?

Well the acceptable numbers that can be target, are: 4,5 and 0, 1, 2. Now how do we know which way to go? Do we go left or right? Because we can't
go both directions in a binary search.

A: The key is to see in our left sorted portion, the smallest value is pointed by `l` right? So if our `target` is even smaller than that `l` value,
in that case, we know that we don't have to search 4, 5, and 6. So we can move `l` to `mid + 1` again.

But if our value is greater than or equal to four, then that means we're gonna run binary search on 4 and 5, so we move `r` to `m - 1`. 

**Note:** We **can't** eliminate the numbers after `m` until the end of the left sorted portion(in this case, 7 is eliminated). Because we simply can't
eliminate sth at the middle! We either eliminate from the left or right.

### If we're on the right portion of the array
Q: We're on right sorted portion right? So the m can be at value number 1(we know somehow we're on the right portion of the array somehow).
What if our target was less than 1?

A: Then we **know** we have to search the left portion of the array. We're not gonna look at 1 and 2 anymore(any value to the right of 1 is greater than
1 so we don't have to look at them in this case).

We don't necessarily have to know where the pivot even is. We just know we have to go left.

Q: What if our target was greater than m(1)?

A: THen our solution could possibly be 2, it could also be any of 4,5,6,7. So then where do we go? Again, we can compare right most value(pointer by `r`)
with target. If target > nums[m] and also target > nums[r], that means we can search the left portion of the array and eliminate the right side, so we do:
`r = mid - 1`.

Q: But what if target > nums[m] but it's less than or equal to nums[r](target <= nums[r])?

A: In that case we only have to run binary search on the right portion of m. So we set: `l = mid + 1`

Initially, left pointer is at index 0 and right pointer at last index and middle pointer at index 3. Now how do we even know if we're in the
left sorted portion or right sorted portion?

If our middle value is greater than or equal to the value pointer by left pointer, then that means our middle value belongs to the left sorted portion.
If this wasn't true, that means our middle value is in right sorted portion.

Q: Why the condition for loop is `while l<=r` ?

Because imagine our nums array would be [1] which has just one element, left and right would be equal in that case but we still have to check
that one value.