# Leetcode 56

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        else:
            intervals = sorted(intervals)
            final = []
            start = intervals[0][0]
            end = intervals[0][1]
            for i in intervals:
                if i[0] <= end:
                    end = max(end, i[1])
                else:
                    l = [start, end]
                    final.append(l)
                    start = i[0]
                    end = i[1]
        l = [start, end]
        final.append(l)
        return final
    
sol = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(sol.merge(intervals))
