There are many ways to solve this problem. The easiest way is to iterate through every el in the input arr and then
take each value and append it to the arr.

Another approach is to create an output arr(it's size is 2*n of original arr) and initially it's empty.
If this problem was asking for three times concatenation or a larger number of times, this approach is more extensible.

We're doing a push O(n + n) times, because input arr is of size n and we're creating a concatenation of it, so n + n
times. So T: O(n).