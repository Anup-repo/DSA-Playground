from typing import List
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        for start, end in intervals:
            events.append((start, 1))  # start of interval: +1 group needed
            events.append((end + 1, -1))  # end of interval: -1 group released (inclusive)

        events.sort(key=lambda x: (x[0], x[1]))

        max_group = 0
        group = 0
        for _, change in events:
            group += change
            max_group = max(max_group, group)

        return max_group

# Example
solution = Solution()
intervals = [[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]
print(solution.minGroups(intervals))
