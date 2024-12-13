Two strings are anagrams of each other, if we take each of them and sort them. If we sort both, we get the **exact same
string**.

### Sorting approach

So one way to group anagrams together would be to take each str in the input and sort them.

Let's say n is the avg length of a str in the input. Time of the sorting a str with length n: n*log(n). Now we have to
do this op for each of the strs. m is how many strs we have. So the overall time complexity of the sorting approach
would be:
`m * n log(n)`

We know, all of the strs are gonna be from `a-z`. So at most we have 26 unique characters.
For each one of the strs, we count how many chars there are for each of the chars from a to z.

For each str, we construct a list of 26 zeroes which represent the num of occurrences for each char from a-z.
Then we make a tuple out of that arr and put it into the res arr. For example a representation tuple would be: 1e, 1a,
1t.