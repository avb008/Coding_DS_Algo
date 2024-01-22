class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """Find number of unique paths from top left to bottom right

            - Time complexity: O(m*n)
            - Space complexity: O(m*n)

        Args:
            m (int): Number of rows
            n (int): Number of columns

        Returns:
            int: Number of unique paths
        """

        paths = [[0 for i in range(n)] for j in range(m)]
        paths[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i + j == 0:
                    continue

                down = paths[i - 1][j] if (i - 1) >= 0 else 0
                right = paths[i][j - 1] if (j - 1) >= 0 else 0

                paths[i][j] = down + right

        return paths[m - 1][n - 1]
