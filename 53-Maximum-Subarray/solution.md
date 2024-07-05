Brute-force:

### cubic solution O(n^3)
Compute every single sub-arr.

In this solution, we're re-computing the sum everytime we move forward.

![](./53-1.png)

### Quadratic solution
Just add the new element to the current some. This saves time.

### Linear solution
Do we have to compute every subarr(starting at every single el of the arr) and compute every single subarr that comes after it?

No.

The negative sums don't contribute to the result.

Kadanes algo is similar to sliding window. We keep incrementing the right pointer as we go through the arr but the left pointer
keeps getting shifted forward IF we ever have a negative prefix(sum). Otherwise, keep the left pointer where it is.