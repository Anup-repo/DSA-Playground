from typing import List

class Solution:
    def maxFallingPathSum(self, matrix: List[List[int]]) -> int:
        def maximum_path(grid,i,j,m):
            if j < 0 or j >= m :
                return float("-inf")
            if i == m-1:
                return grid[i][j]
            left_d = grid[i][j] + maximum_path(grid,i+1,j-1,m)
            right_d = grid[i][j] + maximum_path(grid,i+1,j+1,m)
            down = grid[i][j] + maximum_path(grid,i+1,j,m)
            return max(down,left_d,right_d)
        
        m = len(matrix)
        max_sum = float("-inf")
        for j in range(m):
            max_sum = max(max_sum,maximum_path(matrix,0,j,m))
        return max_sum
    
    # Time Complexity: O(3^m)
    # Space Complexity: O(m)

    def maxFallingPathSumMemo(self, matrix: List[List[int]]) -> int:
        def maximum_path(grid,i,j,m):
            if j < 0 or j >= m :
                return float("-inf")
            if i == m-1:
                return grid[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            left_d = grid[i][j] + maximum_path(grid,i+1,j-1,m)
            right_d = grid[i][j] + maximum_path(grid,i+1,j+1,m)
            down = grid[i][j] + maximum_path(grid,i+1,j,m)
            dp[i][j] = max(down,left_d,right_d)
            return dp[i][j]
        
        m = len(matrix)
        max_sum = float("-inf")
        dp = [[-1] * m for _ in range(m)]
        for j in range(m):
            max_sum = max(max_sum,maximum_path(matrix,0,j,m))
        return max_sum
    
    # Time Complexity: O(m*m)
    # Space Complexity: O(m*m)

    def maxFallingPathSumBottomUp(self, matrix: List[List[int]]) -> int:
        def maximum_path(grid):
            m = len(grid)
            dp = [[-1]*m for _ in range(m)]
            for j in range(m):
                dp[0][j] = grid[0][j]
            for i in range(1,m):
                for j in range(m):
                    up = grid[i][j] + dp[i-1][j]

                    # Handle left diagonal
                    left_d = grid[i][j]
                    if j-1 >= 0:
                        left_d += dp[i-1][j-1]
                    else:
                        left_d = float("-inf")
                    
                    # Handle right diagonal
                    right_diagonal = grid[i][j]
                    if j + 1 < m:
                        right_diagonal += dp[i - 1][j + 1]
                    else:
                        right_diagonal = float("-inf")
                    dp[i][j] = max(up,left_d,right_diagonal)
            return dp
        
        m = len(matrix)
        dp = maximum_path(matrix)
        return max(dp[m-1])
    
    # Time Complexity: O(m*m)
    # Space Complexity: O(m*m)

    def maxFallingPathSumSpaceOptimized(self, matrix: List[List[int]]) -> int:
        def maximum_path(grid):
            m = len(grid)
            dp = [0]*m
            for j in range(m):
                dp[j] = grid[0][j]
            for i in range(1,m):
                temp = [0]*m
                for j in range(m):
                    up = grid[i][j] + dp[j]
                    left_d = grid[i][j]
                    if j-1 >= 0:
                        left_d += dp[j-1]
                    else:
                        left_d = float("-inf")
                    right_diagonal = grid[i][j]
                    if j + 1 < m:
                        right_diagonal += dp[j + 1]
                    else:
                        right_diagonal = float("-inf")
                    temp[j] = max(up,left_d,right_diagonal)
                dp = temp
            return dp
        
        m = len(matrix)
        dp = maximum_path(matrix)
        return max(dp)
    
    # Time Complexity: O(m*m)
    # Space Complexity: O(m)

# Example usage
sol = Solution()
matrix = [[1,2,10,4],[100,3,2,1],[1,1,20,2],[1,2,2,1]]
print(sol.maxFallingPathSum(matrix))
print(sol.maxFallingPathSumMemo(matrix))
print(sol.maxFallingPathSumBottomUp(matrix))
print(sol.maxFallingPathSumSpaceOptimized(matrix))