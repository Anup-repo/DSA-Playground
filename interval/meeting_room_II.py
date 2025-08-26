from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        event = []
        for start, end in intervals:
            event.append((start, 1))  # start of meeting: +1 meeting ongoing
            event.append((end, -1)) # end is non-inclusive so end+1 not needed

        event.sort(key=lambda x: (x[0], x[1]))

        ongoing = 0
        max_meeting = 0
        for _, change in event:
            ongoing += change
            max_meeting = max(max_meeting, ongoing)

        return max_meeting


intervals = [(0, 40), (5, 10), (15, 20)]
sol = Solution()
print(sol.canAttendMeetings(intervals))
