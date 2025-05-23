import heapq
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# T: O(n * log(k))
# M: O(n)
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        # We're guaranteed that root exists
        q = deque([root])

        # at most size = k
        min_heap = []

        while q:
            level_sum = 0

            # go through the current level using snapshot of current length of q. The snapshot part is important because
            # in the loop which relies on q, we're mutating q itself.
            # In other words: process all nodes at the current level by dequeuing them, adding their values to level_sum
            # and enqueuing their children.
            for i in range(len(q)):
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # T: O(log(k))
            heapq.heappush(min_heap, level_sum)

            # If the min_heap size exceeds k, pop the smallest element to keep only the k largest sums.
            if len(min_heap) > k:
                # T: O(log(k))
                heapq.heappop(min_heap)

        # if the size of the min-heap is less than k, then it means we never even added k vals to the min-heap in the first place.
        return -1 if len(min_heap) < k else min_heap[0]
