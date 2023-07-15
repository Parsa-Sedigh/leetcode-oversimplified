Time complexity: O(n)

Space complexity: O(1)

We will be iterating through the list **twice**, but that's not too bad, so time complexity will be `O(2n)` . One for finding the middle of the list
and one for merging the first half and second half(which would be reversed in that point of time).

Note: It's a little bit more tricky to do this without using extra space.

### Using extra memory:

If we were using extra space, we could take the entire linked list and put it in an array and we would leave the first portion as it is and then
we would take the second portion and either reverse that entire portion or just go through it in reverse order by using a two-pointer
approach and build the array that corresponds with the requested output linked list and if we built an array that looked exactly like
the requested linked list, we could create the corresponding linked list.

---

### Without using extra memory
We can have a pointer at the end of the list, we take for example the last element and we put it as the second node and then point that to the 
original second node. We can do this, but the problem arises once we inserted the last node as the second node, then we want to move
the right pointer to the one to last element but the linked list is in one direction, but we wanted the list to be in opposite order. Because
when we traverse the second portion of the list, we're not gonna be going from beginning to end, we're gonna be going from end to beginning.
So how can we do that without extra memory?

The easy way is why not just reverse the links for the second portion of the list.

There are gonna be two phases to this algorithm:
1. take the second portion of the list, reverse it
2. take the two portions and merge them together according to the problem description

Q: When we're reversing the second half of the list, how do we know what is the second half? How do we know we've reached the second half?

A: You can do it in multiple ways, the easiest way is gonna be a fast and slow pointer. Slow pointer is initially at the first node and the fast
pointer initially at the second node. We're gonna be shifting the slow pointer by one. We're gonna be shifting the fast pointer by two and
we're gonna keep going until the fast pointer either reaches the end of the list or the last value of the list and once that's the case, there
are two cases:
- **if the list has even number of nodes:** we know that the slow pointer will be at the middle of the list, in other words, it
will be at the end of the first portion, therefore at that point, the`slow.next` will be the beginning of the second half of the list.
For example `1 -> 2 -> 3 -> 4` . When fast reaches 4, there is no next node, so we stop the loop. At that point, slow will be at second node and 
therefore that node is the end of the first portion and the second portion starts at 3.
- **if the list has odd number of nodes:** When fast reaches null(the imaginary node after 5), the slow will be at third node.
Now the question is: In this case, what's the second half of the list? Well `4, 5` will be the second half of the list. Even though it's shorter than
the first half, it still works. For example `1 -> 2 -> 3 -> 4 -> 5`

**Note:** Finding the middle of the linked list can be done with two pointers, one fast and one slow. Slow starts at head and fast starts at
head.next and moves two nodes at each iteration of the loop.

#### merging the lists
Have a pointer at the beginning of the first list and another one at the beginning of the second list(this list is reversed).

Then we say: 
```python
l1.next = l2.next
```

Now if you pay attention, by executing those the line above, **we broke the link** between the `l1` and the next node. Because now it's pointing
to the l2.next node. So that we can't point the `l2` pointer to the next node of `l1` anymore, in order to reorder the list. 
In order to be able to point the `l2` to the next node of `l1`, we need to save that link before breaking it. So we need temporary
variables for pointing at the next nodes of `l1` and `l2` before breaking those links between the nodes.

**Edge case:** For the last node in the first half of the list, we want it not to pointing at the first node of second half, but since that last node
of the first place will become the last node of the reordered list, we want it to point at null.