from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my approach
# T: O(n)
# M: O(h)
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        nodes = []

        def preorder(root: TreeNode):
            if not root: return

            # Note: Do not put this when calling the preorder func, because append() doesn't return anything and you
            # would pass the result of append() to the next func call, which would be None and at that next func
            # call, the nodes would be None.
            # So this would result in runtime error: preorder(root.left, nodes.append(root.val))
            # (note: here we're assuming the preorder func takes 2 params)
            nodes.append(root.val)

            preorder(root.left)
            preorder(root.right)

        preorder(root)

        return nodes


# 2. Iterative Depth First Search
# T: O(n)
# M: O(h)
# In worst case(skewed tree): O(n)
# In balanced tree: O(log(n)) - since the stack stores nodes along the height of the tree and the height is log(n) in a balanced tree.
class Solution2:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur = root
        stack = []
        res = []

        while cur or stack:
            # Go left as far as possible
            while cur:
                stack.append(cur)
                res.append(cur.val)

                cur = cur.left

            # At this point, cur is None. So we need to look into our stack. Pop from it and set cur to cur.right, to traverse it's
            # right subtree.
            cur = stack.pop()
            cur = cur.right

        return res
