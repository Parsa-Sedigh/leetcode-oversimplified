from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. Depth First Search
# T: O(n * log(n))
# WHY?
# Let's look at it level-by-level.
# - first level which only has root, we halve the `nums`. So n/2 + n/2 = n. So O(n).
# - second level: we have 2 nodes. First node halve the already halved arr, twice. So n/4 + n/4 = n/2. There's another node which
# only does another n/2. So this level takes O(n) as well.
# - third level: again O(n).
# ...
# So every LEVEL takes O(n) and we have log(n) levels(since the tree is balanced) -> T: O(n * log(n))


# M: O(n)
# WHY?
# For space complexity, we consider both the output (the BST) and auxiliary space used during execution:
#
# Output Space: The BST has n nodes, requiring O(n) space.
# Auxiliary Space:
# Recursion Stack: The recursion depth is O(log n) because the tree is balanced.
# Temporary Slices: At any point, the active slices are those along the recursion path from root to leaf.
# The total size of these slices is n + n/2 + n/4 + ... + 1, which sums to approximately 2n (a geometric series), or O(n).
# The peak auxiliary space is O(n) for the slices plus O(log n) for the recursion stack, which is dominated by O(n). Including the output tree, the total space complexity is O(n).

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])

        # NOTE: Subslicing with out of range indexes doesn't throw an error, but indexing individual elements would.
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root


# 2. Depth First Search (Optimal)
# T: O(n)
# M: O(h)
class Solution2:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(l: int, r: int):
            if l > r:
                return None

            mid = (l + r) // 2
            root = TreeNode(nums[mid])

            # the `mid` node is already constructed. So the left subtree gets up until `mid - 1`
            root.left = helper(l, mid - 1)
            root.right = helper(mid + 1, r)

            return root

        return helper(0, len(nums) - 1)


# 3. Iterative DFS
# T: O(n)
# M:
#   - O(log(n)) for stack
#   - O(n) for the output
# So if we don't consider the output space, then the axillary space is O(log(n)) for a balanced tree -> in general: O(H)
class Solution3:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        root = TreeNode(0)

        # This value will be overwritten in the first iteration of the while loop
        stack = [(root, 0, len(nums) - 1)]

        while stack:
            node, l, r = stack.pop()
            m = (l + r) // 2

            node.val = nums[m]

            if l <= m - 1:
                # set a dummy node for left child which it's val will be overwritten later.
                node.left = TreeNode(0)
                stack.append((node.left, l, m - 1))

            if r >= m + 1:
                node.right = TreeNode(0)
                stack.append((node.right, m + 1, r))

        return root
