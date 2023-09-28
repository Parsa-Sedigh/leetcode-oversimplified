Potentially we're gonna have to go through every single character of every single string. That would be the case for example if we had
[flower, floweras, flowerzxc], so we would iterate through all of the elements of array and iterate through each of the "flower"s, because
they're common so we wouldn't stop.

Time: `O(n)` where n is the total number of characters that we're given, or if you wanna say that n is the average size of 
the strings(or minimum size of the strings) and we have m different strings, then you can say: O(n * m).

Overall, we're gonna have to iterate through each character in the entire input once.