from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = result = nums[0]

        for num in nums[1:]:
            if num < 0:  # swap because multiplying by a negative flips roles
                max_prod, min_prod = min_prod, max_prod

            max_prod = max(num, num * max_prod)
            min_prod = min(num, num * min_prod)

            result = max(result, max_prod)

        return result

        # Time complexity: O(n)
        # Space complexity: O(1)
sol = Solution()
nums = [2, 3, -2, 4]
print(sol.maxProduct(nums))