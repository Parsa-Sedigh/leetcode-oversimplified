from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. Recursion - I
class Solution:
    # T: O(h) - in balanced BST: O(log(n)). But in unbalanced BST, it becomes a LL -> O(n)
    # M: O(1)
    def minValueNode(self, root: Optional[TreeNode]):
        curr = root

        # Q: Why not: while curr: ??
        # A: Because we don't want to go out of bounds. So by the time while is done, cur is at the most left node.
        while curr.left:
            curr = curr.left

        return curr

    # T: O(2 * h)
    # M: O(h) - because of recursion stack
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:  # we found the node we wanna delete
            if not root.left:
                return root.right

            if not root.right:
                return root.left

            minNode = self.minValueNode(root.right)
            root.val = minNode.val
            root.right = self.deleteNode(root.right, minNode.val)

        return root


# 2. Recursion - II
# T: O(h)
# M: O(h)
class Solution2:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right

            if not root.right:
                return root.left

            cur = self.minValueNode(root.right)

            # since we wanna remove `root`, attach it's left subtree to cur. Since cur is in right subtree of root, it's also larger
            # than left subtree of root. So this won't mess up the BST order property.
            cur.left = root.left

            # At this point, the right subtree of root is restructured and has the left subtree of root as well. We just return
            # the right subtree to the parent of `root`, which makes it so that the root isn't in the ttree anymore, essentially deleted.
            return root.right

        return root

# 3. Iteration
# T: O(h)
# M: O(1)
# TODO
