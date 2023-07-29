What would be a brute force way to solve?

Let's take every single node and consider it as the top-most node in that diameter. We need to find the maximum path that we can go
to right and maximum path on left of that node. Now when you move, you probably would encounter another node and from that node again we can
go either left or right and at the end, we add the number of edges we moved from that node to furthest left and to furthest right.
So the diameter for a node would be: `total edges to furthest left + total edges to furthest right + 1 + 1`.

The brute force way:

Time complexity: O(n^2) - n is the number of nodes in the tree

---

So what we're doing is recursively finding the diameter from that encountered node. So we can see repeated work.

If we do this in a recursive way, we can eliminate the repeated work. What we talked about was top-down, but what we can do is start from the
bottom recursively.

In the Better approach, we only have to visit every single node **at most once**.

Time complexity: O(n)

We want the diameter of node, right? Declare a max variable initially with 0. Let's first solve the sub-problems: What's the max diameter running through
the right subtree of the current node? Calculate it. Now find the max diameter running though the right sub-tree of current node. To do these,
we have to also find the max diameter of the children of those left and right subtrees.

In reality, we don't just want the diameter through a node, we also want the **height** of the tree starting at the current node.

So for each node, we want the diameter and the height of the tree starting from that node.

**Q:** How can we find the height of the tree starting at a node?

**A:** We wanna look at it's left subtree and it's right subtree, find the height of the max of these two. So: `1 + max(height of left, height of right)`.
The reason of adding one to it, is by convention, we say the height of a null tree(a tree that has no node) is -1 because the height of a tree
with a single node is considered 1 and that `+ 1` helps the math to work out.

The diameter is `height of left tree + height of right tree + 1 + 1`. Why `+ 1 + 1`? Because for each of those trees, there are 1 edge for each going
to them.

The key here is that we're going bottom up. We're finding the diameter from the bottom nodes and then working our way up to the root, that's what
allowing us to cut out some of the repeated work.

Note: The space complexity is `O(h)` and h which is the height of the tree, if our tree is balanced, is logn, but if the tree is inbalanced,
is gonna be `O(n)`. So space complexity(since it's recursive here, means the amount of calls we're gonna have on the callstack), at worst case
is `O(n)`.