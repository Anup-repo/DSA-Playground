from typing import List
class Solution:
    def shortestDistance(self, matrix: List[List[int]], n: int, M: int) -> List[List[int]]:
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

        for i in range(n):
            if matrix[i][i] < 0:
                return [-1]
            
        return matrix
    
# Time Complexity: O(N^3)
# Space Complexity: O(N^2)

# Example 1:
matrix = [[0,1,43], [1, 0, 6], [-1, -1, 0]]
N = 3
M = 3

print(Solution().shortestDistance(matrix, N, M))