class Solution:
    def bellman_ford(self, n, edges, src):
        dist = [float("inf")] * n
        dist[src] = 0
        for _ in range(n - 1):
            for u, v, w in edges:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                return [-1]
        return dist
    
# Time complexity: O(VE)
# Space complexity: O(V)

# Example 1:
V = 5
edges = [[0, 1, 5], [1, 2, 1], [1, 3, 2], [2, 4, 1], [4, 3, -1]]
src = 0

V = 4
edges = [[0, 1, 4], [1, 2, -6], [2, 3, 5], [3, 1, -2]]
src = 0

print(Solution().bellman_ford(V, edges, src))