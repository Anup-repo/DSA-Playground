# Gap theorm

from typing import List
class Solution:
    def swapIfGreater(self, arr1,arr2,i,j):
        if arr1[i] > arr2[j]:
            arr1[i],arr2[j] = arr2[j],arr1[i]

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        len = m + n
        gap = len // 2 + len % 2
        while gap > 0:
            left = 0
            right = gap
            while right < len:
                # arr1 and arr2
                if left < n and right >= n:
                    self.swapIfGreater(nums1, nums2, left, right - n)
                # arr2 and arr2
                elif left >= n:
                    self.swapIfGreater(nums2, nums2, left - n, right - n)
                # arr1 and arr1
                else:
                    self.swapIfGreater(nums1, nums1, left, right)
                left += 1
                right += 1
            if gap == 1:
                break
            gap = gap // 2 + gap % 2

        return nums1, nums2
    
sol = Solution()
nums1 = [1,2,3]
m = 3
nums2 = [2,5,6]
n = 3
print(sol.merge(nums1,m,nums2,n))