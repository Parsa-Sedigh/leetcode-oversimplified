An island is not considered when we have diagonal 1s.

When we get to a 1, we got to an island but then we want to mark the contiguous(vertically or horizontally not diagonally) land of this island as visited.
So the adjacent neighbours(1s) of this one also have to be marked as visited.

We need to use BFS. We're just doing a graph traversal algo starting at the top left and marking each layer of 1s(normal BFS).
The layers for the first island are specified with a line in img.

Note: bfs is not a recursive algo, it's iterative, so we need a DS to use for memory, so a queue is normally used for BFS.

Note: The neet thing about writing it with this approach is: If your interviewer ask you at the end to do it with DFS, you can do it 
really easy by swapping the popleft() with `pop()`(pop from right) which would pop the most recent position of the queue() instead of the first element
that we added, which means it'll basically be a DFS. But it's non-recursive, it's iterative.