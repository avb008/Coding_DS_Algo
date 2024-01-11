from collections import defaultdict, deque
from typing import Optional, List


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, vertex: int, visited: List[int]) -> None:
        """Breadth First Search
            - Time Complexity: O(V + E)
            - Space Complexity: O(V)

            - Start from a vertex and visit all its neighbours
            - Then visit the neighbours of the neighbours and so on
            - Repeat until all vertices are visited
            Note : This is a iterative implementation of BFS & it doesnt work for disconnected graphs

        Args:
            vertex (int): Starting vertex from where to start BFS
            visited (List[int]): List of visited vertices
        """

        traversal = []

        # Create a queue for BFS
        queue = deque()
        queue.append(vertex)
        visited[vertex] = True

        while len(queue) > 0:
            current_node = queue.popleft()
            traversal.append(current_node)

            for neighbour in self.graph[current_node]:
                if visited[neighbour] == False:
                    queue.append(neighbour)
                    visited[neighbour] = True

        return traversal

    def DFS(self, vertex: int, visited: List[int], result: List[int]) -> None:
        """Depth First Search
            - Time Complexity: O(V + E)
            - Space Complexity: O(V)

            - Start from a vertex and go as deep as possible
            - When no more vertices are left to visit, backtrack to the previous vertex and visit its neighbours
            - Repeat until all vertices are visited
            Note : This is a recursive implementation of DFS & it doesnt work for disconnected graphs

        Args:
            vertex (Optional[int]): Starting vertex from where to start DFS
            visited (List[bool]): List to keep track of visited nodes
            result (List[int]): List to store the result

        Returns:
            List[int]: List of nodes in DFS order
        """

        visited[vertex] = True
        result.append(vertex)

        for neighbour in self.graph[vertex]:
            if visited[neighbour] == False:
                self.DFS(neighbour, visited, result)

        return result

    def traverse(self) -> List[int]:
        """
        Traverses the graph using both BFS and DFS.

        Parameters:
        None

        Returns:
        List[int]: The BFS and DFS traversal of the graph.

        Example:
        >>> g = Traversal([[1, 2], [0, 2], [0, 1], [3], [4], [6], [5]])
        >>> g.traverse()
        ([0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 6, 5])
        """

        bfs_traversal = []

        visited = [False] * (len(self.graph) + 1)
        for vertex in range(len(self.graph)):
            if not visited[vertex]:
                bfs_traversal.extend(self.BFS(vertex, visited))

        print("BFS traversal : ", bfs_traversal)

        dfs_traversal = []
        visited = [False] * (len(self.graph) + 1)
        for vertex in range(len(self.graph)):
            if not visited[vertex]:
                self.DFS(vertex, visited, dfs_traversal)

        print("DFS traversal : ", dfs_traversal)


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(5, 6)
    g.add_edge(6, 0)
    g.add_edge(6, 4)
    g.add_edge(6, 5)

    print(g.graph)
    print("BFS and DFS traversal ")
    g.traverse()
