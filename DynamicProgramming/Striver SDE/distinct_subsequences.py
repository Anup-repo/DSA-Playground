class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def count_distinct(s,t,i,j):
            if j < 0:
                return 1
            if i < 0:
                return 0

            if s[i] == t[j]:
                return count_distinct(s,t,i-1,j-1) + count_distinct(s,t,i-1,j)
            else:
                return count_distinct(s,t,i-1,j)

        i = len(s) - 1
        j = len(t) - 1

        return count_distinct(s,t,i,j)

    def numDistinctMemo(self, s: str, t: str) -> int:
        def count_distinct(s, t, i, j):
            if j < 0:
                return 1
            if i < 0:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == t[j]:
                dp[i][j] = count_distinct(s, t, i - 1, j - 1) + count_distinct(
                    s, t, i - 1, j
                )
                return dp[i][j]
            else:
                dp[i][j] = count_distinct(s, t, i - 1, j)
                return dp[i][j]

        i = len(s) - 1
        j = len(t) - 1
        dp = [[-1]*(j+1) for _ in range(i+1)]

        return count_distinct(s, t, i, j)

    def numDistinctTabulation(self,s,t):
        m = len(s)
        n = len(t)
        dp = [[-1]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 1

        for j in range(1,n+1):
            dp[0][j] = 0

        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[m][n]

    def numDistinctSpaceOptimized(self, s, t):
        m = len(s)
        n = len(t)
        prev = [0 for _ in range(n + 1)]
        prev[0] = 1

        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    curr[j] = prev[j - 1] + prev[j]
                else:
                    curr[j] = prev[j]
            prev = curr
        return prev[n]


# s = "babgbag"
# t = "bag"
s = "rabbbit"
t = "rabbit"
sol = Solution()
print(sol.numDistinct(s,t))
print(sol.numDistinctMemo(s,t))
print(sol.numDistinctTabulation(s,t))
print(sol.numDistinctSpaceOptimized(s,t))
