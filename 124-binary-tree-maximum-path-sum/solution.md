Note: The question is about a binary tree not a BST.

### Brute force approach:

For every single node, consider it being the top-most node, then what's the maximum path we can have in the left subtree and right subtree?

---
### better approach:
Why start at the root, when we can solve the sub-problem first and possibly use that sub-problem in the result at the root position?

What's the maximum path we can get from the left subtree if we never end up splitting?

Note: When calculating max path sum, we can only split **once**.

When recursively going through the tree, we do calculate the max path by splitting in each node, but the result we return to the parent is not
the one that we get from splitting in the child. Because if we do that, we would have 2 splitting points in the parent which is incorrect.
But why we do calculate the max path in child by having a split, but not returning it to the parent?
Because with that, we can potentially update the `res` variable that we initialized globally. Note that the path we have at the child with one
splitting point, itself is a correct and acceptable path. But returning it to the parent makes it an incorrect path in this questions.
So we can actually consider it a correct path by itself and update the `res` variable, if it was the `res` path sum yet.

Q: Now what's the value we actually return to the parent?

Well remember what the parent wanted to compute was what's the max it could have if it was allowed to split to the left and it was allowed to
split to the right? But from it's children, it don't want to split again. Only split from itself. So we want to return the value to the parent
is what's the max we can get running through the child if we're not allowed to split?

Q: How do we get that?

A: `node.val + max(left, right)`. So we have to choose one of the left and right, we can't choose both, so we can't have: node.val + left + right .
That would mean we have a splitting point in the current node which is not what we return to the parent.

So for every node, the return value to it's parent is: what the max path without splitting? But we still do update the max variable(if it
was bigger) **with** splitting in that node.

Using the max variable as a global variable makes the code easier, but it's possible to solve this problem without using this global variable.
If you don't want to use a global var, we need to return two values from the `dfs` function: max path sum **with** a split and max path sum **without** a split.

**Edge case:** To get the max path sum when we're **not** allowed to split, it doesn't necessary mean we **have to** include the children, they're optional.
We could choose to not include either of the children of the current node and that's what we would want to do when the children are both negative.
Why we would include some negative numbers to calculate the max path sum? So we need to take the max of three values: `left, right, 0`.

Note: the reason we're making the `res` as list, is because that it'll make it so we can modify it within the recursive function. A little bit easier.

Space complexity: O(n) - because we only look at each node once

Memory complexity: O(h) - usually it's a balanced tree so O(logn), but in an in balanced tree: O(n)