class Solution:
    def knapsack(self, W, val, wt, ind, n):
        if ind == n-1:
            if wt[ind] <= W:
                return val[ind]
            else:
                return 0

        not_pick = self.knapsack(W, val, wt, ind+1, n)
        pick = float("-inf")
        if wt[ind] <= W:
            pick = val[ind] + self.knapsack(W - wt[ind], val, wt, ind+1, n)
        return max(pick, not_pick)
    
    def knapsackMemoization(self, W, val, wt, ind, n, dp):
        if ind == n-1:
            if wt[ind] <= W:
                return val[ind]
            else:
                return 0

        if dp[ind][W] != -1:
            return dp[ind][W]

        not_pick = self.knapsackMemoization(W, val, wt, ind+1, n, dp)
        pick = float("-inf")
        if wt[ind] <= W:
            pick = val[ind] + self.knapsackMemoization(W - wt[ind], val, wt, ind+1, n, dp)
        
        dp[ind][W] = max(pick, not_pick)
        return dp[ind][W]
    
    def knapsackTabulation(self, W, val, wt, n):
        dp = [[0] * (W + 1) for _ in range(n)]

        for w in range(wt[0],W + 1):
                dp[0][w] = val[0]
        
        for i in range(1,n):
            for w in range(W + 1):
                not_pick = 0 + dp[i-1][w]
                pick = float("-inf")
                if wt[i] <= w:
                    pick = val[i] + dp[i-1][w - wt[i]]
                dp[i][w] = max(pick, not_pick)
        return dp[n-1][W]
    
    def knapsackSpaceOptimized(self, W, val, wt, n):
        dp = [0] * (W + 1)
        for w in range(wt[0], W + 1):
            dp[w] = val[0]

        for i in range(1, n):
            temp = [0] * (W + 1)
            for w in range(W + 1):
                not_pick = 0 + dp[w]
                pick = float("-inf")
                if wt[i] <= w:
                    pick = val[i] + dp[w - wt[i]]
                temp[w] = max(pick, not_pick)
            dp = temp
        return dp[W]
    
# Example usage:
sol = Solution()
W = 50
val = [60, 100, 120]
wt = [10, 20, 30]
n = len(val)
print(sol.knapsack(W, val, wt, 0, n))
print(sol.knapsackMemoization(W, val, wt, 0, n, [[-1] * (W + 1) for _ in range(n)]))
print(sol.knapsackTabulation(W, val, wt, n))
print(sol.knapsackSpaceOptimized(W, val, wt, n))

