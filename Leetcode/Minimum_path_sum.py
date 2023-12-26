# Problem link : https://leetcode.com/problems/minimum-path-sum/description/
# Difficulty: Medium

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """Returns the minimum path sum from top left to bottom right

            - Time complexity: O(m*n)
            - Space complexity: O(m*n)
            - Can be optimized to O(n) space complexity

        Args:
            grid (List[List[int]]): Input grid of numbers (2D array)

        Returns:
            int: Minimum path sum from top left to bottom right
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


if __name__ == "__main__":
    obj = Solution()
    print(obj.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))  # 7
    print(obj.minPathSum([[1, 2, 3], [4, 5, 6]]))  # 12
