class Solution:
    def isHappy(self, n: int) -> bool:
        # Keep track of every number that we previously visited, so that if we get to a number that we have visited, we can instantly
        # knowing in O(1) .
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True

        # If we get here, it means we visited a value twice and it wasn't 1, so return false
        return False

    def sumOfSquares(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit

            # update n to find the next digit
            n = n // 10 # integer division

        return output