We don't need make those replacements.

Time: O(26 * n) -> O(n)

---
### brute force:

Check every single substring and we know there's `n^2` substrings.

---
### Sliding window:
How do we know if a window is valid?

We're gonna do take the length of the window and count(number of occurrences) of the most frequent character and subtract them.
Now what does the result tell us? It tells us the number of characters in our window that we need to replace in order to make them
match the most frequent character of window.

As long as the `result value <= k` condition is true, that means our current window is valid, that means we have enough replacements
to make in our current window.

Q: How are we gonna know which character is the most frequent?

A: The brute force way is taking a look at our map of counts and we know the max size of this map could possibly be 26(26 different characters
in english). So finding the max character in the map is gonna be O(26), so that's a little bit more inefficient thant we would like but it's
technically still O(1) . This is why we have O(26 * n) as time complexity of overall algo.

We're gonna use sliding window technique, so we're gonna take our window starting from the beginning, expanding it as long as the condition is
valid, if the condition is not valid, then we're gonna take our left pointer and shift it until the window becomes valid once again.

`Time: O(26 * n)`

---

### Better approach(clever way):
There's one way you can do it without having to look through the entire hashmap everytime you want to find the most frequent character that occurs.
To do this, we have another variable called `maxF`(maxFrequency) which is the count of the most frequent character at any given time.
Now one problem is: If we're trying to maintain the count of the most frequent character, what happens when we take our left pointer
and shift it forward? Because when we do that, we're removing a character and therefore we need to update our count map. In that case,
we need to rescan the entire map and find out what's the new most frequent character and update the `maxF`. But that would defeat the purpose
of this approach. Because we'd still have to do that O(26) scan of the map operation.

But actually you don't have to decrement the maxF in the case of moving the left pointer! Why?

Because we know the res is only gonna maximized as we find a **new** maxF(which means a bigger maxF). Remember what we're doing.
We're taking the length of the window, subtract it by `maxF` and we want the subtract result to be minimum. Note we have: `length - maxF` and
we want the result to be minimized. For this, we want length to be maximum because that's what the `res` is going to set to. We **ALSO** want
the maxF to be maximized because we want to ensure that `length - maxF` is less than or equal to `k` and k is gonna be constant.

For example let's say maxF is 4 but now the new maxF got downgraded to 3. But we're still gonna leave it as 4! Because it's not gonna change
our res. Note that if we ever gonna increase the `res` to 6 to higher, it's required our maxF to **increase**, if it stays the same
or if it decreases, our res is never going to change. Because we only change the res when we increase our maxF because that's the only
way the `length - maxF <= k` condition is going to be true. So if our maxF is downgraded(l is moved forward), we don't have to actually
update it, we don't need to look through the entire hashmap to find the new maxF. But if we increase the maxF, then we do want to update
our maxF and increase it and it's obviously `O(1)`.

`Time: O(n)`

---

Note: The size of the current window is: `r - l + 1`