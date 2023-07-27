Invert binary search tree

The root stays at the same place, but the children swapped their places.

Visit every single node in the tree and everytime we visit a node, take a look at it's two children and swap the positions of the children
and then recursively run `invertTree` on left subtree and run `invertTree` on right subtree.

We can do DFS whether it's preorder or postorder doesn't matter.

This problem would be annoying if it was iterative.