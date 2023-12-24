# Leetcode link : https://leetcode.com/problems/combination-sum/description/
# Difficulty: Medium

from typing import List


class Solution:
    def findCombinations(
        self, index: int, candidates: List[int], target: int, temp_arr: List[int]
    ) -> List[List[int]]:
        """Find all the combinations that add up to the target sum

            - Time complexity: O(2^n)
            - Space complexity: O(n)

            - Algorithm:
                - If the target sum is 0, return the current combination
                - If the index is out of bounds, return empty array
                - Pick the number at the current index
                    - If the number is less than or equal to the target sum, add it to the current combination
                    - Find all the combinations that add up to the target sum - number
                - Dont pick the number at the current index
                    - Find all the combinations that add up to the target sum

        Args:
            index (int): Index of the current element
            candidates (List[int]): Input array of numbers
            target (int): Target sum
            temp_arr (List[int]): Temporary array to store the current combination

        Returns:
            List[List[int]]: List of all the combinations that add up to the target sum
        """

        if index == len(candidates):
            if target == 0:
                return [temp_arr]
            return []

        ans = []
        # pick the number
        if candidates[index] <= target:
            ans += self.findCombinations(
                index,
                candidates,
                target - candidates[index],
                temp_arr + [candidates[index]],
            )
        ans += self.findCombinations(index + 1, candidates, target, temp_arr)

        return ans

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.findCombinations(0, candidates, target, [])


if __name__ == "__main__":
    obj = Solution()
    print(obj.combinationSum([2, 3, 5], 8))
