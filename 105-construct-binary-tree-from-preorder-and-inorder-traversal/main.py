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
		root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
		root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

		return root
