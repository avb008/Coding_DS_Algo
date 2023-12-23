from typing import List


class Solution:
    def generate_all_subsequences(
        self, index: int, temp_arr: List[int], arr: List[int]
    ) -> None:
        if index >= len(arr):
            print(temp_arr, end=" ")
            return

        # pick the element at index
        temp_arr.append(arr[index])  # include
        self.generate_all_subsequences(index + 1, temp_arr, arr)
        temp_arr.pop()  # exclude

        # do not pick the element at index
        self.generate_all_subsequences(index + 1, temp_arr, arr)

    def generate_all_subsequences_of_sum_k(
        self,
        index: int,
        temp_arr: List[int],
        arr: List[int],
        current_sum: int,
        target_sum: int,
    ) -> None:
        if index >= len(arr):
            if current_sum == target_sum:
                print(temp_arr)
            return

        # pick the element at index
        temp_arr.append(arr[index])
        self.generate_all_subsequences_of_sum_k(
            index + 1, temp_arr, arr, current_sum + arr[index], target_sum
        )
        temp_arr.pop()

        # do not pick the element at index
        self.generate_all_subsequences_of_sum_k(
            index + 1, temp_arr, arr, current_sum, target_sum
        )

    def generate_any_subsequence_of_target_sum(
        self,
        index: int,
        temp_arr: List[int],
        arr: List[int],
        current_sum: int,
        target_sum: int,
    ) -> bool:
        if index >= len(arr):
            if current_sum == target_sum:
                print(temp_arr)
                return True
            return False

        # pick the element at index
        temp_arr.append(arr[index])
        if self.generate_any_subsequence_of_target_sum(
            index + 1, temp_arr, arr, current_sum + arr[index], target_sum
        ):
            return True
        temp_arr.pop()

        # do not pick the element at index
        if self.generate_any_subsequence_of_target_sum(
            index + 1, temp_arr, arr, current_sum, target_sum
        ):
            return True
        return False

    def count_number_of_subsequences_of_target_sum(
        self,
        index: int,
        temp_arr: List[int],
        arr: List[int],
        current_sum: int,
        target_sum: int,
    ) -> int:
        if index >= len(arr):
            if current_sum == target_sum:
                return 1  # found a subsequence with target sum
            return 0  # did not find a subsequence with target sum

        # pick the element at index
        temp_arr.append(arr[index])  # include
        included = self.count_number_of_subsequences_of_target_sum(
            index + 1, temp_arr, arr, current_sum + arr[index], target_sum
        )
        temp_arr.pop()  # exclude

        # do not pick the element at index
        excluded = self.count_number_of_subsequences_of_target_sum(
            index + 1, temp_arr, arr, current_sum, target_sum
        )
        return included + excluded


if __name__ == "__main__":
    s = Solution()
    arr = [1, 2, 3, 4]
    print("Input: arr = [1, 2, 3, 4]")
    print("All subsequences of arr: ")
    s.generate_all_subsequences(0, [], arr)
    print()

    print("#" * 100)
    print("Input: arr = [10, 5, 2, 3, 6, 1], target_sum = 22")
    arr = [10, 5, 2, 3, 6, 1]
    print("All subsequences of arr with sum 22: ")
    s.generate_all_subsequences_of_sum_k(0, [], arr, 0, 22)

    print("#" * 100)
    print("Input: arr = [10, 5, 2, 3, 6, 1], target_sum = 22")
    arr = [10, 5, 2, 3, 6, 1]
    print("Any subsequence of arr with sum 22: ")
    s.generate_any_subsequence_of_target_sum(0, [], arr, 0, 22)
