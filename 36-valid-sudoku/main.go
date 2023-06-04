package problem36

import "fmt"

type SquareCoordinates struct {
	x, y int
}

func isValidSudoku(board [][]byte) bool {
	cols := make(map[int][]string)
	rows := make(map[int][]string)
	squares := make(map[SquareCoordinates][]string)

	for rowIndex, r := range board {
		for colIndex, val := range r {
			if string(val) == "." {
				continue
			}

			for _, el := range cols[colIndex] {
				if el == string(val) {
					return false
				}
			}

			for _, el := range rows[rowIndex] {
				if el == string(val) {
					return false
				}
			}

			coordinates := SquareCoordinates{x: rowIndex / 3, y: int(colIndex / 3)}

			for _, el := range squares[coordinates] {
				if el == string(val) {
					return false
				}
			}

			cols[colIndex] = append(cols[colIndex], string(val))
			rows[rowIndex] = append(rows[rowIndex], string(val))
			squares[coordinates] = append(squares[coordinates], string(val))
		}
	}

	fmt.Println("el: ", cols, rows)

	return true
}
