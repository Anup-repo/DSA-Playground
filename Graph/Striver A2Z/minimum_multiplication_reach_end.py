from typing import List
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        distance = [float('inf')] * 100000
        queue = [(0,start)] 
        distance[start] = 0
        mod = 10**5
        while queue:
            setp, current_node = queue.pop(0) 
            for neighbor in arr:
                num = (current_node * neighbor) % mod
                if setp + 1 < distance[num]:
                    distance[num] = setp + 1
                    if num == end:
                        return distance[num]
                    queue.append((setp + 1, num))
        return -1
    
# Example usage:
arr = [3,4,65]
start = 7
end = 66175
solution = Solution()
print(solution.minimumMultiplications(arr, start, end))