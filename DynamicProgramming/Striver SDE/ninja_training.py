from typing import *

"""
The difference is ninja has to do a activity on each day unlike maximum alternative subsequence where you can skip a day
"""
def ninja_training(n: int, points: List[List[int]], last_task: int, day: int) -> int:
    """
    Time complexity: O(3^n) where n is the number of days
    Space complexity: O(n) for the recursive stack
    """
    if day == n:
        return 0

    max_points = 0
    for task in range(3):
        if task != last_task:
            current_points = points[day][task] + ninja_training(n, points, task, day + 1)
            max_points = max(max_points, current_points)
    
    return max_points

def ninja_training_memo(n: int, points: List[List[int]], last_task: int, day: int, dp: List[List[int]]) -> int:
    """
    Time complexity: O(3^n) where n is the number of days
    Space complexity: O(n) for the recursive stack and O(n) for the memoization dp array
    """
    if day == n:
        return 0

    if dp[day][last_task] != -1:
        return dp[day][last_task]

    max_points = 0
    for task in range(3):
        if task != last_task:
            current_points = points[day][task] + ninja_training_memo(n, points, task, day + 1, dp)
            max_points = max(max_points, current_points)
    
    dp[day][last_task] = max_points
    return max_points

def ninja_training_tabulation(n: int, points: List[List[int]], last_task: int, day: int) -> int:
    """
    Time complexity:  O(N*4*3) where n is the number of days
    Space complexity: O(n) for the dp array
    """
    dp = [[0] * 4 for _ in range(n)]
    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0][0], points[0][1], points[0][2])

    for day in range(1, n):
        for last_task in range(4):
            max_points = 0
            for task in range(3):
                if task != last_task:
                    current_points = points[day][task] + dp[day - 1][task]
                    max_points = max(max_points, current_points)
            dp[day][last_task] = max_points

    return dp[n - 1][3]

def ninja_training_space_optimization(n: int, points: List[List[int]], last_task: int, day: int) -> int:
    """
    Time complexity: O(n) where n is the number of days
    Space complexity: O(1) since we are using only a fixed amount of extra space
    """
    prev = [0] * 4

    prev[0] = max(points[0][1], points[0][2])
    prev[1] = max(points[0][0], points[0][2])
    prev[2] = max(points[0][0], points[0][1])
    prev[3] = max(points[0][0], max(points[0][1], points[0][2]))

    for day in range(1, n):
        temp = [0] * 4

        for last in range(4):
            temp[last] = 0

            for task in range(3):
                if task != last:
                    activity = points[day][task] + prev[task]
                    temp[last] = max(temp[last], activity)

        prev = temp

    return prev[3]

points = [[1, 2, 5], [3, 1, 1], [3, 3, 3]]
task = 3 # try (0,1,2,3) 
n = 3
print(ninja_training(n, points, task, 0))

dp = [[-1] * 4 for _ in range(n)]
print(ninja_training_memo(n, points, task, 0, dp))

print(ninja_training_tabulation(n, points, task, 0))
print(ninja_training_space_optimization(n, points, task, 0))
