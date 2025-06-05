from typing_extensions import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# T: O(S * T)
# M: O(S + T)

# S: num of nodes in s and T: num of nodes in t

###

# m: number of nodes in `s` tree
# H_s: height of the `s` tree

# T: O(m * n)
# Number of nodes visited in s: m.
# Work per node: O(n) due to the is_same_tree call.
# So total time is: O(m * n)

# M: O(H_s + H_t)

# overall memory: In worst case, we traverse a lot of s(would be O(H_s)) and then go through is_same_tree() func which would be
# O(min(H_s, H_t)).
# In other words: The total recursion depth occurs when isSubtree is at its deepest level (depth h_s), and from there,
# it calls is_same_tree, which adds up to h_t.
# Thus, the total depth can be O(h_s + h_t) in the worst case.

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

    # T: O(n)
    # Technically it's O(min(m, n)), but since we're checking if t is subtree of s, at most, it processes up to the number of nodes in t.
    # So we say it's O(n)

    # M: O(min(H_s, H_t))

    # - If we were only considering this func itself: O(min(H_s, H_t)). Why not O(H_s + H_t)? Because we're traversing both
    #   trees simultaneously. Now you might say: Well since we're traversing both at the same time, the call stack is having
    #   calls from both s & t, so the memory is: O(H_s + H_t).
    #   BUT note that this func stops when the smaller tree is traversed. So all the nodes of the other tree won't contribute to the
    #   memory complexity. So it's still min(H_s, H_t)

    # there are 3 conditions in this function:
    # - if both trees are empty
    # - if one of the trees is empty
    # - if both trees are not empty
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
