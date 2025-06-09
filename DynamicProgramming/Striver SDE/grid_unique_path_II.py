from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def path(m,n,i,j,obstacleGrid):
            if (i > m or j > n) or (obstacleGrid[i][j] == 1):
                return 0
            if i == m and j == n:
                return 1
            
            right = path(m,n,i,j+1,obstacleGrid)
            down = path(m,n,i+1,j,obstacleGrid)
            return right + down

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        return path(m-1,n-1,0,0,obstacleGrid)
    
    # Time Complexity: O(2^(m*n))
    # Space Complexity: O(m+n)

    # Memoization
    def uniquePathsWithObstaclesMemo(self, obstacleGrid: List[List[int]]) -> int:
        def path(m,n,i,j,obstacleGrid):
            if (i > m or j > n) or (obstacleGrid[i][j] == 1):
                return 0
            if i == m and j == n:
                return 1
            
            if dp[i][j] != -1:
                return dp[i][j]

            right = path(m,n,i,j+1,obstacleGrid)
            down = path(m,n,i+1,j,obstacleGrid)
            dp[i][j] = right + down
            return dp[i][j]

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1] * n for _ in range(m)]
        return path(m-1,n-1,0,0,obstacleGrid)
    
    # Time Complexity: O(m*n)
    # Space Complexity: O(m*n)

    # Bottom Up
    def uniquePathsWithObstaclesBottomUp(self, obstacleGrid: List[List[int]]) -> int:
        def path(m,n,i,j,obstacleGrid):
            for i in range(m):
                for j in range(n):
                    if i > 0 and j > 0 and obstacleGrid[i][j] == 1:
                        dp[i][j] = 0
                        continue
                    # If we are at the starting point, set dp[i][j] to 1.
                    if i == 0 and j == 0:
                        dp[i][j] = 1
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

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1] * n for _ in range(m)]

        return path(m,n,0,0,obstacleGrid)
    
    # Time Complexity: O(m*n)
    # Space Complexity: O(m*n)

    # Space Optimized
    def uniquePathsWithObstaclesSpaceOptimized(self, obstacleGrid: List[List[int]]) -> int:
        def path(m,n,obstacleGrid):
            dp = [0] * n    
            for i in range(m):
                temp = [0] * n
                for j in range(n):
                    if i > 0 and j > 0 and obstacleGrid[i][j] == 1:
                        temp[j] = 0
                        continue
                    # If we are at the starting point, set dp[i][j] to 1.
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

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        return path(m,n,obstacleGrid)
    
# Example
sol = Solution()
print(sol.uniquePathsWithObstacles(obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]))
print(sol.uniquePathsWithObstaclesMemo(obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]))
print(sol.uniquePathsWithObstaclesBottomUp(obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]))
print(sol.uniquePathsWithObstaclesSpaceOptimized(obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]))
