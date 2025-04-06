There are many ways to solve this problem.

## Approach 1

We can iterate char by char, everytime we encounter a space, just ignore it, but if we hit a char, keep track of
whatever the length of the curr word is. For example we see a char, keep adding to the cur length var until we hit a
space. There, reset the cur length to 0. Until we hit another char. Then whatever the length of the last word was,
return it.

## Approach 2

We want the length of **last** word, why do we have to start at the beginning? It's a waste of time. Start at the end.
It's more efficient.

Note: We could have leading spaces at the end as well.