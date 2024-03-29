**Remember a BST by definition means that it's in order**. Meaning that for every node, all of the nodes in it's left subtree is gonna be less
than the current node and everything in it's right, is gonna be greater than the current node.

### In order traversal approach

Is there a way we can take this BST and put it into a sorted array?

Yes, because BST means that if we traverse it **in order** and take each node and it in an array, then we basically solved this problem.

So we just traverse in order and then return the `k - 1` index(because the question supposes the array is 1-index).

### iterative approach
We know that in the recursive approach, we end up **pop back up** which in the recursive calls it uses the call **stack**. Now in iterative solution,
we need a stack to contain the previous nodes that we need to pop back up to.

Start at the root, don't visit it yet which in this case means count it as the kth value because we wanna go through everything on the 
left subtree first(in order). So we're gonna keep going as far left as possible and simultaneously add the nodes to the stack. Why?
Because we know we wanna pop back up to the previous nodes when we're done traversing the left subtree.

When we reach a null, it means it's time to pop back up and go back up to the previous node, remove that previous node.
When we remove a node from the stack, we wanna go to it's right child. So only after we **visit(process)** the node, we wanna go to it's right subtree.
Why? Because remember we're trying to do this **inorder**. Then we add nodes again to the stack as we move right.

**When we remove an element from the stack, that means we're processing(visiting) it.** The order we pop the nodes, we're popping exactly inorder.

When the stack is empty, the algorithm is done. Which means we visited every need.

Note: Conveniently, in this problem, we're guaranteed to have at least k nodes in the tree. So the `if n == k:` is always gonna get executed. We're not
gonna end up exiting the outer while loop, we certainly end up returning in the `if n == k` block. So we don't need a return statement at the
end of the method.

This approach has roughly the same time complexity as the recursive solution.