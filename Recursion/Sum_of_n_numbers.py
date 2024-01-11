class Solution:
    def SumOfnNumbers(self, n: int) -> int:
        """Sum of n numbers

            - Time complexity: O(n)
            - Space complexity: O(n)

        Args:
            n (int): Input number

        Returns:
            int: Sum of n numbers
        """
        if n == 0:
            return 0

        return n + self.SumOfnNumbers(n - 1)

    def SumOfnNumbersParametrized(self, n: int, current_sum: int) -> None:
        if n == 0:
            print(current_sum)
            return

        self.SumOfnNumbersParametrized(n - 1, current_sum + n)


if __name__ == "__main__":
    obj = Solution()
    print(obj.SumOfnNumbers(5))
    obj.SumOfnNumbersParametrized(5, 0)
