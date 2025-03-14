3 ways to solve this:
- recursive DFS
- iterative BFS
- iterative DFS

**All of these approaches have the same time and space complexity which is O(n).**

### recursive DFS:
The simplest way to solve is recursive DFS. 

Note: When using recursion, first think about the base case.

time complexity: O(n) - since we're traversing the entire tree

memory complexity: O(h) - h is the height of the tree, which in the worst case(**unbalanced tree**) is O(n)

### BFS:
There's not a lot of benefits using BFS for this problem comparing to just doing DFS recursively.

Time complexity: O(n)

memory complexity: O(n)

The number of levels is gonna be the same as the max depth.

### iterative DFS:
We're gonna be needing a stack DS, because basically we're gonna be emulating the call stack that we would have in the recursive approach.

We're gonna be implementing preorder DFS with the stack, because preorder is actually by far the easiest one to do iteratively.

What we're gonna do is say: come to this node, process it, then add the left and right children of it to the stack.