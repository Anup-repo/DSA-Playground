class Solution:
    def frog_jump(self,i,n,arr):
        if i == n - 1:
            return 0
        if i >= n:
            return float('inf')

        # Jump 1 step
        jump1 = abs(arr[i] - arr[i + 1]) + self.frog_jump(i + 1, n, arr)

        # Jump 2 steps (if possible)
        jump2 = float('inf')
        if i + 2 < n:
            jump2 = abs(arr[i] - arr[i + 2]) + self.frog_jump(i + 2, n, arr)

        return min(jump1, jump2)
    
    def frog_jump_memo(self,i,n,arr,dp):
        if i == n - 1:
            return 0
        if i >= n:
            return float('inf')
        if dp[i] != -1:
            return dp[i]

        # Jump 1 step
        jump1 = abs(arr[i] - arr[i + 1]) + self.frog_jump_memo(i + 1, n, arr, dp)

        # Jump 2 steps (if possible)
        jump2 = float('inf')
        if i + 2 < n:
            jump2 = abs(arr[i] - arr[i + 2]) + self.frog_jump_memo(i + 2, n, arr, dp)

        dp[i] = min(jump1, jump2)
        return dp[i]
    
    def frog_jump_bottom_up(self,arr):
        n = len(arr)
        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(1, n):
            jump1 = abs(arr[i] - arr[i - 1]) + dp[i - 1]
            jump2 = float('inf')
            if i > 1:
                jump2 = abs(arr[i] - arr[i - 2]) + dp[i - 2]
            dp[i] = min(jump1, jump2)

        return dp[n - 1]
    
    def frog_jump_memory_optimization(self,arr):
        n = len(arr)
        prev = 0
        prev2 = 0
        for i in range(1, n):
            jump1 = abs(arr[i] - arr[i - 1]) + prev
            jump2 = float('inf')
            if i > 1:
                jump2 = abs(arr[i] - arr[i - 2]) + prev2
            prev2 = prev
            prev = min(jump1, jump2)

        return prev
    
# Example usage:
arr = [10,20,30,10]
solution = Solution()
print(solution.frog_jump(0, len(arr), arr))

print(solution.frog_jump_memo(0, len(arr), arr, dp=[-1] * len(arr)))

print(solution.frog_jump_bottom_up(arr))

print(solution.frog_jump_memory_optimization(arr))
