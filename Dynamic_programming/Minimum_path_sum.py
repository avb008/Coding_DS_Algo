from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """Find minimum path sum

            - Time complexity: O(m*n)
            - Space complexity: O(m*n)

        Args:
            grid (List[List[int]]): Grid

        Returns:
            int: Minimum path sum
        """
        m, n = len(grid), len(grid[0])
        paths = [[0 for _ in range(n)] for _ in range(m)]
        paths[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if (i + j) == 0:
                    continue

                down = paths[i - 1][j] if (i - 1) >= 0 else float("inf")
                right = paths[i][j - 1] if (j - 1) >= 0 else float("inf")

                paths[i][j] = min(down, right) + grid[i][j]

        return paths[m - 1][n - 1]
