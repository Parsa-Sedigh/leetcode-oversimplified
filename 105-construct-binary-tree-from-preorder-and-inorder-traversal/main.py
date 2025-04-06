from typing import List


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
		if not preorder or not inorder:
			return None

		# the first value in the preorder array in each recursive call is gonna be the root of the subtree that we're going to build in
		# the next lines. So choose that value as the current root.
		root = TreeNode(preorder[0])

		# find the position of the value in the inorder array.
		# mid tells us how many nodes we want in the left subtree and right subtree
		mid = inorder.index(preorder[0])

		###### build the subtrees ######
		# For preorder, we start at index 1 because we already created the node for the 0 index. the left subtree is gonna be from
		# index 1 until mid(mid + 1 is exclusive, so it's gonna be until `mid`).
		# Q: Why preorder[1:mid + 1]?
		# A: Because we have chose the first one as the root of the current tree. Now all nodes in preorder up until mid(including mid)
		# should be the roots in the left subtree. Note that mid is inclusive, because we haven't chosen the value at mid yet, we chose the
		# first value to be the root in the preorder, hence we didn't include it(we started at 1).
		# And all other nodes after mid in the preorder, should be the roots in the right subtree, hence the preorder[mid + 1:].
		# Also, the nodes of left subtree should be chosen from the inorder and they're up until mid(not mid itself), because mid itself
		# is the root. Therefore: inorder[:mid]
		root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
		root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

		return root
