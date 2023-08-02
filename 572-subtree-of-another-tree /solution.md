Brute force:

Visit every single node and then check (starting from the root), does the tree starting from the current root, match the subRoot tree?

In other words, for every single node in the first tree, compare the tree starting from the current root to the entire second tree.

In the worst case, for every single node in the first tree, we have to go through every single node in the second tree.

We would have the main function that they gave us named `isSubtree` and we also need a helper function, let's name it `sameTree`.

Time complexity: O(S * T) - the size of both trees multiplied together.

### Edge cases
As with most recursive problems, we don't want to forget about the important edge cases(when we're comparing the trees in this case):
- what would happen if both trees where null? In that case are they the same trees? Yes
- What if two trees had the same initial values, but what if one of the trees had an extra node in it's right? Are they the same in this case?
No. So we have to keep track of this in the `sameTree` function.
- What about isSubtree recursive function? If the both trees are null, is our isSubtree gonna return true? In other words: Is a null tree
a subtree of another tree? Yes, a null subtree is a subtree of another null subtree.
- What if the first tree was null but the second one is non-empty? Is the second one a subtree of the first one? No Because the second one can not
be found anywhere in the first tree. What if the opposite was true? What if second one(the subtree) was an empty tree, then is a null tree a subtree of a
non-empty tree? Yes(you can clarify this in the interview). Why? Because we could just go to one of the leaf children of the first tree and
we know they have a null subtree.

Time complexity: O(S * T)