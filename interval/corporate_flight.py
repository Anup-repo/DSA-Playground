from typing import List
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        events = [0] * (n + 2)
        for  first, last, seat in bookings:
            events[first] += seat
            events[last + 1] -= seat

        for i in range(1, n + 1):
            events[i] += events[i - 1]

        return events[1:n + 1]
    
sol = Solution()
bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5
print(sol.corpFlightBookings(bookings, n))
