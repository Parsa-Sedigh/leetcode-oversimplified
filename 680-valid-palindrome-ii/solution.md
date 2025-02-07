### Brute force
Remove one char everytime and check if it becomes a palindrome. That would be O(n^2) where n is the size of
input str.

### Better solution
Since we don't know which char to remove, we have to rem it and then continuing iterating through the arr. We potentially have to do
this 2 times.

So in worst case(unequal chars at the beginning), time would be T: O(2*n)