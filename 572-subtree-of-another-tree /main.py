class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
		if not p and not q:
			return True

		# if this is true, that means only one of them is null. One of them is null but one of them is not null, so they're not the
		# same tree.
		if not p or not q:
			return False

		# if we make it through here, that means both of the trees are non-empty(you can condense this block with the previous if block)
		if p.val != q.val:
			return False

		return (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right))
