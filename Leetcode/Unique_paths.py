# Problem link : https://leetcode.com/problems/unique-paths/
# Difficulty: Medium


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """Returns the number of unique paths from top left to bottom right

            - Time complexity: O(m*n)
            - Space complexity: O(m*n)

            - Can be optimized to O(n) space complexity
            - Also, can be optimized to O(1) space complexity
            - Algorithm: Dynamic Programming
                - Create a 2D array of size m*n
                - Initialize the first row and first column with 1
                - For each cell, the number of unique paths is the sum of the number of unique paths from the cell above
                and the cell to the left
                - Return the last cell of the 2D array

        Args:
            m (int): Number of rows
            n (int): Number of columns

        Returns:
            int: Number of unique paths from top left to bottom right
        """
        paths = [[0 for _ in range(n)] for _ in range(m)]
        paths[0][0] = 1  # 1 way to reach the starting point

        for i in range(m):
            for j in range(n):
                if (i + j) == 0:
                    continue

                down = paths[i - 1][j] if i - 1 >= 0 else 0
                right = paths[i][j - 1] if j - 1 >= 0 else 0

                paths[i][j] = down + right

        return paths[m - 1][n - 1]


if __name__ == "__main__":
    obj = Solution()
    print(obj.uniquePaths(3, 2))  # 3
    print(obj.uniquePaths(7, 3))  # 28
    print(obj.uniquePaths(3, 3))  # 6
    print(obj.uniquePaths(5, 6))  # 126
