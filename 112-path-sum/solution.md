The fact that this is not a BST, means we definitely have to go through every single node of the tree. We have to look at every
possible root to leaf path in the entire tree.

We wanna do an inorder DFS.

We need to only check the current sum when we reach one of the leaf nodes and do not check it at every node.