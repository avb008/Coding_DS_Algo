from typing import List
from collections import deque


class Solution:
    def dfs(
        self, vertex: int, visited: List[bool], stack: List[int], adj: List[List[int]]
    ) -> None:
        """Depth first search

            - Time complexity: O(V+E)
            - Space complexity: O(V)

        Args:
            vertex (int): Input vertex
            visited (List[bool]): Visited array
            stack (List[int]): Stack to store the answer
            adj (List[List[int]]): Adjacency list of the graph

        Returns:
            None: No return
        """
        visited[vertex] = True

        for node in adj[vertex]:
            if not visited[node]:
                self.dfs(node, visited, stack, adj)

        stack.append(vertex)

    def topologicalSortDFS(self, n_vertices: int, adj: List[List[int]]) -> List[int]:
        """Topological sort using DFS

            - Time complexity: O(V+E)
            - Space complexity: O(V)

        Args:
            n_vertices (int): Number of vertices in the graph
            adj (List[List[int]]): Adjacency list of the graph

        Returns:
            List[int]: Topological sort of the graph
        """
        visited = [False] * n_vertices
        stack = []

        for vertex in range(n_vertices):
            if not visited[vertex]:
                self.dfs(vertex, visited, stack, adj)

        # Alternatively, we can use the below code to get the answer
        # answers = []
        # while stack:
        #     answers.append(stack.pop())

        return stack[::-1]

    def topoSortBFS(self, n_vertices: int, adj: List[List[int]]) -> List[int]:
        """Topological sort using BFS

            - Time complexity: O(V+E)
            - Space complexity: O(V)

        Args:
            n_vertices (int): Input number of vertices
            adj (List[List[int]]): Adjacency list of the graph

        Returns:
            List[int]: Topological sort of the graph
        """
        in_degree = [0] * n_vertices  # In degree of each node , initially 0

        # Calculate number of incoming edges for each node
        for nodes in adj:
            for neighbour in nodes:
                in_degree[neighbour] += 1

        # Add all nodes with 0 incoming edges to the queue
        queue = deque()
        for node in range(n_vertices):
            if in_degree[node] == 0:
                queue.append(node)

        topo_sort = []
        while queue:
            node = queue.popleft()
            topo_sort.append(node)

            for neighbour in adj[node]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)

        return topo_sort


if __name__ == "__main__":
    obj = Solution()
    n_vertices = 6
    adj = [[1, 2], [3, 4], [5], [5], [], [], []]
    print(obj.topologicalSortDFS(n_vertices, adj))
    print(obj.topoSortBFS(n_vertices, adj))
