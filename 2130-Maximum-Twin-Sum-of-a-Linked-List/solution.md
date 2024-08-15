Since this is a singly linked list, we can't move in backwards from the end, so we can't use two-pointers yet.

One way is to dump all of the vals into an arr, then we can use the two-pointer technique. But this will get: M: O(n).

If we are allowed to modify the linked list, we can solve this without additional memory.

We're gonna do a slightly different approach than the hints. Because it's code is easier:

We're gonna reverse the first half of the LL. We reverse the first half and we know we reach the first half when using fast and
slow pointers. We know since we have even number of nodes, we have two nodes at the middle. So we'll have a ref to
the first node in half point and another ref to the second node in the middle. Then move forward these two pointers which
go outwards(they get away from each other as moving forward).

Q: How do we get to the middle of the linked list because we don't have it's length initially? We could compute the length
by going through the whole LL which is O(n) and then go to the middle.

A: There's a simpler way which is called two pointer which is slow and fast pointers.