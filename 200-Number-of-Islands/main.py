from collections import deque
from typing import List


# BFS
# T: O(rows * cols)

# In the worst case, each cell of the grid may need to be visited once.
# For each cell visited, the function performs a constant number of operations to check its neighbors and update the visited set.
# Therefore, the time complexity is O(rows * cols), where rows is the number of rows in the grid and cols is the number of columns in the grid.

# M: O(rows * cols)

# The size of the visited set can grow up to the size of the grid in the worst case if all cells are visited.
# Therefore, the space complexity is O(rows * cols) in the worst case.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # If we're given an empty grid, we don't want to run our algo at all. There aren't any islands in that case.
        if not grid: return 0

        # Get the dimensions of the grid(rows and cols)
        rows, cols = len(grid), len(grid[0])
        visited = set() # We could use a 2-d grid as our visited as well
        islands = 0

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            # while queue is not empty, we're gonna be expanding our island(if we have a 1 and other conditions are true)
            while q:
                row, col = q.popleft()

                # We want to check the adjacent positions of the (row, col) position that we just popped. There are 4 directions that we can go
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    # Note: The name of these new variables here should be different than so that we don't mutate the row and col.
                    # Why? Because otherwise, you're gonna mutate row and col and next iterations of this for loop will work with wrong
                    # values of the popped node. So use new variable names here and do not overwrite `row` and `col`. We used r and c here.
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visited):
                        # add this position to queue as well because we have to BFS on it as well.
                        q.append((r, c))
                        visited.add((r, c))


        # We want to visit every single position in the grid
        for r in range(rows):
            for c in range(cols):
                # If we visit a 0, we don't have to do anything, but if we visit a 1, we have to traverse it and mark it as visited(it's done
                # in the bfs() function)
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands

# DFS
# T: O(rows * cols)

# In the worst case, each cell of the grid may need to be visited once.

# M: O(rows * cols)
class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or
                    r == ROWS or c == COLS or
                    (r, c) in visited or grid[r][c] == "0"):
                return

            visited.add((r, c))

            ##########
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r , c - 1)

            visited.remove((r, c))

            # OR:
            # directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            # for dr, dc in directions:
            #     dfs(r + dr, c + dc)
            ##########

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1

        return islands