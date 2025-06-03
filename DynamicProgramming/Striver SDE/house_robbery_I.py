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

# Example usage
nums = [1,2,3,1]
solution = Solution()
print(solution.house_robbery_I(nums,0,len(nums)))
print(solution.house_robbery_I_memo(nums,0,len(nums),[-1]*len(nums)))


