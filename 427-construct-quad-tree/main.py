from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


# 1. Recursion
# T: O(log(n) * n^2)
# M: O(log(n)) - because of recursion stack is the height of decision tree and height is log(n)
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        # The dfs func processes an n x n subgrid starting at position
        # n: dimensions of cur portion of the grid that we're running dfs on,
        # r, c: top-left coordinates of cur quadrant
        def dfs(n: int, r: int, c: int):
            all_same = True

            # BASE CASE: all the vals of cur quadrant are the same
            # go over entire cur quadrant or subgrid(which has n * n dimension)
            # NOTE: We don't need to cover the base case where n = 1. Because it's covered by this loop as well.
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c + j]:
                        all_same = False

                        break

            # all the vals of cur quadrant are the same, so construct the leaf node for this quadrant with the val(doesn't matter
            # we use which cell val, we chose to use the top-left cell val)
            if all_same:
                # since this is a leaf node, so it doesn't have any children, so we don't need to set anything as it's 4 pointers to children.
                return Node(grid[r][c], True)

            n = n // 2

            # recursively run dfs for each of the 4 quadrants of cur quadrant
            top_left = dfs(n, r, c)

            # (r, c+n) is the coordinate of top-left cell of right quadrant
            top_right = dfs(n, r, c + n)
            bottom_left = dfs(n, r + n, c)
            bottom_right = dfs(n, r + n, c + n)

            # Create a node for the cur coordinates that we're at. We know this node is not a leaf node, so the val we give to it,
            # doesn't matter.
            return Node(0, False, top_left, top_right, bottom_left, bottom_right)

        return dfs(len(grid), 0, 0)


# T: O(n^2)
# NOTE: The time is not O(4^n). If we had 4 branches and went n levels deep, we’d get 4^n, but the recursion depth is log(n), not n.
# The time complexity is O(n²) because the recursion forms a tree with n² leaves (one per grid cell),
# and the total number of nodes (calls) is also O(n²), each doing constant work. The “4 recursions” multiply the calls per level,
# but the logarithmic depth keeps it quadratic(n^2), not quartic(n^4).

# M: O(log(n))
# The depth of this recursion depends on how many times we can halve n until reaching 1, which is log(n).
# IT'S PURE log(n) NOT H.
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n: int, r: int, c: int):
            # BASE CASE: If n == 1, the subgrid is a single cell.
            if n == 1:
                # Return a leaf node
                return Node(grid[r][c], True)

            n = n // 2

            # Construct nodes for each quadrant:
            top_left = dfs(n, r, c)
            top_right = dfs(n, r, c + n)
            bottom_left = dfs(n, r + n, c)
            bottom_right = dfs(n, r + n, c + n)

            if (
                    top_left.isLeaf and top_right.isLeaf and
                    bottom_left.isLeaf and bottom_right.isLeaf and
                    top_left.val == top_right.val == bottom_left.val == bottom_right.val
            ):
                return Node(top_left.val, True)

            # Return an internal node
            return Node(0, False, top_left, top_right, bottom_left, bottom_right)

        return dfs(len(grid), 0, 0)
