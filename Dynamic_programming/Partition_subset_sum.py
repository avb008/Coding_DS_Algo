from typing import List


class Solution:
    def subsetSumToK(self, arr: List[int], target: int) -> List[List[bool]]:
        """Check if there is a subset of arr with sum equal to target

            - Time complexity: O(n*target)
            - Space complexity: O(n*target)

        Args:
            arr (List[int]): Input array
            target (int): Sum to be achieved

        Returns:
            List[List[bool]]: 2D array with True/False values
        """

        n = len(arr)
        subset_sum = [[None for _ in range(target + 1)] for _ in range(n)]
        for i in range(n):
            subset_sum[i][0] = True

        if arr[0] <= target:
            subset_sum[0][arr[0]] = True

        for i in range(1, n):
            for j in range(1, target + 1):
                pick = subset_sum[i - 1][j - arr[i]] if j - arr[i] >= 0 else False
                non_pick = subset_sum[i - 1][j]

                subset_sum[i][j] = pick or non_pick

        return subset_sum

    def canPartition(self, nums: List[int]) -> bool:
        """Check if there is a subset of arr with sum equal to target

            - Time complexity: O(n*target)
            - Space complexity: O(n*target)

        Args:
            nums (List[int]): Input array

        Returns:
            bool: True if there is a subset of arr with sum equal to target
        """

        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False

        target_sum = total_sum // 2
        subset_sum = self.subsetSumToK(target_sum, nums)

        return subset_sum[-1][-1]

    def PartitionMinAbsoluteSumDifference(self, nums: List[int]) -> bool:
        """Find the minimum absolute difference between the sum of two subsets

            - Time complexity: O(n*sum(nums))
            - Space complexity: O(n*sum(nums))

        Args:
            nums (List[int]): Input array

        Returns:
            bool: Minimum absolute difference between the sum of two subsets
        """
        total_sum = sum(nums)
        subset_sum = self.subsetSumToK(total_sum, nums)

        min_diff = float("inf")
        for i in range(total_sum // 2, -1, -1):
            if subset_sum[-1][i]:
                min_diff = total_sum - 2 * i
                break

        return min_diff
