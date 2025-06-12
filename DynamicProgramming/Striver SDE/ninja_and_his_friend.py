from os import *
from sys import *
from collections import *
from math import *

from typing import List


def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
    # write your code here
    def max_chocolate(i,j1,j2,r,c,grid):
        if j1 < 0 or j1 >= c or j2 < 0 or j2 >= c:
            return float("-inf")
        if i == r-1:
            if j1 == j2:
                return grid[i][j1]
            else:
                return grid[i][j1] + grid[i][j2]

        maxi = float("-inf")   
        for di in range(-1,2):
            for dj in range(-1,2):
                if j1 == j2:
                    ans = grid[i][j1] + max_chocolate(i+1,j1+di,j2+dj,r,c,grid)
                else:
                    ans = grid[i][j1] + grid[i][j2] + max_chocolate(i+1,j1+di,j2+dj,r,c,grid)
                maxi = max(maxi,ans)
        return maxi
    
    return max_chocolate(0,0,c-1,r,c,grid)

def maximumChocolatesMemoized(r: int, c: int, grid: List[List[int]]) -> int:
    # write your code here
    def max_chocolate(i,j1,j2,r,c,grid,dp):
        if j1 < 0 or j1 >= c or j2 < 0 or j2 >= c:
            return float("-inf")
        if i == r-1:
            if j1 == j2:
                return grid[i][j1]
            else:
                return grid[i][j1] + grid[i][j2]

        if dp[i][j1][j2] != -1:
            return dp[i][j1][j2]

        maxi = float("-inf")   
        for di in range(-1,2):
            for dj in range(-1,2):
                if j1 == j2:
                    ans = grid[i][j1] + max_chocolate(i+1,j1+di,j2+dj,r,c,grid,dp)
                else:
                    ans = grid[i][j1] + grid[i][j2] + max_chocolate(i+1,j1+di,j2+dj,r,c,grid,dp)
                maxi = max(maxi,ans)

        dp[i][j1][j2] = maxi
        return maxi
    
    dp = [[[-1] * c for _ in range(c)] for _ in range(r)]
    return max_chocolate(0,0,c-1,r,c,grid,dp)

def maximumChocolatesTabulation(r: int, c: int, grid: List[List[int]]) -> int:
    # write your code here
    dp = [[[0] * c for _ in range(c)] for _ in range(r)]
    for j1 in range(c):
        for j2 in range(c):
            if j1 == j2:
                dp[r-1][j1][j2] = grid[r-1][j1]
            else:
                dp[r-1][j1][j2] = grid[r-1][j1] + grid[r-1][j2]

    for i in range(r-2,-1,-1):
        for j1 in range(c):
            for j2 in range(c):
                maxi = float("-inf")
                for di in range(-1,2):
                    for dj in range(-1,2):
                        ans = 0
                        if j1 == j2:
                            ans = grid[i][j1]
                        else:
                            ans = grid[i][j1] + grid[i][j2]
                        
                        if j1+di < 0 or j1+di >= c or j2+dj < 0 or j2+dj >= c:
                            ans = float("-inf")
                        else:
                            ans += dp[i+1][j1+di][j2+dj]

                        maxi = max(maxi,ans)
                dp[i][j1][j2] = maxi
    return dp[0][0][c-1]

# Example usecase:
grid = [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]
r = len(grid)
c = len(grid[0])

print(maximumChocolates(r, c, grid))
print(maximumChocolatesMemoized(r, c, grid))
print(maximumChocolatesTabulation(r, c, grid))
