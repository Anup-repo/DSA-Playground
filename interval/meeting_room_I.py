from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        event = []
        for start, end in intervals:
            event.append((start, 1))  # start of meeting: +1 meeting ongoing
            event.append((end+1, -1))

        event.sort(key = lambda x:(x[0], x[1]))

        ongoing = 0
        for _, change in event:
            ongoing += change
            if ongoing > 1:
                return False  # overlap detected

        return True

intervals = [(0, 30), (5, 10), (15, 20)]
sol = Solution()
print(sol.canAttendMeetings(intervals))
