from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def minimum_path(i,j,m,triangle):
            if i == m-1:
                return triangle[i][j]
            down = triangle[i][j] + minimum_path(i+1,j,m,triangle)
            down_right = triangle[i][j] + minimum_path(i+1,j+1,m,triangle)
            return min(down,down_right)
        
        m = len(triangle)
        return minimum_path(0,0,m,triangle)
    
    def minimumTotal_memo(self, triangle: List[List[int]]) -> int:
        def minimum_path(i,j,m,triangle):
            if i == m-1:
                return triangle[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            down = triangle[i][j] + minimum_path(i+1,j,m,triangle)
            down_right = triangle[i][j] + minimum_path(i+1,j+1,m,triangle)
            dp[i][j] = min(down,down_right)
            return dp[i][j]
        
        m = len(triangle)
        
        dp = [[-1] * m for _ in range(m)]
        return minimum_path(0,0,m,triangle)
    
    def minimumTotal_bottom_up(self, triangle: List[List[int]]) -> int:
        def minimum_path(triangle):
            m = len(triangle)
            
            dp = [[0] * m for _ in range(m)]
            for j in range(m):
                dp[m-1][j] = triangle[m-1][j]
            for i in range(m-2,-1,-1):
                for j in range(i,-1,-1):
                    down = triangle[i][j] + dp[i+1][j]
                    down_right = triangle[i][j] + dp[i+1][j+1]
                    dp[i][j] = min(down,down_right)
            return dp[0][0]
        
        return minimum_path(triangle)
    
# Example
sol = Solution()
print(sol.minimumTotal(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]))
print(sol.minimumTotal_memo(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]))
print(sol.minimumTotal_bottom_up(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]))