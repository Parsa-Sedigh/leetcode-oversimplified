from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# T: O(n).
# We have to look into every single node in the tree.

# M: O(h).
# h is the height of the tree. If it's unbalanced tree which is the worst case, it's O(n), but if it's balanced,
# the height is gonna be log(n), so this is gonna be O(log(n))
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # The reason we defined a new func is we need to pass in one more param which the outer func doesn't have. Because we wanna
        # call this func recursively. If we only needed the params of outer func, we didn't need to define a new func.
        def dfs(node: Optional[TreeNode], curSum: int):
            # base case
            # We could be given an empty tree. If it was empty, based on the examples in the question, we have to
            # return False, even if the target sum was 0, we still have to return False, because technically any routes to leaf
            # node doesn't exist when tree is empty and targetSum is 0.
            if not node:
                return False

            curSum += node.val

            # maybe we found the result. But we have to make sure current node is a leaf node.
            if not node.left and not node.right:
                # Why we did this? Because we know here we're at a leaf node. So we have to return back up to the caller anyway.
                # So we return False or True.
                return curSum == targetSum

            # It's not a leaf node, so run dfs() on left and right subtrees
            # Note: We don't need to compensate anything in the second recursive call. Because we don't have any
            # global state that needs to be backtracked so that we can try another path.
            return (dfs(node.left, curSum) or
                    dfs(node.right, curSum))

        return dfs(root, 0)