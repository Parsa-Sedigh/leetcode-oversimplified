from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. Breadth First Search
# T: O(n)
# M: O(n)
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root] if root else [])
        res = []

        while q:
            level = []

            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if len(res) % 2 == 1:
                # T: O(n)
                level.reverse()

            res.append(level)

        return res


# 2. Breadth First Search (Optimal)
# T: O(n)
# M: O(n)
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root] if root else [])
        res = []

        while q:
            level = [0] * len(q)
            for i in range(len(q)):
                node = q.popleft()
                level[i if len(res) % 2 == 0 else len(level) - 1 - i] = node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level)

        return res


# 3. Depth First Search
# T: O(n)
# M: O(H)
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node: Optional[TreeNode], level: int):
            if not node:
                return

            # prepare the cur level
            if level == len(res):
                res.append([])

            res[level].append(node.val)

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        for i in range(len(res)):
            if i % 2 == 1:
                res[i] = res[i].reverse()

        dfs(root, 0)

        return res


# 4. Iterative DFS
# T: O(n)
# M: O(n)
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Empty tree edge case
        if not root:
            return []

        # (node, level)
        stack = [(root, 0)]
        res = []

        while stack:
            node, level = stack.pop()

            # this condition checks if we get to a new level, therefore we should prepare it by appending a [].
            if level == len(res):
                res.append([])

            res[level].append(node.val)

            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))

        for i in range(len(res)):
            if i % 2 == 1:
                res[i].reverse()

        return res
