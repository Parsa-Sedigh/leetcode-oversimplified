### Handling edge cases

Inserting a node between other nodes vs at the beginning of the linked list, are 2 different ops.
When inserting a node at the beginning, the head of the linked list is gonna change to the new node. So we have a bunch of
edge cases that we rather not to deal with. To prevent edge cases, we can create a **dummy node**.

So first we create a dummy node as the head of the linked list and it points at the first node.

**With dummy node technique, when we wanna insert a node at the beginning of the linked list, it would be the same as inserting 
between two nodes op. Also, the head of the linked list doesn't change.**

There is no difference between these ops anymore. This approach removes the edge cases.

With singly linked lists, we can't go backwards.