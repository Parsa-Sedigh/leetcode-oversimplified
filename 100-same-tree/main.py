from cassandra.connection import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. Depth First Search
# T: O(n)
# M: O(h)
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True

        # if this is true, that means only one of them is null. One of them is null but one of them is not null, so they're not the
        # same tree. Remember that both can't be null at this point, because we checked it in prev if block.
        if not p or not q:
            return False

        # if we make it through here, that means both of the trees are non-empty(you can condense this block with the previous if block)
        if p.val != q.val:
            return False

        # both are non-empty and have same vals. Continue the recursion:
        return (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right))


# 2. Iterative DFS
# T: O(n)
# M: O(h)
class Solution2:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        cur_p = p
        cur_q = q
        stack = []

        while cur_p or cur_q or stack:
            while cur_p:
                if (not cur_p and cur_q) or (cur_p and not cur_q):
                    return False

                if cur_p.val != cur_q.val:
                    return False

                stack.append([cur_p, cur_q])

                cur_p = cur_p.left
                cur_q = cur_q.left

            cur_p, cur_q = stack.pop()
            cur_p = cur_p.right
            cur_q = cur_q.right

        return True


# 3. Breadth First Search
# T: O(n)
# M: O(n)
class Solution3:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        queue = deque([[p, q]])

        while queue:
            p_node, q_node = queue.popleft()

            if (p_node and not q_node) or (not p_node and q_node):
                return False

            if p_node and q_node:
                if p_node.val != q_node.val:
                    return False

                queue.append([p_node.left, q_node.left])
                queue.append([p_node.right, q_node.right])

        return True
