class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Codec:

	def serialize(self, root):
		"""Encodes a tree to a single string.

		:type root: TreeNode
		:rtype: str
		"""

		res = []

		# preorder depth first search
		def dfs(node):
			if not node:
				res.append("N")
				return

			res.append(str(node.val))
			dfs(node.left)
			dfs(node.right)

			# we don't need a return at the end of this function

		dfs(root)

		return ",".join(res)


	def deserialize(self, data):
		"""Decodes your encoded data to tree.

		:type data: str
		:rtype: TreeNode
		"""

		vals = data.split(",")

		# we want this i variable to be global. We want it to be accessible inside the dfs function defined inside of deserialize. So
		# we don't need to pass the `i` into it, because `i` is global.
		self.i = 0

		def dfs():
			if vals[self.i] == "N":
				self.i += 1

				return None

			node = TreeNode(int(vals[self.i]))
			self.i += 1

			# the return value is the subtree we created for node.left. This subtree could be None(base case) or a non-empty tree.
			node.left = dfs()
			node.right = dfs()

			# return the created subtree to the parent
			return node

		return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))