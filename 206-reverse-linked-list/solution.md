This problem is a sub problem in other questions(including linked list).

We can use two pointers.

Time complexity: O(n)

memory complexity: O(1)

**Note:** If you set the first pointer to head and second one to head.next, we're gonna have a cycle in the ListNode(we would have a cycle
at the end of the linked list - because after reversing, the first node becomes the last node and ...)!

---

### recursive
Time complexity: O(n)

memory complexity: O(n) . Why?

Because if we were given a linked list of size 2, our recursive call is gonna be of size 2 and ... .

For each node, say: instead of reversing the entire linked list, I'm gonna reverse the remainder of the linked list(whatever is after this current
node). So now we have a sub problem. Now we only have 2 nodes to deal with(the current one and the remainder of the linked list which is consider as
one node).

In this approach, the last node(which becomes the first one when reversed), is not gonna have it's `next` changed **in the second pop from the
call stack(remember the first pop from call stack is the null case which we aren't on a node at all because we reached the end of the list)**.
After popping the null case, then popping the last node(which becomes the first one) which we don't do anything with it(because in code, it's
`head.next` is null, so we won't execute the `if` block), we reach the third call in the call stack and now we can set the `head.next.next` to `head`.
Which means the next node is gonna point at the current node that we're on(reversing). But we also need to set the current node's next(`head.next`) to null.
So far, we have reversed the linked list, so let's go back(we're going backwards because we're popping from the call stack) and reverse them as well.

We reversed the linked list so we need to maintain a new pointer that points to the new head and we call that variable `newHead`.

Try to walk through these cases with recursive solution. Use pen and paper.

- -> 1
- -> 1 -> 2