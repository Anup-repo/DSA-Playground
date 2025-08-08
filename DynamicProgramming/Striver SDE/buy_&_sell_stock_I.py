from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                profit = max(profit, prices[i] - buy)
        return profit
    
# Example usage:
sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5 