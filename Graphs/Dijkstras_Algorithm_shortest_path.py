# Dijkstra's Algorithm shortest path
# Dijkstra's Algorithm is used to find the shortest path from a source vertex to all other vertices in a weighted graph.
# Dijkstra's Algorithm doesn't work for graphs with negative weight edges.

from typing import List, Tuple
from collections import defaultdict
import heapq


class Solution:
    def dijkstra(
        self, n_vertices: int, n_edges: int, edges: List[List[int]], source: int
    ) -> tuple[List[int], List[int]]:
        """Dijkstra's Algorithm is used to find the shortest path from a source vertex to all other vertices in a
        weighted graph.

            - Time Complexity: O(ElogV)
            - Space Complexity: O(V)

        Args:
            n_vertices (int):  Number of vertices in the graph
            n_edges (int): Number of edges in the graph
            edges (List[List[int]]): Edges of the graph
            source (int): Source vertex

        Returns:
            tuple(List[int], List[int]): Returns a tuple of shortest distance array and shortest path array
        """

        # Use defaultdict to avoid key error
        adj = defaultdict(list)  # adjacency list of the graph
        for edge in edges:
            u, v, dist = edge
            adj[u].append((v, dist))
            adj[v].append((u, dist))

        # Initialize the parent array and shortest distance array
        parent = [i for i in range(n_vertices + 1)]
        shortest_distance = [float("inf") for i in range(n_vertices + 1)]

        heap = []  # min-heap
        heapq.heappush(heap, (0, source))
        shortest_distance[source] = 0

        while heap:
            distance, node = heapq.heappop(heap)

            for edge in adj[node]:
                neighbour_node, new_dist = edge
                if distance + new_dist < shortest_distance[neighbour_node]:
                    shortest_distance[neighbour_node] = distance + new_dist
                    heapq.heappush(heap, (distance + new_dist, neighbour_node))
                    parent[neighbour_node] = node

        shortest_path = []
        current_node = n_vertices  # destination node
        while parent[current_node] != current_node:
            shortest_path.append(current_node)
            current_node = parent[current_node]
        shortest_path.append(source)

        return shortest_distance[1:], shortest_path[::-1]


if __name__ == "__main__":
    s = Solution()
    n, m = 5, 6
    edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]
    print(s.dijkstra(n, m, edges, 1))
