from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. Depth First Search
# T: O(n)
# M: O(h) - if unbalanced which is the worst case -> O(n)
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        res = []

        def inorder(root: TreeNode):
            # base case
            if not root: return

            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)

        return res


# 2. Iterative Depth First Search
# 1. Visit the entire left subtree first.
# 2. Process the current node.
# 3. Visit the right subtree.

# T: O(n)
# M: O(h)
class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        # Stack to store nodes we need to process later. Mimicking how recursion would work under the hood
        stack = []
        cur = root

        # Loop until no more nodes left to process
        # This outer while
        while cur or stack:

            # This while loop is for visiting the left subtree. Go as far as you can to left:
            while cur:
                stack.append(cur)
                cur = cur.left

            # At this point, there's no more nodes on the left side. Pop the top node
            cur = stack.pop()
            res.append(cur.val)  # visit the node
            cur = cur.right

        return res


# 3. Morris Traversal
# T: O(n)
# M: O(1) - but if the output arr(res) is also counted -> O(n)
class Solution3:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        cur = root

        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right

                if not prev.right:
                    prev.right = cur
                    cur = cur.left
                else:
                    prev.right = None
                    res.append(cur.val)
                    cur = cur.right

        return res
