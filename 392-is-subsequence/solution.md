Subsequences come up a lot especially in DP problems.

## two pointer approach

pointer i initialized at beginning of s and j at the beginning of t.

- When we don't find a char, just shift the j pointer and i stays where it lives. Because we haven't found the char that
  i points at, yet.
- But when we found a char of s in t, we shift both pointers.

Once i is out of bounds, that means we found every single char in s, in t, so s is a subsequence of t, so we can stop
the algo and return True.

If j is out of bounds, but i is not, it means we have to return False. j is out of bounds before we find every char we
need to. s is not a subsequence of t.

This is O(n) algo where n is the **total** number of chars we're given in s and t. So n = len(s) + len(t) .