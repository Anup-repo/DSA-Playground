class Solution:
    def fibonacci(self, n: int) -> int:
        """
        This function returns the nth Fibonacci number using recursion.
        """
        if n <= 1:
            return n
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)
    
    def fibonacci_memoization(self, n: int, dp: list = None) -> int:
        """
        This function returns the nth Fibonacci number using memoization to optimize the recursive approach.
        """
        if n <= 1:
            return n
        if dp[n] != -1:
            return dp[n]
        dp[n] = self.fibonacci_memoization(n - 1, dp) + self.fibonacci_memoization(n - 2, dp)
        return dp[n]
    
    def fibonacci_bottom_up(self, n: int) -> int:
        """
        This function returns the nth Fibonacci number using a bottom-up dynamic programming approach.
        """
        if n <= 1:
            return n
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
    
    def fibonaccci_memory_optimzed(self,n:int) -> int:
        if n <= 1:
            return n
        a = 0
        b = 1
        for _ in range(2,n+1):
            c = a+b
            a = b
            b = c
        return c
    
# Example usage:
n = 0
solution = Solution()
print(solution.fibonacci(n))  # Output: 5

print(solution.fibonacci_memoization(n, dp=[-1] * (n + 1)))  # Output: 5

print(solution.fibonacci_bottom_up(n))  # Output: 5

print(solution.fibonaccci_memory_optimzed(n))
