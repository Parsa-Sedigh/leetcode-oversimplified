Edge cases:
- it is possible to not actually have a path. That means, we could be blocked. So one thing we wanna check before we even start the algo
is if our starting point is a 1. If it is, there's no way to start from there at all.
- similarly, if the ending point is a 1, we can't reach it.

So we can check for these edge cases at the beginning. After checking these, it's still not guaranteed that we will be able to find the
shortest path, but at least we don't start the bfs algo.

8-directionally means: we can move diagonally as well. 4 directions are added to neighbors arr when diagonal moves are allowed as well.
So in total, in each step, we have 8 directions to move.

The layers that we move in each step is specified in the img:
![](1091-1.png)

- Time: Size of the grid which in this case is n * n, so O(n^2)
- space: O(n^2) because in worst case we have the entire graph loaded in the queue DS

Note: In the base case we can check:
- `r >= N or c >= N` or `r == N or c == N`
- `grid[r][c] == 1` or `grid[r][c]`(if this evaluates to true in py)

Note: You can solve this with A* algo as well.
