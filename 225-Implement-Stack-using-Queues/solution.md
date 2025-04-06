It doesn't even make sense to solve this with two queues!

**When using queues for implementing stacks, we can push values in O(1), but we can't pop in O(1). It's gonna be O(n).**

So popping is gonna be O(n) if we tried to implement a stack with queues.

Can we use a queue to efficiently implement a stack? No, it's not efficient, but we can do it.

Note: We can't remove from the right of the queue(tail), we can only remove from the left(start).
So to remove an element, we start removing from start and pushing the removed item at the end except the last one.