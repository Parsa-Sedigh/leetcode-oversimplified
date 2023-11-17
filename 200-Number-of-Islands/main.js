/**
 * @param {string[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    if (!grid || !grid.length) return 0

    const ROWS = grid.length
    const COLS = grid[0].length
    const visit = new Map()
    let islands = 0

    const bfs = (r, c) => {
        const q = []
        q.push([r, c])

        while (q.length) {
            const [row, col] = q.shift()
            const neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for (const [dr, dc] of neighbors) {
                const r = row + dr
                const c = col + dc

                if (r >= 0 && c >= 0 && r < ROWS && c < COLS && grid[r][c] === '1' && !(visit.has(`[${r}, ${c}]`))) {
                    q.push([r, c])
                    visit.set(`[${r}, ${c}]`, [r, c])
                }
            }
        }
    }

    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            if (grid[r][c] === '1' && !(visit.has(`[${r}, ${c}]`))) {
                bfs(r, c)
                islands++
            }
        }
    }

    return islands
};