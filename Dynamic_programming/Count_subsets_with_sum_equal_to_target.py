from typing import List


class Solution:
    def count(
        self, nums: List[int], target: int, index: int, dp: List[List[int]]
    ) -> int:
        """Count the number of subsets with sum equal to target

        Args:
            nums (List[int]): Input array
            target (int): Sum to be achieved
            index (int): Current index
            dp (List[List[int]]): Memoization array

        Returns:
            int: Number of subsets with sum equal to target
        """

        if target == 0:
            return 1

        if index == 0:
            return nums[index] == target

        if dp[index][target] != -1:
            return dp[index][target]

        ans = 0
        if nums[index] <= target:
            ans += self.count(nums, target - nums[index], index - 1, dp)
        ans += self.count(nums, target, index - 1, dp)

        dp[index][target] = ans
        return ans

    def countSubsetsEqualTarget(self, nums: List[int], target: int) -> int:
        """Count the number of subsets with sum equal to target

            - Time complexity: O(n*target)
            - Space complexity: O(n*target)

        Args:
            nums (List[int]): Input array
            target (int): Sum to be achieved

        Returns:
            int: Number of subsets with sum equal to target
        """
        dp = [[-1 for _ in range(target + 1)] for _ in range(len(nums))]
        return self.count(nums, target, len(nums) - 1, dp)

    def countSubsetsEqualTargetBottomUp(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[0 for _ in range(target + 1)] for _ in range(n)]

        for i in range(n):
            dp[i][0] = 1  # there is always one subset with sum = 0

        if nums[0] <= target:
            dp[0][nums[0]] = 1

        for i in range(1, n):
            for j in range(1, target + 1):
                not_take = dp[i - 1][j]
                take = 0
                if nums[i] <= j:
                    take = dp[i - 1][j - nums[i]]
                dp[i][j] = not_take + take

        return dp[n - 1][target]


if __name__ == "__main__":
    nums = [1, 1, 2, 3]
    target = 3
    sol = Solution()
    ans = sol.countSubsetsEqualTarget(nums, target)
    print(ans)
    ans = sol.countSubsetsEqualTargetBottomUp(nums, target)
    print(ans)
