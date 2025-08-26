# Leetcode 169
# Moore voting algorithm
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        major = nums[0]
        for num in nums:
            if count == 0:
                major = num
            if num == major:
                count += 1
            else:
                count -= 1

        # check if it is the majority element
        count = 0
        for num in nums:
            if num == major:
                count += 1
        if count <= len(nums) // 2:
            return -1
        return major

sol = Solution()
nums = [2, 2, 1, 1, 1, 2, 2]
print(sol.majorityElement(nums))
