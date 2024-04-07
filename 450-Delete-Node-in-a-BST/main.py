from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minValueNode(self, root: Optional[TreeNode]):
        curr = root

        # Q: Why not: while curr: ??
        # A: Because we don't want to go out of bounds. So by the time while is done, cur is at the most left node.
        while curr.left:
            curr = curr.left

        return curr

    # T: O(2 * h)
    # M: O()
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else: # we found the node we wanna delete
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = self.minValueNode(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)

        return root