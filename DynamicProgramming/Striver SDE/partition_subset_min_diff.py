# The array is non-negative
from typing import List

class Solution:
    def minimumDifference(self, arr: List[int]) -> int:
        def partition_two_subset(i,n,arr,target):
            if target < 0:
                return False
            if i == n:
                if target == 0:
                    return True
                else:
                    return False
            
            pick = partition_two_subset(i+1,n,arr,target-arr[i])

            skip = partition_two_subset(i+1,n,arr,target)

            return pick or skip

        target = sum(arr)
        n = len(arr)

        mini = int(1e9)
        for i in range(target+1):
            c = partition_two_subset(0,n,arr,i)
            if c:
                # absolute value of current sum and the complement sum.
                diff = abs(i - (target - i))
                mini = min(mini,diff)
        return mini
    
    # Time Complexity: O(2^n)
    # Space Complexity: O(n)
    def minimumDifferenceMemo(self, arr: List[int]) -> int:
        def partition_two_subset(i,n,arr,target):
            if target < 0:
                return False
            if i == n:
                if target == 0:
                    return True
                else:
                    return False
            
            if dp[i][target] != -1:
                return dp[i][target]

            pick = partition_two_subset(i+1,n,arr,target-arr[i])
            skip = partition_two_subset(i+1,n,arr,target)

            dp[i][target] = pick or skip
            return dp[i][target]

        target = sum(arr)
        n = len(arr)
        dp = [[-1] * (target + 1) for _ in range(n)]

        mini = int(1e9)
        for i in range(target+1):
            dummy = partition_two_subset(0,n,arr,i)
            if dummy:
                diff = abs(i - (target - i))
                mini = min(mini,diff)

        return mini
    
    # Time Complexity: O(n*target)
    # Space Complexity: O(n*target)
    def minimumDifferenceBottomUp(self, arr: List[int]) -> int:
        n = len(arr)
        target = sum(arr)
        dp = [[False]*(target+1) for _ in range(n)]

        # Target is 0
        for i in range(n):
            dp[i][0] = True
        if arr[0] <= target:
            dp[0][arr[0]] = True

        for i in range(1,n):
            for j in range(1,target):
                not_pick = dp[i-1][j]

                pick = False
                if arr[i] <= j:
                    pick = dp[i-1][j-arr[i]]
                dp[i][j] = pick or not_pick
        mini = int(1e9)
        for i in range(target+1):
            if dp[n-1][i]:
                diff = abs(i - (target - i))
                mini = min(mini, diff)

        return mini

# Example usage:
sol = Solution()
arr = [1, 6, 11, 5]
print(sol.minimumDifference(arr))  # Output: 1, because we can partition it into [1, 5, 6] and [11]
print(sol.minimumDifferenceMemo(arr))  # Output: 1, using memoization
print(sol.minimumDifferenceBottomUp(arr))  # Output: 1, using bottom-up DP
