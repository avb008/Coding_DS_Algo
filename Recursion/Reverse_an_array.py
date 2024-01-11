from typing import List


class Solution:
    def reverseArray(self, nums: List[int], index: int) -> None:
        """Reverse an array using recursion

        Args:
            nums (List[int]): Input array
            index (int): Index of the array
        """
        if index == len(nums) // 2:
            return

        nums[index], nums[len(nums) - index - 1] = (
            nums[len(nums) - index - 1],
            nums[index],
        )

        self.reverseArray(nums, index + 1)

    def reverseArrayTwoPointers(self, nums: List[int], left: int, right: int) -> None:
        """Reverse an array using two pointers

        Args:
            nums (List[int]): Input array
            left (int): Left pointer
            right (int): Right pointer
        """
        if left > right:
            return

        nums[left], nums[right] = nums[right], nums[left]
        self.reverseArrayTwoPointers(nums, left + 1, right - 1)


if __name__ == "__main__":
    obj = Solution()
    nums = [1, 2, 3, 4, 5]
    obj.reverseArray(nums, 0)
    print(nums)

    nums = [1, 2, 3, 4]
    obj.reverseArray(nums, 0)
    print(nums)

    nums = [1, 2, 3, 4, 5]
    obj.reverseArrayTwoPointers(nums, 0, len(nums) - 1)
    print(nums)

    nums = [1, 2, 3, 4]
    obj.reverseArrayTwoPointers(nums, 0, len(nums) - 1)
    print(nums)
