from typing import List


class Solution:
    def merge(self, left: List[int], right: List[int], arr: List[int]) -> List[int]:
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
        if len(arr) == 1:
            return arr

        mid = len(arr) // 2
        left = self.mergeSort(arr[:mid])
        right = self.mergeSort(arr[mid:])

        return self.merge(left, right, arr)


if __name__ == "__main__":
    s = Solution()
    arr = [6, 7, 8, 1, 2, 4, 12, 0, -2, 3]
    print(s.mergeSort(arr))
