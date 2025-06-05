from typing import List
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for s,d,c in flights:
            adj[s].append((d,c))

        queue = [(0,src,0)] # (stop,city,price)
        distances = [float('inf')]*n
        while queue:
            stop,node,cost = queue.pop(0)

            if stop > k:
                continue

            for adjNode,adjCost in adj[node]:
                if cost + adjCost < distances[adjNode] and stop <= k:
                    distances[adjNode] = cost + adjCost
                    queue.append((stop+1,adjNode,cost+adjCost))

        return distances[dst] if distances[dst] != float('inf') else -1

    def findCheapestPriceWithPath(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for s,d,c in flights:
            adj[s].append((d,c))

        queue = [(0,src,0)] # (stop,city,price)
        distances = [float('inf')]*n
        parent = [i for i in range(n)]
        while queue:
            stop,node,cost = queue.pop(0)

            if stop > k:
                continue

            for adjNode,adjCost in adj[node]:
                if cost + adjCost < distances[adjNode] and stop <= k:
                    distances[adjNode] = cost + adjCost
                    parent[adjNode] = node
                    queue.append((stop+1,adjNode,cost+adjCost))

        shortest_path = []
        current_node = dst

        while parent[current_node] != current_node:
            shortest_path.append(current_node)
            current_node = parent[current_node]
        shortest_path.append(src)
        shortest_path.reverse()
        print(shortest_path)
        
        return distances[dst] if distances[dst] != float('inf') else -1


def main():
    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    k = 1
    sol = Solution()
    print(sol.findCheapestPrice(n,flights,src,dst,k))
    print(sol.findCheapestPriceWithPath(n,flights,src,dst,k))

if __name__ == '__main__':
    main()
