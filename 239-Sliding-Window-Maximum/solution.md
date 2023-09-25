## Naive approach
You might recognize one solution immediately: For each of the windows, why don't we just scan through the window, we check every value and
see ok this is the max, and then we just shift our window by one.

The time complexity of this is `O(k * (n - k))`. `n - k` is how many windows we're gonna have.
Note: When we have `for (let r = k - 1; r < nums.length; r++) {}` we're iterating `n - k` times not `n` times(assuming length of `nums` is `n`).

Can we make a linear time solution? O(n)? Yes.

## Better approach - Deque
Time: `O(n)`

Memory: `O(n)` - because of the queue

Let's see the repeated work that we're doing in the brute force approach:

Let's say the input array is: [1, 2, 3, 4] and k = 3. Now in first window, first window is [1, 2, 3] and obviously 3 is the max, but
we're still checking 1 and 2. The next window is [2, 3, 4], the max is 4, but we're checking every element. Since we know 3 is greater than
2 anyway, why would we ever need to look at the 2 ever again? It's never going to be the maximum.

Another example: Input is [1, 1, 1, 1, 1, 4, 5] k = 6 . Window is [1, 1, 1, 1, 1, 4]. The max in first window is 4. We checked all the ones and
lastly, 4. Now the next window is [1, 1, 1, 1, 4, 5], but we're still checking all these `1`s. But as soon as we see that 4, we know that
the elements behind it are useless to us, we never have to look at them again. They will never be the maximum inside of our window.

The DS we're gonna use to eliminate these values, is a `deque`.

Again: If we have a window and we see a value that's greater than values that are previously in our window, then we can eliminate those values
from our window.

You're gonna notice that values in our deque, are always going to be in **decreasing** order.

So with deque we say:

Initially our sliding window is of size 6(k). So put the 6 first values -> [1, 1, 1, 1, 1] and the last value is 4, but since 4 is greater than
the value at the top of our deque(or right most position of deque), now we're gonna pop the right most value off and repeat this until the deque is
empty or the current top of the deque is greater than the value that we want to add to deque. In our case, we pop all the `1`s and then add 4 -> [4] .

Now what value are we gonna add to the output array? Well the left most value of deque which is 4.

Now we don't need to consider the elements in our input array up until 4.

Now shift the window by one position. Before adding 5 to deque, we have to check is 4 greater than the value at the top of the dequeue?
Yes, so why would we ever consider 4 as the maximum ever again? We don't have to, so we remove 4 from the deque. Now we can add 5 to the top of deque.

What's the time complexity?

First we took each 1 and added it to the deque. We did that for every single value of the current window, that was expensive and then we also
removed every value from deque(in our example), but we know **adding and removing is O(1) to dequeue** and we had to do that for
every single value in the input **potentially**, so that's `O(n)`.

This problem is of type `Monotonically decreasing queue`. Because our queue is always gonna be in decreasing order.

The reason we're using a queue rather than a stack is because we wanna be able to add and remove elements from the beginning, in O(1) ,
but not only that, as our window shifts, we wanna be able to take an element from the beginning and remove it from the beginning and we wanna
be able to do that in O(1) time which is why we need a queue.

**Note:** The values in queue are in decreasing order.

Another example: input arr: [8, 7, 6, 9] k = 2
First add 8 to queue, then 7 is not greater than 8, so we're allowed to add 7. We only want to remove smaller elements from the queue if they exist,
but in this case that's not true. So now the queue is [8, 7]. Notice the values in queue are in decreasing order. So what that tells us?
Since we want the max value in our sliding window, we can just look at the left most value in the deque(first value) and then add that to the output
array(for each window).

Now shift the window: [7, 6]. First thing to notice is that 8 is no longer in bounds(window). So we gotta pop from the left of the queue and we wanna
do that efficiently which is why we're using a dequeue. Now we see 6. It's not greater than 7, so we're allowed to put 6 at the end(to keep the dequeue
in decreasing order). Now the max value which is the left most value in dequeue is 7. So we add it to the output array and ... .

When the current value is greater than the top value(last value) of queue, we have to pop from the top of the queue(right most position) and then
put the current value in the queue.