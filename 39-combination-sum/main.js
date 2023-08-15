/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    const res = []
    const subset = []

    const dfs = (i) => {
        const currSum = subset.reduce((acc, el) => acc + el, 0)

        if (currSum === target) {
            res.push([...subset])

            return
        }

        if (i >= candidates.length || currSum > target) {
            return
        }

        subset.push(candidates[i])
        dfs(i)
        subset.pop()
        dfs(i + 1)
    }

    dfs(0)

    return res
};