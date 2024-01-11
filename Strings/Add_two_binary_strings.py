class Solution:
    def addBinary(self, a: str, b: str) -> str:
        final = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            final.append(str(carry % 2))
            carry //= 2

        return "".join(final[::-1])


if __name__ == "__main__":
    obj = Solution()
    print(obj.addBinary("11", "1"))
    print(obj.addBinary("1010", "1011"))
    print(obj.addBinary("1", "111"))
    print(obj.addBinary("111", "111"))
    print(obj.addBinary("101", "111"))
