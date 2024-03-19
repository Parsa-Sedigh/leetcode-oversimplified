How many times can we divide the arr by 2?

A: log base 2 of n. This evaluates to how many times we can divide n by 2.

So binary search is log base 2 of n algorithm which is much more efficient than O(n) algo.

There's a bug in line:
```python
m = (l + r) // 2
```
Technically the bug doesn't exist in python because python integers are unbounded. They can
be pretty large. But in most langs like java and C++, you might encounter an overflow. Because suppose we had a
very large input arr and then l and r were very close to 32bit integer like they were 2^31. Then adding them together would
possibly overflow and then we would get the wrong result for m. So how do we fix that?

A: We can still calculate the mid way point between l and r without adding them together! Because we can take the 
distance between them by taking `r - l` and then dividing that by 2 will give us half of the distance between them and we can take 
that and add it to the left index(l) which gives us the midway point:
```python
m = l + ((r - l) // 2)
```
So this gives us the exact same result but this way it will never overflow. Because we're not adding l and r together.