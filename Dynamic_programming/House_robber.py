from typing import List


class Solution:
    def maxRob(self, nums: List[int]) -> int:
        """Find max amount of money that can be robbed from a list of houses

        Args:
            nums (List[int]): List of money in each house

        Returns:
            int: Max amount of money that can be robbed
        """
        n = len(nums)
        max_rob = [0] * n
        for i in range(n):
            non_pick = max_rob[i - 1] if i >= 1 else 0
            pick = max_rob[i - 2] + nums[i] if (i - 2) >= 0 else nums[i]
            max_rob[i] = max(non_pick, pick)

        return max_rob[n - 1]

    def robCircle(self, nums: List[int]) -> int:
        """Find max amount of money that can be robbed from a circle of houses

        Args:
            nums (List[int]): List of money in each house

        Returns:
            int: Max amount of money that can be robbed
        """

        n = len(nums)
        if n == 1:
            return nums[0]

        answer1 = self.maxRob(nums[: n - 1])  # Excluding last element
        answer2 = self.maxRob(nums[1:])  # Excluding 1st element

        return max(answer1, answer2)
