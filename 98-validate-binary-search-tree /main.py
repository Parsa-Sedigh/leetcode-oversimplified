class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


####### Boundaries approach #######
class Solution:
	def isValidBST(self, root: TreeNode) -> bool:

		# left and right are the left and right boundaries
		def valid(node, left, right):
			if not node:
				return True

			# if the current value is not in the defined boundaries, return False
			if not (node.val < right and node.val > left):
				return False

			# the left subtree and the right subtrees need to be valid, so recursively call them, but with updated boundaries
			return (valid(node.left, left, node.val) and
					valid(node.right, node.val, right))

		# the boundaries of the root of the tree could be anything, there are no restrictions on what the value of root of the tree could
		# be.
		return valid(root, float("-inf"), float("inf"))
