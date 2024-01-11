# Leetcode link : https://practice.geeksforgeeks.org/problems/subset-sum-ii/1
# Difficulty: Easy
# Time Complexity : O(n*2^n)
# Space Complexity : O(n*2^n)

from typing import List


class Solution:
    def allUniqueSubsets(
        self,
        nums: List[int],
        index: int,
        temp_arr: List[int],
        all_subsets: List[List[int]],
    ) -> None:
        """Find all the unique subsets of the given array

            - Time complexity: O(n*2^n)
            - Space complexity: O(n*2^n)

            - Algorithm:
                - Sort the array
                - Add the current subset to the list of all subsets
                - For each element in the array
                    - If the element is not the first element and is equal to the previous element, skip it
                    - Add the element to the current subset
                    - Find all the unique subsets starting from the next element
                    - Remove the element from the current subset
                - Return the list of all subsets

        Args:
            nums (List[int]): Input array
            index (int): Index of the current element
            temp_arr (List[int]): Temporary array to store the current subset
            all_subsets (List[List[int]]): List of all the unique subsets
        """
        all_subsets.append(temp_arr.copy())
        for i in range(index, len(nums)):
            # Skip the duplicate elements but not the first element
            # [1,2,2,2] and if the temp_arr is [1,2] we can pick second 2 but not the third 2
            if i != index and nums[i] == nums[i - 1]:
                continue
            temp_arr.append(nums[i])
            self.allUniqueSubsets(nums, i + 1, temp_arr, all_subsets)
            temp_arr.pop()

    def printUniqueSubset(self, nums: List[int]) -> List[List[int]]:
        """Print all the unique subsets of the given array

        Args:
            nums (List[int]): Input array

        Returns:
            List[List[int]] : List[List[int]]: List of all the unique subsets
        """

        nums.sort()
        all_unique_subsets = []
        self.allUniqueSubsets(nums, 0, [], all_unique_subsets)

        return all_unique_subsets


if __name__ == "__main__":
    obj = Solution()
    print(obj.printUniqueSubset([1, 2, 2]))
