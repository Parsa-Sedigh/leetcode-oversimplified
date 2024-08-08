We could write a nested for loop starting from top left going to bottom right. But that's not gonna be super efficient.

We can calculate the prefix sum of a row in O(n). And once we've done that, we can get range sum query for every single
possible subarr in O(1). There are n * (n -1) different subarrays for a row.

So in worst case, to calculate every single subarr, it would be O(n^2). But with prefix sums, this is O(n) because
for any particular sub arr, we can do it in O(1) after we have calculated all the prefix sums.

For each cell in matrix, we wanna store the sum of it's surrounding green matrix. For example, we wanna store the sum of
the green matrix for the cell that has arrow on it:
![](./304-1.png)

If we can do this, we can get any sumRegion() in O(1).

How are we gonna do that?

It's like taking prefix sums.

For example, to get the prefix sum at the specified element:
![](./304-2.png)

Add the prefix sum of it's row until it's cell, with the prefix sum val of the cell above it, which will give us the specified
purple rectangles added together:
![](./304-3.png)

Let's calculate the sum for green box: To get it's sum, we wanna calculate the sum of the cyan box subtracted by the
row [3, 0, 1] and the col [3, 5, 1]. But notice the el 3 appears twice in these. So we have to add it to the result
to counteract that.

We can get rid of the edge cases where we there isn't a top row(for the first row) and the left col(for the first col),
by making the initial matrix larger by one row at top and one col at left and the extra cells are filled with 0.
![](./304-.png)

The pre work is O(n^2) but any subsequent sumRegion() will be O(1).

Space complexity is O(n^2).