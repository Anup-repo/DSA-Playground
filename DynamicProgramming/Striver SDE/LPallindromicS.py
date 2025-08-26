class Solution:
    def longestPalindromicSubsequence(self, s):
        s1 = s[::-1]
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == s1[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n][n]
    
"""
This is longest common subsequence problem. But you have to figure out how to get s2 (reverse of s1) as input.
"""

# Example usecase
s = "bbbab"
sol = Solution()
print(sol.longestPalindromicSubsequence(s))
