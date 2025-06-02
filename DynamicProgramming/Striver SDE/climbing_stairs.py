# This is a variant of the Fibonacci series problem, where you can either climb 1 or 2 stairs at a time.
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        This function returns the number of distinct ways to climb n stairs, where you can either climb 1 or 2 stairs at a time.
        """
        if n == 0:
            return 1
        if n < 0:
            return 0
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
    
    def climbStairsMemoization(self, n: int, dp: list = None) -> int:
        """
        This function returns the number of distinct ways to climb n stairs, where you can either climb 1 or 2 stairs at a time, using memoization to optimize the recursive approach.
        """
        if n == 0:
            return 1
        if n < 0:
            return 0
        if dp[n] != -1:
            return dp[n]
        dp[n] = self.climbStairsMemoization(n - 1, dp) + self.climbStairsMemoization(n - 2, dp)
        return dp[n]
    
    def climbStairsBottomUp(self, n: int) -> int:
        """
        This function returns the number of distinct ways to climb n stairs, where you can either climb 1 or 2 stairs at a time, using a bottom-up dynamic programming approach.
        """
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
    
    def climbStairsSpaceOptimized(self, n: int) -> int:
        """
        This function returns the number of distinct ways to climb n stairs, where you can either climb 1 or 2 stairs at a time, using a space-optimized dynamic programming approach.
        """
        a = 1
        b = 1
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b
    
# Example usage:
solution = Solution()
print(solution.climbStairs(4))  # Output: 5

print(solution.climbStairsMemoization(4, dp=[-1] * 5))  # Output: 5

print(solution.climbStairsBottomUp(4))  # Output: 5

print(solution.climbStairsSpaceOptimized(4))