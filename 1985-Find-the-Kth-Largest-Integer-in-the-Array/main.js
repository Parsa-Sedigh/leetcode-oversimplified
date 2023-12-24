
// my approach(naive)
/**
 * @param {string[]} nums
 * @param {number} k
 * @return {string}
 */
var kthLargestNumber = function(nums, k) {
    nums.sort((a, b) => {
        if (a.length > b.length) {
            return 1
        }

        if (a.length < b.length) {
            return -1
        }

        for (let i = 0; i < a.length; i++) {
            if (a[i] > b[i]) {
                return 1
            }

            if (a[i] < b[i]) {
                return -1
            }
        }

        return 0
    })

    return nums[nums.length - k]
};