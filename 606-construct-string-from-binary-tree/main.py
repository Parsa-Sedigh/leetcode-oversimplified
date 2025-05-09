from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. Depth First Search
# T: O(n * H)
# We go through all nodes -> n
# Now, at each step, there's a string creation op. Since in py, strings are immutable, each concatenation creates a new string,
# and the characters from the subtrees may be copied multiple times as we ascend the recursion tree.
# Now the size of the str that is created, depends on the tree being balanced or skewed.
# If tree is balanced(meaning max depth is log(n)), the size of the str is about log(n).
# But if the tree is unbalanced, max depth is n, so size of the str at the root would be n.
# Hence, the `H`.

# M: O(n)
# Because:
# - Recursion stack: O(H)
# - String length: O(n). Because at the end of the algo, when all recursions are done on both left & right subtrees of the root,
# the str contains ALL node vals + 4 parentheses in the worst case for each node(except leaf). So this would be O(n).
# Now: O(H) + O(n) => O(n)
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        left = self.tree2str(root.left)
        right = self.tree2str(root.right)

        if left and right:
            return f"{root.val}({left})({right})"

        if left:
            return f"{root.val}({left})"

        if not left and right:
            return f"{root.val}()({right})"

        return str(root.val)


# 2. Depth First Search (Optimal)
# T: O(n)
# M: O(n)
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []

        # T: O(n)
        # visits each of the n nodes in the tree exactly once and does a O(1) per node => T: O(n)

        # M: O(H)
        def dfs(root):
            if not root:
                return

            res.append("(")
            res.append(str(root.val))

            dfs(root.left)

            # this block can be written before visiting left subtree as well.
            if not root.left and root.right:
                res.append("()")

            dfs(root.right)
            res.append(")")

        dfs(root)

        # T: O(n)
        # Joining a list of strings takes time proportional to the total length of the resulting string, which is O(n).

        # M: O(n) - if output str is considered
        return "".join(res)[1:-1]


# 3. Iterative DFS
# T: O(n)
# M: O(n)
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # A pointer starting at the root, used to traverse the tree.
        cur = root

        # A stack to keep track of nodes we’ve visited but haven’t fully processed yet (similar to a call stack in recursion).
        stack = []

        # A list to build the string incrementally. Using a list is efficient because concatenating strings repeatedly in Python
        # can be costly due to string immutability. We’ll join the elements into a single string at the end.
        res = []

        # A pointer to the most recently completed node (i.e., a node whose subtrees have been fully processed).
        # This helps us decide when to move up the tree.
        last_visited = None

        # This loop runs as long as there’s a current node to process (cur) or nodes remaining in the stack.
        # It mimics a preorder traversal with two phases: going down the left side and backtracking to handle right subtrees.
        while cur or stack:
            # PHASE 1: Processing a Node (if cur:)
            # When `cur` is not None, we’re visiting a new node:
            if cur:
                # We append the node’s value prefixed with an opening parenthesis, e.g., (1 for a node with value 1.
                # This marks the start of the node’s representation.
                res.append(f"({cur.val}")

                # If the node has no left child but has a right child, we append "()" to indicate the absent left subtree.
                # This ensures the string format matches the requirement (e.g., 1()(3)).
                if not cur.left and cur.right:
                    res.append("()")

                # The current node is added to the stack so we can return to it later to process its right subtree.
                stack.append(cur)

                # Move the cur pointer to the left child to continue the preorder traversal.
                cur = cur.left

            # PHASE 2: Backtracking (else:)
            else:
                # Look at the top node on the stack without removing it. This is the parent node we’re currently processing.
                top = stack[-1]

                # Check Right Subtree: If the top node has a right child and we haven’t processed it yet (i.e., last_visited isn’t the right child),
                # move cur to the right child (cur = top.right) to start processing that subtree.
                if top.right and last_visited != top.right:
                    cur = top.right

                # Otherwise, this node and it's whole subtree is done(since if there’s no right child or the right child has already been visited,
                # this node is done):
                else:
                    # Remove the top node from the stack since its subtrees are fully processed.
                    stack.pop()

                    # Append a closing parenthesis to complete the node’s representation in the string.
                    res.append(")")

                    # Set last_visited to the popped node, marking it as fully processed.
                    last_visited = top

        return "".join(res)[1:-1]
