# neetcode DP - bottom-up
# T: O(m * n) where m and n is length of two strings
# M: O(m * n). Because we're creating a 2-d grid
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Why len(text2) + 1 ? Because we need one more col to have all 0s in it.
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # In these if and else blocks, we're just filling in the values in the grid
                if text1[i] == text2[j]:
                    # dp[i + 1][j + 1] is the next diagonal cell
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]

# Bruteforce
class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int: