from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # First edge case: If we have an empty tree, create a new tree node and return it. This is also the base case if the
        # tree is not empty.
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)

        return root

# Iterative
class Solution2:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # First edge case: If we have an empty tree, create a new tree node and return it. This is also the base case if the
        # tree is not empty.
        if not root:
            return TreeNode(val)

        cur = root

        while True:
            if val < cur.val:
                if not cur.left:
                    cur.left = TreeNode(val)

                    return root

                cur = cur.left
            else:
                if not cur.right:
                    cur.right = TreeNode(val)

                    return root

                cur = cur.right