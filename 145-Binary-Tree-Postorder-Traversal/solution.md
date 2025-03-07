In a binary tree, post-order traversal means:

1. Visit the entire left subtree.
2. Visit the entire right subtree.
3. Visit the node itself.

##

When we pop a node from the stack:

- If its visit flag is True, it means we’ve already processed its subtrees, so we can add the node’s value to the result (res).
- If its visit flag is False, it means we haven’t processed its subtrees yet. We push the node back onto
the stack (with `visit=True`) and then add its right and left children (in that order) with visit=False.
This ensures that the children are processed before the parent, mimicking the post-order rule.

Why we push right child FIRST and THEN the left child?

Since we wanna visit left subtree, but we're dealing with a stack(LIFO). So we have to push the left child **after** the right one.
So that when we do pop(), the left child comes out **first**.

### Why It Works
The visit flag is key:
- False: We’re seeing the node for the first time and need to explore its subtrees.
- True: We’ve processed the subtrees and can now visit the node.

By pushing the node back with visit=True, followed by its right and left children with visit=False, the stack ensures that:
- The left subtree is processed first (since left is pushed last and popped first).
- The right subtree is processed next.
- The node itself is processed last (when it’s popped with visit=True).

This perfectly enforces the post-order rule without recursion.

### Efficiency
- Time Complexity: O(n), where n is the number of nodes. Each node is pushed and popped twice (once with visit=False,
once with visit=True), but all operations are O(1).
- Space Complexity: O(n), as the stack and visit list can hold up to O(n) elements in a skewed tree.