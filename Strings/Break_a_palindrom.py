# Problem Link: https://leetcode.com/problems/break-a-palindrome/


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        """Convert a palindrome to a non-palindrome by changing exactly one character.The resulting string is
        lexicographically smallest.

            - Time complexity: O(n)
            - Space complexity: O(n)

        Args:
            palindrome (str): Palindrome string

        Returns:
            str: Non-palindrome string
        """

        if len(palindrome) == 1:
            return ""

        palindrome = list(palindrome)
        for i in range(len(palindrome) // 2):
            if palindrome[i] != "a":
                palindrome[i] = "a"
                return "".join(palindrome)

        palindrome[-1] = "b"
        return "".join(palindrome)


if __name__ == "__main__":
    s = Solution()
    print(s.breakPalindrome("abccba"))
    print(s.breakPalindrome("a"))
    print(s.breakPalindrome("aa"))
    print(s.breakPalindrome("aba"))
    print(s.breakPalindrome("abba"))
    print(s.breakPalindrome("aaaa"))
    print(s.breakPalindrome("aabaa"))
    print(s.breakPalindrome("aaa"))
