The hard part is that as we're creating new nodes as copy, the random pointer might point to a later node that
we haven't created yet.

So how can we assign a random pointer before the node it's pointing to is not created yet?

A: We're gonna do two passes. The first pass is gonna create a deep copy of the original nodes. We're not even gonna link them yet. 
They're just linked to original nodes. The first pass is also gonna create a hashmap where we map the old node to it's copy.

In second pass we're gonna do pointer connecting.