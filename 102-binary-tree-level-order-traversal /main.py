import collections
from typing import List, Optional


class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
		res = []
		q = collections.deque()

		q.append(root)

		while q:
			# this qLen ensures we iterate through one level at a time.
			qLen = len(q)
			level = []

			for i in range(qLen):
				node = q.popleft()

				# the node could be null
				if node:
					level.append(node.val)

					# this and the right node could be null, but that's why we wrap them into an if block
					q.append(node.left)
					q.append(node.right)

			# after we're done with this level, add the current level to the list of levels(res).
			# Note: our queue could have null nodes, we don't want to add them to the res(we initialized the level as an empty
			# list, but we only add it to the res if current level wasn't empty, so we need this if block)
			if level:
				res.append(level)

		return res
