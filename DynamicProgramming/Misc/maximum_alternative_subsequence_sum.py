from typing import List
class Solution:
    def maxAlternatingSum(self, nums: List[int], i: int, n: int, flag: bool) -> int:
        """
        If you take then the symbol will change, + -> - (or) - -> + and if you don't take then the symbol will not change
        """
        if i == n:
            return 0
        val = nums[i]
        if not flag:
            val = -val
        take = val + self.maxAlternatingSum(nums, i + 1, n, not flag)
        not_take = 0 + self.maxAlternatingSum(nums, i + 1, n, flag)
        return max(take, not_take)
    
    def maxAlternatingSumMemo(self, nums: List[int],dp: List[List[int]], i: int, n: int, flag: bool) -> int:
        if i == n:
            return 0
        if dp[i][flag] != -1:
            return dp[i][flag]
        val = nums[i]
        if not flag:
            val = -val
        take = val + self.maxAlternatingSumMemo(nums,dp, i + 1, n, not flag)
        not_take = 0 + self.maxAlternatingSumMemo(nums,dp, i + 1, n, flag)
        dp[i][flag] = max(take, not_take)
        return dp[i][flag]

    def maxAlternatingSumButtomUp(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0, 0] for _ in range(n+1)]
        for i in range(1, n+1):
            # Even length
            dp[i][0] = max(dp[i - 1][1] - nums[i-1], dp[i - 1][0])

            # Odd length
            dp[i][1] = max(dp[i - 1][0] + nums[i-1], dp[i - 1][1])
        return max(dp[n][0], dp[n][1])

# Example Usage
nums = [4, 2, 5, 3]
solution = Solution()
print(solution.maxAlternatingSum(nums, 0, len(nums), True))

dp = [[-1] * 2 for _ in range(10**5)]
print(solution.maxAlternatingSumMemo(nums,dp, 0, len(nums), True))

print(solution.maxAlternatingSumButtomUp(nums))