from typing import List


class Solution:
    def maxProfitSinglepurchase(self, prices) -> int:
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]

            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit

    # Index to track index , buy : Bool flaf to say if are allowed to buy/not
    def ComputeMaxProfit(self, index: int, buy: int, prices: List[int]) -> int:
        if index == len(prices):
            return 0

        if buy:  # Allowed to buy
            take = -prices[index] + self.ComputeMaxProfit(
                index + 1, 0, prices
            )  # Cant buy , can only sell
            non_take = self.ComputeMaxProfit(
                index + 1, 1, prices
            )  # Can buy since we didnt buy this time
            profit = max(take, non_take)
        else:  # Only allowed to sell
            take = prices[index] + self.ComputeMaxProfit(
                index + 1, 1, prices
            )  # Cant sell , can only buy
            non_take = self.ComputeMaxProfit(
                index + 1, 0, prices
            )  # Can sell since we didnt sell this time
            profit = max(take, non_take)

        return profit

    def ComputeMaxProfitMemoization(
        self, index: int, buy: int, prices: List[int], profits: List[int]
    ) -> int:
        if index == len(prices):
            return 0

        if profits[index][buy]:
            return profits[index][buy]

        profit = 0
        if buy:  # Allowed to buy
            take = -prices[index] + self.ComputeMaxProfit(
                index + 1, 0, prices
            )  # Cant buy , can only sell
            non_take = self.ComputeMaxProfit(
                index + 1, 1, prices
            )  # Can buy since we didnt buy this time
            profit = max(take, non_take)
        else:  # Only allowed to sell
            take = prices[index] + self.ComputeMaxProfit(
                index + 1, 1, prices
            )  # Cant sell , can only buy
            non_take = self.ComputeMaxProfit(
                index + 1, 0, prices
            )  # Can sell since we didnt sell this time
            profit = max(take, non_take)

        profits[index][buy] = profit

        return profits[index][buy]

    def maxProfitMultiplePurchase(self, prices: List[int]) -> int:
        # return self.ComputeMaxProfit(len(prices)-1,0,prices)

        # DP
        n = len(prices)
        profits = [[None for _ in range(2)] for _ in range(n)]

        return self.ComputeMaxProfitMemoization(0, 1, prices, profits)

    def maxProfitMultiplePurchaseDP(self, prices: List[int]) -> int:
        n = len(prices)
        profits = [[None for _ in range(2)] for _ in range(n + 1)]
        profits[n][0], profits[n][1] = 0, 0

        for i in range(n - 1, -1, -1):
            for buy in range(2):
                profit = 0
                if buy:  # Sell
                    profit = max(profits[i + 1][1], -prices[i] + profits[i + 1][0])
                else:  # Buy
                    profit = max(profits[i + 1][0], prices[i] + profits[i + 1][1])

                profits[i][buy] = profit

        return profits[0][1]

    def maxProfitMutiplePurchase2TranscationsRecursion(
        self,
        index: int,
        can_buy: int,
        count_trans: int,
        prices: List[int],
        profits: List[List[List[int]]],
    ) -> int:
        if count_trans == 0 or index == len(prices):
            return 0

        if profits[index][can_buy][count_trans]:
            return profits[index][can_buy][count_trans]

        if can_buy:
            take = -prices[index] + self.maxProfitMutiplePurchase2TranscationsRecursion(
                index + 1, 0, count_trans, prices, profits
            )
            not_take = self.maxProfitMutiplePurchase2TranscationsRecursion(
                index + 1, 1, count_trans, prices, profits
            )
            profits[index][can_buy][count_trans] = max(take, not_take)
            return profits[index][can_buy][count_trans]
        else:
            take = prices[index] + self.maxProfitMutiplePurchase2TranscationsRecursion(
                index + 1, 1, count_trans - 1, prices, profits
            )
            not_take = self.maxProfitMutiplePurchase2TranscationsRecursion(
                index + 1, 0, count_trans, prices, profits
            )
            profits[index][can_buy][count_trans] = max(take, not_take)
            return profits[index][can_buy][count_trans]

    def maxProfitMutiplePurchase2Transcations(self, prices: List[int]) -> int:
        # 3d array (index, buy, transactions)
        n = len(prices)
        profits = [[[None for _ in range(3)] for _ in range(2)] for _ in range(n)]
        return self.maxProfitMutiplePurchase2TranscationsRecursion(
            0, 1, 2, prices, profits
        )

    def maxProfitMutiplePurchase2TranscationsDP(self, prices: List[int]) -> int:
        n = len(prices)
        profits = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]
        # index = n, Base case
        for buy in range(2):
            for trans in range(3):
                profits[n][buy][trans] = 0

        # 0 transactions , Base case
        for i in range(n + 1):
            for buy in range(2):
                profits[i][buy][0] = 0

        for i in range(n - 1, -1, -1):
            for buy in range(2):
                for trans in range(1, 3):
                    profit = 0
                    if buy:  # Sell
                        profit = max(
                            profits[i + 1][1][trans],
                            -prices[i] + profits[i + 1][0][trans],
                        )
                    else:  # Buy
                        profit = max(
                            profits[i + 1][0][trans],
                            prices[i] + profits[i + 1][1][trans - 1],
                        )

                    profits[i][buy][trans] = profit

        return profits[0][1][2]


if __name__ == "__main__":
    s = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(s.maxProfitSinglepurchase(prices))  # Single purchase
    print(s.maxProfitMultiplePurchase(prices))  # Memoization
    print(s.maxProfitMultiplePurchaseDP(prices))  # DP (Tabular)
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    print(s.maxProfitMutiplePurchase2Transcations(prices))  # 2 transactions
