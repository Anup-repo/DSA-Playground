from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
        Given a list of days when tickets are needed and the costs of 1-day, 7-day, and 30-day tickets,
        this function calculates the minimum cost to cover all the days, using 1D dynamic programming.
        The function uses a recursive approach with memoization to avoid recalculating results for the same day.
        """
        last = days[-1]
        dp = [-1] * (last + 1)

        def solve(days, cost, n, i):
            if i >= n: # If we have processed all days, no cost is needed then it is cost + 0
                return 0
            if dp[i] != -1:
                return dp[i]

            # 1 day pass
            cost1 = cost[0] + solve(days, cost, n, i + 1)

            # 7 day pass
            j = i
            while j < n and days[j] < days[i] + 7:
                j += 1
            cost7 = cost[1] + solve(days, cost, n, j)

            # 30 day pass
            j = i
            while j < n and days[j] < days[i] + 30:
                j += 1
            cost30 = cost[2] + solve(days, cost, n, j)

            dp[i] = min(cost1, cost7, cost30)
            return dp[i]

        n = len(days)
        return solve(days, costs, n, 0)

# Example usage:
days = [1,4,6,7,8,20], costs = [2,7,15]
solution = Solution()
print(solution.mincostTickets(days, costs))

# Buttom-up approach
"""
dp[i] represents the minimum cost to reach the day i.
example:
dp[45] = min(dp[44] + 1, dp[38] + 7, dp[15] + 30)
"""

class SolutionBottomUp:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last = days[-1]
        dp = [0] * (last + 1)
        dp[0] = 0
        days_set = set(days)

        for i in range(1, last + 1):
            if i not in days_set:
                dp[i] = dp[i - 1] # skip the day
            else:
                cost1 = dp[i - 1] + costs[0]
                cost7 = dp[max(0, i - 7)] + costs[1] # This ensures we don't go negative if i < 7
                cost30 = dp[max(0, i - 30)] + costs[2]
                dp[i] = min(cost1, cost7, cost30)

        return dp[last]
    
# Example usage for bottom-up approach
days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
solution_bottom_up = SolutionBottomUp()
print(solution_bottom_up.mincostTickets(days, costs))
