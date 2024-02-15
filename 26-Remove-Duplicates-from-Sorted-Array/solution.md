The difficult part is solving this without extra memory.

The return value is how many unique values are in the input arr. We also need to update the arr so that it doesn't contain duplicates, so we can't
just return a number, we also need to update the arr.

**If we could allocate extra memory**: Go through the arr and if you encountered a new element that you haven't seen, add it to the new arr.
Note that since the input arr is sorted, we don't need to keep a hashmap of all the previous unique elements, we just need to check the
previous unique value with current value to see if it's a new value that needs to be added to the new arr.

Solution: We need a pointer like l which is gonna tell us: next time that we see a unique value, we're gonna put it wherever the
l pointer happens to be. The l pointer will also tell us how many unique values we've already seen so far. So the l pointer also takes care of
output value for us.

Q: How do we know as we're going through the arr, if this is a unique value or not? In other words, this is the first time we're seeing this
value or not?

A: Since this arr is sorted in ascending order, by looking at the previous val, we can say if this is the first time we're seeing a val.

Note: We're gonna initialize both l and r at the second index. Why? Because we know that the first value is gonna stay where it is.