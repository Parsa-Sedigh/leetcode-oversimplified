/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length !== t.length) return false

    const sElements = {}
    const tElements = {}

    for (const c of s) {
        if (!sElements[c]) {
            sElements[c] = 1
        } else {
            sElements[c]++
        }
    }

    for (const c of t) {
        if (!tElements[c]) {
            tElements[c] = 1
        } else {
            tElements[c]++
        }
    }

    for (const [c, n] of Object.entries(sElements)) {
        if (!tElements[c] || tElements[c] !== n) {
            return false
        }
    }

    return true
};