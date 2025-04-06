One difficult way of inserting a node is to insert at the root and then rebalance the entire tree around the new root value.
The simpler way is to keep going down until we get to a proper empty position.

There are two ways of doing this. Iterative or recursive. Iterative is easier. Recursive way is trickier because there's an edge case:
What happens if we have an empty BST and we wanna insert sth into it.

- Time complexity: O(h). The tree could be unbalanced, so it would become a linked list, so it could be O(n). O(h) is a more correct answer
because h could be n in the worst case.
- Space: Recursive solution takes extra memory because we have a call stack -> O(h). But if we do it iteratively, it would be O(1).
