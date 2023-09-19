///////////// this doesn't work because of: Time Limit Exceeded /////////////
/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
    const tCount = {}
    const currCount = {}
    let l = 0
    let minLength = Infinity
    let min = []

    const isWindowValid = (curr, target) => {
        for (const [k, v] of Object.entries(target)) {
            if (!curr[k] || curr[k] < v) {
                return false
            }
        }

        return true
    }

    for (const c of t) {
        if (!tCount[c]) {
            tCount[c] = 1
        } else {
            tCount[c]++
        }
    }

    for (let r = 0; r < s.length; r++) {
        if (!currCount[s[r]]) {
            currCount[s[r]] = 1
        } else {
            currCount[s[r]]++
        }

        if (r - l + 1 < t.length) {
            continue
        }

        while(isWindowValid(currCount, tCount) && r - l + 1 >= t.length) {
            currCount[s[l]]--

            if (!currCount[s[l]]) {
                delete currCount[s[l]]
            }

            if (r - l + 1 < minLength) {
                min = [l, r]
                minLength = r - l + 1
            }


            l++
        }
    }

    return s.slice(min[0] , min[1] + 1)
};

///////////// /////////////

/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow2 = function(s, t) {

}
