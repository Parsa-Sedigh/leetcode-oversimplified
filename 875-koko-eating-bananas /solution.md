Brute force solution:

Koko can only eat at most one pile in a given hour. This tells us `len(p) <= h` because if for example we have 5 piles and let's say
we had h=4. With this given h, koko can't eat all of the piles because she can only 1 pile per hour. This is why they guarantee us h
is always gonna be greater than or equal to number of pile.

The brute force approach is to start at index 0 and divide each element by 1, 2, 3 and ...(possible values of `k`) until we find the proper `k`.

Q: We know the min value for k is 1(can't be 0 because that would mean we're not eating any pile), what's the maximum of k given the input array and
number of hours?

We know the number of hours is always gonna be greater than or equal to the number of piles(len(p) <= k), so in the worst case(maximum value of k
which is not what we want, we want the minimum value of k), maximum value of k is the maximum number of bananas in a pile(maximum element of the
array) and with having k as it's maximum possible value, that means we're able to eat the maximum pile in exactly 1 hour and if we can eat the
max pile in 1 hour, that means every other pile is also gonna take 1 hour(for each).

Note: We can't have k as 100 or 200 or sth crazy. Because it's not the minimum. We want the minium value of k, the less, the better! So the maximum(worst
case in this case), is the maximum value of the array.

So in brute force, we can try every single value for k from 1 to the max value of array and the first value that we get that allows
us to eat every single pile in less than or equal to h, is gonna be our output(1, 2, 3, ... as k).

Brute force Time complexity: `O(max(p) * p)`.

We're getting max(p) from the fact that we have to iterate through every single value in the **range of possible values for k**. Which in worst case we have
to go through every single possible value of k, but we can instead apply binary search which can reduce max(p) to `log(max(p))`.

Time complexity: `O(log(max(p)) * p)`.

**Note:** Applying a log on a value will reduce it(log(p) < p).

---
input array: [3, 6, 7, 11] h = 8

We wanna every single pile in less than or equal 8 hours.

So we know that the potential rate that we're eating bananas is gonna be between 1(minium it can possibly be), whatever the max value in input array is(max
possible value) and we can find this max in linear time.

Then do a binary search to find the minimum k. For each possible k, divide each element of input array and **round it up**(we can eat at most
1 pile at every hour). So round .5 to 1 and 1.2 to 2 and ... .

- If you found a k that is less than h, you need to still continue finding the minimum value of k because we want to find the minimum, so continue doing the
binary search on smaller values.
- But if you found a k that is more than h, it means we went over our threshold(h). We took too long to eat these bananas. So we need searching towards
the right of the current index. So move left pointer to index + 1 and continue the binary search.

Note: We don't need to actually create an array of all possible values of k(Do not allocate memory). We just need left and right pointers for
possible values of k and we move them closer until we find the minimum possible value for k.