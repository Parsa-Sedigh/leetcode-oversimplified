////////// This approach gets "Time limit exceeded" //////////

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function(nums, k) {
    let l = 0
    let maxWindow = []

    for (let r = k - 1; r < nums.length; r++) {
        const max = Math.max(...nums.slice(l, r + 1))
        maxWindow.push(max)

        l++
    }

    return maxWindow
};

////////// //////////

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function(nums, k) {
    const output = []
    const q = []
    let l = 0
    let r = 0

    while (r < nums.length) {
        while (q.length && nums[q[q.length - 1]] < nums[r]) {
            q.pop()
        }

        q.push(r)

        if (l > q[0]) {
            q.shift()
        }

        if (r + 1 >= k) {
            output.push(nums[q[0]])
            l++
        }

        r++
    }

    return output
};