We wanna run BFS on our tree and add the values into a list.

We need a queue because we're gonna be adding elements to the right side of the queue and removing elements from the left(**so it's a 
queue not a stack, because we're following FIFO**).

Time complexity: O(n) - we're visiting every single node once

memory complexity: O(n) - because at any given point in time, our queue could have up to n/2 elements in it, because **the biggest level
of a tree could be n/2**(that's how binary trees work) and we know n/2 is rounded to O(n). So memory complexity is O(n) with BFS approach.
