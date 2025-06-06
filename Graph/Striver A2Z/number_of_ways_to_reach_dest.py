from typing import List
import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for s, d, w in roads:
            adj[s].append((d,w))
            adj[d].append((s,w))

        distance = [float("inf")] * n
        ways = [0] * n
        pq = []

        distance[0] = 0
        ways[0] = 1
        heapq.heappush(pq,(0,0))
        mod = 10**9 + 7

        while pq:
            cur_dist, node = heapq.heappop(pq)
            for neighbor, weight in adj[node]:
                new_ditance = cur_dist + weight
                if new_ditance < distance[neighbor]:
                    distance[neighbor] = new_ditance
                    ways[neighbor] = ways[node]
                    heapq.heappush(pq,(new_ditance,neighbor))
                elif new_ditance == distance[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % mod
        
        return ways[n-1] % mod

# Example usage:
n = 7
roads = [
    [0, 6, 7],
    [0, 1, 2],
    [1, 2, 3],
    [1, 3, 3],
    [6, 3, 3],
    [3, 5, 1],
    [6, 5, 1],
    [2, 5, 1],
    [0, 4, 5],
    [4, 6, 2],
]
solution = Solution()
print(solution.countPaths(n, roads))
