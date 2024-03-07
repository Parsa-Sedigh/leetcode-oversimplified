Dummy nodes makes the edge cases easier, like when our list is empty. When the list is empty, inserting is gonna be easier.
Because instead of having an if statement, we just insert a node after the head dummy node. Removing is also gonna be easier.
When we have dummy nodes, every single op is dealing with a node that is in the middle of the linked list. We don't have to deal with
edge cases at the beginning or end. Because we have dummy nodes.
But make sure to ignore them when returning the results.

When deleting a node, technically we would get a memory leak, if we don't de-allocate the node after pointer manipulation.