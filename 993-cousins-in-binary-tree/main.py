from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# T: O(n)
# M: O(n)
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # Don't need to check if tree is empty, since problem says there are at least 2 nodes.

        q = deque([root])

        while q:
            # check if cur level has both x and y. So we declare these vars for this level.
            found_x = False
            found_y = False

            for _ in range(len(q)):
                node = q.popleft()

                if node.val == x:
                    found_x = True
                elif node.val == y:
                    found_y = True

                # If node has children on both left and right, check if those children are x and y, if so, they are siblings, not cousins
                if node.left and node.right and (
                        (node.left.val == x and node.right.val == y) or
                        node.left.val == y and node.right.val == x
                ):
                    return False  # x and y are siblings, not cousins

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            # After processing the level, check if both x and y were found
            if found_x and found_y:
                return True  # x and y are at the same level with different parents

        # If we get to here, x and y are not at the same level
        return False
