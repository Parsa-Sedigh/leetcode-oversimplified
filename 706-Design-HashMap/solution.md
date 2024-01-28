We will have at most 1000 operations, so we won't need to store more than 1000 elements(if all operations are put).

It's misleading to say we have multiple values(in the linked list) stored with the same key, it's just that those multiple keys will
map to the same index in the underlying arr, they are actually different keys(this happens in case of collision and we handle it using
changing).

Edge case when removing:

What if we were removing the first node in the linked list? Well there's no previous pointer, so we would need additional conditions
to handle this case. An easy workaround is to initialize the linked lists with a dummy node(even though there's no node with values).
So if wanted to remove the first node, we have a previous node(the dummy node).

The way we write this hashmap, is the way that it's not gonna be O(1) in every case, because we could have a bunch of values that are
inserted at the same index. But **on average**, assuming they're evenly distributed, it's O(1).

We don't implement the rehashing(increase the capacity of the underlying arr).