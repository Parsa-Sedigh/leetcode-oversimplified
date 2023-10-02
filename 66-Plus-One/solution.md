By decimal they mean every digit is gonna be from 0-9.

One tedious example is [9, 9, 9].

We need to iterate the array in reverse order. But in code, we're actually gonna reverse the entire array and at the end, we're gonna reverse
it back and return it.

`Time: O(n)` - because we have to iterate through the entire input array which is gonna be of size n

`Space: O(1)`. We don't need extra memory in this solution other than the input array which is not considered in space complexity.

Note: the variable `carry` has the name `one` in the needcode's solution

**Note:** You probably don't need to reverse the digits, you can just traverse it in reverse order.