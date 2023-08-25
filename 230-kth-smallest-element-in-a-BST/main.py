class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


####### Boundaries approach #######
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