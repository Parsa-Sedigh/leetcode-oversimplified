The constructed quad tree is shown with same colors as the grid sections in img below:
![](./427-1.png)

The green section of grid has the same val for all it's cells. So it's a leaf node and we don't continue breaking it down further.

We represent each quadrant with it's top-left cell coordinates.

### Time & Space
In worst case, we're gonna keep breaking the grid into quadrants recursively. The first grid dimensions are n.
Then we get to n / 2, then n / 4 ... until n = 1. The height of this is log(n). But at each level in decision tree, we're iterating
over the entire grid => n^2. At each level, the quadrants get smaller but we still have to check them all in worst case.

- number of levels in tree: log(n)
- in each level, we do n^2 op

So T: O(log((n) * n^2)
