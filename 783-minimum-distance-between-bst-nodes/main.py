from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. Brute Force (DFS)
# T: O(n^2)
# M: O(H)
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # since we need to keep a global var as our ultimate result, we need to define a func for traversing the tree and
        # we can't just use the top minDiffInBST func to go through the tree, so we defined the dfs func.
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return float('inf')

            # the result is the minimum dist between these three:
            # 1. the cur node and other ones(min of cur with all other nodes)
            # 2. result of left subtree
            # 3. result of right subtree

            # Get min dist between cur node and all it's subtrees. Which means passing node to both params. Note that the dist
            # between node and itself is ignored.
            node_res = find_min_dist(node, node)

            left_res = dfs(node.left)
            right_res = dfs(node.right)

            subtree_res = min(left_res, right_res)

            return min(node_res, subtree_res)

        # finds the min distance between node1 & it's subtree nodes which are all represented as node2.
        def find_min_dist(node1: TreeNode, node2: Optional[TreeNode]) -> int:
            if not node2:
                return float('inf')

            # node1_res is the min dist between node1 itself and all it's subtree
            node1_res = float('inf')

            # This avoids computing a difference of zero when node1 and node2 are the same node, leading to min dist of 0 which
            # is wrong because we can't consider the same node twice.
            if node1 != node2:
                node1_res = abs(node1.val - node2.val)

            # left_res is the min dist between node1 and it's left subtree
            left_res = find_min_dist(node1, node2.left)

            # Find the minimum difference between node1 and any node in the right subtree of node2.
            right_res = find_min_dist(node1, node2.right)

            subtree_res = min(left_res, right_res)

            # the ultimate min dist of node1 and it's subtree is the min between these three:
            return min(node1_res, subtree_res)

        return dfs(root)


# 2. Brute Force (BFS)
# T: O(n * log(n))
# M: O(n)
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # In the worst case (e.g., a complete binary tree), the queue could hold up to n/2 nodes at the bottom level, which is O(n) space.
        q = deque([root])  # M: O(n/2)
        vals = []  # M: O(n)

        while q:
            node = q.popleft()
            vals.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        # T: O(n * log(n))
        vals = sorted(vals)
        min_diff = float('inf')

        # --- min val is definitely between two consecutive els. But which one? We don't know. We gotta go through the whole vals.
        # --- We can't just say that the min_diff is between vals[0] and vals[1], because there could be two nodes
        #     having BIG values(therefore appearing at the END of `vals`), but with the diff of 1 at the leaf level.
        for i in range(1, len(vals)):
            min_diff = min(min_diff, vals[i] - vals[i - 1])

        return min_diff
