from collections import defaultdict
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. Brute Force (DFS)
# Gets time limit exceeded
# T: O(n^3)
#

# M: O(n)
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        # T: O(n)
        # M: O(H)
        def same(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if not node1 and not node2:
                return True

            # if we get to this line, it might be that one of node1 or node2 is not None, OR both are not None. If one of them
            # is None, the subtrees represented by node1 and node2 don't have the same structure.
            if not node1 or not node2:
                return False

            is_left_same = same(node1.left, node2.left)
            is_right_same = same(node1.right, node2.right)

            return node1.val == node2.val and is_left_same and is_right_same

        # all subtrees in tree
        subtrees = []

        # this func gets all possible nodes, meaning all possible subtrees.
        # T: O(n)
        # M: O(H)
        def dfs(root: Optional[TreeNode]):
            if not root:
                return

            subtrees.append(root)

            dfs(root.left)
            dfs(root.right)

        dfs(root)

        seen = set()
        res = []

        for i in range(len(subtrees)):
            if subtrees[i] in seen:
                continue

            for j in range(i + 1, len(subtrees)):
                if subtrees[j] in seen:
                    continue

                # We should add both subtrees to seen. Note that subtrees[i] could already been added to seen in prev iterations.
                # For example, when we have sth like: 2 1 2 2 and i = 0, j = 3, the first 2 is already added in seen, so first we should
                # check that if subtrees[i] is in seen or not. But subtrees[j] can't already be in seen, because we just got to it.
                # So we don't need to check for it being in seen.
                if same(subtrees[i], subtrees[j]):
                    seen.add(subtrees[j])

                    if subtrees[i] not in seen:
                        res.append(subtrees[i])
                        seen.add(subtrees[i])

        return res


# 2. DFS + Serialization
# serialize each subtree by joining their vals. This is done by first serializing left & right subtrees for each node and
# joining it with the node's val. Then, before storing the result in a dict, check if we already have this serialized version in the dict,
# if so, add the root of one of same subtrees to `res`.

# T: O(n)
# M: O(H)
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = defaultdict(list)
        res = []

        def dfs(node: Optional[TreeNode]):
            if not node:
                return "null"

            left_serialized = dfs(node.left)
            right_serialized = dfs(node.right)

            # `s` is the serialized version of cur node + it's left & right subtrees
            s = ",".join([str(node.val), left_serialized, right_serialized])
            if len(subtrees[s]) == 1:
                res.append(node)

            subtrees[s].append(s)

            return s

        dfs(root)

        return res


# 3. Depth First Search (Optimal) - serialization using node vals
# CORE IDEA: To identify duplicate subtrees, we need a way to uniquely represent each subtree (its structure and values) and
# check if we’ve seen it before.

# Serialization: Convert each subtree into a unique tuple (value, left_subtree, right_subtree) based on its root value and
# serialized forms of its left and right subtrees.

# Counting: Use a dictionary to count how many times each serialized subtree appears. When a subtree appears for the second time,
# add its root to the `res` var.

# T: O(n)
# M: O(n)
# Recursion Stack: O(H)
# Dictionary (count): O(n)

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # Dict to count occurrences of each serialized subtree
        count = defaultdict(int)

        # List to store roots of duplicate subtrees
        res = []

        def dfs(node: Optional[TreeNode]):
            # BASE CASE: if node is None, return a unique identifier for null (-1)
            if not node:
                return -1

            left_serialized = dfs(node.left)
            right_serialized = dfs(node.right)

            # Create a unique tuple for the current subtree
            cur = ((node.val, left_serialized, right_serialized))

            # If we've seen this subtree exactly once before (count == 1), it's the second occurrence, Add the current node to
            # the result as the root of a duplicate subtree
            if count[cur] == 1:
                res.append(node)

            count[cur] += 1

            # Backtracking up: Return the serialized form of the current subtree for use by parent nodes
            return cur

        dfs(root)

        return res
