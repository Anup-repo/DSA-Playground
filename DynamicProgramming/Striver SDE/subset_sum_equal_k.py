class Solution:
    def isSubsetSum (self, arr, sum):
        def subset_sum(i,n,arr,target):
            if target < 0:
                return False
            if i == n:
                if target == 0:
                    return True
                else:
                    return False
            # Pick
            pick = subset_sum(i+1,n,arr,target-arr[i])

            # skip
            skip = subset_sum(i+1,n,arr,target)

            return pick or skip
        
        n = len(arr)
        return subset_sum(0,n,arr,sum)
    
    # Time Complexity: O(2^n)
    # Space Complexity: O(n)

    def isSubsetSumMemo(self, arr, sum):
        def subset_sum(i,n,arr,target):
            if target < 0:
                return False
            if i == n:
                if target == 0:
                    return True
                else:
                    return False

            if dp[i][target] != -1:
                return dp[i][target]    
            # Pick
            pick = subset_sum(i+1,n,arr,target-arr[i])

            # skip
            skip = subset_sum(i+1,n,arr,target)

            dp[i][target] = pick or skip
            return dp[i][target]
        
        n = len(arr)
        dp = [[-1] * (sum + 1) for _ in range(n)]
        return subset_sum(0,n,arr,sum)
    
    # Time Complexity: O(n*sum)
    # Space Complexity: O(n*sum)

    def isSubsetSumBottomUp(self, arr, sum):
        def subset_sum(arr, target_sum):
            n = len(arr)
            dp = [[False] * (target_sum + 1) for _ in range(n)]

            # Base Case: sum 0 is always possible with empty subset
            for i in range(n):
                dp[i][0] = True

            # Can we reach the sum arr[0] using just the first element?
            if arr[0] <= target_sum:
                dp[0][arr[0]] = True

            for i in range(1, n):
                for target in range(1, target_sum + 1):
                    not_pick = dp[i - 1][target]
                    pick = False
                    if arr[i] <= target:
                        pick = dp[i - 1][target - arr[i]]
                    dp[i][target] = pick or not_pick

            return dp[n - 1][target_sum]
        
        return subset_sum(arr, sum)
    
    # Time Complexity: O(n*sum)
    # Space Complexity: O(n*sum)

    def isSubsetSumSpaceOptimized(self, arr, sum):
        def subset_sum(arr, target_sum):
            n = len(arr)
            dp = [False] * (target_sum + 1)
            dp[0] = True
            if arr[0] <= target_sum:
                dp[arr[0]] = True
            for i in range(1, n):
                temp = [False] * (target_sum + 1)
                for target in range(1, target_sum + 1):
                    not_pick = dp[target]
                    pick = False
                    if arr[i] <= target:
                        pick = dp[target - arr[i]]
                    temp[target] = pick or not_pick

                dp = temp
            return dp[target_sum]
        
        return subset_sum(arr, sum)
    
    # Time Complexity: O(n*sum)
    # Space Complexity: O(sum)

# Example usage
sol = Solution()
arr = [3, 34, 4, 12, 5, 2]
sum = 9
print(sol.isSubsetSum(arr, sum))
print(sol.isSubsetSumMemo(arr, sum))
print(sol.isSubsetSumBottomUp(arr, sum))
print(sol.isSubsetSumSpaceOptimized(arr, sum))
