# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
		cur = root

		# Note: p and q are guaranteed to exist in the tree. So curr is never gonna be null, because we definitely are gonna find
		# the result, but this is just a way to get it to execute forever until we find that result:
		while cur:
			if p.val > cur.val and q.val > cur.val:
				cur = cur.right
			elif p.val < cur.val and q.val < cur.val:

			# this case if for when a split occurs, or if we end up actually finding one of the values(p or q)
			else:
				return cur
