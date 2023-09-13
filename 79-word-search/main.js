/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function (board, word) {
    const ROWS = board.length
    const COLS = board[0].length

    const dfs = (r, c, i) => {
        if (word.length === i) return true

        if (r < 0 || c < 0 ||
            r >= ROWS || c >= COLS ||
            word[i] !== board[r][c]) return false

        // set the current position as visited by setting it to sth like '#'
        board[r][c] = '#'

        res = (dfs(r + 1, c, i + 1) ||
            dfs(r - 1, c, i + 1) ||
            dfs(r, c + 1, i + 1) ||
            dfs(r, c - 1, i + 1))

        board[r][c] = word[i]

        return res
    }

    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            if (dfs(r, c, 0)) return true
        }
    }

    return false
};