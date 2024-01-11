class Solution:
    def checkPalindrome(self, string: str, left: int, right: int) -> bool:
        """Check if string is palindrome

        Args:
            string (str): Input string
            left (int): Left pointer
            right (int): Right pointer

        Returns:
            bool: True if string is palindrome, False otherwise
        """
        if left >= right:
            return True

        if string[left] != string[right]:
            return False

        return self.checkPalindrome(string, left + 1, right - 1)


if __name__ == "__main__":
    obj = Solution()
    print(obj.checkPalindrome("abba", 0, 3))
    print(obj.checkPalindrome("abb", 0, 2))
