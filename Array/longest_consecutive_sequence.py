# Leetcode 128
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums:
                length = 1
                while num + length in nums:
                    length += 1
                longest = max(longest, length)
        return longest
    
sol = Solution()
nums = [100,4,200,1,3,2]
print(sol.longestConsecutive(nums))