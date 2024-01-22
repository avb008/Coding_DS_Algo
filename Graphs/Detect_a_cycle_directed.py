from collections import deque
from typing import List


class Solution:
    # Function to detect cycle in a directed graph.
    def isCyclic(self, n_vertices: int, adj: List[List[int]]) -> bool:
        """Detect cycle in a directed graph using BFS

            - Time complexity: O(V+E)
            - Space complexity: O(V)

            - Algorithm:
                - This is a slight modification of the topological sort using BFS algorithm
                - We will use the same algorithm as topological sort using BFS but instead of returning the answer,
                we will check if the count of nodes visited is equal to the number of vertices in the graph or not.
                - If the count is equal to the number of vertices in the graph, then there is no cycle in the graph.
                - If the count is not equal to the number of vertices in the graph, then there is a cycle in the graph.

        Args:
            n_vertices (int): Number of vertices in the graph
            adj (List[List[int]]): Adjacency list of the graph

        Returns:
            bool: True if cycle is present, else False
        """
        in_degree = [0] * n_vertices

        # Calculate in-degree of each node
        for nodes in adj:
            for neighbours in nodes:
                in_degree[neighbours] += 1

        # Add all nodes with 0 incoming edges to the queue
        queue = deque()
        for node in range(n_vertices):
            if in_degree[node] == 0:
                queue.append(node)

        count = 0
        while queue:
            node = queue.popleft()
            count += 1

            for neighbour in adj[node]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)

        if count == n_vertices:
            return False

        return True


if __name__ == "__main__":
    n_vertices = 6
    adj = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 3]]  # Cycle present
    obj = Solution()
    print(obj.isCyclic(n_vertices, adj))

    n_vertices = 6
    adj = [[1, 2], [3, 4], [5], [5], [], []]  # Cycle not present
    print(obj.isCyclic(n_vertices, adj))
