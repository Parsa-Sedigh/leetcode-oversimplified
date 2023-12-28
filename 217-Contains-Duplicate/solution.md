Approach 1: Brute force

Go through every el and compare it to every single number in the rest of the arr.

- Time: O(n^2)
- Space: O(1)

---

Approach 2: sorting

Take the arr and sort it. If we sort it, then any duplicates that do exist in the arr, they're gonna be adjacent. So when we're trying
to detect any duplicates in here, we can only iterate through the arr once and as we do that, we're gonna be comparing two neighbors and see
if they're equal(duplicate).

- Time: O(n log(n))
- space: O(1) . Note this is correct if you don't count the space that's used by the sorting algo

If we use more extra memory, we can achieve better time complexity.

Approach 3: Hashset

Hashset allows us to insert elements into the hashset in O(1). It also allows us to search in O(1).

This is worst case as always:
- Time: O(n)
- Space: O(n)