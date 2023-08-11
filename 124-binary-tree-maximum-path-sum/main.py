class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def maxPathSum(self, root: TreeNode) -> int:
		res = [root.val]

		# return max path sum without split
		def dfs(root):
			if not root:
				return 0

			leftMax = dfs(root.left)
			rightMax = dfs(root.right)

			# leftMax and rightMax could be negative, but we don't want them if they're negative. So calculate the max of each of them
			# with 0.
			leftMax = max(leftMax, 0)
			rightMax = max(rightMax, 0)

			# compute(do not return to the parent) max path sum WITH split. Adding root.val and leftMax and rightMax means we ARE
			# splitting
			res[0] = max(res[0], root.val + leftMax + rightMax)

			# the return value is not res[0]. The return value is what we compute WITHOUT splitting. Which means we can't return the sum of
			# both leftMax and rightMax. Because if we use the sum of both, it means we're splitting. We have to return one of them which in
			# in question means we have to return the max of them.
			return root.val + max(leftMax, rightMax)

		dfs(root)

		return res[0]