from typing import List


# T: O(r * c)
# Note: The time is not O(4 ^ (r * c)) because each cell is only visited once. We're not counting number of paths from start to target
# or sth like that in this problem. We visit a cell, mark it as visited and we won't remove it from the `visit` set anymore, so
# each cell is only visited once.

# M: O(r * c)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # we could use a 2-d array as well
        visit = set()

        def dfs(r, c):
            # we reached out of bounds or we reached water. Note that out of bounds are also considered water.
            # In other words, we reached a perimeter of the island. So we return back to where we came, with 1.
            if (r < 0 or c < 0 or
                    r == ROWS or c == COLS or
                    grid[r][c] == 0):
                return 1

            if (r, c) in visit:
                return 0

            visit.add((r, c))

            # if neither of the two base cases above is true, it means we reached an island cell(we're not out of bounds yet),
            # so we need to go to all 4 directions of the current cell that we arrived.
            perim = dfs(r, c + 1)  # move to right
            perim += dfs(r + 1, c)  # down
            perim += dfs(r, c - 1)  # left
            perim += dfs(r - 1, c)  # up

            return perim

        # we need to find one cell that is a land and we're guaranteed to have at least one ground cell. To find it, iterate over
        # entire grid potentially.
        for r in range(ROWS):
            for c in range(COLS):
                # if we hit a land, start dfs from there.
                if grid[r][c]:
                    return dfs(r, c)
