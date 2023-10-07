There's a lot of different ways to solve this.

We can use BFS, basically serializing the tree level by level. But there's also a way to do it with DFS using preorder traversal and we'll be using
this approach because it requires a little bit less code.

We do add nulls to the string when serializing, to indicate that place of the subtree can not be continued.

Q: How do we know when the left subtree stops and when the right subtree starts?

It's simple. For every single leaf node we specified what their children gonna be. If a leaf node has 2 nulls as children, we're done with
that subtree.

Note: We do need the i variable to know where we're currently in the vals list.

Time: O(n) for serializing and O(n) for deserializing.