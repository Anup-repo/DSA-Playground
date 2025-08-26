from typing import List
import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        used = [] # min heap(end,room)
        available = [i for i in range(n)] # 0,1,2,3
        count = [0] * n

        for start, end in meetings:
            # can start new meeting
            while used and start >= used[0][0]:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)

            # not available
            if not available:
                cur_end, room = heapq.heappop(used)
                end = cur_end + (end-start)
                heapq.heappush(available, room)

            # we can create meeting
            room = heapq.heappop(available)
            heapq.heappush(used, (end, room))
            count[room] += 1
        
        return count.index(max(count))

n = 2
meetings = [[0,10],[1,5],[2,7],[3,4]]
sol = Solution()
print(sol.mostBooked(n, meetings))
