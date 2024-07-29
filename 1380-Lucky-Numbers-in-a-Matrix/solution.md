The first solution has T: O(m * n) and M: O(m + n). But we can reduce the space to `O(max(m, n))`.

## Optimized solution
Note: The problem says every number in the matrix is unique.

The idea we always use when trying to implement a greedy solution, is a math technique named proof by contradiction.

**IF** we were looking for els that are max in both row and col:

If we find a max in a row, then we're eliminating every other el in that row. Meaning the other els of that row, can't be a lucky number.

So for example in this example, we have 3 lucky numbers in the matrix:
![](./1380-1.png)

So the number of lucky numbers is limited to max(r, c).

But our problem is different: we're looking for the els that are min in it's row and the max in it's col.

Consider 12. It's minimum in it's row. So none of the other els in that row are gonna be lucky(they're crossed out) and it's
also the max in it's col, so other els in that col are not gonna be lucky. Now we know all the els in the row that 12 lives,
are gonna be > 12(12 is min in that row). And all the els in the col that 12 lives, are gonna be < 12 (12 is max in that col).

So for any num in that remaining region, to be considered lucky, they have to be greater than 12(to be max in their col), because all of the numbers in that
last row are > 12. And **also** they have to be min in their row and we know the els in the last cell of those rows are less than 12.
So they have to simultaneously greater than 12 and smaller than 12. This is a contradiction.

Therefore, if we found a lucky number, there can't be possibly more than one lucky num. Now we can solve the problem in M: O(1).

Note: There doesn't have to be exactly one lucky num. There could be 0 lucky nums. An example:
![](./1380-2.png)

Q: How do it in M: O(1)?

A: It all hinges on the fact that if we identify the min in each row, among those, it's actually impossible for the smaller ones
to be the lucky el. Only the max of them could possibly be a lucky el and it's possible that even the max might not be a lucky
num. Why?

For example, in the ex, we know 1 is min in row, but in the next row, the min el is 3 and it's greater than 1.
Now since 3 is the min in the next row, it means it's less than all other els in that row, so 1 is less than those els as well.
We know one of the els in that next row(3 or 9 or 8 or 7) is in the same col as 1. Now for 1 to be considered lucky, has to be 
greater than those els which is not true.

Another ex: For 3 to be lucky, 12 is the min in it's row. 3 is smaller than the min of the next row, so there is definitely an el
in it's col that is larger than 3, so 3 can't be lucky. 

Therefore, only the max of all min_rows could be the result.

So go through the grid and keep track of the max of the min_rows.

Then, we need to go through the col of the max of min_rows and find out if the max of the col is the same as our curr max.
If it is, it's the answer, otherwise, answer is [].

For this, we can also go through the whole arr instead of the col of the curr max, find the max in each col and if we found the max
in a given col and it's the same num as the curr max, it's the result. We can return immediately, because there can be at most one
lucky num.