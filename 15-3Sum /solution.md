The input array can have duplicates. One problem is we can not have duplicates in our result.

## Brute force way:
We need 3 numbers so we're gonna have 3 loops. Get every single combination of three numbers.

We don't want to have duplicate triplets. In order to do this, we don't want the same element in the same position of a triplet. Because
then if there are some numbers after that element in input array, we could potentially have duplicates.
For example if we had -3 in the first position of a triplet before and now we encountered -3 again for that same position, we should skip it.

The format of a result array is: [a, b, c] where a, b and c are placeholders for numbers that add up to zero. Now if we had -3 in position a
and we again put it in position a, this would be a recipe for finding duplicates, which is not what we want.

To fix this problem, we need to sort the input array.

When we find first number of triplet, we need to find the other two, but now we're facing a two-sum problem.

Time complexity:

We're sorting so -> O(nlogn)

and then we're using the fact that the input array is sorted to our advantage. We're using one loop to tell us the first element of a triplet and
we're using a second loop to solve two-sum. So O(n^2)

So in total we have: O(nlogn) + O(n^2) ---> O(n^2)

Space complexity:

Depending on the implementation it could be O(1) or O(n). Because sorting actually does take extra memory in some libraries and languages.