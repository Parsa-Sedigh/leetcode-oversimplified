from collections import deque
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# DFS
# T: O()
# M: O()
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # maps old nodes to new nodes, so that we don't create another clone of the nodes, if we already have them as we continue the
        # algo.
        oldToNew = {}

        # Edge case
        # if not node:
        #     return None

        def dfs(node):
            # if we've already made a clone of it, return that clone
            if node in oldToNew:
                return oldToNew[node]

            # the clone of this node doesn't exist, create it
            copy = Node(node.val)

            # map the old node(node) to the new node(copy)
            oldToNew[node] = copy

            for nei in node.neighbors:
                # the return value of dfs(nei) is the clone of nei. So we wanna append the clone of the neighbor to the list
                # of neighbors of current node.
                copy.neighbors.append(dfs(nei))

            return copy

        # You can have the check of the node being None here, or in the beginning of the method(commented).
        return dfs(node) if node else None

# BFS
# T: O(N) where N is number of nodes
# M: O(N)
class Solution2:
    # Visit neighbors
    # if neigh is not in cloned, add it to cloned, then add it to queue
    # add neigh to list of neighbors of current node
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cloned = {}
        cloned[node] = Node(node.val, [])
        q = deque([node])

        while q:
            cur = q.popleft()

            # clone all of the neighbors if they aren't cloned yet.
            # We don't need a visited hashset here, because our cloned dict will actually act as a visited set
            for nei in cur.neighbors:
                # nei represents the original node not the cloned version
                if nei not in cloned:
                    cloned[nei] = Node(nei.val, [])
                    q.append(nei)

                cloned[cur].neighbors.append(cloned[nei])

        return cloned[node]