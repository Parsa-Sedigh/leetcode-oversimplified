To evaluate an RPN expression, you process the tokens from left to right:
- When you encounter a number (operand), you "store" it.
- When you encounter an operator (+, -, *, /), you apply it to the two most recently stored operands, compute the result, and
store that result back.

In question it says division should truncate towards zero. But in at least python the division operator(/) always rounds down which is not
rounding towards zero necessarily because imagine if we had `-3/2` which results in -1.5 and then python rounds it down to **-2** but this is not
what we want to do(we want to round towards zero). There's a trick in python to do this.

In Java and C++ though it automatically rounds towards zero.

When we reach an operator, any operator is gonna be applied to the previous two elements and there are no edge cases, so for example we're guaranteed
that there are going to be two previous value(and those two values are gonna be removed from the stack). Then we're gonna replace those 
two previous values and that operator into one value(by applying that operator on those two previous values).

As we read through the input, each value is gonna be added to the stack. But anytime we reach an operator, the previous two values are
gonna be removed from the stack and then we're gonna do the operation on those two and then we take the result and then push it back onto the stack.

**Q:** When we have a `-` or `/`, which order the values are gonna be subtracted or divided?

Well, it's gonna be the older - newer(bottom - top) in the stack.

So for `-` and `/` , the order of popped elements matters.

Time complexity: O(n) - actually it's O(2n)

Space complexity: O(n)