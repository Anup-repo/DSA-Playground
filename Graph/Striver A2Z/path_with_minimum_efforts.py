from typing import List
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        The question is stating to find the minimum of the maximum efforts, so efforts should be maximum and sitance should have minimum values of those maximized efforts.
        """
        pq = []
        n = len(heights)
        m = len(heights[0])
        distance = [[float("inf")] * m for _ in range(n)]
        distance[0][0] = 0
        heapq.heappush(pq,(0,0,0))
        delrow = [-1,0,1,0]
        delcol = [0,1,0,-1]

        while pq:
            diff,row,col = heapq.heappop(pq)

            if row == n-1 and col == m-1:
                return diff

            for i in range(4):
                nrow = row + delrow[i]
                ncol = col + delcol[i]

                if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m:
                    new_effort = max(abs(heights[row][col] - heights[nrow][ncol]), diff)
                    if new_effort < distance[nrow][ncol]:
                        distance[nrow][ncol] = new_effort
                        heapq.heappush(pq,(new_effort,nrow,ncol))

# Example
heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
sol = Solution()
print(sol.minimumEffortPath(heights))
