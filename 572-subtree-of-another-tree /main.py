from typing_extensions import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# T: O(S * T)
# M: O(S + T)

# S: num of nodes in s and T: num of nodes in t
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # NOTE: this function is gonna be recursive, so let's start with the base cases
        # NOTE: if t is empty, then OFC it's gonna be the subtree of the s, regardless of whether s is empty or not. This is because
        # we traversed t to the end. So it was found in s completely. This also cover the edge case of t being None, then we
        # have to return True.
        # Note: The order of these if statements is very important.
        if not t: return True

        # we could write: `if not s and t:`, but it's not necessary because we checked that previously by saying: if t is empty, return.
        # So if t is empty, we won't get here at all.
        if not s: return False

        # at this point, we know both of the trees are not empty, so let's compare both trees
        # NOTE: At each step in recursion, we have to check if
        if self.is_same_tree(s, t):
            return True

        # if they're not the same tree, but remember, we can compare t to the subtrees of s(left and right subtrees)
        # if t was subtree of either of the left or right subtrees of s, we can return true
        return (self.isSubtree(s.left, t) or
                self.isSubtree(s.right, t))

    # there are 3 conditions in this function:
    # - if both trees are empty
    # - if both trees are not empty
    # - if one of the trees is empty
    def is_same_tree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        # base case 1
        if not s and not t:
            return True

        # base case 2
        if (s and not t) or (not s and t):
            return False

        if s.val != t.val:
            return False

        # at each node, both s and t should be equal. So do the recursion on left and right subtrees:
        return self.is_same_tree(s.left, t.left) and self.is_same_tree(s.right, t.right)
