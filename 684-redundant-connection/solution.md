We're given n nodes and n unique edges. Is it guaranteed that we're always gonna have a cycle? In other words, if we add
an edge
to a connected graph, then we're gonna have a cycle, why?

A: Yes, if we have n nodes and n unique edges, we're gonna have a cycle no matter what.

---

Example of union find algo: Let's say we have [[1, 2], [1, 3], [2, 3]] as list of edges. n is 3.

Par arr would be: [1, 2, 3]

Rank arr: [1, 1, 1] or you can say: [0, 0, 0]

To run the union find algo, go through the list of edges:

1. edge [1, 2]: we wanna union node 1 and 2(connect 1 and 2). Get the ranks of both nodes. Both are 1.
   We can set 1 as parent of 2. So in par arr, so instead of 2, write 1. Now the par arr is: [1, 1, 3]. Now the rank of
   1 would be 2.
2. edge [1, 3]: rank of node 1 is 2 and rank of node 3 is 1. So 3 is gonna be the child of 1. Now the par arr
   is: [1, 1, 1] and
   rank of node 1 is gonna be 3. So rank: [3, 1, 1]
3. edge [2, 3]: we wanna connect 2 and 3 together. So first go to their parent. But their parent is the same. That means
   if we add
   this new edge to the graph, we're gonna add a redundant connection. So this edge is the edge we wanna return as the
   result.

Note: The rank updates in the solution is different than the one in pamphlet of neetcode-advanced-algorithms. But it's
fine. Because the actual value of ranks doesn't matter. Instead, the comparison of them matters. 