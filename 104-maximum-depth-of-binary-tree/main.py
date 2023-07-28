from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def maxDepthRecursiveDFS(self, root: Optional[TreeNode]) -> int:
		if not root:
			return 0

		return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

	def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
		if not root:
			return 0

		level = 0
		q = deque([root])

		while q:

			# Here, we're taking a snapshot of the length of the `q`. In other words, traverse the entire current level.
			# For first level, the length of q is 1, so this loop is gonna run once. For the second level, the q would have for example
			# 2 elements so len(q) would be 2, so this loop will run 2 times, so basically traversing the entire level and adding the
			# children of the second level. For the third level, it will run number of times equal to the number of elements of q which means
			# equal to the number of elements in the third level and ... .
			for i in range(len(q)):
				node = q.popleft()

				if node.left:
					q.append(node.left)

				if node.right:
					q.append(node.right)

			level += 1

		return level

	def maxDepthIterativeDFS(self, root: Optional[TreeNode]) -> int:
		# You can get rid of this check if you set res to 0 initially. If res is 0 initially, yeah the while loop will be executed once,
		# but we won't go into the if block and therefore the res will stay 0 and we return 0 in that case.
		if not root:
			return 0

		stack = [[root, 1]]
		res = 1

		while stack:
			node, depth = stack.pop()

			# yeah, in this approach it's possible that the node could be null, so we need to check for it
			if node:
				res = max(res, depth)

				# we're not checking that the node.left and node.right exist, so we might add null nodes to the stack, so we need to
				# check for it after popping, so we don't do anything with null nodes. So even if the node.left and node.right are null,
				# we're still adding them to the stack, but we check for this in the `if node` block above
				stack.append([node.left, depth + 1])
				stack.append([node.right, depth + 1])

		return res
