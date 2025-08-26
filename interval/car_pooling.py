"""
👇 Steps:
Add (start, +num_passengers) to lst

Add (end, -num_passengers) to lst

Sort lst by location

Traverse and maintain running total pas (current passengers)

If at any point pas > capacity, return False
"""

from typing import List
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        lst = []
        for n, start, end in trips:
            lst.append((start, n))  # Pickup: add passengers
            lst.append((end, -n))  # Dropoff: remove passengers
        lst.sort()  # Sort by location (time/distance)

        pas = 0
        for _,cur_pas in lst:
            pas += cur_pas  # Add or subtract passengers
            if pas > capacity:
                return False
        return True

# Example usage
sol = Solution()
trips = [
    [2, 1, 5],  # 2 passengers from 1 to 5
    [3, 3, 7],  # 3 passengers from 3 to 7
]
capacity = 4
print(sol.carPooling(trips, capacity))
