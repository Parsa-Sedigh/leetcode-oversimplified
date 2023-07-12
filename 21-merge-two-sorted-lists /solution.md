Note: We have to use the original nodes, we can't create copies of the nodes.

**Note:** To prevent edge cases, we create a dummy node at the beginning and we return `.next` as the result(because the first one is dummy).
With this, we avoid the edge case of the initial empty list. So the result is: `dummy -> <actual result>`, therefore we
return head.next or sth like that to return the actual result. So to avoid the edge case of inserting into an empty list,
create a dummy node.

At the end, one of the lists is still remaining, in order to merge them as well, just connect the end of the result to the first node of
the remaining of the list.