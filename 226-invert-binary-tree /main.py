from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. Breadth First Search
# T: O(n)
# M: O(n)
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # Check for edge case: root: []
        if not root:
            return None

        # NOTE: we're not emulating a call stack, so we shouldn't use a stack. We want to pop els in the order they were added,
        # so we need a queue not a stack.
        queue = deque([root])

        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return root


# 2. Depth First Search - preorder
# T: O(n)
# M: O(h)
# 	- in a balanced tree, height is log(n), so: O(log(n)).
#	- but in a skewed tree(resembling a linked list), height is n: O(n)
class Solution2:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # base case
        if not root:
            return None

        # swap the children
        root.left, root.right = root.right, root.left

        # recursively invert the subtrees

        # invert the left subtree
        self.invertTree(root.left)

        # invert the right subtree
        self.invertTree(root.right)

        return root


# 3. Iterative DFS
# T: O(n)
# M: O(h)
class Solution3:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        # since it's DFS, we need to go as deep as possible. So we need a stack
        stack = [root]

        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return root
