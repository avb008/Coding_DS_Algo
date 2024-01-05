class Solution:
    def isValid(self, s: str) -> bool:
        """Checks if the input string is valid. A string s is valid if:
            - Open brackets must be closed by the same type of brackets.
            - Open brackets must be closed in the correct order.

            - Time Complexity: O(n) where n is the length of the input string
            - Space Complexity: O(n) since one has to keep a stack of n elements

        Args:
            s (str): Input string

        Returns:
            bool: True if the input string is valid, False otherwise
        """
        map_paranthesis = {")": "(", "}": "{", "]": "["}

        stack = []
        for char in s:
            if char in map_paranthesis:
                if not stack or map_paranthesis[char] != stack.pop():
                    return False
            else:
                stack.append(char)

        return not stack
