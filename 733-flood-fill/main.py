from collections import deque
from typing import List


# DFS
# T: O(r * c)
# M: O(r * c)
# The memory complexity is because of the visit hashset which in worst case of all cells being lands, is r * c land cells.
# So the visit hashset could have up to r * c els.
# The recursive callstack also contributes to the memory complexity. Since you're using DFS, the recursive stack depth
# could go up to the size of the largest connected component of land cells. In the worst case (if all cells are connected land cells),
# the stack depth could be O(m×n). So (r * c) + (r * c) => O(r * c)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        visit = set()
        original_color = image[sr][sc]

        def dfs(r, c):
            if (min(r, c) < 0 or
                    r == ROWS or c == COLS or
                    (r, c) in visit or
                    image[r][c] != original_color):
                return

            visit.add((r, c))
            image[r][c] = color

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            return image

        return dfs(sr, sc)


# DFS without visit hashset
# T: O(r * c)
# M: O(r * c)
class Solution2:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        original_color = image[sr][sc]

        def dfs(r, c):
            # if the cell is already the `color`, we shouldn't visit it. It means we've already visited it. So we put this condition
            # as well: image[r][c] == color
            if (min(r, c) < 0 or
                    r == ROWS or c == COLS or
                    image[r][c] == color or
                    image[r][c] != original_color):
                # we might not get to the actual logic of this func at all and the first call to dfs() might get into this if block,
                # we also need to `return image` here.
                return image

            image[r][c] = color

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            return image

        return dfs(sr, sc)


# BFS
# T: O(r * c)
# M: O(r * c)
class Solution3:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        original_color = image[sr][sc]

        image[sr][sc] = color

        def bfs():
            queue = deque()
            visit = set()
            queue.append((sr, sc))
            visit.add((sr, sc))

            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()
                    neighbors = [[1, 0], [0, 1], [-1, 0], [0, -1]]

                    for dr, dc in neighbors:
                        new_r, new_c = r + dr, c + dc

                        if (min(new_r, new_c) < 0 or
                                new_r == ROWS or new_c == COLS or
                                (new_r, new_c) in visit or image[new_r][new_c] != original_color):
                            continue

                        image[new_r][new_c] = color
                        queue.append((new_r, new_c))
                        visit.add((new_r, new_c))

        bfs()

        return image
