The tasks are limited to the characters from A-Z, so 26 characters.

We want to return the minium of units of time that the CPU will take to finish all of the tasks.

Note: It doesn't really make sense to worry about which character were looking it. There isn't a difference between a `B` and a `C`.
But we should keep track of how many of each character there is. We can just focus on the count of them not the characters themselves.

What order should we process the characters in?

It's probably better to process the more frequent character(task) first. Because we know there's gonna be some idle time(probably) and
processing the more frequent one first, basically gives us more time to not be idle.

We're gonna use a max heap which will allow us to continuously figure out which task is the most frequent one and max heap allows us to
determine that in `log n` time(figuring out which character is the most frequent and pop it), but in this case it's even better than that, it's about
O(log 26), since we only have 26 different characters. So O(log 26) is kinda a constant time operation anyway.

`Overall Time: O(n * m)` - m represents what the idle time is, because in the worst case, we have to go through that idle time for each
task that we have. Suppose that the tasks were: [A, A, A, A], in that case we have to go through the idle time for each task.
Because we have to count the occurrences of each character(we have to go through the entire input array) and we're gonna be
popping every value from our max heap and adding every value to our maxHeap.

We're also gonna use a queue as well.

To have a max heap in python, we need to make each of the values negative. For example in popping, we're gonna end up popping the minimum, but
we're gonna convert it back to positive and this will work.

Once a task becomes 0, we know that we don't have to process it anymore. So when it's 0, we're not gonna add it to the queue, 
we just pop it from the max heap.

![](../img/621-1.png)

Note: Even though popping and pushing to our max heap is usually `log n` operation, in this case, it's gonna be O(log 26) and the
overall time complexity in this case is O(n) - because we have to go through every single task.

`Space: O(n)`

---

## greedy approach
This approach is a little bit more **true** linear time solution

`Time: O(n)`