from typing import List


class Solution:
    """
    This question says you have to find he maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.
    This can be solved ny sorting and then check the difference between the first and the second element. tc: O(nlogn), sc: O(n)
    But the bucket sort can be used to solve this problem.
    you need to mosify the code a little to create min amd max bucket.
    tc: O(n), sc: O(n)
    """
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0

        n = len(nums)
        bucket_count = n - 1
        bucket_size = (max_val - min_val) // bucket_count

        bucket_min = [float("inf")] * bucket_count
        bucket_max = [float("-inf")] * bucket_count

        for num in nums:
            if num == min_val or num == max_val:
                continue
            bi = (num - min_val) // bucket_size
            bucket_min[bi] = min(bucket_min[bi], num)
            bucket_max[bi] = max(bucket_max[bi], num)

        max_gap = 0
        prev = min_val
        for i in range(bucket_count):
            if bucket_min[i] == float("inf"):
                continue
            max_gap = max(max_gap, bucket_min[i] - prev)
            prev = bucket_max[i]

        max_gap = max(max_gap, max_val - prev)
        return max_gap

print(Solution().maximumGap([1, 10000000]))
