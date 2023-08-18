/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function(nums) {
    const res = []

    nums.sort((a, b) => b - a)

    const backtrack = (i, subset) => {
        if (i === nums.length) {
            res.push([...subset])

            return
        }

        subset.push(nums[i])
        backtrack(i + 1, subset)

        subset.pop()

        while (i + 1 < nums.length && nums[i] === nums[i + 1]) {
            i++
        }

        backtrack(i + 1, subset)
    }

    backtrack(0, [])

    return res
};