class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def unique_path(i, j, n, m):
            if i == n and j == m:
                return 1
            if i > n or j > m:
                return 0

            right = unique_path(i, j + 1, n, m)

            down = unique_path(i + 1, j, n, m)

            return right + down

        return unique_path(0, 0, n - 1, m - 1)

        # Time Complexity: O(2^(n+m))
        # Space Complexity: O(n+m)

    def uniquePaths_memo(self, m: int, n: int) -> int:
        dp = [[-1] * m for _ in range(n)]

        def unique_path(i, j, n, m, dp):
            if i == n and j == m:
                return 1
            if i > n or j > m:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            right = unique_path(i, j + 1, n, m, dp)

            down = unique_path(i + 1, j, n, m, dp)

            dp[i][j] = right + down

            return dp[i][j]

        return unique_path(0, 0, n - 1, m - 1, dp)

        # Time Complexity: O(n*m)
        # Space Complexity: O(n*m)

    def  uniquePaths_bottom_up(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                up = 0
                left = 0
                
                # Check if moving up is a valid option (not out of bounds).
                if i > 0:
                    up = dp[i - 1][j]
                
                # Check if moving left is a valid option (not out of bounds).
                if j > 0:
                    left = dp[i][j - 1]
                
                # Calculate and store the number of ways to reach the current cell.
                dp[i][j] = up + left

        return dp[m - 1][n - 1]

        # Time Complexity: O(n*m)
        # Space Complexity: O(n*m)

    def uniquePaths_space_optimized(self, m: int, n: int) -> int:
        dp = [0] * n

        for i in range(m):
            temp = [0] * n
            for j in range(n):
                if i == 0 and j == 0:
                    temp[j] = 1
                    continue

                up = 0
                left = 0
                
                # Check if moving up is a valid option (not out of bounds).
                if i > 0:
                    up = dp[j]
                
                # Check if moving left is a valid option (not out of bounds).
                if j > 0:
                    left = temp[j - 1]
                    
                # Calculate and store the number of ways to reach the current cell.
                temp[j] = up + left

            dp = temp
        return dp[n - 1]

        # Time Complexity: O(n*m)
        # Space Complexity: O(m)

# Example Useage:
m = 3
n = 2
solution = Solution()
print(solution.uniquePaths(m, n))
print(solution.uniquePaths_memo(m, n))
print(solution.uniquePaths_bottom_up(m, n))
print(solution.uniquePaths_space_optimized(m, n))