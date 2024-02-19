Dynamic programming

Decision tree representation: At every decision, we can take 1 step or 2 steps.

We have two base cases in this problem.

Red means, we return 0, green means we can return 1.

This is a DP question, so we need to find the duplicate work that we're doing. How to find them? Draw the decision tree.
You see that for example, when we get to stair #4, you see the next climbs will be the same. So we're repeating the exact same problem
multiple times. How we can better do it?

To find the solution, we count the number of green circles which are the different paths **from the beginning** that could reach step 5.

![](./70-1.png)

If we solve the problem using recursion and with DFS(because we have a tree), what would be the time?

We have **2** decisions at each step, so it's gonna be **2** to the power of height of the tree and the height of the tree is roughly gonna be
equal to the `n`. Time: O(2^n). So it's not efficient and as you see, we're repeating the same problem multiple times in the decision tree.

Note: The number of decisions at each step, specifies the base number of power, in time complexity. For example if we have 3 decisions at each
step, the time complexity would be: `3^n`.

### Memoization
For example, when we get to stair 2, we're asking how many different ways(with 1 or 2 incrementing) starting from 2, we can get to 5?
And we would find the number of different ways. So when we get to the same position in the decision tree later, why do we have to
recompute the exact same thing?

The purple decision trees are the same. In other words, in both cases, we're solving the exact same sub-problem and since we're doing it DFS,
the left sub-problem is gonna solved first.
So we can store the result of left purple tree in memory and when we get to the right sub-problem which is what we've already solved,
we won't draw any levels when we get to the 2, the second time. So we're eliminating the repeated work.

But that's not all the repeated work! We have another same sub-problem at stair #3 and again, since we're solving this using DFS,
the left blue subtree is gonna end up being computed before the right blue one. So when we get to the 3 again, we already know the answer and won't
recompute.

Another one is the orange sub-problem.

![](./70-2.png)

So when we do eliminate all the repeated work, our decision tree ends up the yellow one:
![](./70-3.png)

This is roughly O(n) time complexity. Because we're only solving each sub-problem once. The problems we solve are at:
0, 1, ... 5(n is 5) and each of them are being solved once. So the time is O(n).

This was the DP solution where we're caching the result aka memoization.

Note: But this problem can actually be solved with a true DP solution(we're still using memoization). It means, the result
of 0 sub-problem depends on 1, the result of 1 itself depends on 2 and ... . So let's start at bottom, solve the base case and 
then work our way up to the original problem at 0. This is called a bottom up dynamic programming.

Let's say we wanna know how many ways we can get to 5 from 3?

A: From 3, we can go to 4 or 5 and we know the solutions of 4 and 5. So we just need to sum the solutions of 4 and 5 for 3.
This is like the fibonacci sequence.
![](./70-4.png)

- Time: O(n)
- Space: If we use an array of size n, it would be O(n). But is it needed to have an array with the size of input? No. Notice
how each value depends on two values that come after it. So we don't need an entire arr, we just need two variables.

Now if we initialize two variables(`one` and `two`) for the values of last two func calls in the call stack, we need to compute `n - 1` values. We have to
loop `n - 1` times and then our one variable arrives at 0, we return the result.