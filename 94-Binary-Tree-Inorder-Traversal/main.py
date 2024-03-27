from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

# iterative
# T: O(n)
# M: O(n)
class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
                
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right

        return res