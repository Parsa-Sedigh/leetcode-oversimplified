Initially we understand, every queen has to be in a **different row**. Because two queens on the same row can attack each other.
Also each queen has to be on a **different column**.

These two were easy, but the hard one is diagonal:

Each queen has to be in a separate positive diagonal ![](../img/51-1.png)

What about negative diagonals?

They are shown in image below:
![](../img/51-2.png)

So each queen is in a separate negative diagonal. Because we don't want any queens to attack each other diagonally.

---

approach 1:

What a really really brute-force idea that you might have is start putting queens in every possible position, starting from:
`['QQQQ', ..., ..., ...]` and ... .

Why is there any reason to do this? This is **too** brute-force. There's a simple way to do it. Because for each queen instead of having
`n^2` choices, how about we just have n choices, because we know for sure each queen is definitely going to be in a different row. 

---

approach 2:

So for the first queen, we say: We can decide to put it in any position of the first row.

Then go to the next row. Now our goal is to find a different location for putting the second queen in the second row. We can put it anywhere
in that second row except the position that is in the same column of previous queen that we have put. Therefore, we need to **maintain the
columns** of whatever previous queens that we've already placed. We don't need to maintain the rows though. Because we just saw the reason.
Because every time we place a queen, we're gonna move to the next row anyway until we get to the bottom(last row) and in that last row,
if we put a queen in a valid position, then we're done.

In addition to keep track of which columns we place our queens, we also have to keep track of the positive diagonals that we're placing them and
also keep track of negative diagonals.

We can keep track of these three with sets.

We need to know what index does a diagonal belong to?

There's a bit of a pattern when it comes to diagonals(positive and negative).

### Identifying diagonal pattern
To find the pattern of a diagonal, see how the row and column along the diagonal change?

The positions are in format of `(r, c)`

The pattern for the center diagonal:

For example along the center diagonal, the row and column start from (0, 0) , then goes to (1, 1) then (2, 2) , so the pattern is:
`r - c = 0`. 

The pattern for the short diagonal:

As we can see, the diagonal starts at (0, 2) then goes to (1, 3), so the pattern is: `r - c = -2`

![](../img/51-3.png)

All of the negative diagonals are:
![](../img/51-4.png)

Is there a similar pattern we can use for positive diagonals?

**In positive diagonals, we're going from bottom left to top right.**

Let's assume we start one positive diagonal at (3, 0) then we go to (2, 1) . Notice that `r - c` is not gonna stay constant. So we can't use r - c for 
positive diagonals pattern. But `r + c` is going to stay the same. Because we're decrementing one of them, but we're increasing the other.

### Decision tree
Try each of the four positions in the first row. So in decision tree for the second level is 1, 2, 3, 4 . Now we're gonna do the similar
thing for the third level(second row of board). But we can't put the second queen in the same column as the previous one. How we're gonna
detect that we can't do this? We can see that the first queen is already placed in the same column in the `column` set. Also we can't put
the second queen in the next position, because the first queen is added to the negative diagonal set. Therefore, we can put the second queen in
(1,2) and (1,3) positions.

As we discussed, we can't put second queen in (1,0) and (1,1):
![](../img/51-5.png)

---

Note: To create the board, `["."] * n` is gonna indicate one empty row. We want n rows, so: `[["."] * n for i in range(n)]`.

Note: We're gonna do the backtracking row by row.