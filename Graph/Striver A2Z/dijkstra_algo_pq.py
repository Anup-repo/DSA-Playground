import heapq

class Solution:

    def constructAdjacencyList(self, edges):
        graph = [[] for _ in range(len(edges))]
        for edge in edges:
            u, v, weight = edge
            graph[u].append((v, weight))
            graph[v].append((u, weight))
        return graph
    
    def dijkstra(self, graph, start):
        distances = [float('inf')] * len(graph)
        distances[start] = 0
        pq = [(0, start)]
        while pq:
            current_distance, current_node = heapq.heappop(pq)

            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        return distances
    
# Example usage:
sol = Solution()
edges = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]] 
graph = sol.constructAdjacencyList(edges)
print(graph)
print(sol.dijkstra(graph, 0))