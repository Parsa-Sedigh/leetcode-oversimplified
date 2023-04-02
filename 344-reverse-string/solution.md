The easiest way to solve this is actually the most efficient, especially when it comes to space complexity.

The input string is given as an array and the reason that's important is because if you were given a single string and you had to
reverse the characters in it, that wouldn't be efficient because in most languages, when you swap characters in a string or just
reassign a single character of string, it's actually a O(n) operation, because it has to rebuild the entire string.

It's more efficient to swap positions(like reversing) in an array.

In the stack approach, the memory complexly would be O(n).

This approach is more efficient in terms of time, but it takes more space.

The third approach is recursion and the space complexity is gonna be O(n) because we're gonna need recursion and recursion takes extra
space on the call stack.