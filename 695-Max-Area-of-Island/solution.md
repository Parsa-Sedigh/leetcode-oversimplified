We don't know which cells are zero and which ones are one until we look at every single individual cell of the grid,
we have to look at every single cell.

### Time & space
Since we're gonna be visiting each cell once, time complexity is the size of the grid. So: T: O(m * n).

The memory is also O(m * n) because we're having a hashset which in the worst case could contain every single cell and also DFS is
recursive so there's a callstack that we have to keep in memory as well but overall it's: M: O(m * n)