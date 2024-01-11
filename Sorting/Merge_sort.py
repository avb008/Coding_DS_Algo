from typing import List


class Solution:
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        """Merge two sorted arrays

            - Time complexity: O(n)
            - Space complexity: O(n)

            - Merge two sorted arrays into one sorted array
            - Use two pointers to iterate through the two arrays and compare the values at the pointers
              Append the smaller value to the sorted array and increment the pointer
            - If one of the arrays is exhausted, append the remaining values of the other array to the sorted array
            - Return the sorted array

        Args:
            left (List[int]): Left sorted array
            right (List[int]): Right sorted array

        Returns:
            List[int]: Sorted array
        """
        start1, start2 = 0, 0
        sorted_arr = []
        while start1 < len(left) and start2 < len(right):
            if left[start1] < right[start2]:
                sorted_arr.append(left[start1])
                start1 += 1
            else:
                sorted_arr.append(right[start2])
                start2 += 1

        while start1 < len(left):
            sorted_arr.append(left[start1])
            start1 += 1
        while start2 < len(right):
            sorted_arr.append(right[start2])
            start2 += 1

        return sorted_arr

    def mergeSort(self, arr: List[int]) -> List[int]:
        """Merge sort

            - Time complexity: O(nlogn)
            - Space complexity: O(n) (for the extra temporary array when merging two)

            - Divide and conquer
            - Recursively split the array into two halves
            - Merge the two sorted halves

        Args:
            arr (List[int]): Input array

        Returns:
            List[int]: Sorted array
        """
        if len(arr) == 1:
            return arr

        mid = len(arr) // 2
        left = self.mergeSort(arr[:mid])
        right = self.mergeSort(arr[mid:])

        return self.merge(left, right)


if __name__ == "__main__":
    s = Solution()
    arr = [6, 7, 8, 1, 2, 4, 12, 0, -2, 3]
    print(s.mergeSort(arr))
