from typing import List
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs(s1, s2, i, j):
            if i < 0 or j < 0:
                return 0
            if s1[i] == s2[j]:
                return 1 + lcs(s1, s2, i - 1, j - 1)
            else:
                return 0 + max(lcs(s1, s2, i - 1, j), lcs(s1, s2, i, j - 1))

        i = len(text1) - 1
        j = len(text2) - 1
        return lcs(text1, text2, i, j)

    def longestCommonSubsequenceMemo(self, text1: str, text2: str) -> int:
        def lcs(s1, s2, i, j):
            if i < 0 or j < 0:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]
            if s1[i] == s2[j]:
                dp[i][j] = 1 + lcs(s1, s2, i - 1, j - 1)
            else:
                dp[i][j] = 0 + max(lcs(s1, s2, i - 1, j), lcs(s1, s2, i, j - 1))
            return dp[i][j]

        i = len(text1) - 1
        j = len(text2) - 1
        dp = [[-1] * (j + 1) for _ in range(i + 1)]
        return lcs(text1, text2, i, j)

    def longestCommonSubsequenceTabulation(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[-1] * (n + 1) for _ in range(m + 1)]
        """
        Since i < 0 or j < 0 is not possible, we can set dp[0][j] = dp[i][0] = 0 and taking the dp matrix as dp[m + 1][n + 1]
        """
        for i in range(m + 1):
            dp[i][0] = 0
        for j in range(n + 1):
            dp[0][j] = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]

    def longestCommonSubsequenceSpaceOptimization(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        prev = [0] * (n + 1)

        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            curr[0] = 0
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr
        return prev[n]
    
# Example usage:
text1 = "abcde"
text2 = "ace"
solution = Solution()
print(solution.longestCommonSubsequence(text1, text2))
print(solution.longestCommonSubsequenceMemo(text1, text2))
print(solution.longestCommonSubsequenceTabulation(text1, text2))
print(solution.longestCommonSubsequenceSpaceOptimization(text1, text2))