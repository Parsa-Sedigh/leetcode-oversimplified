from typing import List


# My solution
# r is number of rows, c is number of cols
# T: O(r * c)
# M: O(r + c)
# Note: Considering the lists used and ignoring the space used by the input matrix itself, the total space complexity is:
# O(r) + O(c) + O(min(r, c)) => O(r + c)
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        rows_min = []
        cols_max = []

        # T: O(c)
        for i in range(COLS):
            # M: O(c)
            cols_max.append(matrix[0][i])

        for i in range(ROWS):
            row_min = matrix[i][0]

            for j in range(COLS):
                row_min = min(row_min, matrix[i][j])
                cols_max[j] = max(cols_max[j], matrix[i][j])

            # M: O(r)
            rows_min.append(row_min)

        res = []

        for min_n in rows_min:
            for max_n in cols_max:
                if min_n == max_n:
                    # In the worst case, if all elements are lucky numbers, `res` can store up to min(r, c), elements, which
                    # is at most O(min(r, c))
                    res.append(min_n)

        return res

# T: O(r * c)
# M: O(r + c)
class Solution2:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # dimensions
        ROWS, COLS = len(matrix), len(matrix[0])
        res = []
        row_min = set()
        col_max = set()

        for r in range(ROWS):
            # Or: Do another loop and get the min
            row_min.add(min(matrix[r]))

        # Here, first we're iterating over COLS and then ROWS. Which means we're going from top to bottom of the matrix. So at each
        # iteration, we're going one row forward. So the inner loop should be iterating over ROWS.
        for c in range(COLS):
            # We can't do a shortcut here like what we did with rows. Because matrix[c] doesn't mean the whle column, it means a whole ROW.
            # But here, we want to get the max el in whole col.
            # We could pick any value in the current column, but we picked the first el in each col of the matrix as initial
            # maximum.
            cur_max = matrix[0][c]

            for r in range(ROWS):
                cur_max = max(cur_max, matrix[r][c])

            # here, we're at the end of a col. So add the max el of this col to the col_max hashset.
            col_max.add(cur_max)

        # Go through the row_min or col_max
        for n in row_min:
            if n in col_max:
                res.append(n)

        return res

# T: O(r * c)
# M: O(max(r, c))
# We can solve this problem without using col_max.
# So when we get the cur_max, we check if it's also inside row_min and if it is, add it to the res.
class Solution3:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = []
        row_min = set()

        for r in range(ROWS):
            row_min.add(min(matrix[r]))

        for c in range(COLS):
            cur_max = matrix[0][c]

            for r in range(ROWS):
                cur_max = max(cur_max, matrix[r][c])

            if cur_max in row_min:
                res.append(cur_max)

        return res

# T: O(r * c)
# M: O(1)
class Solution4:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])

        max_of_row_mins = float("-Inf")

        # first find the min in every single row
        for r in range(ROWS):
            row_min = min(matrix[r])

            # we want the max among all of the row minimums
            max_of_row_mins = max(max_of_row_mins, row_min)

        for c in range(COLS):
            col_max = matrix[0][c]

            # go through every row in the current col
            for r in range(ROWS):
                col_max = max(col_max, matrix[r][c])

            # if this is true, the max_of_row_mins is a min in it's row and also now, we know it's the max in it's col, so it's lucky
            if col_max == max_of_row_mins:
                return [max_of_row_mins]

        # we're not guaranteed that we will have a lucky num in the input
        return []
