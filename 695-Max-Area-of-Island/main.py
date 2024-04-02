from collections import deque
from typing import List

# DFS
# T: O(m * n)
# M: O(m * n)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # We don't actually need an external visit hashset, we can just use the grid itself to determine if we visited a cell or not.
        # But we're not guaranteed that we can write over the input grid. You can clarify this with interviewer.
        visit = set()
        maxArea = 0

        def dfs(r, c):
            # base case
            if (min(r, c) < 0 or
                    r == ROWS or c == COLS or
                    (r, c) in visit or
                    grid[r][c] == 0):
                return 0

            visit.add((r, c))

            #####
            # The area for current cell is 1. We have to sum it with other cells in the current island.
            area = 1
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)

            # OR:
            # return 1 + (dfs(r + 1, c) +
            #             dfs(r - 1, c) +
            #             dfs(r, c + 1) +
            #             dfs(r, c - 1))
            #####

            return area

        for r in range(ROWS):
            for c in range(COLS):
                area = dfs(r, c)
                maxArea = max(maxArea, area)

        return maxArea

# BFS
class Solution2:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxArea = 0

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))
            area = 1

            while q:
                # Note: We could be going over all of the elements in the current q in one iteration of the while loop, but
                # it doesn't matter, because eventually we will go over all of them. If this question had said: get the
                # minimum time or minimum or ..., we had to go all of the elements of the q(snapshot manner) in one iteration of while loop.
                # In other words, we had to do multi-source BFS, by having another loop inside the while loop by saying:
                # `for i in range(len(q)):`

                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == 1 and
                        (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))
                        area += 1

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = bfs(r, c)
                    maxArea = max(maxArea, area)


        return maxArea