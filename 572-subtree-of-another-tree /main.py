class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
		# this function is gonna be recursive, so let's start with the base cases

		# if t is empty, the OFC it's gonna be the subtree of the s, regardless of whether s is empty or not
		# Note: The order of these if statements is very important.
		if not t: return True

		# we could write: `if not s and t:`, but it's not necessary because we checked that previously
		if not s: return False

		# at this point, we know both of the trees are not empty, so let's compare both trees
		if self.sameTree(s, t):
			return True

		# if they're not the same tree, but remember, we can compare t to the subtrees of s(left and right subtrees)
		# if t was subtree of either of the left or right subtrees of s, we can return true
		return (self.isSubtree(s.left, t) or
				self.isSubtree(s.right, t))

	# there are 3 conditions in this function:
	# - if both trees are empty
	# - if both trees are not empty
	# - if one of the trees is empty
	def sameTree(self, s, t):
		if not s and not t:
			return True

		# if this condition is true, yeah we know that the CURRENT nodes of s and t are the same but we still have to compare the rest
		# of the subtrees(left and right).
		if s and t and s.val == t.val:
			leftIsTheSame = self.sameTree(s.left, t.left)

			# we also wanna know if the right subtrees are the same
			rightIsTheSame = self.sameTree(s.right, t.right)

			return leftIsTheSame and rightIsTheSame  # or we could say: self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)

		if not s or not t:
			return False

		# if one of the trees is empty
		return False
