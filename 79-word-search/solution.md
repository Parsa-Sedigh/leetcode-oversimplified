THere is not an efficient algorithm to solve this. Because we wanna go through brute force solution and that brute force solution is
gonna be backtracking.

We're gonna do recursive backtracking or in other words with DFS.

In this type of questions, first we can get the dimensions. So define `ROWS` and `COLS` variables and initialize them.

Note: We can't re-visit the same character twice within our path therefore we need a variable for our path and we're gonna use a set
to add all the current values(positions) from our board that are currently within our path to make sure that we don't revisit the same
position twice within our path.

It's good to create a function for doing the backtracking(we named it `dfs` in this solution) inside the function given by the problem, so that
we don't have to pass in some of the variables that we're using inside the dfs function.

The current position that we're at are named `r`(row) and `c`(column).

`i` arg is gonna tell us the current character within our target `word` that we're looking for.

Invalid cases:
- `r < 0 or c < 0 or
r >= ROWS or c >= COLS`
Means are we out of bounds of the board?
- `word[i] != board[r][c]` means what if the character that we're at currently in our word, is not equal to the character that we're at in our board?(we're
at the wrong character in the board).
- `(r, c) in path` what if the (row, column) position that we're at, is inside of our `path` set? What does that mean? It means we're visiting
the same position twice within our `path`(we saw the same character twice).

The solution is definitely not efficient because we're running through entire board.

Time complexity: O(n * m * dfs) - time complexity of running through the entire board. n and m are the dimensions of our board and they're gonna be
multiplied by the dfs function because we're calling that dfs function every single time for every position in the board.

Now what's the time complexity of dfs function?

A: The call stack of the dfs function in this case is always gonna be the length of the `word`. Because the `word` can only be so long, we can only
go through so many characters for the `word`.

**Note:** For finding the time complexity we say: We have 2 nested loops, one is gonna run n times and one gonna run m times. So n * m.
But we also have recursive calls in our solution, so we also need to find it's time complexity as well and since we're calling that recursive call
for each run of the loop, we need to multiply them altogether.

We have 4 different branches of dfs. We're calling dfs 4 different times. So it's gonna be 4^(len(word)). So it's gonna be sth like 4^(n) where
n is the length of the word.

Time: `O(n * m * 4^len(word))`.

**Note:** We use the path variable to not togo over the correct characters that we have found until now, **again**. Because they are right,
there's no point to go over them.