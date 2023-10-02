/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function (digits) {
    let carry = false
    for (let i = digits.length - 1; i >= 0; i--) {
        if (i === digits.length - 1) {
            if (digits[i] === 9) {
                digits[i] = 0
                carry = true

                if (i === 0) {
                    digits.unshift(1)
                }
            } else {
                digits[i]++
                carry = false
            }
        } else {
            if (carry) {
                if (i === 0 && digits[i] === 9) {
                    digits[i] = 0
                    digits.unshift(1)

                    break
                } else if (digits[i] === 9) {
                    digits[i] = 0
                } else {
                    digits[i]++
                    carry = false
                }
            }
        }
    }

    return digits
};