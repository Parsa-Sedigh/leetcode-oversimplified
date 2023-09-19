## Brute force
The count map of `t`, specifies how many we **need** and the count of window(current hashmap), specifies how many we **have**.

In this approach, we have to repeatedly check every one of the elements in current hashmap, even if we already know the count of some of them
is met. This is what we need to eliminate in better approach.

## Linear solution
The question is: Do we have to check every single one of the current window elements?

If the current char count is not exactly equal to the related char in `need` count, we don't update the `have` to be `have + 1`.

Time: O(n)