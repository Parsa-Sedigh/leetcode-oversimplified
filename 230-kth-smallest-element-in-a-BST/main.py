from typing import Optional, List


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


####### Boundaries approach #######
# T: O(n)
# M: O(n)

# The space complexity is determined by the size of the stack used for the iterative inorder traversal.
# In the worst-case scenario, the stack could contain all nodes of the tree if it's skewed, resulting in a space complexity of O(n).
# However, in the average case or for balanced trees, the stack size will be proportional to the height of the tree.
# For a balanced binary tree, the height is O(log n), where n is the number of nodes.
# Therefore, the space complexity is O(n) in the worst-case scenario and O(log n) in the average or balanced case.
class Solution:
	def kthSmallest(self, root: TreeNode, k: int) -> int:
		# this variable tells us the number of nodes that we visited. Once n == k, we can return the current value as the result
		n = 0

		# since we're solving this problem iteratively, we somehow want to simulate the call stack. So we need a stack
		stack = []

		# cur tells us what node we're currently at
		cur = root

		while cur or stack:

			# while cur is not null, we're gonna keep going left and if there is nothing at the left, we visit the node that we're at
			while cur:
				stack.append(cur)
				cur = cur.left

			# When the previous loop is done, that means cur is None which means we went too far and that means we have to pop
			# the last element that we added to our stack
			cur = stack.pop()

			# process the current node which in this is updating the n variable(we visited another node, so we can increment n by 1)
			n += 1

			if n == k:
				return cur.val

			# if there are no node left on the left side and also the current node is not the kth element, we need to go through the
			# right subtree of the current node. By doing this, we're gonna go through the while loops again.
			cur = cur.right

		# we don't need a return statement here, because we're guaranteed to have at least k nodes, so the if n == k block is always gonna
		# get executed.

# naive approach. Traverses all of the nodes of the BST
# T: O(n)
# M: O(n). We store a list
class Solution2:
	def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
		nodes = self.inorder(root, [])

		return nodes[k - 1]

	def inorder(self, root: Optional[TreeNode], nodes: List[int]):
		if not root:
			return

		self.inorder(root.left, nodes)
		nodes.append(root.val)
		self.inorder(root.right, nodes)

		return nodes

# Time Complexity: O(h + k)
# where h is the height of the binary search tree. This is because the algorithm does an inorder traversal,
# which visits every node once, and also stops as soon as it finds the kth smallest element.
# In the worst-case scenario, the algorithm may need to visit the entire left subtree (height h)
# and up to k additional nodes in the worst case.

# Space Complexity: O(h).
# The space complexity is determined by the depth of the recursion stack, which is equivalent to the
# height of the binary search tree. In the worst-case scenario, where the tree is highly unbalanced, the
# recursion depth could be O(n), where n is the number of nodes in the tree. In a balanced binary search tree,
# the height is O(log n). Therefore, the space complexity is O(H) in general.
class Solution3:
	def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
		self.k = k
		self.result = -1
		self.inorder(root)

		return self.result

	def inorder(self, node):
		if not node:
			return

		self.inorder(node.left)
		self.k -= 1

		if self.k == 0:
			self.result = node.val

			# we don't care about the return value, so return nothing. Instead, we have set the result in
			# the object using: self.result = node.val
			return

		self.inorder(node.right)