/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    if (digits.length === 0) return []

    // global result
    const result = []

    const alpha = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    // dfs recursive helper
    const dfs = (i, slate) => {
        // base case
        if (i === digits.length) {
            result.push(slate.join(''))

            return
        }

        // dfs recursive case
        let chars = alpha[digits[i]]

        for (let char of chars) {
            slate.push(char)

            dfs(i + 1, slate)

            slate.pop()
        }
    }

    dfs(0, [])

    return result
};