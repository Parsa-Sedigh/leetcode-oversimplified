class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x^-n = 1 / x ^ n

        # with this function, we don't ever pass a negative exponent into it.
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1

            # Here, we could pass x * x instead of x and with this, we won't need the `res = res * res` line. With this, the call of
            # helper(x, n // 2) will return x^(n//2) multiplied by itself(or with an * x if n was odd), so: x^(n//2) * x^(n//2)
            res = helper(x, n // 2)

            # With this we eliminate work(multiplying the result by itself instead of n times multiplying by x)
            res = res * res

            # if n % 2 is non zero, it means n is odd, so we need to multiply iy by x one more time, otherwise, just return the res
            return x * res if n % 2 else res

        res = helper(x, abs(n))

        # What if n was negative? we return 1/res
        return res if n >= 0 else 1 / res