The graph is completely connected, this is convenient.

When edge is undirected, it means node a is the neighbor of node b and vice versa.

Time: O(E + V) where E is number of edges and V number of vertices. Because we have to create a clone of each of the edges and vertices.

---

Cracking FAANG:

When a question involves "cloning" like cloning a linked list or graph, we wanna maintain a mapping dictionary which the key is the old node and
the value is the new cloned node.

Traverse the old graph using a queue, clone each node, put it in mapping dict.

We touch every single element once, so: T: O(N) where N is number of nodes in the graph.

We're cloning our original DS, so the amount of space we need to store all those nodes, depends on how big the original graph is,
which is the number of nodes in our original graph.