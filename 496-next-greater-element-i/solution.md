## Hashmap solution

Go through each el in nums2. If it's in `nums1ToIdx` hashmap, it means we need to find it's next greater el. Otherwise,
we can just
skip this el. The reason for this, is that nums1 is a subset of nums2.

Now that we need to query(find next greater el) this el, write a for loop starting from next index and find the first
next greater el.
When you find it, we need to put this next greater el in the correct index in `res`. How we find this correct index?

This index is in `nums1ToIdx`.

## Stack solution

The stack is always going to be in decreasing order, hence it's a **monotonic** stack in decreasing order. And it has to be this way.
Because by definition, if we found a val greater than top of the stack, this el should be the next greater el of els in stack that
are smaller than cur.  So for each of them(smaller ones), we find their index with the help of hashmap and put them in res.

After this, we check if cur is an el that we care, meaning it's in nums1(by the help of hashmap). If it is, we put it in the stack.

So the stack keeps the els that we care about but still haven't found their next greater el. So it helps us solve the problem in one pass
by remembering those els instead of using another loop.

Why we used an inner loop in the second approach?

Because we didn't have a DS for remembering the vals that haven't found their next greater el. So as soon as hitting an el that we cared,
we have to find it's next greater el immediately by using a nested loop. But with a stack, we can put it in stack. And also 
pop from it, if we've found it's next greater el which would be in `cur` variable.
