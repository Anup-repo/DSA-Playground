# Reversal algorithm

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap_array(i, j):
            while i <= j:
                nums[i],nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        n = len(nums) - 1 
        swap_array(0,k)
        swap_array(k+1, n)
        swap_array(0,n)

sol = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
sol.rotate(nums,k)
print(nums)
