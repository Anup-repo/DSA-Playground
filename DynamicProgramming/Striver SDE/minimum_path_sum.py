from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def minimum_path(i,j,m,n,grid):
            if i == m and j == n:
                return grid[i][j]
            if i > m or j > n:
                return float("inf")
            right = grid[i][j] + minimum_path(i+1,j,m,n,grid)
            down = grid[i][j] + minimum_path(i,j+1,m,n,grid)
            return min(right,down)

        m = len(grid)
        n = len(grid[0])
        return minimum_path(0,0,m-1,n-1,grid)
    
    def minPathSum_memo(self, grid: List[List[int]]) -> int:
        def minimum_path(i,j,m,n,grid):
            if i == m and j == n:
                return grid[i][j]
            if i > m or j > n:
                return float("inf")
            if dp[i][j] != -1:
                return dp[i][j]
            right = grid[i][j] + minimum_path(i+1,j,m,n,grid)
            down = grid[i][j] + minimum_path(i,j+1,m,n,grid)
            dp[i][j] = min(right,down)
            return dp[i][j]
        
        m = len(grid)
        n = len(grid[0])
        dp = [[-1] * n for _ in range(m)]
        return minimum_path(0,0,m-1,n-1,grid)
        
        
    def minPathSum_bottom_up(self, grid: List[List[int]]) -> int:
        def minimum_path(grid):
            m = len(grid)
            n = len(grid[0])
            dp = [[-1]*n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == 0 and j == 0:
                        dp[i][j] = grid[i][j]
                        continue
                    up = grid[i][j]
                    left = grid[i][j]
                    
                    if i > 0:
                        up += dp[i - 1][j]
                    else:
                        up = float("inf")
                    
                    if j > 0:
                        left += dp[i][j - 1]
                    else:
                        left = float("inf")
                    dp[i][j] = min(up,left)
            return dp[m-1][n-1]
        return minimum_path(grid)
                
    def minPathSum_space_optimized(self, grid: List[List[int]]) -> int:
        def minimum_path(grid):
            m = len(grid)
            n = len(grid[0])
            dp = [0]*n
            for i in range(m):
                temp = [0]*n
                for j in range(n):
                    if i == 0 and j == 0:
                        temp[j] = grid[i][j]
                        continue

                    up = grid[i][j]
                    left = grid[i][j]
                    
                    if i > 0:
                        up += dp[j]
                    else:
                        up = float("inf")
                    
                    if j > 0:
                        left += temp[j - 1]
                    else:
                        left = float("inf")
                    temp[j] = min(up,left)
                dp = temp
            return dp[n-1]
        return minimum_path(grid)

# Example
sol = Solution()
print(sol.minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]]))
print(sol.minPathSum_memo(grid = [[1,3,1],[1,5,1],[4,2,1]]))
print(sol.minPathSum_bottom_up(grid = [[1,3,1],[1,5,1],[4,2,1]]))
print(sol.minPathSum_space_optimized(grid = [[1,3,1],[1,5,1],[4,2,1]]))