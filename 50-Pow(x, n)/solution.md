`n` can be negative. Even `x` can be negative. `x` can even be a decimal but that doesn't change the problem.

The power(n) itself can't be a decimal, we can't have 2^10.5 . That would make this problem a little bit difficult, but we don't have
to deal with it.

Negative exponent(negative `n`) means putting the res in the dominator. So 2^-2 means: 1/(res) where res is 2*2 in this case.

`Time: O(n)`. Because we can just do a while or for n times. But this doesn't pass the test cases. Why? Because there's a better solution.

## Better solution
It's not a common sense solution. Let's say x = 2 and n = 10. Instead of multiplying 2 10 times, is there a shorter way to do that?
The way math works out, isn't it true that we don't have to do this 10 times, we could just do it 5 times and then once we calculated that number
(2^5) can't we just say: 2^5 * 2^5? With this, we're eliminating half of the work.

But why stop there? Can't we also further break 2^5 down as well? Well, we can't divide it by 2, so it's gonna be a little bit more annoying but
we can say: 2^5 = 2^2 * 2^2 * 2 . With this, we still did eliminate half of the work and we just have a constant(2) left.

We're doing a divide and conquer.

Now 2^2 = 2^1 * 2^1 .

About time complexity: How many times can we divide n by 2? Until it finally equals 1. That's basically the definition of log .
So the answer of how many times we can divide it by 2, is: `log n`(the base of log is 2). So O(log n) (base of log is 2) is the time complexity.

Since we're doing this with a divide and conquer approach, it's gonna lend itself to recursion. Because when we're trying to solve 2^10,
we can't solve it, so we're gonna solve the sub problems.

What's the base case?

Any number to the power of 0, is always gonna be 1. So one base case is n = 0, then return 1. Now this isn't really a base case because
x is never gonna be modified, we're gonna be dividing n by 2, but x is gonna stays the same, but if we ever got an input such that x was 0,
no matter the `n`, it's gonna always be 0. So the x = 0, is another base case which we return 0 in that case.

Note: The way we're gonna handle the negative exponent case is: We're not even gonna worry about negative exponents until the end.
So regardless of what n is, we're gonna take the abs() value of it and use it in the calculations. If n is a negative number, we're not gonna
calculate negative numbers, we're gonna calculate x to the power of positive n. And at the end we're gonna take the result and return 1/res.

About `res = helper(x, n // 2)`:

What if we had n = 5(odd number). If we divide it by 2, n is gonna be 2.5 , so we have to handle this. If n is an odd number, we have to multiply
it by x one more time. Why? Because for example: 2^5 = 2 * 2^2 * 2^2 , as you can see, we had to multiply it by 2(x) one more time.
The helper function is what's gonna calculate (x ^ 2)s in the line that we have : `res = res * res`, but if n was odd, we have to multiply it by x again.