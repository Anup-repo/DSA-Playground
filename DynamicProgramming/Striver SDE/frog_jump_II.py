class Solution:
    def frog_jump_II(self,stones,i,n,k):
        if i == n - 1:
            return 0  # already at the end
        if i >= n:
            return float("inf")

        result = float("inf")
        for j in range(1, k + 1):  # loop over possible jump lengths
            if i + j < n:
                cost = abs(stones[i] - stones[i + j]) + self.frog_jump_II(stones, i + j, n, k)
                result = min(result, cost)
        return result
        
    def frog_jump_II_memo(self,stones,i,n,k,dp):
        if i == n - 1:
            return 0
        if i >= n:
            return float("inf")
        if dp[i] != -1:
            return dp[i]
        result = float("inf")
        for j in range(1, k + 1):
            if i + j < n:
                cost = abs(stones[i] - stones[i + j]) + self.frog_jump_II_memo(stones, i + j, n, k, dp)
                result = min(result, cost)
        dp[i] = result
        return dp[i]
    
    def frog_jump_II_bottom_up(self,stones,k):
        n = len(stones)
        dp = [float("inf")] * n
        dp[0] = 0
        for i in range(1, n):
            miniCost = float("inf")
            for j in range(1, k + 1):
                if i - j >= 0:
                    cost = abs(stones[i] - stones[i - j]) + dp[i - j]
                    miniCost = min(miniCost, cost)
            dp[i] = miniCost
        return dp[n - 1]
    
# Example usage
stones = [30, 10, 60, 10, 60, 50]
k = 2
solution = Solution()
print(solution.frog_jump_II(stones, 0, len(stones), k))
print(solution.frog_jump_II_memo(stones, 0, len(stones), k, [-1] * len(stones)))
print(solution.frog_jump_II_bottom_up(stones, k))