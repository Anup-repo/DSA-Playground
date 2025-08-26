# Leetcode `https://leetcode.com/problems/count-of-smaller-numbers-after-self/`

from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * n
        indexed_nums = list(enumerate(nums))  # (index, value)

        def merge_sort(start, end):
            if start >= end:
                return
            mid = (start + end) // 2
            merge_sort(start, mid)
            merge_sort(mid + 1, end)
            merge(start, mid, end)

        def merge(start, mid, end):
            temp = []
            i, j = start, mid + 1
            while i <= mid and j <= end:
                if indexed_nums[i][1] <= indexed_nums[j][1]:
                    temp.append(indexed_nums[j])
                    j += 1
                else:
                    # indexed_nums[i] is greater → it has (end - j + 1) smaller elements after it
                    counts[indexed_nums[i][0]] += end - j + 1
                    temp.append(indexed_nums[i])
                    i += 1

            while i <= mid:
                temp.append(indexed_nums[i])
                i += 1
            while j <= end:
                temp.append(indexed_nums[j])
                j += 1

            for k in range(start, end + 1):
                indexed_nums[k] = temp[k - start]


        merge_sort(0, n - 1)
        return counts


# Test
sol = Solution()
nums = [5, 2, 6, 1]
print(sol.countSmaller(nums))  # [2, 1, 1, 0]
