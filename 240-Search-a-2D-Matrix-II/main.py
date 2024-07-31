from typing import List

# My solution
# T: O(r * log(c))
# M: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        for row in range(ROWS):
            l, r = 0, COLS - 1

            while l <= r:
                m = (l + r) // 2

                if matrix[row][m] < target:
                    l = m + 1
                elif matrix[row][m] > target:
                    r = m - 1
                else:
                    return True

        return False
