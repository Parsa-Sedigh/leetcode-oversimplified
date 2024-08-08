class NumMatrix:

    # T: O(rows * cols)
    # M: O(rows * cols)
    def __init__(self, matrix: List[List[int]]):
        # ROWS and COLS are number of rows and cols
        ROWS, COLS = len(matrix), len(matrix[0])

        # why ROWS + 1 and COLS + 1? Because we wanna get rid of handling the edge case
        self.sumMatrix = [[0] * (COLS + 1) for r in range(ROWS + 1)]

        for r in range(ROWS):
            # calculate prefix sum for current row
            prefix = 0

            for c in range(COLS):
                # While we're at r+1, c+1 in sumMatrix, we're at r, c at matrix.
                prefix += matrix[r][c]

                # Why self.sumMatrix[r][c + 1]? Because we're currently at r + 1, c + 1. So row above is prev row,
                # hence r. The cols are the same.
                above = self.sumMatrix[r][c + 1]

                # we have to use next index, because of those extra row and col that self.sumMatrix has
                self.sumMatrix[r + 1][c + 1] = prefix + above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottomRight = self.sumMatrix[row2][col2]

        # Note: self.sumMatrix[row1 - 1][col2] won't go out of bounds because we added those extra row and col at the top and
        # left of the self.sumMatrix.
        above = self.sumMatrix[row1 - 1][col2]
        left = self.sumMatrix[row2][col1 - 1]
        topLeft = self.sumMatrix[row1 - 1][col1 - 1]

        # when we subtract both above and left areas, we're subtracting the topLeft area twice. So to counter this, add topLeft once.
        return bottomRight - above - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)