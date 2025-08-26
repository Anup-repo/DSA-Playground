class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[-1] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = 0
        for j in range(n + 1):
            dp[0][j] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return (m + n) - 2 * dp[m][n]

"""
this is longest common subsequence problem, for insertion length of word2 - LCS and deletion length of word1 - LCS
In short it is lenght of word1 + word2 - 2 * LCS
"""

# example usage
word1 = "intention"
word2 = "execution"
sol = Solution()
print(sol.minDistance(word1, word2))
