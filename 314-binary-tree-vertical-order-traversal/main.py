from collections import deque, defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. Breadth First Search + Sorting
# T: O(n * log(n))
# M: O(n)
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([(root, 0)])
        cols = defaultdict(list)

        # T: O(H)
        while queue:
            node, col = queue.popleft()

            if node:
                queue.append((node.left, col - 1))
                queue.append((node.right, col + 1))
                cols[col].append(node.val)

        # We wanna go through the cols dict in increasing order.
        # sorted(cols) gives the keys of cols dict in a sorted list.

        # NOTE: For example if cols: {0: [1, 5, 6], -1: [2], 1: [3], -2: [4], 2: [7]}
        # Then sorted(cols): [-2, -1, 0, 1, 2]
        # Then we just index it using: cols[i]

        # T: O(n * log(n)) because of sorting.
        return [cols[i] for i in sorted(cols)]


# 2. Depth First Search + Sorting
# T: O(n * log(n))
# M: O(n)
class Solution2:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = defaultdict(list)

        # In DFS, since we go as deep as we can, it has a contradiction with the problem's expectation which wants the result
        # from top to bottom. So we need to keep track of every node's level(row) and then sort them to have the top ones appear first.
        def dfs(root: Optional[TreeNode], col: int, level: int):
            if not root:
                return

            cols[col].append((level, root.val))
            dfs(root.left, col - 1, level + 1)
            dfs(root.right, col + 1, level + 1)

        dfs(root, 0, 0)

        res = []

        # First sort the cols, so that we start from left to right
        for col_idx in sorted(cols):

            # Then sort by the level, so that the result would be from top to bottom(this step is only required in DFS).
            col_vals = sorted(cols[col_idx], key=lambda x: x[0])
            res_vals = []

            for lvl, val in col_vals:
                res_vals.append(val)

            res.append(res_vals)

        return res


# 3. Breadth First Search (Optimal)
# T: O(n)
# M: O(n)
class Solution3:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([(root, 0)])
        cols = defaultdict(list)

        # Instead of sorting the cols to get it's indices in correct order, track the min and max col numbers that we saw when we run
        # the bfs. Then by using range() on min_col and max_col, we get the indices in correct order. So no need to use sorted at all.
        # This would make this solution more efficient.
        min_col, max_col = 0, 0

        while queue:
            node, col = queue.popleft()

            cols[col].append(node.val)
            min_col = min(min_col, col)
            max_col = max(max_col, col)

            if node.left:
                queue.append((node.left, col - 1))

            if node.right:
                queue.append((node.right, col + 1))

        return [cols[i] for i in range(min_col, max_col + 1)]


# 4. Depth First Search (Optimal)
# T: O(w * H * log(H))
# M: O(n)

# n: number of nodes
# h: height of the tree(i.e. maximum number of nodes in any vertical line of the tree)
# w: width of the tree (i.e. maximum number of nodes in any of the levels of the tree)
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        cols = defaultdict(list)
        min_col, max_col = 0, 0

        def dfs(root: Optional[TreeNode], col: int, level: int):
            if not root:
                return

            nonlocal min_col
            nonlocal max_col

            min_col = min(min_col, col)
            max_col = max(max_col, col)
            cols[col].append((level, root.val))
            dfs(root.left, col - 1, level + 1)
            dfs(root.right, col + 1, level + 1)

        dfs(root, 0, 0)

        res = []

        # How many times this for loop is gonna run? Well it depends on the width of the tree. Because the number of cols depends
        # on the WIDTH of the tree.
        # NOTE: Now at each iteration of loop, we're doing a `h * log(h)` op. So the total time of this for loop is: w * (H * log(H))
        for col in range(min_col, max_col + 1):
            # T: O(H * log(H)) - since we're sorting a column and the maximum number of nodes at a col is H
            col_vals = sorted(cols[col], key=lambda x: x[0])

            # T: O(H)
            # NOTE:
            res.append([val for _, val in col_vals])

        return res
