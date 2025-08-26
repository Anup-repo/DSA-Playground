# Leetcode 53
# Kadane's Algorithm
from typing import List

class Solution:
    def maximumSubarray(self, nums: List[int]) -> int:
        maxx = float("-inf")
        current = 0
        for num in nums:
            current += num
            if current > maxx:
                maxx = current
            if current < 0:
                current = 0
        return maxx

# Time Complexity: O(n)
# Space Complexity: O(1)

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
sol = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(sol.maximumSubarray(nums))