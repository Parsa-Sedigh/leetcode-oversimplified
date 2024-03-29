/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    let l = 1
    let r = Math.floor(x/2) + 1

    while (l <= r) {
        const mid = Math.floor((l + r) / 2)

        if (mid * mid > x) {
            r = mid - 1
        } else if (mid * mid < x) {
            l = mid + 1
        } else {
            return mid
        }
    }

    return r
};