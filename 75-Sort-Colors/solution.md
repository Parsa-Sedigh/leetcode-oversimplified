Many ways to solve this with varying efficiencies and memory complexities.

**Programming language's sort func is `n*log(n)`.**

---

Approach 1: Bucket sort

The question description states that there's only 3 different potential values => 3 different buckets.

If the values ranged from 0 to n where n could be an arbitrary large value, then we couldn't do this in O(n).

Yes we need extra memory but it's gonna be a constant in size => Memory complexity: O(constant) => O(1)

We have to go through the entire input arr twice: once to create the buckets and then once to overwrite the input array and make
it as the output arr.

- Time: O(n)
- Space: O(1)

---

approach 2: One pass solution

We know the partition part in quicksort.

If we take a value pointed by i and swap it by the value pointed by r pointer(based on the defined conditions), we could potentially
introduce 0 in the middle of our array which is sth we don't want to do. In that case if we do that, we don't want to shift our i pointer.
For example, in case of [0, 1, 2], if we ever encounter a 2, yes we're gonna swap it with the r pointer but in that case, we're not gonna increment
our i pointer. But that's not gonna be the case if we find a 0 pointed by r and then swap it by the value pointed by l pointer. In this case,
we do increment the i.

Once i surpasses the r, we're done because we know the portion to the right of the r pointer is gonna be sorted anyway. So we're done.