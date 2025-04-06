from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. Recursive DFS
# T: O(n) - yeah n not h. Since we're going through every node in the tree
# M: O(h) - but this one is h. Since memory complex in a recursive approach is the maximum of function calls in the call stack:
#   - in a balanced tree(best case), h: log(n)
#   - in a skewed tree(worst case), h: n
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # depth of left subtree of the current node(root)
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # when we backtrack, we wanna return the max depth of current node to it's parent. So that at the end of the algom
        # we'll return the max depth of root of the tree.
        # NOTE: max depth of curr node, is the depth of itself(1) plus the max depth of it's left and right subtree.
        return 1 + max(left_depth, right_depth)


# 2. Iterative DFS (Stack)
# T: O(n)
# M: O(h)
#   - in a skewed tree: h is n
#   - in a balanced tree: h is log(n)
class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # You can get rid of this check if you set res to 0 initially. If res is 0 initially, yeah the while loop will be executed once,
        # but we won't go into the if block and therefore the res will stay 0 and we return 0 in that case.
        if not root:
            return 0

        stack = [[root, 1]]
        max_depth = 1

        while stack:
            node, depth = stack.pop()

            # yeah, in this approach it's possible that the node could be null, so we need to check for it
            if node:
                max_depth = max(max_depth, depth)

                # we're not checking that the node.left and node.right exist, so we might add null nodes to the stack, so we need to
                # check for it after popping, so we don't do anything with null nodes. So even if the node.left and node.right are null,
                # we're still adding them to the stack, but we check for this in the `if node` block above
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return max_depth


# 3. Breadth First Search (queue)
# T: O(n)
# M: O(n)
class Solution3:
    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        level = 0
        q = deque([root])

        while q:
            # Here, we're taking a snapshot of the length of the `q`. In other words, traverse the entire current level.
            # For first level, the length of q is 1, so this loop is gonna run once. For the second level, the q would have for example
            # 2 elements so len(q) would be 2, so this loop will run 2 times, so basically traversing the entire level and adding the
            # children of the second level. For the third level, it will run number of times equal to the number of elements of q which means
            # equal to the number of elements in the third level and ... .
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            level += 1

        return level
