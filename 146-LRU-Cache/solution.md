We're gonna keep the key-value pairs in order. Because we wanna remove the least recently used. So we gotta remember in what order
we added these key-value pairs. But we're trying to do this in O(1). So how can we know instantly, what the value of a key is?
The easiest way to do that is with a hashmap.

The size of the hashmap shouldn't exceed the capacity.

As the key-value pair, it's better to make the value be a pointer to the node itself(a pointer to a Pair instance).
So the key of the hashmap is the same key we get from the input and the value is a pointer to the node in the doubly linked list.

We're gonna keep track of the most recent and least recent by having a left and right pointer.

**The left is for least recently used and the right one is for most recently used.**

We're gonna be swapping these two nodes. To keep the ordering of these, we need a doubly linked list.
Why doubly? Because remember we can easily look up where the value of the key is in the hashmap, but if we also want to reorder them quickly(which
happens everytime we use a get()), we wanna make that node, the most recently used. But when doing a get(), the hashmap won't need to be updated
to accommodate for the least recently used and most recently used. Because the values are gonna be pointers and they will point to the correct 
node(since we reordered the linked list).

The left and right pointers are also gonna be dummy nodes.


**Note: Dummy node means it's `.next` will tell us the actual node we want.**

Remove:
![](../img/146-1.png)

Insert:
![](../img/146-2.png)