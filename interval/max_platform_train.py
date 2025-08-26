class Solution:
    def maxNumberOfTrains(self, arrival, departure) -> int:
        trains = []
        for i in range(len(arrival)):
            trains.append((arrival[i], 1))  # train arrives → need platform
            trains.append((departure[i] + 1, -1))  # train departs → release platform (end is inclusive, so +1)

        trains.sort(key=lambda x: (x[0], x[1]))
        platforms = 0
        max_platforms = 0

        for time, change in trains:
            platforms += change
            max_platforms = max(max_platforms, platforms)

        return max_platforms

# Example usage:
solution = Solution()
print(solution.maxNumberOfTrains([1, 2, 3], [2, 3, 4]))  # Output: 3
print(solution.maxNumberOfTrains([1, 2, 3], [3, 4, 5]))  # Output: 2
