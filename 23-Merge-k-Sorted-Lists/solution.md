We're extending #21.

Brute force approach: for each list, iterate it and merge it into the current result. We have k lists and the total number of nodes we have
is n, so everytime we're merging a list, we're gonna potentially have to iterate through every single node we have.

`Time: O(n * k)`

---

approach 2: Using merge sort

**How many times we can divide k by 2? log k**

Yes again we have to potentially iterating through every node, so we have a O(n) . But we're dividing the lists by 2 every time.
Now how many times we can take k lists and divide them by 2? `log k`. log k is the number of times where we're repeating this O(n) step.

Neetcode: `Time: O(n * log k)`

Bard: Breakdown of the complexity:

- Merging two lists: The mergeLists function has a time complexity of O(n), where **n is the length of the shorter list between the two being merged**.
This is because the comparison and insertion happen based on the shorter list.
- Reducing k lists: The outer loop iterates through pairs of lists merging them until only one list remains. The number
of iterations required is approximately log(k) (similar to merge sort analysis). 
- Total complexity: Combining the two factors, the overall time complexity becomes O(nk log(k)).

This revised version clarifies that the overall complexity depends on both the total number of elements (n) and the number of 
individual lists (k). While the average length of each list (K) influences the actual runtime in practice, using m provides a more general 
and accurate expression of the time complexity.

---

approach 3: Heap