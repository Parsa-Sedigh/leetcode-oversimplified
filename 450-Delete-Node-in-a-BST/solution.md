Edge cases about the node we wanna remove:
- doesn't have any children or just one child
- has two children: We wanna pick a value from the right subtree of the node we wanna remove, intelligently. A value that satisfies
the ordered property of BST. **We should we pick the smallest value of it's right subtree.** Why? Because if we put it in the place of
the node we wanna remove, then every value on it's right is larger than it and also every value on it's left is less than it. Hence
preserving the sorted property.

Note: We could pick a value from the left subtree as well.

Then we have to delete the node that we picked. Now if it had children, we would end up with a chain of recursive delete node calls.
Because we're going to delete their parent, so we have to again find the min value on the right subtree and put it in place of it's 
parent to avoid having duplicate nodes because we just moved their parent to the top and the same for their children and ... .

There are portions of the tree that we have to visit twice or more. Because we wanna find the min value of the right subtree for the 
node we wanna remove and also the children of the node that we replaced it with and the children of it's children and ... .
To do these, we're gonna call self.deleteNode() multiple times but each time from a node at a deeper level, so we would have a less path
to find the min value than the last time we called this func. 

So in the worst case, we're gonna go 2 times of the height of the tree. One for finding the value we wanna delete and another for
replacing the nodes possibly multiple times(but at total, this step consists of one O(h)).

T: O(2 * h) => O(h)

### Recursion II
When the node we wanna delete have both left & right subtrees:

What happens to left subtree:

- `root.left` is the entire left subtree of the node we’re deleting. All its values are less than root.val.
- Originally, cur.left is None (because it’s the leftmost node). By setting cur.left = root.left, we attach the left subtree under cur.
- This maintains the BST property: all nodes in cur.left (the old root.left) are less than cur.val, and cur remains in 
the right subtree, where all values are greater than the deleted root.val.

What happens to right subtree:

- The right subtree (root.right) becomes the new root of this part of the tree. So it gets the place of the `root` that we deleted.
This is achieved via returning root.right to the parent of `root`. So now the parent of `root` no longer points to `root`, instead
it points to the right subtree of `root` which is what we want, we wanna exclude(remove) the `root`.
- So after attaching root.left to cur.left, the variable res is set to root.right: `res = root.right`. Then, res is returned as the new root
to it's parent.

**Side note:** Since `cur` is a node within root.right (it’s the leftmost node of the right subtree), modifying 
cur.left updates the structure of root.right. When we return root.right, it includes cur with the attached `root.left` subtree.

### Why It Works
- Why assign root.left to cur.left?
  - We need to preserve the left subtree (`root.left`) because it contains valid BST nodes that are less than `root.val`. 
  Attaching it to cur—the smallest node in the right subtree—works because cur has no left child, and all values in 
  root.left are less than cur.val, keeping the BST order intact.
- What happens to root.right?
  - root.right isn’t lost—it becomes the new root of the subtree after deletion. Since cur is part of root.right, 
  attaching root.left to cur.left modifies root.right in place. Returning root.right gives us the restructured tree.

### Summary
When deleting a node with both children:

- The successor (`cur`) is the smallest node in the right subtree.
- The left subtree (root.left) is attached to cur.left.
- The right subtree (root.right), now including the attached left subtree, replaces the deleted node by returning it to the parent.