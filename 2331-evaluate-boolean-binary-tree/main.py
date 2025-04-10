from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# T: O(n)
# M: O(H)
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # Note: tree is a full binary tree.
        # this is not needed, since according to desc, there's at least 1 node in the given tree:
        # if not root:
        #     return

        if not root.left and not root.right:
            return root.val == 1

        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)

        if root.val == 2:
            return left or right

        return left and right
