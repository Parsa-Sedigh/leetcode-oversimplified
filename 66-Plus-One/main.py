from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Note: We initialized this to 1, because we do have to at least add a single one to the digits array.
        carry = 1

        # The index of the digits that we're currently at.
        i = 0

        # reverse the input array
        digits = digits[::-1]

        # While we still have to increment
        while carry:
            # While i is in bounds, increment the digits
            if i < len(digits):
                # special case.
                if digits[i] == 9:
                    # so the carry variable should stay as value 1. We're guaranteed the carry variable right now is 1, so we don't have to
                    # write the next line. Because our loop was executed which allowed us to arrive to this line, so we don't need to
                    # set it to 1 again.
                    # carry = 1

                    digits[i] = 0
                else: # if the current digit is not 9(and we have a carry - because the loop is still executing), just increment the currrent digit
                    digits[i] += 1

                    # we're not gonna have a carry anymore
                    carry = 0
            else: # if we go out of bounds, there's no more digits to add on, but we still have a carry, so append 1 to digits and set carry to 0
                digits.append(carry)

                # Setting this to 0 is gonna termine the while loop
                carry = 0

            i += 1

        return digits[::-1]