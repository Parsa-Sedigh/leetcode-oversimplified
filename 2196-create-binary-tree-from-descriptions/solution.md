This question is similar to adjacency list in graphs.

Instead of looking for the root directly, we construct the tree from the leaf and work our way up until the root.

We need a way of knowing we've already created a node, so we don't create it again. So we need fast lookup for this.
We can use hashset or hashmap. Now since in addition to knowing we've already created it, we also wanna have a reference to that
already created node, use a hashmap instead of hashset.

To find the root, we can first create a hashset of children as we loop through them. After fully going over the descriptions,
go through them again and check if a node is not in the children, if it wasn't, it's the root.