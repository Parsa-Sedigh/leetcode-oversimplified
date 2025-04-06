from typing import List


# Union find
class Solution:
    # T: O(E * ɑ(V)) - where E is number of edges in the graph and V number of vertices. With our two optimization techniques -> T: O(E)

    # Note: α(V): The inverse Ackermann function, which grows extremely slowly (so much that for practical input sizes,
    # it's nearly constant and considered O(1)). So we could say, T: O(E)

    # M: O(V)
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # why + 1 in len(edges) + 1? Because our nodes start from 1 but len(edges) start from 0. So we want to add 1 to it.

        # T: O(E)
        # M: O(V)
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        # T: O(α(V)). Since we're using both path compression and union by rank(height) -> T: O(1)
        # M: O(1)
        # finds the root parent of n in it's set
        def find(n: int) -> int:
            p = par[n]

            while p != par[p]:
                # path compression: shorten the links as we go up the chain of parents. So it would be faster the next time
                # we go the same route.
                par[p] = par[par[p]]
                p = par[p]

            return p

        # T: O(α(V)). With our two optimization techniques -> T: O(1)
        # M: O(1)
        # returns false if n1 and n2 are already merged. Because they can't be unioned again.
        def union(n1: int, n2: int) -> bool:
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            # union p1 and p2 by rank(in this case their height)
            if rank[p1] > rank[p2]:
                # p1 is the parent of p2
                par[p2] = p1
                rank[p1] += rank[p2]
            elif rank[p1] < rank[p2]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return True

        # T: O(E) - where E is length of edges
        for n1, n2 in edges:
            if not union(n1, n2):
                # we know it's guaranteed that at least one edge is going to lead to redundant connection in this
                # problem. Meaning it's nodes are already merged, so their union() op should return false,
                # so this line will definitely get executed. So we don't have to put another return statement after
                # the loop.
                return [n1, n2]


# DFS
class Solution2:

    # T: O(v^v) IMO
    # M: O(v)
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # T: O()
        # M: O()
        def dfs(node: int, target: int, adjList: dict, visited: set) -> bool:
            if node in visited: return False
            if node == target: return True

            visited.add(node)

            for neighbor in adjList[node]:
                if neighbor not in visited and dfs(neighbor, target, adjList, visited):
                    return True

            visited.remove(node)

            return False

        adjList = {}

        # T: O(E)
        for src, dst in edges:
            visited = set()

            # If both nodes are already connected (i.e., there's a path from u to v),
            # then adding this edge creates a cycle, so it's the redundant edge. Note that this edge is actually the last
            # edge that causes the cycle. Since we have only one edge
            if src in adjList and dst in adjList and dfs(src, dst, adjList, visited):
                return [src, dst]

            if src not in adjList:
                adjList[src] = []

            if dst not in adjList:
                adjList[dst] = []

            adjList[src].append(dst)
            adjList[dst].append(src)
