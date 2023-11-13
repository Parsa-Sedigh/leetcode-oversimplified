/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const elements = {}

    for (const num of nums) {
        if (!elements[num]) {
            elements[num] = 1
        } else {
            return true
        }
    }

    return false
};