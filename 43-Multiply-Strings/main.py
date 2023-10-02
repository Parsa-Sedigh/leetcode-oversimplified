class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # If either of the numbers happens to be zero, we can just return 0(any value multiplied by zero equal zero).
        if "0" in [num1, num2]: return "0"

        # allocate an array of all zeroes and the length of the array is `len(num1) + len(num2)`
        res = [0] * (len(num1) + len(num2))

        # We're gonna be iterating through both numbers(num1 nad num2) in reverse order, so before actually iterating through them,
        # reverse each of them
        num1, num2 = num1[::-1], num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])

                # Before actually stroing the into the related position in res, we might already have a carry in this position,
                # so add the current calculations to whatever is in that position in res already.

                # Note: The `digit` could be a 1-digit value like 2 or it could be a 2-digit value like 12. So it's possible we have 2-digit value
                # stored at res[i1 + i2]. So one thing we have to do if we did have a 2-digit value there, we would need to mod it by 10 again.
                # So on the line where we have: res[i1 + i2] = res[i1 + i2] % 10, we're modding the value at res[i1 + i2] by 10 to make it be a
                # 1-digit value. If it was a 1-digit value, it would remain the same and if it was a 2-digit value like 12, then we get the
                # 2 and put it there.
                res[i1 + i2] += digit

                # The carry might be zero or it might not be zero, either way, we're gonna put it in i1 + i2 + 1, so the next position is
                # where we put the carry.
                # Get the carry and add it to next position
                res[i1 + i2 + 1] += res[i1 + i2] // 10

                # This should be after the previous line.
                # Get the 1-digit value that we should put here
                res[i1 + i2] = res[i1 + i2] % 10

        # Note: Let's say we have num1 = 10 num2 = 10 to calculate. In this case, the res would end up being: 0100 till this line.
        # The reason we whave a leading zero is because when we allocated the res, in this case, we allocated an array of four 0s.
        # So that first 0 is redundant and we wanna get rid of it. In other words, we want to get rid of any leading zeroes.
        # Now before we try to get rid of the leading zeroes, let's first reverse the res back.
        # Note: beg is beginning pointer.
        res, beg = res[::-1], 0

        # While we have leading zeroes(which are now at the right(end) of the res), increment the beginning pointer until the point we don't
        # have any leading zeroes anymore
        while beg < len(res) and res[beg] == 0:
            beg += 1

        # currently we have an array of integers not an array of strings, we need to convert every single value from the beginning pointer
        # until the end which would also get rid of the leading zeroes as well(subarray starting from the beginning pointer)
        res = map(str, res[beg:])

        return "".join(res)