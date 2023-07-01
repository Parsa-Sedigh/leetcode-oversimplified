Brute force approach: We can do this problem in O(m*n), by searching every single value in the input array.

But we can do better because this matrix is sorted.

Binary search can be used to search an element in a **sorted** array. Which has O(logn).

If we run binary search on every single row until we found the target, time complexity would be O(m*logn). This approach is only using the
first property of the given question(each row is sorted).

Can we do even better than this?

Yes, we can use the second given fact which is each row itself is in sorted order(each value of previous row is gonna be smaller than all of the
values of the next row). So instead of searching through every row, we can do a binary search just to figure out which one of these rows to search
in the first place! Let's say target=3. Can a row with the value starting from 10 and 20 have that? No impossible. So if the target value is not
in that row, we can cross that row out, but now are we gonna look at the row above it(previous row) or at the next row? Of course the one above.
Because the one above is gonna have smaller values than the bottom(next) one. So with binary search we can decide which one of those
m rows we're gonna need search? So we can reduce O(m*logn) to O(logm + logn) because after we ran that logm search for the target **row**,
then we know this is the row that we have to do our second binary search whcih will have `logn`.