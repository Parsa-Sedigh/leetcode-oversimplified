In this problem, we actually aren't required to find the square root, because we're not actually trying to return the distance,
we're just trying to determine which point is the closest. For example let's say we had a point that it's `x^2 + y^2` totaled up to
5 and another point that totaled up to 4. Now if we take the square root of 4, it's gonna be `2` and the square root of 5 is gonna be
`2....`. So we're not required to take the square root, because we just want to be able to compare which one is greater. Obviously
we know 5 is greater than 4 so it's square root is also gonna be greater than 4, so we're not technically required to take that
square root.

## Approach 1 - sorting
If we have a list of size n and for each one of these points we compute the distance formula without square root and use the result
of that to sort the entire list of points, the time complexity of that is going to be: `O(n log n)` , the k is not gonna change the
time complexity, because we're sorting the entire list and then once we have that we take the k closest ones.

But since we only looking for k elements, we don't need to sort the entire thing, we just need the k closest points. So this problem
can be simplified using a **min heap**.

## Approach 2 -  min heap
Let's say the input array we're given is: [[1, 3], [-2, 2]], k = 1

Note: We don't take the square root for calculations because it's not needed.

Now the distances are: [10, 1, 3], [8, -2, 2]

Notice we put the distance as the first value. Because when we put these in a min heap, we want the first element of them to be the value
that we order them by in the min heap. Then we run the function `heapq.heapify()` which is not O(n logn), it's actually `O(n)`.
Now we want to pop from this heap k times. Because everytime we want to pop, we want to pop the closest one.

Q: How many times are we gonna pop from the min heap?

A: k times - we want to find the k closest points and what's the time complexity of operation for popping from the heap? It's `O(log<size of the heap>)`,
which in worst case is gonna be `O(log n)`. So we would have `O(k logn)`, that's why the min heap solution is slightly more efficient than
`O(nlogn)`. Because if `k` is small, it's gonna be a lot better than `O(n logn)`