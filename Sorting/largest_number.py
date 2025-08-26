# leetcode 179
# https://leetcode.com/problems/largest-number/

from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        
        def merge_sort(arr, low, high):
            if low >= high:
                return
            mid = (low + high) // 2
            merge_sort(arr, low, mid)
            merge_sort(arr, mid + 1, high)
            merge(arr, low, mid, high)
        
        def merge(arr, low, mid, high):
            temp = []
            i = low
            j = mid + 1
            while i <= mid and j <= high:
                if arr[i] + arr[j] < arr[j] + arr[i]:
                    temp.append(arr[j])
                    j += 1
                else:
                    temp.append(arr[i])
                    i += 1
            while i <= mid:
                temp.append(arr[i])
                i += 1
            while j <= high:
                temp.append(arr[j])
                j += 1
            for i in range(low, high + 1):
                arr[i] = temp[i - low]

        merge_sort(nums, 0, len(nums) - 1)

        if nums[0] == "0":
            return "0"
        
        return "".join(nums)
    
# Time: O(nlogn)
# Space: O(n)
sol = Solution()
nums = [3, 30, 34, 5, 9]
print(sol.largestNumber(nums))
