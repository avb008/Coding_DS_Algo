# Problem: Partition Equal Subset Sum
# Problem link: https://leetcode.com/problems/partition-equal-subset-sum/
# Difficulty: Medium

from typing import List


class Solution:
    def PossibleSubsetSumToK(self, index: int, k: int, arr: List[int]) -> bool:
        """Returns True if the array has a subset with sum equal to k

        Args:
            index (int): Index of the array
            k (int): Target sum
            arr (List[int]): Input array

        Returns:
            bool: True if the array has a subset with sum equal to k
        """
        if k == 0:
            return True

        if index == 0:
            return k == arr[0]

        pick = (
            self.PossibleSubsetSumToK(index - 1, k - arr[n], arr)
            if k - arr[index] >= 0
            else False
        )
        non_pick = self.PossibleSubsetSumToK(index - 1, k, arr)

        return pick or non_pick

    def canPartition(self, nums: List[int]) -> bool:
        """Returns True if the array can be partitioned into 2 subsets with equal sum

            - Time complexity: O(n * target)
            - Space complexity: O(n * target)

        Args:
            nums (List[int]): Input array

        Returns:
            bool: True if the array can be partitioned into 2 subsets with equal sum
        """
        if sum(nums) % 2 != 0:
            return False

        n, target = len(nums), sum(nums) // 2

        partitions = [[None for j in range(target + 1)] for i in range(n)]

        for i in range(n):
            partitions[i][0] = True

        if nums[0] <= target:
            partitions[0][nums[0]] = True

        for i in range(n):
            for j in range(target + 1):
                pick = partitions[i - 1][j - nums[i]] if nums[i] <= j else False
                non_pick = partitions[i - 1][j] if i > 0 else False

                partitions[i][j] = pick or non_pick

        return partitions[n - 1][target]


if __name__ == "__main__":
    obj = Solution()
    print(obj.canPartition([1, 5, 11, 5]))  # True
