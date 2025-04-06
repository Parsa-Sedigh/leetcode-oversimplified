## O(n) space
shuffle method

This problem is easy to do if we allocate a separate arr for the output.

- Time: O(n)
- Space: O(n)

## O(1) space - without declaring an output arr
shuffle2 method

Requires bit manipulation.

We know the maximum val in the input arr is going to be less than or equal to 1000(from the problem's constraints section). What that
means is that normally we have integers and they take up 32 bits(not in python but in most langs a number will have 32 bits allotted for it.)
If a number is gonna be less than or equal to 1000, it's not gonna take up those full 32 bits. A number of 1000 can be represented
with 10 bits. Because 2^10 = 1024. So 1023 is the max integer we can represent(1024 - 1).

So we only need 10 bits.

Now here's the tricky part: For every val in the first half of the arr(until `n`), what we can do is combine the pair of values.
We can take x and y and then store them in the first spot. Then we can take the next pair of x and y, store them together in the second spot.
Why we can do this?
Because we have the 32 bits available for us, we know each of these values is gonna require 10bits, so we can store them together in 32 bits.

Q: Now why exactly we want to do that? Suppose we can do it, why would we do it?

A: Let's say we have those all those pairs ready in the first half of the arr. What we can do? By iterating from the beginning to the end,
we can extract those values. We can extract x and y stored in each index(spot). The x val is gonna stay in that spot, but the y val
needs to go to the next position. But notice there's a problem here because if we take the y and overwrite the next spot, we would lose
the next spot's val! This is the problem with this solution. This problem is hard to solve without extra memory, or in another approach,
without overriding data. But it is possible. Instead of going from the start to the end of the arr, we're gonna go from the end to start.
We can extract the values and store y in the last position and x in the second to last position of the arr. Then go backwards, now extract,
put y in the third to last position and x in fourth to last position and ... .
We do this for every pair in the first half of the arr.

The reason we stored them in the first half of the arr is we didn't want to override data in the second half that we're gonna need later on.
Again, why we stored them in the first half?

Because we're gonna iterate from the end to start, now if we stored them in second half and go backwards, we're gonna encounter a value again and
it would be overriden.

---

There are a couple of bit manipulation tricks:
- how can we store the x and y values in a 32-bit integer?
We know by putting x into the 32 bits space of a variable, it's gonna take up to the first 10 bits. One thing we can do is take this x and
shift it to the left. This makes 10 first bits available for us to add the y value. So y would take up to the first 10 bits and x will take up to the
next 10 bits. How do we add y? That's bit wise OR. Because we know when the x value is at the second 10 bits, the first 10 bits are gonna
filled with 0s. Now whatever y value is, maybe it's 4 which is `100`, all those 0s are gonna be ORed with `100`.
That's how we store the values in bits.
- how to extract x and y from a variable(32 bit integer)?
One way to do that is by using bit wise AND operator using a bunch of 1s. For example, for getting x, we just shift it 10 bits to the right.
To get y, we need 10 1s to logic AND it(why ANDing with 1s? Because ANDing with 0s will make all the bits as 0!). Because y is occupying 10 bits.
We need 10 bits to AND the y with them. Now how do we get 10 1s in a row? Well we take 2^10 which is gonna be a 1 followed by 10 0s and then
we subtract 1 from this number which is gonna give us a 0 followed by 10 1s. Note that that 0 is not important here and won't cause problems because
y is 10 bits and we have 10 1s to AND it with.
So we need `2^10 - 1` which is gonna be a 0 followed by 10 `1`s. So `2^10 - 1`is the number we logic AND the number in 
the spot, in order to extract the y value.

- Time: O(n)
- Space: O(1)


