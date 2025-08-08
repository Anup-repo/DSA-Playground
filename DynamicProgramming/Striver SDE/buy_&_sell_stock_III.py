from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def max_profit_earned(ind,n,prices,buy,cap):
            if cap == 0:
                return 0
            if ind == n:
                return 0
            
            if buy == 0:
                return max(-prices[ind] + max_profit_earned(ind+1,n,prices,1,cap), 0 + max_profit_earned(ind+1,n,prices,0,cap))
            else:
                return max(prices[ind] + max_profit_earned(ind+1,n,prices,0,cap-1), 0 + max_profit_earned(ind+1,n,prices,1,cap))
        
        n = len(prices)
        return max_profit_earned(0,n,prices,0,2)
    
    def maxProfitMemo(self, prices: List[int]) -> int:
        def max_profit_earned(ind,n,prices,buy,cap):
            if cap == 0:
                return 0
            if ind == n:
                return 0
            if dp[ind][buy][cap] != -1:
                return dp[ind][buy][cap]
            if buy == 0:
                dp[ind][buy][cap] = max(-prices[ind] + max_profit_earned(ind+1,n,prices,1,cap), 0 + max_profit_earned(ind+1,n,prices,0,cap))
            else:
                dp[ind][buy][cap] = max(prices[ind] + max_profit_earned(ind+1,n,prices,0,cap-1), 0 + max_profit_earned(ind+1,n,prices,1,cap))
            return dp[ind][buy][cap]
        
        n = len(prices)
        dp = [[[-1]*3 for _ in range(2)] for _ in range(n+1)]
        return max_profit_earned(0,n,prices,0,2)
    
    def maxProfitTabulation(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-1]*3 for _ in range(2)] for _ in range(n+1)]
        

    
sol = Solution()
prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(sol.maxProfit(prices))
print(sol.maxProfitMemo(prices))
