Each number in the `height` array, represent the height of the bar in consecutive positions of x-axis. 

For example: `height = [0,1,0,2,1,0,1,3,2,1,2,1]`. It means in the first position in the x-axis, there is no bar, since the height is 0.
The next bar has height of 1, so look at the image, you see the first black bar on the x-axis and has height of 1.
The next position doesn't have any bars since the height is 0 at that index.
The next bar has height of 2(see the first bar with height of 2).
and ... .

**Note:** each bar has width of 1(on the x-axis)

**Note:** As you see in the img, in the first position(the empty one, before first black bar), there's no boundary on the left of it,
so no matter how much water we would add over there, it will all just spill to the left.

We're gonna use `min(<maximum left height>, <maximum right height>) - height[i]` to determine how much water we can trap in position `i`.
It could give us negative numbers which means we can trap 0 water in that position.

Q: Why we use min()?

Because it's gonna help us determine how much water we can trap in that position.

Note: A position means a bar. We do the above calculation for every single bar(position).

Both of the solutions are gonna be O(n) time(linear time complexity).

## O(n) memory solution
For every single position to know how much water we can trap at index `i`, we need to know what's the max left and max right height?
We need to be calculating the max of left and max of right for each position, so we're gonna need to be doing that calculation a lot. So we can
make an array and store that calculation for us so that we only have to do it a single time each.

To find the `maxLeft`, we iterate through the array from index 0 and for each element of array, we calculate it's maxLeft and put it in the same
index of `maxLeft`.

Then to find `maxRight`, we do the same but this time we start iterating from the last index of the array backwards.

Note that we can't calculate `maxLeft` and `maxRight` simultaneously for each element, because for example if we start at index 0, we don't know
what are the next elements of current element in order to calculate it's `maxRight`.

![](../img/42-1.png)

`Time: O(n)`

`Space: O(n)`

## O(1) memory solution
We use two pointers to reduce the memory complexity from O(n) to O(1). We don't need those maxLeft and maxRight arrays in this approach.

maxL and maxR are gonna be keeping track of the maximum left pointer and maximum right pointer so far.

Which pointer we shift?

We're gonna shift the one that has smaller max value. For example if maxL is less than maxR, we're gonna shift `l`(OFC forward!). Because
we should calculate the tallest block on each side.

FYI: We know that we can't have any water stored on the endpoints(first and last element of height array).

Q: Now how much water a position can contain?

A: We take the maxL.

Q: How come we don't need the `maxR`?

A: Let's say we're at index `1`. We know at that position the maxL(max of left so far, current position not included) is `0`. Now we technically
don't know what the maxR of current position **really** is. Why really is bold? Because even though the current maxR is `1`, it's what
maxR `so far` is, it's not the correct value for current position. The correct value of maxR for index = 1, is `3`. It's the true maxR for index 1.
So now that we even don't have the right maxR, why is it that we **don't need** that value(`maxR`)?
Because remember we want the minimum of the maxL and maxR. Now we clearly know what the `maxL` is and we know it's smaller than what current
maxR is, and we want the minimum of maxL and maxR, so no matter how big the real maxR of current position is, it doesn't matter how big it is,
we know `maxL` is our bottleneck, remember we shifted our l pointer because what l was pointing was smaller than what r is pointing.
That's why we shifted it. That's how we're able to calculate the water that's trapped in the current position without knowing what the `maxR`
is.

So now what's the amount of water that we can trap at index = 1? It's 0 because maxL - height[i] which is 0 - 1 => negative(we don't count
negatives) => 0

The amount of water for each position is: `min(maxL, maxR) - height[i]`

Now let's move to index = 2. At this position, maxL is 1 and maxR is also 1. So now we're at a dilemma. When maxL and maxR are equal, so
it doesn't really matter which one to shift. Let's shift the left one again.

We always shift the minimum pointer between maxL and maxR. When we shift a pointer, we calculate the height in the new position.

Note: In this approach, we didn't use the `maxLeft` and `maxRight` arrays, instead just `maxL` and `maxR` numbers.

![](../img/42-2.png)

`Time: O(n)`

`Space: O(1)`