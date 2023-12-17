/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
// bucket sort
// time: O(n)
// space: O(1)
var sortColors = function (nums) {
    const counts = [0, 0, 0]

    for (const num of nums) {
        counts[num]++
    }

    let i = 0
    for (let j = 0; j < counts.length; j++) {
        for (let k = 0; k < counts[j]; k++) {
            nums[i] = j
            i++
        }
    }

    return nums
};