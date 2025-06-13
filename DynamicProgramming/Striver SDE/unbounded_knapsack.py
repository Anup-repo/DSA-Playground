class Solution:
    def unboundedKnapsack(self, W, val, wt, n):
        def knapsack(W, val, wt, n,i):
            if i == n-1:
                return (W // wt[i]) * val[i]

            not_take = knapsack(W,val,wt,n,i+1)
            take = float("-inf")
            if wt[i] <= W:
                take = val[i] + knapsack(W-wt[i],val,wt,n,i)
            return max(take,not_take)
        
        return knapsack(W, val, wt, n, 0)
    
    def unboundedKnapsackMemo(self, W, val, wt, n):
        def knapsack(W, val, wt, n,i):
            if i == n-1:
                return (W // wt[i]) * val[i]

            if dp[i][W] != -1:
                return dp[i][W]
            not_take = knapsack(W,val,wt,n,i+1)
            take = float("-inf")
            if wt[i] <= W:
                take = val[i] + knapsack(W-wt[i],val,wt,n,i)
            dp[i][W] = max(take,not_take)
            return dp[i][W]
        
        dp = [[-1] * (W + 1) for _ in range(n)]
        return knapsack(W, val, wt, n, 0)
    
    def unboundedKnapsackTabulation(self, capacity, values, weights, num_items):
        dp_table = [[0] * (capacity + 1) for _ in range(num_items)]

        # Initialize first row with maximum value possible using only first item
        for weight in range(weights[0], capacity + 1):
            dp_table[0][weight] = (weight // weights[0]) * values[0]

        # Fill dp table
        for item_idx in range(1, num_items):
            for current_capacity in range(capacity + 1):
                skip_item = dp_table[item_idx - 1][current_capacity]
                take_item = 0
                if weights[item_idx] <= current_capacity:
                    take_item = values[item_idx] + dp_table[item_idx][current_capacity - weights[item_idx]]
                dp_table[item_idx][current_capacity] = max(take_item, skip_item)
        
        return dp_table[num_items - 1][capacity]
    
# Example usage:
sol = Solution()
W = 8
val = [1, 4, 5, 7]
wt = [1, 3, 4, 5]
n = len(val)
print(sol.unboundedKnapsack(W, val, wt, n))  # Output: 11
print(sol.unboundedKnapsackMemo(W, val, wt, n))  # Output: 11
print(sol.unboundedKnapsackTabulation(W, val, wt, n))  # Output: 11
    