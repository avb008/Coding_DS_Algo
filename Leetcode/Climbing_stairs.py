# Problem link : https://leetcode.com/problems/climbing-stairs/description/
# Difficulty: Easy


class Solution:
    def climbStairs(self, n: int) -> int:
        """Returns the number of ways to climb n stairs

        Args:
            n (int): Input number of stairs

        Returns:
            int: Number of ways to climb the stairs
        """
        ways = [0] * (n + 1)
        ways[0] = 1  # 1 way to climb 0 stairs

        for i in range(1, n + 1):
            if i == 1:
                ways[i] = ways[i - 1]  # Only 1 way of reaching the 1st stair
            else:
                ways[i] = ways[i - 1] + ways[i - 2]  # Either take 1 step or 2 steps

        return ways[n]


# ========================================================================================================================
if __name__ == "__main__":
    obj = Solution()
    print(obj.climbStairs(2))  # 2
    print(obj.climbStairs(3))  # 3
    print(obj.climbStairs(4))  # 5
