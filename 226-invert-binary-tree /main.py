class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def invertTree(self, root: TreeNode) -> TreeNode:
		# base case
		if not root:
			return None

		# swap the children
		tmp = root.left
		root.left = root.right
		root.right = tmp

		# recursively invert the subtrees

		# invert the left subtree
		self.invertTree(root.left)

		# invert the right subtree
		self.invertTree(root.right)

		return root