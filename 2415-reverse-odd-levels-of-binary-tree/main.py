# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# T: O(n)

# Why O(n) and not O(n^2)?
# First of all, the outer `while q` doesn't say anything about the time complexity, in contrast to a for loop like for i in range(len(n)).
# So we can't say anything about that yet.
# In the `while l < r` loop:
# Since the while loop only reverses odd levels, we need to consider the total number of nodes across all odd levels.
# In a binary tree, the sum of nodes across all levels equals n. The odd levels contain approximately
# half the nodes in the worst case (e.g., a complete binary tree). Thus, the total time spent reversing is proportional to
# the number of TOTAL nodes processed, which is still O(n) across all odd levels combined.

# M: O(n)
# due to the queue storing up to the maximum width of the tree, which is proportional to n in the worst case.
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        level = 0

        while q:
            # NOTE: The els in `q` are pointing to the same memory location that els of the tree lives. So if we mutate `q` els,
            # we're mutating the tree els.
            # NOTE: we can use this as well: `if level & 1` which means if the level is odd
            # NOTE: We need to do a reverse. So a two-pointer rings the bell!
            # T: O(n) IN TOTAL
            if level % 2 == 1:
                l, r = 0, len(q) - 1
                while l < r:
                    q[l].val, q[r].val = q[r].val, q[l].val

                    l += 1
                    r -= 1

            # Traversal takes O(n) in total
            # level-order traversal boilerplate
            # Note: We're taking a snapshot of `q`(the expression in range() is not evaluated in each iteration.
            for _ in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            level += 1

        return root
