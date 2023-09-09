There are two solutions:
- first one with O(26 * n)
- second one with O(n)

Note: Every string itself counts as a permutation of itself. So ab counts as a permutation of itself.

We're looking for a window in s2 the same size as s1 and it has to contain the exact same characters with same count. So it's the
same thing as looking for an **anagram**.

Now if we were comparing the exact characters, that would be annoying: O(n * m) where n is size of s2 and m is size of s1.
But we can do it a bit better in O(26 * n) if we use a hashmap. Why 26? Because the question tells us all the characters in both of the
strings are gonna be limited to a-z. Therefore, the size of the hashmap is gonna be at most size 26.

We're gonna have one hashmap for s1 and it's gonna stay the exact same and also a second hashmap for s2 which is gonna have the characters
of the **current window** that we're at. So everytime we have a new window(each time we shift our window to the right), we're only adding
one character and removing the character that was on the left(because of fix sized sliding window) and then we're gonna compare them
if they're equal which is a 26 operation(there's only at most 26 characters), so O(26 * n).

But there's a better way.

---

### slightly more optimal solution - O(n)
We still have two hashmaps.

The difference in this solution is we're not actually gonna be comparing the two hashmaps together. We won't need to. Because we're gonna
keep track of one more variable named `matches`. This variable is gonna be a shortcut that's gonna allow us to not have to compare the
entire hashmaps each time which we know in worst case is O(26 * n), because we're looking through every key of hashmap which in english
can be 26.

The matches variable is gonna maintain the total number of equal characters in each of the hashmaps. We wanna know: Does the `a` count of
s1 and s2 match? If yes, do `matches + 1` and we wanna know the number of matches for every single character and we wanna know that
initially.

Note: Although s1 and s2 maybe doesn't have all of the a-z chars, we can't make the count of absent chars as 0 in each hashmap.

Once we have 26 matches, that means that for some window in s2, we have 26 matches with s1.

Note: For the **only** time we are actually gonna iterate through both of the hashmaps comparing each character. We actually do have to do 
that at least one time, but it's a `O(26)` operation and then after that, we'll only have to iterate through the s2 string, so the overall
time complexity: `O(26) + O(n) = O(n)` .  This is definitely better than `O(26 * n)`.

As we make changes to the s2 hashmap(which means shifting the window), we wanna know does it affect the number of `matches`. So when shifting
the window, we update s2 hashmap and if a mismatch was introduced we decrease the `matches` variable. Note that when we shift the window,
we remove one character form the beginning and add one to the s2 hashmap.

Note: Whenever the `matches` value gets to 26, we stop the algo and return true. Because all we're looking for is does a single permutation of
s1 exist in s2 or not?(Does there exist an anagram of s1?)

Time: O(n)

Note: We can implement the s1Count and s2Count as arrays instead of hashmaps as well because we're working with fixed number of values in this
problem(a-z) and we can say each position of array is the count of that character in alphabet, in order.

Note: It's better to use a hashmap instead of array for this solution.

---
### edge case
If s1 length is longer than s2 -> it's impossible to find a permutation of s1 in s2.
