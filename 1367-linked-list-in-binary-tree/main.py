from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# T: O(n * m)
# n: number of nodes in the binary tree.
# m: number of nodes in the linked list.
# Because we go through every node of the tree(by traversing both it's subtrees), and for each node, in worst case we traverse the
# most of the LL.

# M: O(H)
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def is_downward_path(list_node, tree_node) -> bool:
            # we reached the end of the LL, so we saw all the vals we wanted
            if not list_node:
                return True

            # if we get here, it means we haven't reached the end of the LL. Now if we reached the end of the tree, we didn't find
            # all the LL vals in the cur tree path, so return False.
            # OR if the cur vals are not equal.
            # NOTE: The not tree_node cond should be first because otherwise, it could be None and the second cond would throw an err.
            if not tree_node or list_node.val != tree_node.val:
                return False

            # NOTE: If the first recursion branch returns True, it won't go to the right subtree at all.
            return (
                    is_downward_path(list_node.next, tree_node.left) or
                    is_downward_path(list_node.next, tree_node.right)
            )

        # checks the root of the cur tree represented by `root`
        if is_downward_path(head, root):
            return True

        # We will check the left & right subtrees of cur root in the next lines, but first we need to check if we went out of bounds or not:
        if not root:
            return False

        # So for every node in the tree: First check if starting from itself, resembles the LL? This is done by calling the prev `if` block.
        # If node can't resemble the LL starting from itself, check it's left & right subtrees.
        return (
                self.isSubPath(head, root.left) or
                self.isSubPath(head, root.right)
        )
