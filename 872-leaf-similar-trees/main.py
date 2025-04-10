from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. Depth First Search
# T: O(n1 + n2)
# Note: The comparison at the end takes O(min(n1, n2)) because if they don't match, it stops. So the time taken is number of nodes
# in the smaller tree.
# But the "traversal of both tress" dominates which takes O(n1 + n2).

# M: O(n1 + n2)
# the recursion stacks take O(max(H1, H2)). But we're storing the list of leaf vals as well and it dominates the recursion stacks.
# The memory complexity of lists is: O(n1 + n2), because at the leaf level of binary trees at the worst case(full binary tree),
# we have n/2 nodes. So: n1/2 + n2/2 => O(n1 + n2).
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode], leafs: List[int]):
            if not root:
                return

            if not root.left and not root.right:
                leafs.append(root.val)

                return

            dfs(root.left, leafs)
            dfs(root.right, leafs)

        leafs1, leafs2 = [], []
        dfs(root1, leafs1)
        dfs(root2, leafs2)

        # T: O(min(n1, n2)) where n is number of nodes
        return leafs1 == leafs2


class Solution2:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        pass


# 3. Iterative DFS
# T: O(n1 + n2)
# The function processes both trees fully, leading to a time complexity of O(n1 + n2),
# where n1 and n2 are the number of nodes in root1 and root2, respectively.

# M: O(H1 + H2)
#   - best case: O(log(n1) + log(n2))
#   - worst case: O(n1 + n2)
# Each stack stores nodes along a path from the root to a leaf
# The maximum number of nodes in a stack is the height of the tree(H)
class Solution3:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaf(stack: List[TreeNode]):
            while stack:
                node = stack.pop()

                if node.right:
                    stack.append(node.right)

                if node.left:
                    stack.append(node.left)

                if not node.left and not node.right:
                    return node.val

        stack1, stack2 = [root1], [root2]

        while stack1 and stack2:
            if get_leaf(stack1) != get_leaf(stack2):
                return False

        return not stack1 and not stack2
