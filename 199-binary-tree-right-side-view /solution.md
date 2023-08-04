There are BFS(level order traversal) and DFS solutions for this but BFS is easier in this case.

Solution: For each level, we want the right most node.

It's important that at each level, we add the nodes from left to right. Because we always want to get the right most value.

**In queue, we pop the elements from left and we add them at right.**

Note: When the queue becomes empty(after while loop is done), it means we've gone through every single level of the tree.