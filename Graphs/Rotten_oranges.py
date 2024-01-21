# Problem: https://leetcode.com/problems/rotting-oranges/
from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """Finds the minimum time required to rot all the oranges in the grid

            - Time Complexity: O(rows * cols)
            - Space Complexity: O(rows * cols)

        Args:
            grid (List[List[int]]): Grid of oranges

        Returns:
            int: Minimum time required to rot all the oranges
        """
        queue = deque()
        fresh_oranges = 0
        time = 0
        visited = set()

        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    queue.append((i, j, time))
                    visited.add((i, j))

        if fresh_oranges == 0:
            return time

        x_d = [-1, 0, 1, 0]
        y_d = [0, 1, 0, -1]

        while queue:
            x, y, time = queue.popleft()

            for i in range(4):
                new_x = x + x_d[i]
                new_y = y + y_d[i]

                if (
                    0 <= new_x < rows
                    and 0 <= new_y < cols
                    and grid[new_x][new_y] == 1
                    and (new_x, new_y) not in visited
                ):
                    fresh_oranges -= 1
                    queue.append((new_x, new_y, time + 1))
                    visited.add((new_x, new_y))

        return time if fresh_oranges == 0 else -1


if __name__ == "__main__":
    s = Solution()
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(s.orangesRotting(grid))
