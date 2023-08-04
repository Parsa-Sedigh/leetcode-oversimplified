import collections
from typing import List, Optional


class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def rightSideView(self, root: TreeNode) -> List[int]:
		res = []

		# in python, we can have a queue like this:
		# note: It's possible that the root could be null, so it's possible that our q(queue) could have null values, therefore
		# we need to handle this
		q = collections.deque([root])

		while q:
			rightSide = None

			# capture the length of the queue at this point, because at the next lines, we're gonna update the queue but we don't want
			# to iterate through the queue with the new length
			qLen = len(q)

			# after this entire for loop is done executing, what `rightSide` is gonna have, is the last node that was in the current
			# level of the queue(with qLen)
			for i in range(qLen):
				# pop elements from the left of the queue
				node = q.popleft()

				if node:
					rightSide = node

					# it's possible that left or right(or both) could be null, but we're checking for this in the next iteration of the
					# while loop using the if statement that we have(`if node:`).
					# Note: It's important that you add left child before the right one.
					q.append(node.left)
					q.append(node.right)

			# rightSide could be null for example once we reached the last level(leaf level), so check for this
			if rightSide:
				res.append(rightSide.val)

		return res