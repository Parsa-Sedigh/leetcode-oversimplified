More of a math problem than a coding problem.

How do we know how many permutations we can even make from that?

We have 3 positions, in the first position we can pick any of those three values. So we have three choices. In the second position since we
already chose one of the values, now we only have two values left. So we have 2 choices. In last position, there's only one value
remaining, so one choice.

Total permutations: 3 * 2 * 1 .

In decision tree, in the first choice, we have 3 choices. We can pick 1, 2, 3. 

If we picked 1, now we have 2 choices, we can't pick one again. We can pick 2 or 3 and ... .

Some of the valid permutations are shown in the screenshot:
![](../img/46-1.png)

![](../img/46-2.png)

When you do backtracking, typically you make some sort of change to the things, then you fully explore that path with the change using recursion
and when you wanna go back up, you undo it, so that the next path won't have it's things messed up.