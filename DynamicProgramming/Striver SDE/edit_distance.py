class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def min_distance(i,j,word1,word2):
            if i < 0: # insertion
                return j + 1
            if j < 0: # deletion
                return i + 1

            if word1[i] == word2[j]:
                return min_distance(i-1,j-1,word1,word2)
            else:
                return 1 + min(min_distance(i-1,j,word1,word2), min(min_distance(i,j-1,word1,word2), min_distance(i-1,j-1,word1,word2)))

        return min_distance(len(word1)-1,len(word2)-1,word1,word2)

    def minDistanceMemo(self, word1: str, word2: str) -> int:

        def min_distance(i, j, word1, word2):
            if i < 0:  # insertion
                return j + 1
            if j < 0:  # deletion
                return i + 1

            if dp[i][j] != -1:
                return dp[i][j]
            if word1[i] == word2[j]:
                dp[i][j] = min_distance(i - 1, j - 1, word1, word2)
                return dp[i][j]
            else:
                dp[i][j] = 1 + min(
                    min_distance(i - 1, j, word1, word2),
                    min(
                        min_distance(i, j - 1, word1, word2),
                        min_distance(i - 1, j - 1, word1, word2),
                    ),
                )
                return dp[i][j]

        dp = [[-1] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        return min_distance(len(word1) - 1, len(word2) - 1, word1, word2)
    
    def minDistanceTabulation(self, word1, word2):
        m = len(word1)
        n = len(word2)
        dp = [[-1]* (n+1) for _ in range(m+1)]

        for i in range(m+1):
            dp[i][0] = i

        for j in range(n+1):
            dp[0][j] = j

        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], min(dp[i-1][j], dp[i-1][j-1]))

        return dp[m][n]
        


# Example usage
word1 = "intention"
word2 = "execution"
sol = Solution()
print(sol.minDistance(word1, word2))
print(sol.minDistanceMemo(word1,word2))
print(sol.minDistanceTabulation(word1,word2))
