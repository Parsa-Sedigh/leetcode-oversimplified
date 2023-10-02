The `num1` and `num2` could be extremely large numbers and because of that, these integers are gonna be represented as strings.

The good thing is that these integers are always gonna be eiter positive or they could be zero.

We can't just convert these strings to integers, we actually want to do this with strings themselves. Because there's no guarantee that
a large integer could fit into a 32 bit or 64 bit.

There's gonna be two parts to this problem:
1. remember how you actually multiply two numbers in the first place(elementary school!)
2. take the idea and translate it into code

## Multiplying(elementary school)
How we decide where we put the digit when we multiply two digits together?

When we have a carry, we handle it differently than what we do in our mind. We're gonna put the carry right at the index that we're gonna do
the next multiplication. Because when we're keeping track of a carry, we could keep track of it like in a separate variable but it's kinda
easier to just put it in the next index, because we know it's gonna be added to whatever next value that we put there.

It's gonna be the sum of the indices of the digits(two digits) that we're multiplying.

The maximum number of digits the output could be is: the sum of the number of digits of each of the input numbers. So for example
if we had three digits number multiplied by 3 digits number, the output could be up to 6 digits, but it could be less than that. So
it's gonna be less than or equal to the sum of the number of digits.

Note: We're gonna iterate through the integers in reverse order, similarly we're gonna building our result(output) in reverse order(from right
to left). So at the end we need to reverse it.

Note: We're gonna pre-allocate the result array(`res`) and the length of output array is sum of length of digits of num1 and num2,
The res array won't contain string elements, even though the inputs are given to us as strings.

We're gonna build the res as an array just because it's a bit easier. You could do it with a string, but then we have to do a lot of conversions,
converting a char to integer and vice versa. At the end we're gonna take this array, reverse it and convert it back to a string.

We're gonna start at the right of each input string(hence reverse iteration of them) and when we build the res array and fill it,
we're gonna build it in opposite order(so least valuable digit is at left). In other words, the res array is filled in reverse order to
the calculations that we actually do. At the end, we reverse the array and convert it to string.

![](../img/43-1.png)

When we multiply two digits(like 9 * 9), we can get the result(to put it in correct position in `res`) by using `% 10` and we can get the carry
using `// 10`. Because when we have 9 * 9 which is 91 and mod it by 10, we get 1 which is the one that we put in res and when we do 81 // 10,
we get the carry which is 8.

Time: We're gonna have a nested loop -> `O(n * m)` where n is the number of digits in num1 and m is the number of digits in the num2.

Space: `O(n + m)`. Because we're gonna be using an additional array just to have the result digits and it's length is `n + m`.