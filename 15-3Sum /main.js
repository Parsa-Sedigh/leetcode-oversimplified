/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    let res = [];

    nums.sort((a, b) => a - b);

    for (let index = 0; index < nums.length; index++) {
        let l = index + 1;
        let r = nums.length - 1;

        if (index > 0 && nums[index] === nums[index - 1]) continue

        while (l < r) {
            const sum = nums[index] + nums[l] + nums[r];

            if (sum < 0) {
                l++
            } else if (sum > 0) {
                r--;
            } else {
                res.push([nums[index], nums[l], nums[r]]);
                l++

                while(nums[l - 1] === nums[l] && l < r) {
                    l++
                }
            }
        }
    }



    return res

};