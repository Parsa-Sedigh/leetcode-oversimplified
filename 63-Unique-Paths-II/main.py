from collections import deque
from typing import List


# Dynamic programming
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        row = []

        for i in range(COLS):
            row.append(1 if not obstacleGrid[len(obstacleGrid) - 1][i] == 0 else 0)

        for i in range(ROWS - 1):
            new_row = []

            for j in range(COLS):
                new_row.append(1 if obstacleGrid[j][i] == 0 else 0)

            print("NEW: ", new_row)

            for j in range(COLS - 2, -1, -1):
                new_row[j] = new_row[j + 1] + row[j]

            row = new_row

        return row[0]

# DFS
# Time limit exceeded
# T: O(2^(m+n))
# S: O(m * n) + O(m + n) => O(m * n)
# Note: The recursive call stack gets up to m + n calls. The memo dict gets up to m * n elements.
class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        paths = 0

        def dfs(row, col):
            # reached the target?
            if row == ROWS - 1 and col == COLS - 1 and obstacleGrid[row][col] == 0:
                nonlocal paths
                paths += 1

            # out of bounds?
            if (row >= ROWS or col >= COLS or
                    obstacleGrid[row][col] == 1):
                return

            # dfs on neighbors
            dfs(row + 1, col)
            dfs(row, col + 1)

        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0

        dfs(0, 0)

        return paths

# DFS with memoization
# T: O()
# S:
class Solution3:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        def dfs(row: int, col: int) -> int:
            # reached the target?
            if row == ROWS - 1 and col == COLS - 1 and obstacleGrid[row][col] == 0:
                return 1

            # out of bounds or hit an obstacle?
            if (row >= ROWS or col >= COLS or
                    obstacleGrid[row][col] == 1):
                return 0

            # If already computed this cell
            if (row, col) in memo:
                return memo[(row, col)]

            # dfs on right and down paths
            right_paths = dfs(row, col + 1)
            down_paths = dfs(row + 1, col)

            memo[(row, col)] = right_paths + down_paths

            return memo[(row, col)]

        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0

        memo = {}

        return dfs(0, 0)

# BFS
class Solution4:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0

        if obstacleGrid[0][0] == 1:
            return 0

        if obstacleGrid == [[0]]:
            return 1

        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        paths = 0
        visited = set()
        queue = deque()

        queue.append((0, 0))
        visited.add((0, 0))

        while queue:
            row, col = queue.popleft()
            neighbors = [[0, 1], [1, 0]]

            for dr, dc in neighbors:
                new_row = row + dr
                new_col = col + dc

                if new_row == ROWS - 1 and new_col == COLS - 1 and obstacleGrid[new_row][new_col] != 1:
                    paths += 1

                if (new_row >= ROWS or new_col >= COLS or
                        (new_row, new_col) in visited or
                        obstacleGrid[new_row][new_col] == 1):
                    continue



                queue.append((new_row, new_col))
                visited.add((new_row, new_col))

        return paths

# neetcode - top down DP
# T: O(m * n)
class Solution5:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Get the dimensions of the grid
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        # we could use a 2-dimensional grid as the cache as well.
        # Note: Instead of this initialization, we could add a base case in the dfs for when we reach the target, as well
        cache = {(ROWS - 1, COLS - 1): 1}

        def dfs(r, c):
            if r == ROWS or c == COLS or obstacleGrid[r][c]:
                return 0

            if (r, c) in cache:
                return cache[(r, c)]

            cache[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)

            return cache[(r, c)]

        return dfs(0, 0)

# neetcode - real DP(bottom-up)
# T: O(m * n)
# S: O(n)
class Solution6:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        cache = [0] * COLS
        cache[COLS - 1] = 1

        # go through each row but in reverse order
        for r in reversed(range(ROWS)):
            for c in reversed(range(COLS)):
                if obstacleGrid[r][c]:
                    cache[c] = 0
                elif c < COLS - 1:
                    # the new cache[c] is the sum of the previous cache[c] which indicates the bottom cell and the right cell
                    # which is cache[c + 1]. Now the cache[c] can't go out of bounds(accessing an out of bounds index), but the
                    # cache[c + 1] can. You can imagine the reason for this is that we have initialized the bottom row in
                    # the line: cache = [0] * COLS, so we already have that row, we can't go out of bounds. But this is not true
                    # for the right cells.

                    # If c + 1 is equal to COLS, we go out of bounds. So we need a check for this by saying: elif c < COLS - 1:
                    cache[c] = cache[c] + cache[c + 1]

                # note: The values at the far right, are always 1: dp[c] = dp[c] + 0. This means, the value at the far-right cell,
                # is equal to the value at the bottom cell plus the right cell, but the right cell is out of bounds, so 0.

        # by the time, the algo is done, the value at the top left has the ultimate result.
        return cache[0]