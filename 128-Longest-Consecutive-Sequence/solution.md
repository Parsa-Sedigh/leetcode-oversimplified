It doesn't matter what order the numbers appear in the input array, we just wanna know the longest consecutive sequence that we can 
**make from** the input array.

The most obvious way to solve this problem is by sorting. But the time complexity is gonna be `O(n logn)`. **Because sorting is `O(n logn)`**.

So the question is: Can we do better?

When we have [1, 2, 3, 4, 100, 200] , we have 3 distinct sequences.

---

### Better approach - using set:
We can get the start of each sequence by looking at our entire array and then we should figure out which numbers don't have a left neighbor.
Meaning, if we wanted to check if 1 had a left neighbour, we would check does our array contain the number 0? If we wanted to know if 100
had a left neighbour, we check does the nums array contain 99? The easiest and most efficient way to do this is by taking our initially array
and converting it into a **set**.

If it doesn't have a left neighbour in the set, it's the start of a sequence. Now let's get the length of this sequence. To find the length,
we check if the next consecutive number exist in the set?

For example: Iterate through the input array(without sorting OFC), when we arrive to a number, we check if it's start of a sequence?
For this, we check if it has a left neighbour, if it doesn't have, it is the start of a sequence. Now let's check the next consecutive number exist
in the set, let's say the current number that we're looking at in the input aray is `a` - we just look if `a + 1` exist in the set or not. 
If it does, we can make the current sequence a little bit longer. Then check if the `a + 1` exist in the set and ... .

Time: `O(n)`

Space: `O(n)` - we used additional memory to create a set. Because we wanted to check if neighbours existed in the set

Note: n is the size of the input array