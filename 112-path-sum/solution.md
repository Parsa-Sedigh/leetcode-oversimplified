The fact that this is not a BST, means we definitely have to go through every single node of the tree. We have to look at every
possible root to leaf path in the entire tree.

We wanna do an inorder DFS.

We need to only check the current sum when we reach one of the leaf nodes and do not check it at every node.

### iterative DFS
If we don't maintain a state(cur_sum up until every node), we need to backtrack the current sum. Why? Because if we 
go up until a leaf and it isn't the correct root-to-leaf path, we need to find another path by removing the vals of nodes
that are not among the path.

But backtracking it is hard because we need to find out we're actually backtracking up. It's done automatically in recursive solution,
but we need to do it manually by decreasing from the global cur_sum.

Instead of a global cur_sum, we use local cur_sum(state) by putting the node and it's diff with prev cur_sum(cur_sum - node.val),
in the stack.

With this, we kinda have the result of backtracking at each node.