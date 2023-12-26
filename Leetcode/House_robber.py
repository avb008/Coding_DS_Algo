# Problem link : https://leetcode.com/problems/house-robber/description/
# Difficulty: Medium

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """Returns the maximum amount of money that can be robbed

        Args:
            nums (List[int]): Input list of numbers

        Returns:
            int: Maximum amount of money that can be robbed
        """

        n = len(nums)
        max_money = [0] * n
        for i in range(n):
            pick = nums[i] + max_money[i - 2] if i >= 2 else nums[i]
            non_pick = max_money[i - 1] if i >= 1 else 0

            max_money[i] = max(pick, non_pick)

        return max_money[n - 1]


if __name__ == "__main__":
    obj = Solution()
    print(obj.rob([1, 2, 3, 1]))  # 4
    print(obj.rob([2, 7, 9, 3, 1]))  # 12
