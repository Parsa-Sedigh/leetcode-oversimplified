package main

type NumMatrix struct {
	rows      int
	cols      int
	sumMatrix [][]int
}

// T: O(rows * cols)
// M: O(rows * cols)
func Constructor(matrix [][]int) NumMatrix {
	rows, cols := len(matrix), len(matrix[0])

	var sumMatrix [][]int

	for r := 0; r < len(matrix)+1; r++ {
		row := make([]int, 0, cols)

		for c := 0; c < len(matrix[0])+1; c++ {
			row = append(row, 0)
		}

		sumMatrix = append(sumMatrix, row)
	}

	for r := 0; r < len(matrix); r++ {
		prefix := 0

		for c := 0; c < len(matrix[0]); c++ {
			above := sumMatrix[r][c+1]
			prefix += matrix[r][c]
			sumMatrix[r+1][c+1] = prefix + above
		}
	}

	return NumMatrix{
		rows:      rows,
		cols:      cols,
		sumMatrix: sumMatrix,
	}
}

// T: O(1)
// M: O(1)
func (n *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
	row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1

	bottomRight := n.sumMatrix[row2][col2]
	top := n.sumMatrix[row1-1][col2]
	left := n.sumMatrix[row2][col1-1]
	topLeft := n.sumMatrix[row1-1][col1-1]

	return bottomRight - top - left + topLeft
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * obj := Constructor(matrix);
 * param_1 := obj.SumRegion(row1,col1,row2,col2);
 */
