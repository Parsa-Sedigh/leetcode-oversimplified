We can can have a key named `foo` and a list of values associated with that key and every element of that list is in format of: [<value>, <timestamp>].

We're gonna support 3 operations:
- constructor
- set
- get

Note: When we do a get operation, normally on a hashmap, we just need a key, but in this case we need two values: the key and the timestamp because
we know for a single key, it's not enough to identify a value. Because there could be multiple values associated with a key and therefore we need a
timestamp to identify the actual value.

On leetcode we have sth like:
`
["TimeMap","set","get","get","set","get","get"]
[[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
`
as the input. The first line is the name of the operations that will be done to test our solution and on the second line there are the values
for each operation. So for example as the second operation, we have a `set` operation and the thing it's gonna set has the key of `foo`, value of
`bar` and timestamp of `1`.

Another example:

For third element of input, we have a `get` and it's related values are: ["foo",1] which means get the list associated with the key `foo` and find the
element with timestamp of `1`.

**If you don't find an exact match in the key-value store(no element with the requested timestamp but there are some with the requested `key`), then
return the most recent one.** In get operation, we wanna look for an exact match and if we can't find an exact match, we want to find the most
recent value with the same value.

The set operation is always gonna be constant time(`O(1)`) because finding the key in hashmap is `O(1)`. But **in this case**, since we have multiple
values for a key and they are in sorted order by the timestamp(so we can use binary search), the get operation is gonna be O(logn).

Adding an item to the end of the array is `O(1)` .

By doing linear scan through the array, worst case is gonna be `O(n)` .

**Binary search requires the values to be sorted.**

Since we're searching for an exact match with the **timestamp**, the values have to be sorted by the **timestamp**.

Note: If we had to sort every time we wanted to set sth, the time complexity would be: `O(nlogn)` which is worse than `O(n)`.

Question says: `All the timestamps timestamp of set are strictly increasing.`. So everytime we set a value, the timestamp is gonna be
in increasing order. So the list is gonna be sorted by the timestamp by default.

**Note:** A very good question to ask is: Are the set operations gonna be in sorted order?

**Note:** If the requested key in the get operation doesn't exist in the store, just return an empty string.

**Note:** To make sure we check the last value in binary search, use <= instead of < in: `while l <= r:`.

**Note:** Technically the solution is not optimal as it could be because in the first case(`values[m][1] <= timestamp`) if we even find an **exact match**
to the timestamp, we're not returning, we're still continuing the binary search. But still it doesn't change the overall time complexity(still
`O(logn)`). In this case the tutor prefers the concise code because we're done with the function after that while loop is over and we won't do anything
else after it(if we were, we could consider the exact match as a separate case and return in that case so we won't do anything more in that
function).