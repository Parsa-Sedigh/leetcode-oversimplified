This question is about a binary tree not a binary search tree. Therefore you need both preorder and inorder traversals to build the binary tree.
So when we place the first value of preorder as the root of our tree, **we don't know** which values are going to the left subtree and
which are going to the right subtree. But how we can determine which nodes go to which subtree?

Well that's why we need our inorder traversal for.

Now if you find the root's value in the inorder traversal, we see that every value to the left of the root in the inorder array, is at the left
subtree of root and every value to the right of the root in the inorder array is at the right subtree of the root.

This is convenient for us because that's the purpose of inorder traversal. It guarantees that we're gonna go through the tree inorder.

So first we take the first value in the preorder array. We don't need it anymore because we're gonna create a node from that value. Now
we need to know which values are gonna go to the left subtree of this node and which are gonna go to the right subtree? We can know this by
finding the index of the current value in the inorder array(we call this index `mid`). Now we don't need that value in the inorder array
as well. So we can get rid of it. The values on the left of that node are gonna go to the left subtree and the values on the right of that
found node in inorder array are gonna go to the right subtree. Now we need to construct those subtrees.

Note: The first value in preorder traversal is always going to be the root. But the first value in inorder traversal is no the root node.

Note: Every value in the traversal is guaranteed to be unique.

You can create a helper function to pass the indices in the recursive calls, if you can't create sublists in the language you're using.

Q: Why we skipped the first index in preorder[1:mid + 1] ?

A: Because the index 0 is considered as the root of the subtree in the previous line.

Q: What does `root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])` mean?

A: The root of the left subtree is gonna be the first element of preorder[1:mid + 1] and the elements in that left subtree are in
inorder[:mid]. Note that the root which is at the `mid` index of the inorder, is not being included in the elements. Because when
sub-arraying, the last element is excluded which in this case is the root of the subtree.

If the given preorder traversal included the null nodes as well, we could only use preorder to construct the tree without using inorder and
vice-versa(see problem #297).

