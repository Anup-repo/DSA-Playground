class Solution:
    def longestSubarraySum(self, nums, k):
        longest_val = 0
        num_map = {}
        current_sum = 0
        for i, num in enumerate(nums):
            current_sum += num

            if current_sum == k:
                longest_val = max(longest_val, i+1)

            rem = current_sum - k

            if rem in num_map:
                longest_val = max(longest_val, i - num_map[rem])

            if current_sum not in num_map:
                num_map[current_sum] = i
        return longest_val

nums = [-1,1,1]
k = 1
sol = Solution()
print(sol.longestSubarraySum(nums,k))
