from typing import List


class Solution:
    def partition(Self, arr: List[int], low: int, high: int) -> int:
        """Partition the array into two parts

            - Time complexity: O(n)
            - Space complexity: O(1)

            - Choose a pivot value
            - Iterate through the array and move all values smaller than the pivot to the left of the pivot
            - Return the index of the pivot

        Args:
            arr (List[int]): Input array
            low (int): Starting index
            high (int): Ending index

        Returns:
            int: Index of the pivot
        """
        pivot = arr[high]
        i = low - 1
        # Move all values smaller than the pivot to the left of the pivot
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quickSort(self, arr: List[int], low: int, high: int) -> None:
        """Quick sort

            - Time complexity: O(nlogn) (average case) / O(n^2) (worst case)
            - Space complexity: O(1)  (average case) / O(n) (worst case)

            - Divide and conquer
            - Choose a pivot value and partition the array into two parts (smaller than the pivot and larger than the pivot)
            - Recursively quick sort the two parts

        Args:
            arr (List[int]): Input array
            low (int): Lower bound
            high (int): Upper bound

        Returns:
            None
        """
        if low < high:
            partition_index = self.partition(arr, low, high)
            self.quickSort(arr, low, partition_index - 1)
            self.quickSort(arr, partition_index + 1, high)


if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    Solution().quickSort(arr, 0, len(arr) - 1)
    print(arr)
