# Leetcode link : https://practice.geeksforgeeks.org/problems/subset-sums2234/1
# Difficulty: Easy
# Time Complexity : O(2^n)
from typing import List


# User function Template for python3
class Solution:
    def subsetSums(self, arr: List[int], N: int) -> List[int]:
        """Subset sums

        Args:
            arr (List[int]): Input array
            N (int): Length of the input array

        Returns:
            List[int]: List of all the subset sums
        """
        # code here
        subset_sums = []
        self.computeAllSubsetSums(arr, N, 0, 0, subset_sums)
        subset_sums.sort()

        return subset_sums

    def computeAllSubsetSums(
        self, arr: List[int], N: int, index: int, cur_sum: int, sum_arr: List[int]
    ) -> None:
        """Compute all the subset sums

            - Time complexity: O(2^n)
            - Space complexity: O(n)

        Args:
            arr (List[int]): Input array
            N (int): Length of the input array
            index (int): Index of the current element
            cur_sum (int): Current sum
            sum_arr (List[int]): List of all the subset sums
        """
        if index == N:
            sum_arr.append(cur_sum)
            return

        # pick an element
        self.computeAllSubsetSums(arr, N, index + 1, cur_sum + arr[index], sum_arr)
        # Dont pick the element
        self.computeAllSubsetSums(arr, N, index + 1, cur_sum, sum_arr)


if __name__ == "__main__":
    obj = Solution()
    print(obj.subsetSums([2, 3], 2))
