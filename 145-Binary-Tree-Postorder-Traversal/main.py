from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. Depth First Search
# T: O(n)
# M: O(h)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        nodes = []

        def postorder(root: TreeNode):
            if not root: return

            postorder(root.left)
            postorder(root.right)
            nodes.append(root.val)

        postorder(root)

        return nodes


# T: O(n)
# M: O(h)
# 2. Iterative Depth First Search - I
class Solution2:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Stack to hold nodes to process
        stack = [root]

        # A parallel list of True/False flags that tracks whether a node’s subtrees have been visited.
        visit = [False]
        res = []

        while stack:
            cur, v = stack.pop(), visit.pop()

            if cur:
                if v:
                    res.append(cur.val)
                else:
                    stack.append(cur)
                    visit.append(True)

                    # first push right child and THEN the left child. So that the left child will be popped first later, which is
                    # what we want. We wanna traverse the left subtree before right subtree.
                    stack.append(cur.right)
                    visit.append(False)

                    stack.append(cur.left)
                    visit.append(False)

        return res


# T: O(n)
# M: O(h)
# 3. Iterative Depth First Search - II
class Solution3:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root

        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right

            # At this point, we've traverse the right subtree of `cur`. So we need to traverse it's left subtree, so in the next line,
            # set cur to cur.left.
            # NOTE: yeah first right then left, because we're gonna reverse the result before ending the algo.
            cur = stack.pop()
            cur = cur.left

        res.reverse()

        return res

# 4. Morris Traversal
# T: O(n)
# M: if we don't consider output arr as extra memory -> O(1). Otherwise: O(n)
# TODO
