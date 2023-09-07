/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    /* There's no need to calculate this hashmap inside the for loop. We just need to make it global(define it here) and update it
    in case the l pointer moves forward. If you define it inside of for loop which means allocating it on each iteration of loop,
    we could have get time limit exceeded.*/
    const count = {}
    let res = 0
    let l = 0

    for (let r = 0; r < s.length; r++) {
        if (!count[s[r]]) {
            count[s[r]] = 1
        } else {
            count[s[r]]++
        }

        let max = -Infinity
        Object.values(count).forEach(v => {
            if (v > max) max = v
        })

        while (((r - l + 1) - max) > k) {
            count[s[l]]--
            l++
        }

        res = Math.max(res, r - l + 1)
    }

    return res
};