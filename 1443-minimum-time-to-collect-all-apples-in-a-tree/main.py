from typing import List


# 1. Depth First Search
# The solution uses a graph representation of the tree

# T: O(n)
# M: O(n)
# The space is dominated by the adjacency list (O(n)) and the recursion stack (O(H)), resulting in an overall space complexity of O(n).

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # initializes the adjacency list for all n vertices, where each vertex starts with an empty list of neighbors.
        # T: O(n)
        # M: O(n)
        adj = [i for i in range(n)]

        # After this loop, adj fully represents the tree structure, allowing traversal in
        # any direction(since tree is undirected) from any vertex.
        for child, par in edges:
            # Since the tree is UNDIRECTED, each edge is added to both vertices
            adj[par].append(child)
            adj[child].append(par)

        # T: O(n) - The depth-first search (DFS) visits each node exactly once, which is O(n).
        # M: O(H)
        # NOTE: We don't wanna stuck in an infinite loop. The only way we get stuck here is if we keep going from par
        # to child and then from child back up to par. To avoid this, for every node, pass it's parent as well to check for this.
        def dfs(cur: int, par: int) -> int:
            # NOTE: each time we start a dfs from a vertex, we wanna track the total time of getting all apples starting from that vertex.
            # So initialize this var for each dfs.
            # NOTE: total time to get all apples from the subtree rooted at `cur`
            # If a vertex has no children (other than its parent) and no apple, time remains 0, naturally handling leaf nodes.
            time = 0

            # instead of left and right subtrees like (dfs(left), dfs(right)), we go through the children using a for loop.
            for child in adj[cur]:
                # We don't wanna go upwards towards parent of cur. We wanna go downward(this is a dfs algo).

                # NOTE: Since there's an edge between cur-par and also par-cur, we should be careful not to go upwards which in that case,
                # the par is child. Because let's say in adj we have: {2: [1, 3, 4]}, meaning 2 is child of 1. But it also
                # has an edge towards it's parent, but we don't want to traverse that. In this adj, 1 is a child of 2(because of tree being undirected).
                if child == par:
                    continue

                child_time = dfs(child, cur)

                # We only include the time to visit a child if:
                # 1- The child’s subtree contained at least one apple, meaning: child_time > 0
                # 2- The child itself has an apple, meaning: hasApple[child]
                # If either condition is true, add 2 + childTime to time:
                # - 2 accounts for round trip (1 unit to go to the child, 1 unit to return).
                # - child_time is the time to collect apples within the child’s subtree, which must be added to the total time.
                # NOTE: So if there's some nodes in subtree rooted at `child`, that are apple, we need to
                # add `the time to get them` to `time` + the time to get to the child which is 2.
                # For example, a leaf vertex doesn't have any child_time itself, but could be an apple itself. So we use `or` in the cond.

                if child_time > 0 or hasApple[child]:
                    # time to get to the child(2) that has some apples in it(either itself or it's subtree).
                    time += 2 + child_time

                return time

        # root vertex doesn't have a parent. So we pass a vertex that doesn't exist in the graph at all - like `-1`.
        return dfs(0, -1)
