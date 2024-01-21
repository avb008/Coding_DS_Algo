from typing import List
from collections import deque


class Solution:
    def BFS(
        self, vertex: int, parent: int, visited: List[bool], adj: List[List[int]]
    ) -> bool:
        """Breadth First Search to detect cycle in an undirected graph

            - Time Complexity: O(V + E)
            - Space Complexity: O(V)

            - Start from a vertex and visit all its neighbours
            - Add all the neighbours to a queue
            - Pop the first element from the queue and repeat the above steps
            - If a vertex is already visited and is not the parent of the current vertex, then there is a cycle

        Args:
            vertex (int): _description_
            parent (int): _description_
            visited (List[bool]): _description_
            adj (List[List[int]]): _description_

        Returns:
            bool: _description_
        """

        visited[vertex] = True
        queue = deque([(vertex, parent)])

        while queue:
            node, parent = queue.popleft()

            for neighbour in adj[node]:
                if visited[neighbour] is False:
                    queue.append((neighbour, node))
                    visited[neighbour] = True
                else:
                    if neighbour != parent:
                        return True

        return False

    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        """Function to detect cycle in an undirected graph

            - Time Complexity: O(V + E)
            - Space Complexity: O(V)

        Args:
            V (int): Number of vertices
            adj (List[List[int]]): Adjacency list

        Returns:
            bool: True if cycle is present, else False
        """
        visited = [False] * V
        parent = -1
        for vertex in range(V):
            if visited[vertex] is False:
                if self.BFS(vertex, parent, visited, adj):
                    return True

        return False


if __name__ == "__main__":
    V = 5
    adj = [[1, 2], [0, 2], [0, 1, 3, 4], [2, 4], [3, 2]]
    obj = Solution()
    print(obj.isCycle(V, adj))
