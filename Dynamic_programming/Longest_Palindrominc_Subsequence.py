class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        reverse = s[::-1]

        current = [0 for i in range(n + 1)]
        previous = [0 for i in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == reverse[j - 1]:
                    current[j] = 1 + previous[j - 1]
                else:
                    current[j] = max(previous[j], current[j - 1])

            previous = [x for x in current]

        return current[n]
