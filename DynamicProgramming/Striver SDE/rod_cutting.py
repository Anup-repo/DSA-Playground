class Solution:
    def cutRod(self, price):
        def rod_cutting(price,n,i):
            """
            if you only have length 1 rods to work with, and the rod you still have is length n, then there’s only one thing to do — cut it into n pieces of length 1 and sell each for price[0].
            """
            if i == 0:
                return n * price[0]
        
            not_pick = rod_cutting(price,n,i-1)
        
            pick = float("-inf")
            rod_length = i+1
            if rod_length <= n:
                pick = price[i] + rod_cutting(price,n-rod_length,i)
            return max(pick,not_pick)
        
        return (rod_cutting(price,len(price),len(price)-1))
    
    def cutRod_memo(self, price):
        def rod_cutting(price,n,i,dp):
            if i == 0:
                return n * price[0]
            if dp[i][n] != -1:
                return dp[i][n]
            not_pick = rod_cutting(price,n,i-1,dp)
            pick = float("-inf")
            rod_length = i+1
            if rod_length <= n:
                pick = price[i] + rod_cutting(price,n-rod_length,i,dp)
            dp[i][n] = max(pick,not_pick)
            return dp[i][n]
        
        n = len(price)
        dp = [[-1 for _ in range(n+1)] for _ in range(n)]
        return rod_cutting(price,n,n-1,dp)
    

    def cutRod_bottom_up(self, price):
        n = len(price)
        dp = [[0 for _ in range(n+1)] for _ in range(n)]
        
        for j in range(n+1):
            dp[0][j] = j * price[0]
        
        for ind in range(1, n):
            for N in range(n+1):
                not_pick = dp[ind-1][N]
                pick = float("-inf")
                rod_length = ind + 1
                if rod_length <= N:
                    pick = price[ind] + dp[ind][N - rod_length]
                dp[ind][N] = max(pick, not_pick)
        
        return dp[n-1][n]
    
    def cutRod_optimization(self, price):
        n = len(price)
        prev = [0] * (n + 1)
        
        for j in range(n + 1):
            prev[j] = j * price[0]
        
        for ind in range(1, n):
            curr = [0] * (n + 1)
            for N in range(n + 1):
                not_pick = prev[N]
                pick = float("-inf")
                rod_length = ind + 1
                if rod_length <= N:
                    pick = price[ind] + curr[N - rod_length]
                curr[N] = max(pick, not_pick)
            prev = curr
        
        return prev[n]
    
# Example usage

price = [3, 5, 8, 9, 10, 17, 17, 20]
solution = Solution()
print(solution.cutRod(price))  # Using recursion
print(solution.cutRod_memo(price))  # Using memoization
print(solution.cutRod_bottom_up(price))  # Using bottom-up DP
print(solution.cutRod_optimization(price))  # Using space optimization