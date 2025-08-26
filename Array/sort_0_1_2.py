# Leetcode 75
# Dutch National flag algorithm

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1
        low, mid = 0, 0
        high = n

        while mid <= high:
            if nums[mid] == 1:
                mid += 1
                continue
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                mid += 1
                low += 1
            if nums[mid] == 2:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
                mid += 1
        return nums

sol = Solution()
nums = [2, 0, 2, 1, 1, 0]
print(sol.sortColors(nums))
