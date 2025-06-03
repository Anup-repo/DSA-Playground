import heapq
class Solution:
    def printShortestPath(self, adj, src, dest):
        pq = []
        parent = [i for i in range(len(adj))]
        dist = [float("inf")] * len(adj)
        dist[src] = 0

        heapq.heappush(pq, (0, src))
        while pq:
            c_dist, node = heapq.heappop(pq)
            for adj_node, adj_dist in adj[node]:
                if c_dist + adj_dist < dist[adj_node]:
                    dist[adj_node] = c_dist + adj_dist
                    parent[adj_node] = node
                    heapq.heappush(pq, (dist[adj_node], adj_node))

        if dist[dest] == float("inf"):
            return -1
        path = []
        node = dest

        while parent[node] != node:
            path.append(node)
            node = parent[node]
        path.append(src)
        path.reverse()
        return path


edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]
n = 6  # max node id is 5, so total 6 nodes
adj = [[] for _ in range(n)]
for u, v, w in edges:
    adj[u].append((v, w))
    adj[v].append((u, w))
sol = Solution()
print(sol.shortest_path(1, 5, adj))
