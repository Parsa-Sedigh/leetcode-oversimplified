You can implement a stack with linked list or arr.

The naive way for getMin() func would be to iterate over whole stack -> O(n) time to get the minimum. But we wanna do it in O(1).

If we just store a var as minimum and keep updating it when pushing, we have a problem at popping the minimum itself. Because when
we pop it, what would be the new minimum val? In order to find out, we should do an iteration over whole stack which is O(n).
So another better approach is for each position of the stack, write down the minimum at that point.

So we're actually defining another stack for minium values up until any point of the original stack. Each element in the 
second stack tells us the minimum value that we have so far.

### About one stack solution(third one)
- Instead of storing actual values, store the difference from min
- If the difference is negative, it means we updated min
- If popping a negative value, restore the previous min

#### pop()
- When popping positive values, nothing special happens.
- When popping negative values, it means we need to restore the previous minimum.
- The stored differences allow us to track how far we’ve gone below the previous minimum and recover it.

#### top()
- If top is positive, it means the value was stored as val - min, so we recover it with top + min.
- If top is negative or zero, it means that value was the minimum when it was pushed, so we just return self.min.

![](155-1.png)
