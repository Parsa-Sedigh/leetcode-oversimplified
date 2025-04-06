from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. Brute Force
# T: O(n^2)
# Why?
# - At each node, maxHeight(root) is called, which itself runs in O(n).
# - Since diameterOfBinaryTree(root) is called O(n) times overall (once per node), and each call involves an O(n) traversal
#   due to maxHeight(root), the final complexity is O(n²). So we call this func n times and each call involves a O(n) operation.
#   So overall: O(n^2)

# M: O(h) - since the max size of call stack is O(log(n)) in a balanced tree and O(n) in a skewed tree
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_height = self.max_height(root.left)
        right_height = self.max_height(root.right)

        diameter = left_height + right_height

        sub_tree_diameter = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        return max(diameter, sub_tree_diameter)

    def max_height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_height = self.max_height(root.left)
        right_height = self.max_height(root.right)

        return 1 + max(left_height, right_height)


# 2. DFS(postorder)
# T: O(n)
# M: O(h)
class Solution2:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # define basically a global variable. The reason this is global is because we're gonna have a nested function named dfs and we
        # pass it only the root and so since this `res` variable is outside of that nested function, this variable is gonna be
        # accessible in that function.

        # NOTE: We used a list here, since if we use an int, we have to use nonlocal `res` in the `dfs` func.
        res = [0]

        def dfs(root):
            # base case:
            if not root:
                # return the height. The height of an empty tree or a null tree(this if statement) is not 0, because that's what the
                # height would be for a sinle node. But for a null tree, the height is actually -1, because that lets our math work out.
                return -1

            left_height = dfs(root.left)
            right_height = dfs(root.right)

            # find the diameter of the current root and we can do this using the left and right heights.
            # The math with `2 +` works because if there's no left or right subtrees, they would be -1.
            # So a node without any left and right subtrees(leaf node), would get: max(res[0], 0). So it doesn't contribute anything
            # to the diameter, but it DOES contribute to the height by adding 1 to it(that's why we add `1 +`) when we're done with this
            # node(next line of code).
            res[0] = max(res[0], 2 + left_height + right_height)

            # We want to return the height.
            # NOTE: The height is from root to it's DEEPEST leaf. So we use max() of left and right heights.
            return 1 + max(left_height, right_height)

        dfs(root)

        return res[0]


# 3. DFS but more readable
# T: O(n)
# M: O(h)
class Solution3:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root: Optional[TreeNode]):
            nonlocal res

            # empty tree doesn't have any height. So return 0
            if not root:
                return 0

            left_height = dfs(root.left)
            right_height = dfs(root.right)

            # At each node visit, calculate the `res`
            res = max(res, left_height + right_height)

            # return the height of current node.

            # The height is the max of it's left and right subtree + itself(the node itself
            # contributes by 1 to the height)
            return 1 + max(left_height, right_height)

        dfs(root)

        return res


# 4. Iterative DFS
# T: O(n) - each node is processed once.
# M: O(n)
class Solution4:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]

        # node -> (height, diameter).
        # The diameter val is not necessarily the diameter by passing that node. It's the max diameter in
        # subtree of the node(without passing from node), OR the diameter by passing the node.
        # This is why, we get the max(left_dia, right_dia, `dia passing by node itself`) and not only the
        # `dia passing by node itself`.
        # NOTE: dia passing by node itself is: left_height + right_height
        mp = {None: (0, 0)}

        while stack:
            node = stack[-1]

            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                # if we reach here, it means the left and right subtrees are visited and their height and dia are added to `mp`.
                # So now we can visit this node. We visit it by popping it from the stack and calc it's height and max dia of it
                # with or without passing this node.
                node = stack.pop()

                left_height, left_dia = mp[node.left]
                right_height, right_dia = mp[node.right]

                # get the max dia. The max diameter could pass this node or could not. If it passes this node, then
                # left_height + right_height is the maximum among three.
                max_dia = max(left_dia, right_dia, left_height + right_height)

                # the height of a node is max height of left and right subtrees, with the node itself(+ 1)
                mp[node] = (1 + max(left_height, right_height), max_dia)

        return mp[root][1]
