from typing import List


class Solution:
    def minJumpsBruteForce(self, arr: List[int]) -> int:
        """Returns the minimum number of jumps required to reach the end of the array.

            - Time complexity: O(n^2)
            - Space complexity: O(n)

        Args:
            arr (List[int]): The array of integers.

        Returns:
            int: The minimum number of jumps required to reach the end of the array.
        """
        # Write your code here.
        n = len(arr)
        jumps = [n + 1 if i != 0 else 0 for i in range(n)]

        for i in range(n - 1):
            j = 1
            while j < min(arr[i] + 1, n):
                if (i + j) < n:
                    jumps[i + j] = min(jumps[i + j], jumps[i] + 1)
                j += 1

        return jumps[n - 1] if jumps[n - 1] != n + 1 else -1

    def minJumpsOptimzed(self, arr: List[int]) -> int:
        """Returns the minimum number of jumps required to reach the end of the array.

            - Time complexity: O(n)
            - Space complexity: O(1)

        Args:
            arr (List[int]): The array of integers.

        Returns:
            int: The minimum number of jumps required to reach the end of the array.
        """
        n = len(arr)

        if n <= 1 or arr[0] == 0:
            return 0

        maxReach = arr[0]  # Maximum index that can be reached
        step = arr[0]  # Number of steps that can be taken
        jump = 1  # Number of jumps required

        for i in range(1, n):
            if i == n - 1:
                return jump  # Reached the end

            maxReach = max(maxReach, i + arr[i])  # Update maxReach
            step -= 1  # One step taken

            if step == 0:  # No more steps can be taken
                jump += 1
                if i >= maxReach:
                    return -1
                step = maxReach - i

        return -1

    def canJump(self, nums: List[int]) -> bool:
        """Returns whether the end of the array can be reached.

            - Time complexity: O(n)
            - Space complexity: O(1)

        Args:
            nums (List[int]): The array of integers.

        Returns:
            bool: Whether the end of the array can be reached.
        """
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:  # if we can reach the goal from this index
                goal = i

        return not goal  # if goal is 0, we can reach the end

    def jump(self, nums: List[int]) -> int:
        """Returns the minimum number of jumps required to reach the end of the array.

            - Time complexity: O(n)
            - Space complexity: O(1)

        Args:
            nums (List[int]): The array of integers.

        Returns:
            int: The minimum number of jumps required to reach the end of the array.
        """
        num_jumps = 0
        furthest_jump = 0
        current_jump_limit = 0

        if len(nums) == 1:  # If the array is of length 1, we don't need to jump
            return 0

        for index in range(len(nums)):
            furthest_jump = max(furthest_jump, index + nums[index])

            if (
                index == current_jump_limit
            ):  # If we reach the current jump limit, we need to jump (end of current window)
                num_jumps += 1
                current_jump_limit = furthest_jump

            if furthest_jump >= len(nums) - 1:
                return num_jumps

        return -1


if __name__ == "__main__":
    obj = Solution()
    arr = [2, 3, 1, 1, 4]
    print("Brute force solution for arr = [2, 3, 1, 1, 4]:")
    print(obj.minJumpsBruteForce(arr))
    print("Optimized solution for arr = [2, 3, 1, 1, 4]:")
    print(obj.minJumpsOptimzed(arr))
    arr = [3, 2, 1, 0, 5]
    print("Brute force solution for arr = [3, 2, 1, 0, 5]:")
    print(obj.minJumpsBruteForce(arr))
    print("Optimized solution for arr = [3, 2, 1, 0, 5]:")
    print(obj.minJumpsOptimzed(arr))
    arr = [1, 1, 1, 1, 1]
    print("Brute force solution for arr = [1, 1, 1, 1, 1]:")
    print(obj.minJumpsBruteForce(arr))
    print("Optimized solution for arr = [1, 1, 1, 1, 1]:")
    print(obj.minJumpsOptimzed(arr))
    arr = [1, 2, 3, 4, 5, 6]
    print("Brute force solution for arr = [1, 2, 3, 4, 5, 6]:")
    print(obj.minJumpsBruteForce(arr))
    print("Optimized solution for arr = [1, 2, 3, 4, 5, 6]:")
    print(obj.minJumpsOptimzed(arr))

    print("Can jump solution for arr = [2, 3, 1, 1, 4]:")
    print(obj.canJump(arr))
