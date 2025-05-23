from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# T: O(n)
# M: O(n)
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_sum = []
        q = deque([root])

        # Phase 1: Construct sum of each level
        while q:
            cur_level_sum = 0

            for i in range(len(q)):
                node = q.popleft()
                cur_level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level_sum.append(cur_level_sum)

        # Phase 2: Replace the val of each child with: `level_sum - nodes.val - sibling's val`

        # children_sum is the sum of node's direct children vals
        q = deque([(root, root.val)])  # (node, <node's level children_sum>)
        level = 0

        while q:
            for i in range(len(q)):
                node, val = q.popleft()
                node.val = level_sum[level] - val

                # we do this when we're at the parent. Because from parent, we have access to the siblings. But we don't have
                # access to the sibling when we get to the children.
                children_sum = 0
                if node.left:
                    children_sum += node.left.val

                if node.right:
                    children_sum += node.right.val

                if node.left:
                    q.append((node.left, children_sum))

                if node.right:
                    q.append((node.right, children_sum))

        return root
