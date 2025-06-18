class Solution:

    def printLCS(self, s1: str, s2: str) -> str:
        def lcs(i, j):
            if i < 0 or j < 0:
                return ""
            if s1[i] == s2[j]:
                return lcs(i - 1, j - 1) + s1[i]
            else:
                res1 = lcs(i - 1, j)
                res2 = lcs(i, j - 1)
                return res1 if len(res1) > len(res2) else res2

        return lcs(len(s1) - 1, len(s2) - 1)

        # Time Complexity: O(2^(n+m))
        # Space Complexity: O(n+m)

    def printLCSTabulation(self, X, Y, m, n):
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if X[i - 1] == Y[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        length = dp[m][n]
        ans = [""] * length
        ind = length - 1

        while m > 0 and n > 0:
            if X[m-1] == Y[n-1]:
                ans[ind] = X[m-1]
                m -= 1
                n -= 1
                ind -= 1
            elif dp[m-1][n] > dp[m][n-1]:
                m -= 1
            else:
                n -= 1
        return "".join(ans)

        # Time Complexity: O(n*m)
        # Space Complexity: O(n*m)

# Example usecase:
X = "GXTXAYB"
Y = "AGGTAB"
m = len(X)
n = len(Y)
print(Solution().printLCS(X, Y))
print(Solution().printLCSTabulation(X, Y, m, n))
