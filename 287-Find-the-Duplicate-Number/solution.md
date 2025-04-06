The len of the arr is n + 1. Every single val is gonna be within [1, n] inclusive. This implies at least one of the els is gonna be
duplicate and the question says only one el is duplicate. Why? Because there's n different vals but there's n + 1 positions.

Easy way to solve this is using hashset. We don't need hashmap since the mapping doesn't matter, just the
key matters, hence using hashset.
- T: O(n)
- M: O(n)

But the question says M should be constant or O(1). We can't modify the input arr as well. So we can't sort it.

##  Floyd's algorithm(tortoise and hare)
1. this is a linked list cycle problem.
2. know floyd's algo which tells beginning of a cycle in the LL

**Think** of each el as a pointer. If we do this, each val is gonna point at some position in the arr.
So the val of el specifies the index at which it points, for example:
[1, 3, 4, 2, 2]

The el 1, points to index 1. The el 3 points to index 3. The el 2 points to index 2 and ... .

No matter what val we look at, it's gonna point at some val inside the arr. It's never gonna be an exit condition. None of these
vals are gonna point outside of the range.

We can draw the LL version of the given arr:

So the range [3 ... 2] forms a cycle. But el 1 is not in the cycle because none of the other els is pointing at index 0(we don't
have any el with val 0).

When we have a duplicate num, that means there are multiple nodes pointing to that node in the LL. So that number is the start of
the cycle in LL.

The beginning of the cycle in equivalent LL is the result we wanna return. It's the duplicate val.

Note: The p portion could be very long. It could be longer than the entire length of the cycle. But the math would work. But in this
case, the fast must loop the cycle multiple times until it meets the slow.