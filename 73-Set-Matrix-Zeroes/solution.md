## O(m * n) space
We declare a copy of our input array(matrix). Why?

Because if we want to make the column and row of the cell with value zero, to zero, in future, we would see the cells that were converted
to zero(**not originally zero**) and again make their col and row to zero. This would give us an incorrect result. That's the reason
we would need a copy of the **original** matrix.

So when we wanna make changes, we're gonna make the changes to our copy matrix and when we read the values, we're gonna read from the input matrix not
the copy one.

It could be the case that when we want to set some row or column in the copy matrix to 0, it's already set to 0, so this shows you
the **repeated work**. It kinda shows you maybe having a copy is not the best solution.

Having a copy of the input array takes `O(m * n) memory` and it's not the most time efficient algo either.

We're noticing for every single cell in our input matrix, we're potentially having to update an entire row and an entire column(if the cell
was 0). Can we prevent this repeated work? Yes.

Time: Greater than time complexity of two next approaches.

Space: O(m * n)

## O(m+n) space solution
We see that we have a fixed number of rows(m) and columns(n), so worst case scenario all we're gonna have to do is make sure that
every row is set to 0 and every column is set to 0. So as we iterate through every single value in our input matrix, let's not update the `copy` matrix.
We actually don't need the copy matrix. We need less memory. We can have one array for number of columns and one array for the number of rows
and then we can mark these whether we want to fill in zeroes or not and then at the end, we can actually fill in the zeroes in our
input matrix, without even needing a copy matrix.

Note: An empty element in the columns array or rows array(the arrays that we actually create) indicate that we don't have to zero the related row
or column in the input matrix.

When we see a 0 cell, we put a 0 in the related elements in the rows array and columns array of that cell. Note that we're not gonna
set the rows and columns of this cell to 0 yet, because we don't wanna overwrite the next columns that we haven't visited in the row and
column of this cell.

We go through every cell in the input matrix. So we could visit cells with value 0 but their related elements in rows and columns array are already
marked to 0.

After iterating over all cells, we look at the columns array and it tells us which columns need to be set to 0. Next we look at the rows
array and see which rows need to be set to 0?

The advantage of this is the memory we use. We didn't need to create an entire copy of the input matrix, we just needed two arrays.

`Time: O(m * n)`, because we're iterating over the entire matrix at most 3 times. One we iterate through every cell, one where we fill in the
columns if the element in column array was 0 and one when we fill in the rows(where the related element in rows array is 0). The time
complexity of this approach is better than previous one.

`Memory: O(m + n)` where m and n are the dimensions of the matrix.

![](../img/73-1.png)

## O(1) space solution
Note: We know the best time complexity we can do is O(m * n) because we do have to iterate through every single position in the input matrix.

Is there a way where we can take the rows array and put it into the matrix? So that we can do this in place? If we put it in the
matrix(like the first row)? Is it possible that we take the columns array and put it into our matrix? Like put it in the first column?
Yes we can take these two arrays and put them in our matrix, so we do this in-place.

The problem is: We have one position that is overlapping and that is the top left position((0, 0)). The two arrays are overlapping at
that positions, so we do need a tiny bit more memory, we just need one more variable, but we know that's still O(1).
So for the rows array that tells us which rows we need to set to 0, we're gonna have it have one less cell because we don't want it
to overlap with the columns array. Note that we don't need the rows and columns input arrays anymore in this approach.

We just need a variable for (0, 0) position and it's gonna tell us whether we need to zero out the first row or not.

Again, run through the whole input matrix. Now what are we gonna do when we arrived at a 0 position?

Well, we're gonna mark the first row as 0 - the green area on the img(first row acts as the columns array in the previous approach).
Also, if we were on the first row, we set the variable(we use to avoid overlapping) that represents if the first row should set to 0 or not, to 0.
The cells in green area tell us if that column needs be zeroed out.

So when we hit a zero, we set the respected element of matrix in the first row, to 0, to indicate that that column needs to be zeroed out,
we also need to set the respected element(same row) of the first column of the row to 0, to indicate that that row needs to be zeroed out.

Q: Why overwriting cells in this approach works? I mean overwriting cells in first row and first column?

A: Because we **already visited** those cells. So we can overwrite it. The reason this works is we start at the top left and work our way down(typical
matrix iteration). Note that we only set the first row and first column cells to 0 at the time we've already seen the related cell there.
So this won't make the result incorrect.

Note: In the img, when we arrive at (2, 0), we need to set (0, 0) and (2, 0) to 0, note that (0, 0) cell is different than `rowZero` variable. That variable
is shown in the purple area on the img(it's just a single variable).

We set (0, 0) to 0 to indicate the column that needs to set to 0 and (2, 0) to 0 to indicate the row needs to be set to 0.

Now that we know which rows and columns we need to zero out. All we have to do is fill in the rows and columns to 0. Go through
first row and first column and the `rowZero` variable and if an element was zero, zero out the row or column depending on whether that
element is responsible for zeroing out the row or column.

Purple are responsible for zeroing out the row and greens for columns.

`Space: O(1)` - all we needed was one extra variable which still would be O(1).

---

In the algo, first we determine which rows and columns to zero out. Then we zero out most the matrix. Then we zero out the first **column** if we need to.

Then we zero out the first **row** if we need to.

Note: We have to first find out if we can zero out the first column not the first row, because we could overwrite the matrix[0][0] but only
the rowZero was 0, the matrix[0][0] wasn't. So we only had to zero out the first row. But now that we first zero out the first row
and then the first column, we would get an incorrect result. So since rowZero can affect the first matrix[0][0], hence potentially
overwriting it, but matrix[0][0] can't affect rowZero(because it's not stored in the matrix), we first need to zero out the first column
by checking matrix[0][0] and then the first row using `rowZero`.