Stream means we can continue to add numbers to the list of numbers.

`They say that the kth largest element is the kth largest in the sorted order, not the kth distinct element` and what they mean by that
is if we for example had: `k = 3, 1, 2, 2, 3`, meaning we want the third largest number, if we look at the distinct values, 3 is the largest,
but they say we wanna return the kth largest in sorted order, meaning 3 is the first largest, 2 is the second largest and 2(first one
from left) is the third largest. We're not just looking at the distinct elements, if we had multiple copies, we include those as well.

The initial list of elements(`nums` arr), it could be at least k elements or it could be less than k elements or it could be more than
k elements. So that's sth we're gonna have to take care of.

Note: They do tell us that whenever we call the `add` function, we're guaranteed to have at least k elements in the stream. So that's good.
Even though we might not have k elements when we initialize it(the original array might not have k elements), we will have k elements
when we call the `add` function.

---

How can we efficiently solve this problem?

## Scan the original array
Scan through the entire input to find the kth largest

`Time: O(n)`

## Sort
The intuitive approach is to sort the input array, so that we can look through and find the kth largest element a little bit faster.

When the array is sorted, we can use the binary search to find the kth largest which will run in `O(log n)`

`Time: O(log n)`

But the problem is inserting a new value. So when we run `add(3)`, yeah, we can use binary search to add the value as well. We can find where
to insert it using binary search. But when you insert in a middle of the array, it's a `O(n)` operation.

**Note: Inserting into an array is O(n).**

So the question is: Is there a better approach, is there a different DS that we can use? Yes, the DS that's gonna help us the most in this case,
is a **min heap** and we're gonna require it to be of size k. Why?

## Min heap

Because a heap is a DS that has a somewhat a sorted property. We can add and pop elements from the min heap in `O(log n)` time.
We can also get the minimum value of the min heap is `O(1)`. Obviously this is a little bit better than an array especially in an unsorted array.

Q: Why are we going to require the heap to be of size k? and why are we using a min heap rather than a max heap?

A: One thing we're gonna use to our advantage is that we're only gonna be adding elements to our stream of data, we're never gonna be removing
anything. So in example of: `k = 3, [4, 5, 8, 2]`, we're given 4 numbers, but we only need a min heap of size k, because we only need the
k largest values from the array. In this case, it's 4, 5 and 8. Why is that? Why do we never need the 2?

Because we want the third largest value, so we have three numbers that are bigger than 2. Is 2 ever going to be the third largest value in our
stream of data? No, it's never going to be. Because we're never going to remove any of these elements. We might add elements.
Another thing: If we add 6 to the previous example using add(), we don't want to include 4 anymore. Then we only wanna keep track of
6, 5, 8. Now 5 is gonna be the third largest element. So 2 is never going to be in our min heap of size k. If we added a small element
like 1, we don't care about it.

**Note:** Kth largest means the kth smallest element! So we can be clever and create a min heap of size k. Now the kth largest element is actually
the minium value of our heap of size k, which would be the root node, so we can get it in O(1).

About `add` function: Let's say we wanna add 3 to [4, 5, 8], how do we know 3 is included among our kth largest values? There's multiple ways,
but the easiest way is to take that 3 and add it to our min heap, so now we have 4 values in our min heap of size 3. We added that 3 in `O(log n)`.

Now we want to pop the minimum value from min heap, because we want the third largest value but we have four values. Let's pop the **smallest** one,
which is 3, we can do that again in `O(log n)`. Now we wanna know among the remaining, what's the smallest value? 4.

So we can do the add function in `O(log n)`.

How many times are we gonna run the add()? Who knows. Let's call it M. So the overall time complexity of add() if we count all the function calls: 
`O(M * log n)`.

Now in terms of our constructor function, generating the entire heap is potentially in worst case: `O(n log n)`. Because we turn the whole
input array into a heap in O(n), but then remember, we had to keep popping elements until we only have k elements in the heap. A pop
in heap is gonna be O(log n) and potentially we're gonna pop `n - k` times, so time complexity of constructor function is: `O((n - k) logn)`.
k could be really small => `O(n logn)`.

`constructor function time: O(n logn)`

`add function time: O(log n)`. If we were using an array instead of heap(which is implemented by array, but has special properties), the time
would be O(n)

**Edge case:** our heap might be initialized with less than k elements. If it has more than k elements, the while loop in constructor function
is gonna run, which is good, but what if it has less than k elements? Then if we add a value to the heap, we don't want to pop from the heap which
is what we do in `add` at all if it has less than k elements of equal to k elements. So we only wanna pop if the len of minHeap is greater than k.