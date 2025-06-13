from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def max_coin(coins,amount,i,n):
            if amount == 0:
                return 1
            if i == n-1:
                if amount % coins[i] == 0:
                    return 1
                else:
                    return 0

            not_take = max_coin(coins,amount,i+1,n)

            take = 0
            if coins[i] <= amount:
                take = max_coin(coins,amount-coins[i],i,n)
            return take+not_take

        return max_coin(coins,amount,0,len(coins))
        
    def changeMemo(self, amount: int, coins: List[int]) -> int:
        def max_coin(coins,amount,i,n):
            if amount == 0:
                return 1
            if i == n-1:
                if amount % coins[i] == 0:
                    return 1
                else:
                    return 0
            if dp[i][amount] != -1:
                return dp[i][amount]
            not_take = max_coin(coins,amount,i+1,n)

            take = 0
            if coins[i] <= amount:
                take = max_coin(coins,amount-coins[i],i,n)
            dp[i][amount] = take+not_take
            return dp[i][amount]

        dp = [[-1]* (amount+1) for _ in range(len(coins))]

        return max_coin(coins,amount,0,len(coins))
    
    def changeTabulation(self, amount: int, coins: List[int]) -> int:
        def max_coin(coins, target_amount):
            dp = [[-1] * (target_amount + 1) for _ in range(len(coins))]

            for current_amount in range(target_amount + 1):
                if current_amount % coins[0] == 0:
                    dp[0][current_amount] = 1

            for coin_index in range(1, len(coins)):
                for current_amount in range(target_amount + 1):
                    skip_current_coin = dp[coin_index - 1][current_amount]
                    use_current_coin = 0
                    if coins[coin_index] <= current_amount:
                        use_current_coin = dp[coin_index][current_amount - coins[coin_index]]
                    dp[coin_index][current_amount] = skip_current_coin + use_current_coin
            return dp[len(coins) - 1][target_amount]
        return max_coin(coins, amount)
        
# Example usage:
sol = Solution()
print(sol.change(5, [1, 2, 5]))  # Output: 4
print(sol.changeMemo(5, [1, 2, 5]))  # Output: 4
print(sol.changeTabulation(5, [1, 2, 5]))  # Output: 4
