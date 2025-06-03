import heapq
class Solution:
    def printShortestPath(self, adjacency_list, source, destination):
        priority_queue = []
        parent_nodes = [i for i in range(len(adjacency_list))]
        distances = [float("inf")] * len(adjacency_list)
        distances[source] = 0

        heapq.heappush(priority_queue, (0, source))
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            for neighbor, edge_weight in adjacency_list[current_node]:
                if current_distance + edge_weight < distances[neighbor]:
                    distances[neighbor] = current_distance + edge_weight
                    parent_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distances[neighbor], neighbor))

        if distances[destination] == float("inf"):
            return -1
        shortest_path = []
        current_node = destination

        while parent_nodes[current_node] != current_node:
            shortest_path.append(current_node)
            current_node = parent_nodes[current_node]
        shortest_path.append(source)
        shortest_path.reverse()
        return shortest_path


edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]
num_nodes = 6  # max node id is 5, so total 6 nodes
adjacency_list = [[] for _ in range(num_nodes)]
for source, destination, weight in edges:
    adjacency_list[source].append((destination, weight))
    adjacency_list[destination].append((source, weight))
solution = Solution()
print(solution.shortest_path(1, 5, adjacency_list))
