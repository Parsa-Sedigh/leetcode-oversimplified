from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. Breadth First Search
# T: O(n)
# M: O(n)
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # NOTE: We're guaranteed that tree has at least one node. So we don't need to first check for the edge case of tree being empty.
        #       We can initialize the q with the root node without any worries.
        q = deque([root])

        while q:
            node = q.popleft()

            if node:
                q.append(node.left)
                q.append(node.right)
            else:
                while q:
                    if q.popleft():
                        return False

        return True


# 2. Breadth First Search (Optimal)
# Once we see a None node, any non-None node after it means a gap exists.

# T: O(n)
# M: O(n)
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        null_seen = False

        while q:
            node = q.popleft()

            # NOTE: We're traversing level-by-level. So when we add the children of a leaf node(which are None), they will be
            #       processed when we get to next level of leaf level, which means before getting to them, we've traversed the whole tree.
            #       And if tree was complete, we're gonna have a lot of NULLs at the end of `q`, but that won't cause any problems,
            #       because there won't be any node with actual value in between those NULLs. Our q would look like this: 1, 3, 4, 5, None, None, None ... .
            if node:
                if null_seen:
                    return False

                q.append(node.left)  # could be None
                q.append(node.right)  # could be None
            else:
                # If the node is None, mark that we've seen a None
                null_seen = True

        return True


# 3. Depth First Search (Two Pass)
# T: O(n)
# M: O(H)
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # First calculate the total number of nodes in the tree
        def count_nodes(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            # Return 1 (for the current node) plus the number of nodes in the left subtree and the right subtree.
            return 1 + count_nodes(node.left) + count_nodes(node.right)

        num_of_nodes = count_nodes(root)

        # Assign an index to each node based on its position in a <hypothetical> complete binary tree.
        # The indexing follows the heap-like numbering system:
        # For a node at index i:
        # - It's left child is at index 2 * i + 1.
        # - It's right child is at index 2 * i + 2.
        def dfs(node: Optional[TreeNode], index: int) -> bool:
            # An empty subtree is trivially complete
            if not node:
                return True

            # In a complete binary tree with n nodes, all nodes must have indices from 0 to n-1.
            # If a node exists at an index >= n, it violates the completeness property.
            # For example, if tree has 3 nodes(n=3), their indices should be 0 to 2. If there is a node with i = 3, the tree is not complete.
            if index >= num_of_nodes:
                return False

            is_left_complete = dfs(node.left, 2 * index + 1)
            is_right_complete = dfs(node.right, 2 * index + 2)

            # for each node, it's subtree is complete if it's left & right subtrees are both complete:
            return is_left_complete and is_right_complete

        return dfs(root, 0)


# 4. Depth First Search (Optimal)
# T: O(n)
# M: O(H)
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # node depth: num of edges from root to that node.
        # node height: num of edges from that node down to a leaf node in its subtree.
        # For example, if a tree has 3 levels, the depth of a leaf node is 2(assuming there was a path from root to that node).
        # Because there are 2 edges from root to that node.

        # Height of the tree, set by the first None encountered.
        # NOTE: At the end of the algo, the val of this, is actually considering the height of out of bounds level as well.
        tree_height = 0
        null_seen = False

        def dfs(node: Optional[TreeNode], node_height: int) -> bool:
            nonlocal tree_height, null_seen

            if not node:
                # If tree_height == 0: This is the first None node encountered. Set tree_height = hgt, establishing the tree’s height
                # based on the leftmost path to a null node.
                # NOTE: Remember that at the beginning, root of the tree has height of 0. Because we haven't
                # NOTE: When does this if block run?
                #       Happens ONLY ONCE in the whole algo. When traverse the left-most path and then go out of bounds.
                # NOTE: Here, we set tree_height based on the first None encountered
                # AFTER LAST LEVEL:
                if tree_height == 0:
                    tree_height = node_height

                # ON LAST LEVEL:
                # If this cond is true, it means we're at the last level.
                elif node_height == tree_height - 1:
                    # Gap before the last level: invalid
                    null_seen = True

                # BEFORE last level:
                # No Gaps should exist before Last Level: If a None node appears at a height less than tree_height, return False
                elif node_height != tree_height:
                    return False

                return True

            # If we've seen a hole at this level and now found a non-None node, tree is not complete:
            if node_height == tree_height - 1 and null_seen:
                return False

            left_complete = dfs(node.left, node_height + 1)
            right_complete = dfs(node.right, node_height + 1)

            return left_complete and right_complete

        return dfs(root, 0)
