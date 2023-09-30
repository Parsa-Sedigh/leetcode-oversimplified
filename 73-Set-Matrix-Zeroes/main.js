// space: O(m * n). m is number of rows and n is number of columns

/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes1 = function (matrix) {
    const ROWS = matrix.length
    const COLS = matrix[0].length

    let newMatrix = []
    for (let i = 0; i < ROWS; i++) {
        newMatrix.push([])

        for (let j = 0; j < COLS; j++) {
            newMatrix[i].push(matrix[i][j])
        }
    }


    for (let i = 0; i < ROWS; i++) {
        for (let j = 0; j < COLS; j++) {
            if (matrix[i][j] === 0) {

                for (let p1 = 0; p1 < ROWS; p1++) {
                    newMatrix[p1][j] = 0
                }

                for (let p1 = 0; p1 < COLS; p1++) {
                    newMatrix[i][p1] = 0
                }
            }
        }
    }

    for (let i = 0; i < ROWS; i++) {
        for (let j = 0; j < COLS; j++) {
            matrix[i][j] = newMatrix[i][j]
        }
    }

};

// space: O(m + n).
/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes1 = function (matrix) {

}