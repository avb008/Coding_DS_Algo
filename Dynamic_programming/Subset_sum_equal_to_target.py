from typing import List


class Solution:
    def PossibleSubsetSumToK(self, index: int, target: int, arr: List[int]) -> bool:
        """Check if there is a subset of arr[0..index] with sum equal to target

            - Time complexity: O(2^n)
            - Space complexity: O(n)

        Args:
            index (int): Current index of arr
            target (int): Sum to be achieved
            arr (List[int]): Input array

        Returns:
            bool: True if there is a subset of arr[0..index] with sum equal to target
        """
        if target == 0:
            return True

        if index == 0:
            return arr[0] == target

        pick = (
            self.PossibleSubsetSumToK(index - 1, target - arr[index], arr)
            if target - arr[index] >= 0
            else False
        )
        not_pick = self.PossibleSubsetSumToK(index - 1, target, arr)

        return pick or not_pick

    def subsetSumToK(self, arr: List[int], target: int) -> bool:
        """Check if there is a subset of arr with sum equal to target

            - Time complexity: O(n*target)
            - Space complexity: O(n*target)

        Args:
            arr (List[int]): Input array
            target (int): Sum to be achieved

        Returns:
            bool: True if there is a subset of arr with sum equal to target
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

        return subset_sum[n - 1][target]


if __name__ == "__main__":
    arr = [2, 3, 7, 8, 10]
    target = 11
    sol = Solution()
    print(sol.PossibleSubsetSumToK(len(arr) - 1, target, arr))
    print(sol.subsetSumToK(arr, target))
