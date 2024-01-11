from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """Calculates the time taken for all oranges to rot.

            - Time Complexity: O(m*n)
            - Space Complexity: O(m*n)

        Args:
            grid (List[List[int]]): 2D grid of oranges.

        Returns:
            int: Time taken for all oranges to rot.
        """
        queue = deque()
        fresh = 0
        m, n = len(grid), len(grid[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j, 0))
                    visited.add((i, j))

        x_d = [-1, 0, 1, 0]
        y_d = [0, 1, 0, -1]

        t = 0
        while queue:
            x, y, t = queue.popleft()

            for _ in range(4):
                i = x + x_d[_]
                j = y + y_d[_]

                if (
                    0 <= i < m
                    and 0 <= j < n
                    and (i, j) not in visited
                    and grid[i][j] == 1
                ):
                    queue.append((i, j, t + 1))
                    visited.add((i, j))
                    fresh -= 1

        return t if fresh == 0 else -1
