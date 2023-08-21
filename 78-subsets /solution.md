[1, 2] and [2, 1] are considered the same. We don't care about the order. This is not a permutation. This is a subset. So we consider
these duplicate.

If we want to create all the subsets from the given input, for each element, we have 2 choices:
- include that element in the subset
- not include it

So for each element we have 2 choices. In other words we have 2^n choices for all of the subsets where n is the size of the input.

`2^n = number of subsets`

How long could a subset be?

This is not gonna be an efficient problem to solve. We have 2^n subsets and each subset could be up to n size. So worst case time complexity is
`O(n * 2^n)` regardless of how efficient we make it. Because given the constraints of this problem, we don't want the number of subsets, we want the
subsets themselves. We have to make it inefficients.

So we must do brute-force. Let's do backtracking. This is pretty much the most efficient way.

The decision tree:

![](../img/78-1.png)

The two `dfs(i + 1)` calls that we have although they look the same, they're gonna behave slightly differently. Because the first dfs() is gonna
have a different subset when executing(the recursion calls) and the second dfs() is gonna have an empty subset given to it.

Note: Luckily the order of subsets in the result doesn't matter(the order that we put the subsets in, doesn't matter).