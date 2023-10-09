The challenge is doing it in place.

For example: We take the first row and move it to the right most column.

1   2   3 ->    1
                2
                3

The problem is when you're moving for example 1 to it's new position, you have to save the 3 temporarily. OR,
once you move i to the place of 3, you move 3 to place of 9 and move 9 to place of 7 and move 7 to place of 1:

![](../img/48-1.png)

## General algo - O(n^2)
O(n^2) means we only have to look at each cell in the matrix once. Remember the dimensions are n by n.

We're gonna rotate the most outer layer(square) first and then we're gonna move inward and rotate the inside layers next.

Note: Even though the most outer layer is n * n, we actually do `n - 1` rotations. Look at the img, we did the blue, green and the red
rotations => 3 rotations.

Once we completely rotated the outer most layer(which forms a square in the outer most layer), then we know we have an inner matrix(square)
that we have to rotate again. So it can be treated as a sub-problem because we know no matter what, it's going to be a square matrix, so all
we have to is take all of our pointers and shift them by one.

![](../img/48-2.png)

Note how the pointers changed:
![](../img/48-3.png)

After this, if we update our pointers, the r would cross the l, so we know the algo is over. We don't have anymore matrixs left to rotate.

About the rotation: We know the top left is gonna be put in the top right position. So we have to store top right position in a tmp variable.
Now we replace the bottom right with top right(which is in a tmp) and then move bottom right to be at the place of bottom left and note that
we should store bottom left at a tmp variable and then replace top left with bottom left.
So we need a lot of temporary variables. A slight improvement to writing the code easier(doesn't have any optimization effects). Let's do
the rotation in reverse order.
![](../img/48-4.png)

So instead of moving top left to top right, first we move bottom left to top left(we have previously stored top left in a tmp variable).
So now are we gonna move the top left(in a tmp now) to top right? Nope. we're gonna do this in reverse order. Since bottom left has already
been moved, let's take bottom right and place it in bottom left. Now do the rotation from top right to bottom right and at last, top left(in a tmp
variable) to top right. So we did the exact same rotation but in reverse order(counter-clock wise)

To do the next rotation(next matrix to rotate), the new top left of the new matrix would be one step further to right.
So the new top left is gonna be at (0, 1). Our top right is gonna be from (0, len(matrix) - 1) to (1, len(matrix) - 1). From the previous
bottom right position, we move one spot to left and from our bottom left position we move one spot up and we start the rotations.

We can handle this easily in our code. We can use the `i` variable to handle this. For example instead of
`
topLeft = matrix[top][l]                => topLeft = matrix[top][l + i]
matrix[top][l] = matrix[bottom][l]      => matrix[top][l + i] = matrix[bottom - i][l]
matrix[bottom][l] = matrix[bottom][r]   => matrix[bottom] - i[l] = matrix[bottom][r - i]
matrix[bottom][r] = matrix[top][r]      => matrix[bottom][r - i] = matrix[top + i][r]
matrix[top][r] = topLeft                => matrix[top + i][r] = topLeft
`
we say:
```python

```

![](../img/48-5.png)

`Time: O(n^2)`

`Memory: O(1)`