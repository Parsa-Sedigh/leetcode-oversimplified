In this question, the 2,2,3 and 3,2,2 are considered duplicate. In this question we want combinations not permutations, that end up summing to
the target value.

Note: The difficult part about this problem is trying to figure out how to eliminate duplicate combinations.

If we brute force it using a decision tree, we know we have `candidates.length` values that we can choose and we can choose each of them
an unlimited number of times. At the first place, we have `candidates.length` decisions in our decision tree.

When we found the elements that sum up to the target, we don't need to continue down, since all the numbers are positive so as we add
more numbers, we're only gonna get a sum larger than the target, so we don't continue that subtree of the decision tree.

This type of decision tree does not work, because we're gonna have duplicates. The duplicates are `2,2,3` and `2,3,2` .
This decision tree works for finding the correct combinations but we end up getting duplicate combinations.

So what kind of decision tree can we try that gets us the result that we want but does not have duplicates?

![](../img/39-1.png)

In the first step of decision tree, in the left decision we're definitely including at least one 2. Now for the right decision, we want to
make sure that none of the combinations down that decision(path) ever match the combinations in the left subtree. How can we guarantee that?

Well, in the left subtree we're saying we definitely including at least one 2, how about on the right subtree we don't include even a single 2?
So basically we skip 2 on the right subtree. So we decide not to include 2 which makes it a decision with an empty array. Because we were deciding on
whether or not include 2 and we didn't - we don't work with other elements yet because their decision time has not come yet. So that in the
next decision on the right subtree, we can include the elements other than 2 and therefore we won't have any 2 in that right subtree.

That's gonna guarantee non of the combinations on both sides are gonna be matching.

Note that we can include multiple 2s if we want to. So one decision is to include another 2(shown in the left subtree).

When we have for example [2, 2], the path from that place is gonna include all combinations that include at least two 2s.

On the right subtree of [2], we say since we don't want any combinations down the right subtree to be the same as the left subtree,
we make a decision of not include 2 in the right subtree, so the right subtree will be [2] (not include another 2).

In the [2, 2] node, for the left subtree we say let's add a 3, but for the right subtree, we say: we don't want to add a single 3 because
we would have a duplicate combination with the left subtree. So we decide **not to** add a 3, so we would have [2, 2] again on the right subtree.

Note: In each step of decision tree, we decide whether to add the next element or not. We can't decide on two elements. In other words:
We can't decide to add for example 1 in the left subtree and add 2 on the right subtree. This is false. We only decide whether add 1 or not.

Another example is in [2] at the third level, for it's right subtree we're not allowed to add any 3. So it's gonna be [2] again for the right
subtree.

Notice as we're going to the right paths, we're eliminating the possible elements that we can choose from. Because on their left subtree, we 
**decided** to add the element, so on the right subtree, our decision is not to add that element.

Time complexity: At each recursion step, we're making 2 decisions. So it's gonna 2^<sth> and sth is the height of the decision tree. Now what's the height of
our tree?

Well, each value of the candidates array that builds the decision tree is gonna be positive and at least 1. So the height of the decision tree
can be at most whatever the `target` value is. Let's say `t`. So the time complexity is: `2^t` .

Q: Why we used copy()?

A: Since we're only maintaining a single variable for current, we need to use it's copy when appending because we're gonna continue to use this
variable when doing other combinations recursively. So we don't end up mutating it. Because after appending the cur, if we don't pass a copy
of it to append(), in the next steps we're gonna mutate cur again and the value appended to the `res` is gonna get mutated down the tree. We don't
want this.

This works:
![](../img/39-2.png)

Note: Look at the right subtree, nothing is being added. Because the decision is not to add that current element that we're deciding on.