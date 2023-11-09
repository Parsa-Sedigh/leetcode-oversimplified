### Brute force
We're guaranteed that there's exactly one solution, so we don't have to worry about not finding a solution and we don't have to 
worry about multiple solutions.

The most intuitive solution is to check every combination of two values and see if they can sum up to our target.

Time: O(n^2)

### Better way
We could add every value in the input array into the hashmap **before** we start iterating through it, but there's an easier way to do it.
If we added the entire array into the hashmap initially, then we would get to the value 2 first(look at the example in description),
now we would wanna check does the difference between target(4) minus the current value(2) which is equal to 2, exist in our hashmap?
We would find that 2 does exist in our hashmap(but it's in the same index as our current value!) but we're not allowed to reuse the same one,
because they're both at the same index, we can't use the same value twice, to fix this, we would have to compare our current value
with the index of the value that is in our hashmap.

There's an easier way to do this.

### Clever way
Don't fill the hashmap at the beginning.

Initially our hashmap is empty, so we get to value 2 first of all and we wanna look for difference <target> - <current value>. Our hashmap
is empty, so we don't find 2. So then **after** we visited this element, then we can add it to our hashmap.

So we only have to iterate through the array once.

So with this solution, we don't have to worry about edge cases in comparisons(previous solution has it!).

Time: O(n)

Space: O(n) - we could potentially add every value to the hashmap