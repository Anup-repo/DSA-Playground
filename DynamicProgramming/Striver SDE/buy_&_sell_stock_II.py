from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def max_profit_earned(ind,n,prices,buy):
            if ind == n:
                return 0
            
            if buy == 0:
                return max(-prices[ind] + max_profit_earned(ind+1,n,prices,1), 0 + max_profit_earned(ind+1,n,prices,0))
            else:
                return max(prices[ind] + max_profit_earned(ind+1,n,prices,0), 0 + max_profit_earned(ind+1,n,prices,1))
        
        n = len(prices)
        return max_profit_earned(0,n,prices,0)
    
    def maxProfitMemo(self, prices: List[int]) -> int:
        def max_profit_earned(ind,n,prices,buy):
            if ind == n:
                return 0
            
            if dp[ind][buy] != -1:
                return dp[ind][n]
            if buy == 0:
                return max(-prices[ind] + max_profit_earned(ind+1,n,prices,1), 0 + max_profit_earned(ind+1,n,prices,0))
            else:
                return max(prices[ind] + max_profit_earned(ind+1,n,prices,0), 0 + max_profit_earned(ind+1,n,prices,1))
        
        n = len(prices)
        dp = [[-1]*2 for _ in range(n)]
        return max_profit_earned(0,n,prices,0)
    
    def maxProfitTabulation(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1]*2 for _ in range(n+1)]
        dp[n][0], dp[n][1] = 0,0

        for ind in range(n-1,-1,-1):
            for buy in range(2):
                if buy == 0:
                    dp[ind][buy] = max(-prices[ind] + dp[ind+1][1], 0 + dp[ind+1][0])
                else:
                    dp[ind][buy] = max(prices[ind] + dp[ind+1][0], 0 + dp[ind+1][1])
        return dp[0][0]

sol = Solution()
prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))
print(sol.maxProfitMemo(prices))
print(sol.maxProfitTabulation(prices))
