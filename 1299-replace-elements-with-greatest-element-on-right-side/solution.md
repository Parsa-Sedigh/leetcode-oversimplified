We need to iterate through the arr in **reverse order** to cut down the repeated work.

Look at the img. The top arr is showing the approach with repeated work and the bottom one is when we itearte backwards.
There's no repeated work anymore, because as we move backwards, the value that we have to put at each index is the max
of next val and the blue val on top of it. For example, the val for the position that has val 4 in it,
is: max(6, 1).

![](1299-1.png)