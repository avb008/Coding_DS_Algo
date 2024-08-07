class Solution:
    def climbStairs(self, n: int) -> int:
        """Find the number of ways to reach the top of the stairs

            - Time complexity: O(n)
            - Space complexity: O(n)

        Args:
            n (int): Number of stairs

        Returns:
            int: Number of ways to reach the top of the stairs
        """

        ways = [0 for i in range(n + 1)]
        ways[0] = 1

        for i in range(1, n + 1):
            ways[i] = ways[i - 1]
            if (i - 2) >= 0:
                ways[i] += ways[i - 2]

        return ways[n]
