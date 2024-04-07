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