# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def goodNodes(self, root: TreeNode) -> TreeNode:

		# maxVal is the max value so far from the root
		def dfs(node, maxVal):
			if not node:
				# an empty tree doesn't have any good nodes, so we return 0 here
				return 0

			# is this node a good node?
			res = 1 if node.val >= maxVal else 0

			# update maxVal so far, because we're gonna need to pass this along to dfs() recursive call
			maxVal = max(maxVal, node.val)

			# calling dfs() will count the number of good nodes, so we add the results of these. We're gonna add the number of good nodes in the
			# left and right subtree.
			res += dfs(node.left, maxVal)
			res += dfs(node.right, maxVal)

			return res

		# we can pass negative infinity because we can have a really small negative number. So we need to pass the smallest value which is
		# negative infinity. But it works out as well if we just pass the root.val . Because as long as this root is greather than or equal to
		# the maxVal(look at the dfs function), it does count as a good node and we know that the root node alaways counts as a good node. Why?
		# Because in the first iteration, we would have: node.val >= maxVal(which maxVal in the first iteration is node.val) .
		return dfs(root, root.val)

