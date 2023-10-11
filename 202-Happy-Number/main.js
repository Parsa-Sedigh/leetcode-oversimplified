/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    const seen = {}

    const sum = (num) => {
        const arr = num.split('').map(el => Number(el))

        const total = arr.reduce((acc, el) => {
            return acc + (el * el)
        }, 0)

        if (seen[total]) {
            return false
        }

        seen[total] = true

        if (total === 1) {
            return true;
        }

        return sum(total.toString())
    }

    return sum(n.toString())
};