## Brute force
We can take every single combination. Let's try every single combination of `l` and `r`. Try every single possible container we can make.

`Time: O(n^2)`

## Optimal solution - two pointer
`Time: O(n)`

The minimum height is our bottleneck(limiting factor). We don't want small heights.

First we initialize the l pointer all the way at the left(0 index) and initialize the r pointer all the way to the right(`height.length - 1`).
Why?

Because we wanna maximize the area. We want the width to be as big as possible. Because if the left line is super tall and if the right line is
super tall, then we've instantly found our result.

How are we gonna update our l and r pointers?

Why would we shift the pointer when it's pointing to a taller line? We don't do that.

When both of the lines pointed by l and r have equal height, it doesn't matter which pointer that we shift. But if you wanted to,
you could shift the one that has a taller line a head of it(shift l if l + 1 is taller than r - 1 or shift r if r - 1 is taller than l + 1).
But it actually doesn't matter. You could shift either one.