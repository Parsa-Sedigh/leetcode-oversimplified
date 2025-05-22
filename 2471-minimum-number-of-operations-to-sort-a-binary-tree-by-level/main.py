from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# T: O(n * log(n))
# Earlier levels have fewer nodes(e.g., 1, 2, 4, ..., up to n/2), and their costs are smaller (e.g, O(1), O(2 log2), ... , O(4 log4), etc).
# The dominant term comes from the widest level, leading to a total time of O(n * log(n))

# M: O(n)
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:

        # T: O(n * log(n))
        # M: O(n)
        def count_swaps(nums: List[int]) -> int:
            swaps = 0

            # The python's sorted() func creates a NEW copy(it won't sort it in place).
            # T: O(n * log(n))
            sorted_nums = sorted(nums)

            # T: O(n)
            idx_map = {n: i for i, n in enumerate(nums)}

            for i in range(len(nums)):
                # is nums[i] in the right place?
                # if this condition is true, it means nums[i] is not at the right place, so we wanna sort it. It has to be
                # where sorted_nums[i] lives(remember all vals are unique) in nums. But we don't know the index that we should use
                # to do the swap.
                # To get that index, we can iterate over nums every time, to find sorted_nums idx there and perform the swap.
                # But that would be inefficient. We can do some preprocessing and build up a hashmap of val -> idx and keep that
                # hashmap updated everytime we do a swap.
                if nums[i] != sorted_nums[i]:
                    swaps += 1

                    j = idx_map[sorted_nums[i]]
                    nums[i], nums[j] = nums[j], nums[i]

                    # NOTE: We don't need to update the mapping of nuns[i] because we won't access it again anymore.
                    # There's a new val as nums[i]. So we have to update this new val which resides at ith index, in the idx_map.
                    # The same goes for nums[j].
                    # To understand this part, run through an example.
                    idx_map[nums[i]] = i
                    idx_map[nums[j]] = j

            return swaps

        # M: O(n)
        q = deque([root])
        swaps = 0

        while q:
            # Since levels are processed sequentially, this is at most M: O(n)
            level: List[int] = []

            # take a snapshot of q. This is equivalent to:
            # size = len(q)
            # for i in range(size):
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            swaps += count_swaps(level)

        return swaps
