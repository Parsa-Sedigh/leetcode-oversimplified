We can get to some positions in multiple different ways and these are the repeated works. When we reach a position in multiple
ways, from there, we're doing repeated work all the way to the end.

The cache[r][c] says the number of ways we can reach the end from that position.

The overall result we're looking for is: cache[0][0]

What is the base case?

We know the ending position is the bottom right pos. How many unique paths from there we can reach the finish(get to itself)?

We can choose to define that as 1. Also, from every position in the bottom row, we can reach the target in 1 unique path.

The number of unique paths from each position is specified in img:
![](62-1.png)