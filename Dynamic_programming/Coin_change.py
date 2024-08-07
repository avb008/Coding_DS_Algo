from typing import List


class Solution:
    def minCoinChange(self, coins: List[int], amount: int, index: int) -> int:
        """Min coin change problem with unlimited supply of coins

        Args:
            coins (List[int]): Coin denominations
            amount (int): Amount to be made
            index (int): Index of coin

        Returns:
            int: Minimum number of coins required to make the amount
        """

        if index == 0:
            if amount % coins[0] == 0:
                return amount // coins[0]
            return amount + 1

        not_take = self.minCoinChange(coins, amount, index - 1)
        take = amount + 1
        if amount >= coins[index]:
            take = 1 + self.minCoinChange(coins, amount - coins[index], index)

        return min(take, not_take)

    def coinChange(self, coins: List[int], amount: int) -> int:
        """Min coin change problem with unlimited supply of coins

        Args:
            coins (List[int]): Coin denominations
            amount (int): Amount to be made

        Returns:
            int: Minimum number of coins required to make the amount
        """

        coins.sort()
        min_coins = [amount + 1] * (amount + 1)
        min_coins[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    min_coins[i] = min(min_coins[i], min_coins[i - coin]) + 1

        return min_coins[amount] if min_coins[amount] < (amount + 1) else -1


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    sol = Solution()
    print(sol.coinChange(coins, amount))
