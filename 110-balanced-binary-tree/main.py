# Definition for a binary tree node.
from typing import Optional


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def isBalanced(self, root: Optional[TreeNode]) -> bool:
		def dfs(root):
			# the base case
			# if the condition is true, it means we have an empty tree. An empty tree is considered balanced
			if not root:
				return [True, 0]

			# first determine if it's balanced from the left subtree and then determine if it's balanced from the right subtree
			left, right = dfs(root.left), dfs(root.right)

			# this balanced variable doesn't only mean the tree is only balanced from the current root position, it also shows is the
			# entire tree is balanced at all. Because remember if the left subtree or the right subtree was not balanced, then the below
			# condition is gonna evaluate to false.
			balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

			# the height is calculated by the max of height of the left subtree and the height of the right subtree, plus 1
			return [balanced, 1 + max(left[1], right[1])]

