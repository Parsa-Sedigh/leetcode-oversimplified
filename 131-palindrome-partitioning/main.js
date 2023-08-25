const isPalindrome = (s, start, end) => {
    while (start < end) {
        if (s[start] !== s[end]) return false

        start++
        end--
    }

    return true
}

/**
 * @param {string} s
 * @return {string[][]}
 */
var partition = function(s) {
    // global result
    const result = []

    // dfs recursive helper
    const dfs = (i, slate) => {
        // backtracking case(we don't need in this case)

        // base case. We're at the leaf level of the tree
        if (i === s.length) {
            result.push(slate.slice())

            return
        }

        // dfs recursive case
        /* Note: Yeah we're doing DFS, but we use for loop to do breadth first on current level. We're going DFS to the leaf,
        but at the root level, we have multiple choices to go, hence the for loop. */
        for (let j = i; j < s.length; j++) {
            // here, we have to do some checking to whether we wanna go further down the recursive tree or not
            // if the range between i and j is a palindrome, then we wanna add the range to the slate
            if (isPalindrome(s, i, j)) {
                // slice is not inclusive from the end, that's why we use `j + 1`
                slate.push(s.slice(i, j + 1))

                dfs(j + 1, slate)

                slate.pop()
            }
        }
    }

    dfs(0, [])

    return result
};