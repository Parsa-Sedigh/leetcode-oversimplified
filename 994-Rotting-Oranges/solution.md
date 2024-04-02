We could be given multiple rotten oranges at the beginning.

The initial rotten oranges are simultaneously going to be making the adjacent oranges rotten.

We have to run BFS simultaneously on multiple sources at the same time. So we have to run multi-source BFS. We have to initialize
the queue with all of the initial rotten oranges. It's multi-source, but we'll still only are gonna be visiting each cell at most once.
So the time complexity is O(n * m) and the worst case the memory complexity is also gonna be O(n * m), because we have a queue.

The way we're gonna know about if there is a fresh orange after we ran BFS on all adjacent oranges, is we keep track of how many
fresh oranges there are initially and then how many are remaining after BFS is done.

We don't use visited hashset in this problem, because we're gonna mutate the grid itself(make the oranges rotten) and we don't do
anything with the empty cells as well.