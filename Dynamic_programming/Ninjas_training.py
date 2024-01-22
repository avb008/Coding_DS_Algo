from typing import List


class Solution:
    def maxPossibleHappiness(self, n: int, points: List[List[int]]) -> int:
        """Find max possible happiness

            - Time complexity: O(n)
            - Space complexity: O(n)

        Args:
            n (int): Input n
            points (List[List[int]]): Input points

        Returns:
            int: Returns Max possible happiness
        """
        dp = [[0 for _ in range(3)] for _ in range(n)]

        for i in range(3):
            dp[0][i] = points[0][i]

        for i in range(1, n):
            dp[i][0] = points[i][0] + max(dp[i - 1][1], dp[i - 1][2])
            dp[i][1] = points[i][1] + max(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] = points[i][2] + max(dp[i - 1][0], dp[i - 1][1])

        return max(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2])
