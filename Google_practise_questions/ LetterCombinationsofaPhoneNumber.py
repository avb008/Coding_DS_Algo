from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number
        could represent. Return the answer in any order.

            - Time Complexity: O(3^N * 4^M) where N is the number of digits in the input that maps to 3 letters and M is
            the number of digits in the input that maps to 4 letters, and N+M is the total number digits in the input.
            - Space Complexity: O(3^N * 4^M) since one has to keep 3^N * 4^M solutions.

        Args:
            digits (str): Input string containing digits from 2-9 inclusive

        Returns:
            List[str]: List of all possible letter combinations that the number could represent
        """
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        combinations = [""]
        for digit in digits:
            new_combinations = []
            for combination in combinations:
                for letter in digit_map[digit]:
                    new_combinations.append(combination + letter)
            combinations = new_combinations

        return combinations


if __name__ == "__main__":
    obj = Solution()
    print(obj.letterCombinations("23"))
