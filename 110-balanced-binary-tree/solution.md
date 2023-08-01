We need to make sure that the height of left and right subtrees of **every single** node differ by at most 1.

### naive approach
First question we're asking: are the left and right subtrees balanced?

How do we even determine left and right subtrees are balanced?

We can do a recursive dfs on the left subtree to determine the height of the left subtree and do a recursive dfs on the right subtree
to determine the height of the right subtree and then we can compare those and make sure that the difference is less than or equal to one.
We need to do this for every single node.

We're doing dfs on left and right, that means we go through every single node in the tree, so that question itself is O(n).
In other words, since we're running a recursive dfs on every single subtree(each time we ask the question: is this subtree balanced, it will
be O(n)), it will be `O(n^2)` .

### better approach
Can we do better than that? Is there any repeated work? 

Yes there is repeated work and it can be eliminated by asking the question in a different order. What I mean is instead of first asking: is the entire
tree balanced from the root, we need to ask this question **bottom up**. We ask the question lower and lower and the last question is
answered first(which is the base case). Once we get to the base case, we're gonna go back up and this will end up eliminating the repeated work.
If we do it this order, we'll only have to visit each node at most one time which will ensure the overall time complexity is gonna be `O(n)` rather 
than O(n^2). 

So in the better approach, when we get to the root, before we check if it's balanced from there, we're gonna check if it's balanced from it's
left subtree and before getting the answer for that, ask if it's balanced from it's left subtree and ... , until we hit the base case.

As we're determining if a subtree is balanced, let's also at the same time(simultaneously) get the height of this subtree. Because if we do that,
once we go back up to the parent node of this subtree, it will be easy, because we have the height of the right and left subtree and we can take
the difference between those, if it's less than or equal to 1, it's still balanced. Now we don't need to revisit the subtrees again.

We would have recursion, therefore we need to define another method. Why we can't just call the given function? Because it just returns a boolean,
but we wanna implement it by returning 2 values. So we're gonna write a nested recursive function(you could define a method as well), named `dfs`.

The line below means: is the left subtree is balanced and the right subtree is balanced and also the current subtree starting from the current
root is balanced. So all three have to be true in order for the current subtree to be balanced.

**At each step, the left subtree and right subtree and the subtree starting from the current root should be balanced.**

```python
balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
```
Why we said: `left[0] and right[0]`, because if either of the left or right subtrees ever return False in the first return value, then
we know for sure that the entire tree is not balanced.

When we said: `abs(left[1] - right[1]) <= 1`, it means is from the current root subtree, are we balanced?