# Leetcode 31
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        breaking_point = -1
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                breaking_point = i
                break
        
        if breaking_point == -1:
            nums.reverse()
            return nums
        
        # find the greater element than the breaking point and swap
        for i in range(n-1,breaking_point,-1):
            if nums[i] > nums[breaking_point]:
                nums[i], nums[breaking_point] = nums[breaking_point], nums[i]
                break
        
        # reverse the element from breaking point + 1 to the end
        nums[breaking_point+1:] = nums[breaking_point+1:][::-1]
        
        return nums
    
sol = Solution()
nums = [3,2,1]
print(sol.nextPermutation(nums))