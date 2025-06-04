class Solution:
    def house_robbery_I(self,nums,i,n):
        if i >= n:
            return 0
        # pick
        rob = nums[i] + self.house_robbery_I(nums,i+2,n)
        # not pick
        not_rob = self.house_robbery_I(nums,i+1,n)
        return max(rob,not_rob)
    
    def house_robbery_I_memo(self,nums,i,n,dp):
        if i >= n:
            return 0
        if dp[i] != -1:
            return dp[i]
        # pick
        rob = nums[i] + self.house_robbery_I_memo(nums,i+2,n,dp)
        # not pick
        not_rob = self.house_robbery_I_memo(nums,i+1,n,dp)
        dp[i] = max(rob,not_rob)
        return dp[i]
    
    def house_robbery_bottom_up(self, nums):
        n = len(nums)
        if n == 0:
            return 0

        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            pick = nums[i]
            if i > 1:
                pick += dp[i - 2]
            not_pick = 0 + dp[i - 1]
            dp[i] = max(pick, not_pick)

        return dp[n - 1]
    
    def house_robbery_optimization(self,nums):
        prev2 = 0
        prev1 = nums[0]
        for i in range(1,len(nums)):
            pick = nums[i]
            if i > 1:
                pick += prev2
            not_pick = 0 + prev1
            curr = max(pick, not_pick)
            prev2 = prev1
            prev1 = curr
        return prev1

# Example usage
nums = [1,2,3,1]
solution = Solution()
print(solution.house_robbery_I(nums,0,len(nums)))
print(solution.house_robbery_I_memo(nums,0,len(nums),[-1]*len(nums)))
print(solution.house_robbery_bottom_up(nums))
print(solution.house_robbery_optimization(nums))
