class Solution:
	def diameterOfBinaryTree(self, root: TreeNode) -> int:
		# define basically a global variable. The reason this is global is because we're gonna have a nested function named dfs and we
		# pass it only the root and so since this `res` variable is outside of that nested function, this variable is gonna be
		# accessible in that function.
		res = [0]

		def dfs(root):
			# base case:
			if not root:
				# return the height. The height of an empty tree or a null tree(this if statement) is not 0, because that's what the
				# height would be for a sinle node. But for a null tree, the height is actually -1, because that lets our math work out.
				return -1

			left = dfs(root.left)
			right = dfs(root.right)

			# find the diameter of the current root and we can do this using the left and right heights.
			res[0] = max(res[0], 2 + left + right)

			# we want to return the height
			return 1 + max(left, right)

		dfs(root)

		return res[0]