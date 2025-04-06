At each el, we have two choices:
1. including this el with all of the previous elements
2. discard all prev elements and only include the curr el as the curr_max

So it would be: curr_max = max(curr_max + n, n)

There are two possibilities for finding the max sub arr:
1. the max subarr sum could be a straightforward one where it's just in the middle of the arr
2. the max subarr is comprised of some portion of the ending of the arr and the beginning of the arr

We don't know which one the result is gonna be. So we have to try both ways.

The first way is kadane's algo. But we also want to be greedy.

Note: We have to set global_max to the first el. Why? Because there's an edge case where if we set the global_max to 0,
the nums arr could be all negative. Then we would return 0 as the global max which is wrong. So we set global_max to any el
of the nums, for example the first one.

The first case is handled by a simple kadane. 

**But for the second case:** if we actually also keep track of curr_min and the global_min contiguous subarr
that go through the middle(if we can find the middle contiguous min subarr sum), then we know for sure that
the remaining portion is gonna be the maximum subarr sum. The remaining portion means the ending and beginning portions.
Now if we take the middle contiguous subarr sum(global_min) and also total of the arr and if we do: `total - global_min`,
this will get us to a **possible** solution. The ultimate solution will either be this one or the global_max that we get from
the simple kadane algo.

**So we cover the max subarr in the middle with simple kadane using curr_max and global_max. But we can't cover max at the edges portion
which the result could lie in there. Why? Because it's hard. Instead of doing this, we find the `min subarr in the middle` and also the `total`**
and then subtract them to get the max subarr in the edges. The ultimate result is the max of these two groups:
`max(global_max, total - global_min)`. But there's an edge case:

Edge case: What if every val in the input arr is negative?

In that case, we would get a wrong answer. Because in this case, total - global_min would be 0 and the global_max would be 
the highest el in the arr and it would be a negative number. Now the result of `max(total - global_min, global_max)` would end up 0
and we would return 0 which is clearly wrong because all elements are negative and 0 is not in the elements.
If we even had one positive num, the global_max would be equal to that el and we would end up returning global_max even though
the `total - global_min` would still be 0.

To handle this, check if global_max is negative. Since it's negative, then we know for sure there wasn't a single positive val in the
input, because if it was, that number would be assigned to global_max. So if global_max < 0, then instead of doing:
`return max(total - global_min, global_max)` which would give us a wrong answer in this scenario, we're gonna return global_max.