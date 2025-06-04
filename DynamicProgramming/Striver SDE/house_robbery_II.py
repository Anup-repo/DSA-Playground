class Solution:
    def house_robbery_optimization(self,nums):
        prev2 = 0
        prev1 = nums[0]
        for i in range(1,len(nums)):
            pick = nums[i]
            if i > 1:
                pick += prev2
            not_pick = 0 + prev1
            curr = max(pick, not_pick)
            prev2 = prev1
            prev1 = curr
        return prev1
    
# Example usage
nums = [1,2,3,1]
solution = Solution()

"""Edge case"""
if len(nums) == 1:
    print(nums[0])

solution1 = solution.house_robbery_optimization(nums[1:])
solution2 = solution.house_robbery_optimization(nums[:-1])
print(max(solution1,solution2))