The easiest way is also the most efficient way!

After iteration over the elements in the outer most layer, we take the outer most layer and shrink it, so now we have a sub rectangle or
sub matrix.

For each matrix, we start at the top left and we go in spiral order.

Look at the img. After the green rotation and blue rotation, when we want to do another rotation(white), we see that L and R are at the same
position. They overlapped, so we don't have to continue anymore.

Let's walkthrough the algo and see the things we're gonna do slightly differently:

Initialize l at zeroth index but the r at `len(matrix[0])` instead of `len(matrix[0]) - 1`, so one position out of bounds. This will make
the code a bit easier. Also the top boundary is at 0 and bottom at `len(matrix)` instead of `len(matrix) - 1`.
Look at the position of indexes in the img.

At the most outer layer, when we're done with the first row, we shift the top boundary **down**. Why? Because we did the first entire row of whole
matrix, so top boundary should be shifted down. Look at the img, the remaining elements are at the green rectangle.
![](../img/54-1.png)

Now when we're done with the right column, we want to update the right boundary, because when you look at the new rectngle(red), we moved
the top boundary down(previously) but we can also take our right boundary and move it to the left(decrement it by 1).

When we finish the bottom row, the bottom boundary should be shifted up by one. Now the new rectangle is the red one:
![](../img/54-2.png)

When we finish the left column and shift it to right.

We start at 6(top left) and go right until we reach the right boundary. Now since we finished the top row, now we wanna update the
top pointer and shift it down but now top and bottom are the same value and that's one of the conditions for terminating.

In this case, top and bottom pointers reached, but it could've been possible that left and right reach the same position, if either of those
happen, then we can stop the algo because we know we've done every single element that we needed to.

Q: What's the if statement at the middle of while loop for breaking out of the while?

A: If we had a single row matrix like [1, 2, 3] or a single column matrix like:
[1,
 2,
 3]

`Time: O(m * n) m and n are dimensions of the matrix`

`Memory: O(1)` - if you don't count the output `res` as extra memory