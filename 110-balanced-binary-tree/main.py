# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. Brute Force
# T: O(n^2) - if balanced: O(n*log(n)). So in total: O(n*h)
# First of all run isBalanced() on ALL the nodes. Because at each node, we run this method on both left & right subtrees,
# so in total, we'll run it on all nodes.
# Now, at each step(node), we do another O(n) operation which is getting it's height.
# So in total, time is O(n^2).

# M: O(h)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        # if this condition is not true, it means this node itself is balanced, but there's no guarantee that it's left and right
        # subtrees are balanced as well. We gotta check them as well.
        # So in addition to this check, we run isBalanced() on left and right subtrees and they BOTH should return True.
        # So use `and` operator.
        if abs(left_height - right_height) > 1:
            return False

        ##################### instead of next line, we could say: ############################
        # if not self.isBalanced(root.left):
        #     return False
        #
        # if not self.isBalanced(root.right):
        #     return False
        #
        # return True
        ###################################

        # The recursion acts like a for loop(O(n)). The calculation of height acts as the body of the for loop which takes another O(n).
        # So T: O(n^2). But since the for loop is shorter in balanced trees, T: O(h*n)
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        return 1 + max(left_height, right_height)


# 2. Depth First Search
# T: O(n)
# M: O(h)
class Solution2:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            # the base case
            # if the condition is true, it means we have an empty tree. An empty tree is considered balanced
            if not root:
                return [True, 0]

            # before we determine is this tree balanced from this root node, first determine if it's balanced from the left subtree and then
            # determine if it's balanced from the right subtree. So call dfs recursively on the left and right subtrees.
            left = dfs(root.left)
            right = dfs(root.right)

            # now we wanna know from the "root" node, is it balanced?
            # this balanced variable doesn't only mean the tree is only balanced from the current root position, it also shows is the
            # entire tree is balanced at all. Because remember if the left subtree or the right subtree was not balanced, then the below
            # condition is gonna evaluate to false.
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            # the height(second return value) is calculated by the max of height of the left subtree and the height of the right subtree, plus 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]


# 3. Depth First Search (iterative - Stack)
# T: O(n)
# M: O(h)
class Solution3:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [root]

        # This None: 0 is very crucial. Because when we get to a leaf node, it's gonna look for: height[None] which is 0 and makes sense.
        # The height of an empty tree is 0.
        heights = {None: 0}

        while stack:
            cur = stack[-1]

            # the part `cur.left not in heights` is important because as we calc the leaf nodes and store their height in `heights` map,
            # we go to the parent. But in the parent, we don't want to add that child to the stack again, because it was already processed.
            # So as we go back up, we need to somehow MARK the processed nodes. The marking is done via adding the height of nodes to
            # the `heights` map.
            if cur.left and cur.left not in heights:
                stack.append(cur.left)
            elif cur.right and cur.right not in heights:
                stack.append(cur.right)
            else:
                cur = stack.pop()
                res = abs(heights[cur.left] - heights[cur.right])
                if res > 1:
                    return False

                heights[cur] = 1 + max(heights[cur.left], heights[cur.right])

        return True
