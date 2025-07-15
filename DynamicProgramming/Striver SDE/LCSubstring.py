class Solution:
    def longestCommonSubstr(self, s1, s2):
        def LCS(s1,s2,i,j,count):
            if i < 0 or j < 0:
                return count
            if s1[i] == s2[j]:
                count = LCS(s1,s2,i-1,j-1,count+1)
            return max(count,LCS(s1,s2,i-1,j,0),LCS(s1,s2,i,j-1,0))
        
        return LCS(s1,s2,len(s1)-1,len(s2)-1,0)
    
    def longestCommonSubstrTabulation(self, s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_len = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    max_len = max(max_len, dp[i][j])
                else:
                    dp[i][j] = 0
        return max_len
    
    def longestCommonSubstrSpaceOptimize(self, s1, s2):
        m, n = len(s1), len(s2)
        max_len = 0
        prev = [0] * (n + 1)
        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = prev[j - 1] + 1
                    if curr[j] > max_len:
                        max_len = curr[j]
                # else: curr[j] = 0  # already zero by initialization
            prev = curr
        return max_len

    
# Example usecase
sol = Solution()
s1 = "abcjklp"
s2 = "acjkp"
print(sol.longestCommonSubstr(s1,s2))
print(sol.longestCommonSubstrTabulation(s1, s2))
print(sol.longestCommonSubstrSpaceOptimize(s1,s2))