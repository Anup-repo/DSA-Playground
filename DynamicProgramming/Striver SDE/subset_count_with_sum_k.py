class Solution:
    def isSubsetSum(self, arr, sum):
        def subset_sum(i, n, arr, target):
            if target < 0:
                return 0
            if i == n:
                if target == 0:
                    return 1
                else:
                    return 0
            # Pick
            pick = subset_sum(i+1, n, arr, target - arr[i])
            # Skip
            skip = subset_sum(i+1, n, arr, target)
            return pick + skip
        
        n = len(arr)
        return subset_sum(0, n, arr, sum)

    def isSubsetSumMemo(self, arr, sum):
        def subset_sum(i, n, arr, target):
            if target < 0:
                return 0
            if i == n:
                if target == 0:
                    return 1
                else:
                    return 0

            if dp[i][target] != -1:
                return dp[i][target]    
            # Pick
            pick = subset_sum(i+1, n, arr, target - arr[i])
            # Skip
            skip = subset_sum(i+1, n, arr, target)

            dp[i][target] = pick + skip
            return dp[i][target]
        
        n = len(arr)
        dp = [[-1] * (sum + 1) for _ in range(n)]
        return subset_sum(0, n, arr, sum)

    def isSubsetSumBottomUp(self, arr, sum):
        n = len(arr)
        # dp[i][j] represents number of ways to get sum j using first i elements
        dp = [[0] * (sum + 1) for _ in range(n)]

        if arr[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1
        
        if arr[0] != 0 and arr[0] <= sum:
            dp[0][arr[0]] = 1

        for i in range(1, n):
            # why from 0 to sum + 1?
            # because we want to include sum 0
            for target in range(sum + 1):
                # Don't pick current element
                not_pick = dp[i - 1][target]
                
                # Pick current element (if possible)
                pick = 0
                if arr[i] <= target:
                    pick = dp[i - 1][target - arr[i]]
                
                dp[i][target] = pick + not_pick

        return dp[n-1][sum]

    def isSubsetSumSpaceOptimized(self, arr, sum):
        n = len(arr)
        dp = [0] * (sum + 1)
        if arr[0] == 0:
            dp[0] = 2
        else:
            dp[0] = 1
        
        if arr[0] != 0 and arr[0] <= sum:
            dp[arr[0]] = 1

        for i in range(1, n):
            temp = [0] * (sum + 1)
            for target in range(sum + 1):
                # Don't pick current element
                not_pick = dp[target]
                
                # Pick current element (if possible)
                pick = 0
                if arr[i] <= target:
                    pick = dp[target - arr[i]]
                
                temp[target] = pick + not_pick
            dp = temp

        return dp[sum]


# Example usage and testing
sol = Solution()

# Test case 1
arr = [0, 0, 1]
target_sum = 1
print(f"Array: {arr}, Target: {target_sum}")
print("Recursive:", sol.isSubsetSum(arr, target_sum))
print("Memoized:", sol.isSubsetSumMemo(arr, target_sum))  
print("Bottom-up:", sol.isSubsetSumBottomUp(arr, target_sum))
print("Space optimized V1:", sol.isSubsetSumSpaceOptimized(arr, target_sum))
