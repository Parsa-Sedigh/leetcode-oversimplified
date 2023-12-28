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

// This would throw Time Limit Exceeded on leetcode
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate2 = function(nums) {
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] === nums[j]) {
                return true
            }
        }
    }

    return false
};

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate3 = function(nums) {
    nums.sort((a, b) => a - b)

    for (let i = 1; i < nums.length; i++) {
        if (nums[i - 1] === nums[i]) {
            return true
        }
    }

    return false
};