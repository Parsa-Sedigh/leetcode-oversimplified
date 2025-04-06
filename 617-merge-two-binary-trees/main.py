from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. Depth First Search (Creating New Tree)
# T: O(m + n)
# M: O(max(H1, H2))
#   - in worst case which is when we have two skewed trees, one left skewed and another right skewed: O(max(m, n))
#   - in best case which is when we have two balanced trees: O(max(log(m), log(n)))
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2

        if not root2:
            return root1

        root = TreeNode(root1.val + root2.val)
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)

        return root


# 2. Depth First Search (In Place)
# T: O(min(m, n))
# M: O()
class Solution2:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # if there's no root1, all the nodes in current root2 branch are added to root1. So return root2
        if not root1:
            return root2

        # there's no root2 in this branch, so root1 won't get modified, we can safely return root1 as it is
        if not root2:
            return root1

        root1.val += root2.val

        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1


# 3. Iterative DFS (Creating New Tree)
# T: O()
# M: O()
# TODO

# 4. Iterative DFS (In Place)
# T: O(min(m, n))
# M: O()
# Where m and n are the number of nodes in the given trees.
class Solution4:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2

        if not root2:
            return root1

        stack = [(root1, root2)]

        while stack:
            node1, node2 = stack.pop()

            if not node1 or not node2:
                continue

            # at this point, node2 certainly exist.
            node1.val += node2.val

            if node1.left and node2.left:
                stack.append((node1.left, node2.left))
            elif not node1.left:
                node1.left = node2.left

            if node1.right and node2.right:
                stack.append((node1.right, node2.left))
            elif not node1.right:
                node1.right = node2.right

        return root1
