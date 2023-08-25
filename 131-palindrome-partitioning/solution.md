One thing to notice is: no matter what string we're given, it's possible to partition it in the way the question is asking. Why?
Because let's say input is `aab`, we know that any single character is a palindrome. So one way to partition this is take each character
and separate it.

The brute-force way to solve this problem happens to also be the mai nway to solve it, which is backtracking.

We're gonna create every single possible way to partition this and then check if those partitions form palindromes and if they do,
we're gonna add them to our result.

**Note:** The elements of each partition that is valid, should all be palindromes.

Note: Backtracking is not an efficient way.

Time O(N * 2^N) | Space O(N^2)