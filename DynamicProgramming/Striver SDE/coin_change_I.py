from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def minimum_coins(coins, amount, ind, n):
            if ind == n - 1:
                if amount % coins[ind] == 0:
                    return amount // coins[ind]
                else:
                    return int(1e9)

            not_take = minimum_coins(coins, amount, ind + 1, n)
            take = int(1e9)
            if coins[ind] <= amount:
                take = 1 + minimum_coins(coins, amount - coins[ind], ind, n)
            return min(not_take, take)

        min_coin = minimum_coins(coins, amount, 0, len(coins))
        if min_coin == int(1e9):
            return -1
        return min_coin

    def coinChangeMemo(self, coins: List[int], amount: int) -> int:
        def minimum_coins(coins, amount, ind, n):
            if ind == n - 1:
                if amount % coins[ind] == 0:
                    return amount // coins[ind]
                else:
                    return int(1e9)

            if dp[ind][amount] != int(1e9):
                return dp[ind][amount]

            not_take = minimum_coins(coins, amount, ind + 1, n)
            take = int(1e9)
            if coins[ind] <= amount:
                take = 1 + minimum_coins(coins, amount - coins[ind], ind, n)
            dp[ind][amount] = min(not_take, take)
            return dp[ind][amount]

        dp = [[int(1e9)] * (amount + 1) for _ in range(len(coins))]
        min_coin = minimum_coins(coins, amount, 0, len(coins))
        if min_coin == int(1e9):
            return -1
        return min_coin

    def coinChangeTabulation(self, coins: List[int], target_amount: int) -> int:
        num_coins = len(coins)
        dp = [[float('inf')] * (target_amount + 1) for _ in range(num_coins)]
        
        for amount in range(target_amount + 1):
            if amount % coins[0] == 0:
                dp[0][amount] = amount // coins[0]
        
        for coin_index in range(1, num_coins):
            for amount in range(target_amount + 1):
                not_use_coin = dp[coin_index - 1][amount]
                use_coin = float('inf')
                if coins[coin_index] <= amount:
                    use_coin = 1 + dp[coin_index][amount - coins[coin_index]]
                dp[coin_index][amount] = min(not_use_coin, use_coin)
        return dp[num_coins - 1][target_amount] if dp[num_coins - 1][target_amount] != float('inf') else -1
    
# Example usecase
coins = [1, 2, 5]
amount = 11
print(Solution().coinChange(coins, amount))
print(Solution().coinChangeMemo(coins, amount))
print(Solution().coinChangeTabulation(coins, amount))
