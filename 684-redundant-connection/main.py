from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # why + 1 in len(edges) + 1? Because our nodes start from 1 but len(edges) start from 0. So we want to add 1 to it.
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        # finds the root parent of n in it's set
        def find(n: int) -> int:
            p = par[n]

            while p != par[p]:
                # path compression: shorten the links as we go up the chain of parents. So it would be faster the next time
                # we go the same route.
                par[p] = par[par[p]]
                p = par[p]

            return p

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

        for n1, n2 in edges:
            if not union(n1, n2):
                # we know it's guaranteed that at least one edge is going to lead to redundant connection in this
                # problem. Meaning it's nodes are already merged, so their union() op should return false,
                # so this line will definitely get executed. So we don't have to put another return statement after
                # the loop.
                return [n1, n2]
