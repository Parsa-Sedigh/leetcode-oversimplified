**Brute force way**: **O(n^2)** - for every temperature, we would look through the entire array after it and see how many days it take us to find a 
temperature greater than the current one? and then do the same thing for the next element(temperature), look at all the elements after it(worst
case) and see what's the first day that we can find a greater temperature.

Second approach:

If we use some extra memory, we can reduce time complexity.

Iterate through the input array once, but we have to remember the previous temperatures that we looked at.

Our stack is gonna be in monotonic decreasing order(not strictly decreasing because we could have equal temperatures on the stack). This is
a type of stack problem.

In each element of stack, we're gonna add the temperature itself and also the index of the temperature so that we can calculate the difference for
number of days that took us to find a greater temperature.

Time complexity: O(n)

memory complexity: O(n)