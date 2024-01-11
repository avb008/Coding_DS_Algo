from collections import deque
from typing import List


class Solution:
    def BFS(
        self, index: tuple, grid: List[List[str]], visited: List[List[bool]]
    ) -> None:
        """Breadth first search.

        Args:
            index (tuple): Index of the current element.
            grid (List[List[str]]): Grid of elements.
            visited (List[List[bool]]): Visited array.
        """
        x, y = index
        m, n = len(grid), len(grid[0])

        x_dir = [-1, 0, 1, 0]
        y_dir = [0, 1, 0, -1]

        visited[x][y] = True
        queue = deque([index])
        while queue:
            x, y = queue.popleft()

            for i in range(4):
                x_p = x + x_dir[i]
                y_p = y + y_dir[i]
                if (
                    0 <= x_p < m
                    and 0 <= y_p < n
                    and grid[x_p][y_p] == "1"
                    and visited[x_p][y_p] == False
                ):
                    queue.append((x_p, y_p))
                    visited[x_p][y_p] = True

        return

    def numIslands(self, grid: List[List[str]]) -> int:
        """Calculates the number of islands.

        Args:
            grid (List[List[str]]): Grid of elements.

        Returns:
            int: Number of islands.
        """
        islands = 0
        m, n = len(grid), len(grid[0])
        visited = [[False for i in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and visited[i][j] == False:
                    self.BFS((i, j), grid, visited)
                    islands += 1

        return islands
