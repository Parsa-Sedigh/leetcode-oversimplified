We have to solve this without using division. It would be really easy with division because we could take the product of all of these
values and then divide that total product with the current element for the result in that index. Because division 
of all product is basically taking the entire product without that specific element.

---

## First approach

O(n) solution

O(n) time complexity

O(n) memory complexity

If we want to get the product of all except 3, one way we can break it down is get the product of every value before 3 in input array and
get the product of every value after 3 and then to calculate the result in each index, look at the input array. Then look at the
`index - 1` prefix of the current index and multiply it by the postfix at `index + 1`.

Note: At index 0, since there are no prefix at index - 1 in prefix array, we assume 1 and the same goes for postfix for last index.

We wanna do this for every element in input array but by computing the prefix product for every single element in input array and put it
in a prefix array and also the postfix product of every single position. We can compute both of these in O(n)

---

## Second approach

O(n) time complexity

O(1) memory complexity

Note: Output array does not count as extra memory.

We don't need prefix and postfix extra arrays. We can compute them and then store them in output array.

To do this, we're gonna do 2 passes on our input array.