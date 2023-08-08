Time complexity: O(n)

Space complexity: O(log n) - in other words O(h). The height of the tree technically could be greater than log n . It could be as big
as `n` in inbalanced tree.

We're gonna be using preorder DFS. Meaning when we recursively run DFS, we're gonna process each node before we traverse recursively the left
subtree and recursively the right subtree.

Note: Technically the root node does count as a good node.

Note: We don't want to consider the max on the left subtree in the right subtree or vice-versa. We need to consider the max from the root, for each
subtree.

We know we're gonna have a recursive function, **but in our recursive function we're gonna have to pass in more than just the current root,
that's why we define we a separate function(in this case named `dfs`)**.