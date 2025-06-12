class Solution:
    def countPartitions(self, arr, d):
        def subset_sum(i, n, arr, target):
            if target < 0:
                return 0
            if i == n:
                if target == 0:
                    return 1
                else:
                    return 0
            # Pick
            pick = subset_sum(i + 1, n, arr, target - arr[i])
            # Skip
            skip = subset_sum(i + 1, n, arr, target)
            return pick + skip

        n = len(arr)
        total_sum = sum(arr)
        if total_sum - d < 0 or (total_sum - d) % 2 != 0:
            return 0
        s2 = (total_sum - d) // 2
        return subset_sum(0, n, arr, s2)

    def countPartitionsMemo(self, arr, d):
        mod = 10 ** 9 + 7
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
            pick = subset_sum(i + 1, n, arr, target - arr[i])
            # Skip
            skip = subset_sum(i + 1, n, arr, target)

            dp[i][target] = (pick + skip) % mod
            return dp[i][target]

        n = len(arr)
        total_sum = sum(arr)
        if total_sum - d < 0 or (total_sum - d) % 2 != 0:
            return 0
        s2 = (total_sum - d) // 2
        dp = [[-1] * (s2 + 1) for _ in range(n)]
        return subset_sum(0, n, arr, s2)

    def countPartitionsBottomUp(self, arr, d):
        mod = 10 ** 9 + 7
        n = len(arr)
        total_sum = sum(arr)
        if total_sum - d < 0 or (total_sum - d) % 2 != 0:
            return 0
        s2 = (total_sum - d) // 2
        dp = [[0] * (s2 + 1) for _ in range(n)]

        if arr[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1

        if arr[0] != 0 and arr[0] <= s2:
            dp[0][arr[0]] = 1

        for i in range(1, n):
            # why from 0 to sum + 1?
            # because we want to include sum 0
            for target in range(s2 + 1):
                # Don't pick current element
                not_pick = dp[i - 1][target]

                # Pick current element (if possible)
                pick = 0
                if arr[i] <= target:
                    pick = dp[i - 1][target - arr[i]]

                dp[i][target] = (pick + not_pick) % mod

        return dp[n - 1][s2]

    def countPartitionsSpaceOptimized(self, arr, d):
        mod = 10 ** 9 + 7
        n = len(arr)
        total_sum = sum(arr)
        if total_sum - d < 0 or (total_sum - d) % 2 != 0:
            return 0
        s2 = (total_sum - d) // 2

        dp = [0] * (s2 + 1)
        if arr[0] == 0:
            dp[0] = 2
        else:
            dp[0] = 1

        if arr[0] != 0 and arr[0] <= s2:
            dp[arr[0]] = 1

        for i in range(1, n):
            temp = [0] * (s2 + 1)
            for target in range(s2 + 1):
                # Don't pick current element
                not_pick = dp[target]

                # Pick current element (if possible)
                pick = 0
                if arr[i] <= target:
                    pick = dp[target - arr[i]]

                temp[target] = (pick + not_pick) % mod
            dp = temp

        return dp[s2]


# Example usage and testing
sol = Solution()

# Test case 1
arr = [1,1,1,1]
arr = [5,2,6,4]
target_sum = 3 # 0
print(f"Array: {arr}, Target: {target_sum}")
print("Recursive:", sol.countPartitions(arr, target_sum))
print("Memoized:", sol.countPartitionsMemo(arr, target_sum))
print("Bottom-up:", sol.countPartitionsBottomUp(arr, target_sum))
print("Space optimized V1:", sol.countPartitionsSpaceOptimized(arr, target_sum))
