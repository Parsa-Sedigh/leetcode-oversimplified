Take the sum of the left and right of the el(the el itself is not in the sum of the left and right), if they are equal,
it's a pivot index.

## Brute force
In worst case, this solution is O(n^2) because we're gonna compute sum for each el.

## better approach
In brute force, we have some repeated work. For left side sum, as we move forward, we calculate what was already been calculated with a new el.
So this is the repeated work. So if we maintain a variable for that, we don't have to re-calculate it again.

Q: What about repeated work in right side?

We know the total sum of the arr is constant. It's not gonna change. Since we're not changing any values in the arr.

The right sum is `total sum of arr - left sum - curr el`. So we can compute right sum in O(1).