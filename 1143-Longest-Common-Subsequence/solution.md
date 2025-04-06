It's 2 dimensional dynamic programming. A 2-d grid is used to solve these problems.

Notice that for each char in both strings, there's a cell.

The ultimate result is in the top left cell of the grid. But to compute that, we need to solve the sub-problems from the bottom
and then work our way up back to the top left corner.

At each step, we have two choices:

- the characters match, then we go diagonally to compare the next character in both strings. Why? Because the current two chars match,
so we need to go to the next chars in both strings. So we head to the next sub-problem. Again why move diagonally? Because we wanna
see the remaining chars of each string. When we go diagonally up, we need to add 1 to the current number, because we had a match.
- the characters don't match, then we have to check two different sub-problems(cells). It means that the next char in subsequence
could be found in next chars and to check those, we need to go right or down and we need to take the max(right, down) paths and then
put it in the current cell. When we go up these routes, we won't add 1 to the current number.

![](1143-1.png)

Then, when we go back up the recursion:
![](1143-2.png)
![](1143-3.png)

The pics are intuitive but the way we'll code it, is gonna be brute-force ish, although it's DP.

So to compute the top left, we need to go from last row of grid up to the first row(bottom-up DP).

Bottom-up DP means we're gonna solve it in reverse order.

Note: i tells us the row and j tells the column.