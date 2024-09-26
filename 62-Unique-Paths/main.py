# This gets: Time Limit Exceeded
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1

        ROWS, COLS = m, n
        visit = set()
        count = 0

        def dfs(row, col):
            nonlocal count

            if (row < 0 or row == ROWS or
                    col < 0 or col == COLS or
                    (row, col) in visit):
                return 0

            if row == ROWS - 1 and col == COLS - 1:
                return 1

            visit.add((row, col))

            count = 0

            count += dfs(row + 1, col)
            count += dfs(row, col + 1)

            if (row, col) in visit:
                visit.remove((row, col))

            return count

        dfs(0, 0)

        return count

# T: O(m * n)
# M: O(n) - because n is the length of a row
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS = m
        COLS = n # number of cols is the length of a row

        # initially, the bottom row
        row = [1] * n

        # go through every row except the last row because the last row is all 1.
        for _ in range(m - 1):
            # new_row is the row above the `row` and we know in this new row, we can reach the target in at least 1
            # way and also the last col of this row is always 1. So we initialize it as 1.
            new_row = [1] * n

            # go through every column except the right most column, because the right most col(last val in every row)
            # is gonna be 1.
            for j in range(n - 2, -1, -1):
                # add the values of right cell and the below cell
                new_row[j] = new_row[j + 1] + row[j]

            row = new_row

        return row[0]
