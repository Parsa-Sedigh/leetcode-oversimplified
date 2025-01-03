from typing import List


# My solution
# T: O(n^2)
# M: O(n^2) - if we count the output arr as extra space.
# Why n^2?
# Because `res` would become an arr of size n with each el as an arr of size up to n(in worst case which is when n becomes
# too large, each arr has n up to vals and it's considered n, so n * n => n^2).
# n: number of rows
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(1, numRows):
            cur_row = [1]

            # Although the inner loop doesn't iterate n times for each iteration of the outerloop,
            for j in range(1, i):
                cur_sum = res[i - 1][j - 1]

                if len(res[i - 1]) >= j:
                    cur_sum += res[i - 1][j]

                cur_row.append(cur_sum)

            cur_row.append(1)
            res.append(cur_row)

        return res


# Dynamic Programming - I
# T: O(n^2)
# M: O(n^2)
# n: number of rows
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        # since we already crossed the first row
        for i in range(numRows - 1):
            prev_row_tmp = [0] + res[-1] + [0]
            cur_row = []

            # length of the curr row is length of prev row + 1.
            for j in range(len(res[-1]) + 1):
                cur_row.append(prev_row_tmp[j] + prev_row_tmp[j + 1])

            # at this point, cur_row is constructed, we just need to append it to res
            res.append(cur_row)

        return res


# Dynamic Programming - II
# T: O(n^2)
# M: O(n^2)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1] * (i + 1) for i in range(numRows)]

        for i in range(2, numRows):
            for j in range(1, i):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]

        return res
