The nums arr are the houses.

### Brute force approach:
We wanna get every single combination. The first combination is where we pick the first house, the decision tree would be:
![](198-1.png)

Note: When we wanna rob the house 3 or 1(the last one), we should choose one of them, because they're adjacent. So at the decision tree,
we have two choices.

But if we didn't rob first house and decided to rob the second house? The max rob would be 3. The decision tree would be:
![](198-2.png)

What is the sub problem here?

We know the first choice is robbing the first index and then find the max from the remaining houses. The sub-problem is finding
the max of a subarray. The second choice is we skip the first index and then we need to find the max of the entire remaining 
subarr(not including first and second vals).

`rob = max(arr[0] + rob[2:n], rob[1:n])`

This is the re-occurrence relationship.

If we didn't rob the first index, then we simply only have the subproblem: `rob[1:n]`

`rob` is the max that we can rob from the entire arr. Each rob can be broken down to it's own sub-problem.

As we move forward, we can decide to rob the current house or not: 
- if we decide to rob it, then we would want the max up until
the two previous value(not the current and previous value). We already computed that value and we just add it to the value of
current house. 
- Or we can decide not to rob the current house, we can use the max up until previous value. We've already computed that value.

Notice we don't have to store the entire blue numbers. To compute each value(max rob up until that point), we only need to look at
the previous two results that we've computed and the reason for this is because we could either decide to rob the current house
or not. If we rob it, we add the max up until two previous elements and current house and if we decide not to rob current house,
just use the max rob up until prev house.