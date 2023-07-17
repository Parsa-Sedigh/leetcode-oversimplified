Note: You can't just find the maximum and minimum numbers in the input array and subtract them. Because we know time moves in one direction.
So maybe the maximum we found was earlier than the minimum. So we bought at the maximum price which obviously is stupid!

Use two pointers.

Initialize left pointer on day 1 and right pointer on day 2 and then on each iteration, we see what's the **current** profit from `l` to `r`?

Note: `l` pointer shows the day we buy and `r` shows the day we sell.

If our `r` value is less than `l`, we update the pointers in the way: `l = r` and `r = r + 1`. But if l value is less than r, first
calculate the profit and update it if it's more than current's max. Then since we're buying low and selling high, that means we can 
leave `l` where it is and update `r` to be `r + 1`.

Time complexity: O(n)

Space complexity: O(1)