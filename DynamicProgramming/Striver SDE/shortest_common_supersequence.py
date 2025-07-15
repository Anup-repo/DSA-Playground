"""
This is an extension of the Longest Common Subsequence (LCS) problem. To find the shortest common supersequence of two strings, first we find the LCS, then length of the supersequence can be calculated as: len(str1) + len(str2) - len(LCS(str1, str2)).
Example:
# str1 = "abc"
# str2 = "ac"
# LCS = "ac"
# Length of SCS = len("abc") + len("ac") - len("ac") = 3 + 2 - 2 = 3
# One way is to combine both the string which is not the shortest so to get shortest, first we have to write the common elements once then rest of the elements.
"""
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)

        dp = [[-1]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            dp[i][0] = 0
        
        for j in range(n+1):
            dp[0][j] = 0

        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return m + n - dp[m][n]
    
# Example usage:
str1 = "abc"
str2 = "ac"
solution = Solution()
print(solution.shortestCommonSupersequence(str1, str2))  # Output: 3
