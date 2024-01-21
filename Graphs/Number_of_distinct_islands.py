from collections import deque
from typing import List


class Solution:
    def BFS(
        self, index: tuple, grid: List[List[str]], visited: List[List[bool]]
    ) -> None:
        """Function to perform BFS on a grid

        Args:
            index (tuple): Index of the node
            grid (List[List[str]]): Input grid
            visited (List[List[bool]]): Visited array

        Returns:
            None: None
        """
        m = len(grid)
        n = len(grid[0])

        x_neighbours = [-1, 0, 1, 0]  # clock-wise
        y_neighours = [0, 1, 0, -1]

        visited[index[0]][index[1]] = True

        queue = deque([index])
        while queue:
            node = queue.popleft()

            for i in range(4):
                x = node[0] + x_neighbours[i]
                y = node[1] + y_neighours[i]
                if (
                    0 <= x < m
                    and 0 <= y < n
                    and grid[x][y] == "1"
                    and visited[x][y] == False
                ):
                    queue.append((x, y))
                    visited[x][y] = True

    def numIslands(self, grid: List[List[str]]) -> int:
        """Function to find number of distinct islands in a grid

            - Time Complexity: O(m*n)
            - Space Complexity: O(m*n)

        Args:
            grid (List[List[str]]): Input grid

        Returns:
            int: Number of distinct islands
        """
        m = len(grid)
        n = len(grid[0])
        visited = [[False for i in range(n)] for j in range(m)]

        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and visited[i][j] == False:
                    islands += 1
                    self.BFS((i, j), grid, visited)

        return islands
