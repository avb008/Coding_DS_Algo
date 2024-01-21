# Problem : https://leetcode.com/problems/reverse-words-in-a-string/description/


class Solution:
    def reverseWords(self, s: str) -> str:
        """Given an input string, reverse the string word by word.

            - Time complexity: O(n)
            - Space complexity: O(n)

            - Also remove any extra spaces between words.

        Args:
            s (str): Input string

        Returns:
            str: Reversed string
        """
        return " ".join(s.strip().split()[::-1])


if __name__ == "__main__":
    s = Solution()
    print(s.reverseWords("the sky is blue"))
    print(s.reverseWords("  hello world!  "))
    print(s.reverseWords("a good   example"))
    print(s.reverseWords("  Bob    Loves  Alice   "))
    print(s.reverseWords("Alice does not even like bob"))
    print(s.reverseWords("  hello world!  "))
