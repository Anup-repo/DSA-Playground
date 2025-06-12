# This is an extension of the subset sum equal to k problem
# We need to find if the array can be partitioned into two subsets such that the sum of the subsets is equal
# We can use the same approach as the subset sum equal to k problem
# We need to find if the sum of the array is even
# If it is even, we can find if there is a subset with sum equal to sum/2
# If there is, then the array can be partitioned into two subsets such that the sum of the subsets is equal
# If there is no subset with sum equal to sum/2, then the array cannot be partitioned into two subsets such that the sum of the subsets is equal

from typing import List

class Solution:
    
    def isSubsetSum(self, nums: List[int], target_sum: int) -> bool:
        n = len(nums)
        dp = [[False] * (target_sum + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        if nums[0] <= target_sum:
            dp[0][nums[0]] = True
        
        for i in range(1,n):
            for target in range(1,target_sum + 1):
                not_pick = dp[i-1][target]
                pick = False
                if nums[i] <= target:
                    pick = dp[i-1][target-nums[i]]
                dp[i][target] = pick or not_pick
        return dp[n-1][target_sum]
    
    def isSubsetSumSpaceOptimized(self, nums: List[int]) -> bool:
        target_sum = sum(nums)
        if target_sum % 2 != 0:
            return False
        target_sum = target_sum // 2

        n = len(nums)
        dp = [False] * (target_sum + 1)
        dp[0] = True
        if nums[0] <= target_sum:
            dp[nums[0]] = True
        for i in range(1,n):
            temp = [False] * (target_sum + 1)
            temp[0] = True
            for target in range(1,target_sum + 1):
                not_pick = dp[target]
                pick = False
                if nums[i] <= target:
                    pick = dp[target-nums[i]]
                temp[target] = pick or not_pick
            dp = temp
        return dp[target_sum]
    
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target_sum = total_sum // 2
        return self.isSubsetSum(nums, target_sum)
    
# Example usage:
sol = Solution()
nums = [1, 5, 11, 5]
print(sol.canPartition(nums))  # Output: True, because we can partition it into [1, 5, 5] and [11]
print(sol.isSubsetSumSpaceOptimized(nums))
