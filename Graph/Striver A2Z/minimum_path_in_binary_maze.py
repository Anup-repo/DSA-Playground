class Solution:
    def minimum_path_in_grid(self, grid, source, destination):
        queue = [(0,source[0],source[1])]
        dist = [[float("inf")] * len(grid[0]) for _ in range(len(grid))]
        dist[source[0]][source[1]] = 0
        delrow = [-1,0,1,0]
        delcol = [0,1,0,-1]
        while queue:
            distance, row,col = queue.pop(0)
            for i in range(4):
                newrow = row + delrow[i]
                newcol = col + delcol[i]
                if newrow >= 0 and newrow < len(grid) and newcol >= 0 and newcol < len(grid[0]) and grid[newrow][newcol] == 1 and distance + 1 < dist[newrow][newcol]:
                        dist[newrow][newcol] = distance + 1
                        if newrow == destination[0] and newcol == destination[1]:
                            return dist[newrow][newcol]
                        queue.append((dist[newrow][newcol], newrow, newcol))

        return -1
    
# Example usage:
grid = [[1,1,1,1],[1,1,0,1],[1,1,1,1],[1,1,0,0],[1,0,0,1]]
source = [0,1]
destination = [2,2]
solution = Solution()
print(solution.minimum_path_in_grid(grid, source, destination))

        